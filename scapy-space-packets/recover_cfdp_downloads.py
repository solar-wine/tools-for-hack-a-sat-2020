#!/usr/bin/env python3
"""Recover files that are downloaded using CFDP protocol"""
import argparse
import os.path
from pathlib import Path
import re
import socket
import sys

from all_packets import CFDP_TlmPkt, Packet, cfdp_checksum, pump_cosmos_ccsds_packets  # noqa


class CFPDState:
    def __init__(self, src_file_name, file_size):
        self.src_file_name = src_file_name
        self.file_size = file_size
        self.chunks = {}

    def add_data_segment(self, offset, data):
        try:
            existing_data = self.chunks[offset]
        except KeyError:
            # Usual case: new data chunk
            self.chunks[offset] = data
            return
        if existing_data == data:
            # Ignore duplicate packet
            return
        print(f"Warning: replacing data at offset {offset:#x} from {existing_data.hex()} to {data.hex()}")
        self.chunks[offset] = data

    def finalize(self, file_size, file_checksum):
        if file_size != self.file_size:
            print(f"Warning: Metadata file size {self.file_size} != EOF file size {file_size}")
        # Merge the chunks together, ensuring their size matches the offset
        merged = bytearray(file_size)
        current_offset = 0
        for offset, chunk in sorted(self.chunks.items()):
            if offset > current_offset:
                print(f"Error: missing chunk {current_offset:#x}..{offset:#x} ({offset - current_offset} bytes)")
                return None
            if offset != current_offset:
                print(f"Error: unexpected chunk offset {offset:#x} != {current_offset:#x}, for {self.src_file_name!r}")
                return None
            if offset + len(chunk) > file_size:
                print(f"Error: unexpected chunk end {offset + len(chunk):#x} > {file_size:#x}, for {self.src_file_name!r}")  # noqa
                return None
            merged[offset:offset + len(chunk)] = chunk
            current_offset += len(chunk)

        if current_offset != file_size:
            print(f"Error: missing chunk from {current_offset:#x} < {file_size:#x}, for {self.src_file_name!r}")
            return None

        # Verify the checksum
        computed = cfdp_checksum(merged)
        if computed != file_checksum:
            print(f"Error: invalid CFDP checksum {computed:#x} != {file_checksum:#x}, for {self.src_file_name!r}")
            return None
        return bytes(merged)


def unique_file_name(src_file_name, file_size, file_checksum):
    if src_file_name.startswith('/cf/../'):
        # Remove /cf/../ prefix
        file_name = src_file_name[7:]
    elif src_file_name.startswith('/cf/'):
        # Remove /cf/ prefix
        file_name = src_file_name[4:]
    else:
        file_name = src_file_name

    file_name = file_name.strip('.').replace('/', '__') + f'__{file_size}__{file_checksum:08x}.cfdp'
    if not re.match(r'^[0-9A-Za-z._]+$', file_name):
        print(f"Warning: tried to use an invalid file name {file_name!r} for {src_file_name!r}")
        return None
    return file_name


class SpaceCFDPPacketProcessor:
    def __init__(self, show_data: bool = False):
        self.show_data = show_data
        self._active_connections = {}
        # Chunks for failed CFDP downloads: (filename, size, cksum) -> offset -> chunk -> count
        self._saved_failed_chunks = {}

    @property
    def active_connections(self):
        return self._active_connections

    def process_space_to_gnd_pkt(self, ccsds_pkt: Packet):
        if ccsds_pkt.apid == 0x7fd:  # CF_SPACE_TO_GND_PDU
            cfdp_pkt = ccsds_pkt.payload
            assert isinstance(cfdp_pkt, CFDP_TlmPkt)
            conn_triple = f'{cfdp_pkt.src_id.hex()}-{cfdp_pkt.dst_id.hex()}-{cfdp_pkt.trans_seq.hex()}'

            if cfdp_pkt.pdu_type == 1:  # Data
                data_file_offset = cfdp_pkt.data_file_offset
                data = cfdp_pkt.data
                if self.show_data:
                    print(f"<{conn_triple}> Data packet [{data_file_offset:#08x}, {len(data)}]: {data.hex()}")
                if conn_triple not in self._active_connections:
                    print(f"Warning: data for unknown active connection {conn_triple}")
                else:
                    self._active_connections[conn_triple].add_data_segment(data_file_offset, data)

            elif cfdp_pkt.pdu_type == 0 and cfdp_pkt.directive_code == 0x07:  # Metadata
                src_file_name = cfdp_pkt.src_file_name.decode('utf-8', 'replace')
                file_size = cfdp_pkt.payload.file_size
                print(f"<{conn_triple}> Metadata for {src_file_name!r}: {file_size} bytes")
                if conn_triple in self._active_connections:
                    print(f"Warning: dropping active connection {conn_triple}")
                self._active_connections[conn_triple] = CFPDState(src_file_name, file_size)

            elif cfdp_pkt.pdu_type == 0 and cfdp_pkt.directive_code == 0x04:  # EOF
                file_checksum = cfdp_pkt.payload.file_checksum
                file_size = cfdp_pkt.payload.file_size
                print(f"<{conn_triple}> EOF packet: size={file_size}, cksum={file_checksum:#x}")
                if conn_triple not in self._active_connections:
                    print(f"Warning: EOF for unknown active connection {conn_triple}")
                else:
                    conn = self._active_connections[conn_triple]
                    data = conn.finalize(file_size, file_checksum)
                    saved_key = (conn.src_file_name, file_size, file_checksum)
                    if data is None:
                        # There was an issue, keep the chunks to use them with future retries
                        if saved_key not in self._saved_failed_chunks:
                            self._saved_failed_chunks[saved_key] = {}
                        for offset, chunk in conn.chunks.items():
                            if b'\xde\xad\xbe\xef' in chunk:
                                # Ignore chunks that contain a synchronisation pattern,
                                # as they are unlikely to be right
                                continue
                            if offset not in self._saved_failed_chunks[saved_key]:
                                self._saved_failed_chunks[saved_key][offset] = {}
                            if chunk not in self._saved_failed_chunks[saved_key][offset]:
                                self._saved_failed_chunks[saved_key][offset][chunk] = 1
                            else:
                                self._saved_failed_chunks[saved_key][offset][chunk] += 1

                        # Now, add the previous chunks to the conn and try again
                        is_modified = False
                        for offset, data_count in self._saved_failed_chunks[saved_key].items():
                            chunk, count = max(data_count.items(), key=lambda x: x[1])
                            if offset not in conn.chunks:
                                print(f"  ... inserting chunk at offset {offset:#08x} (seen {count})")
                                conn.chunks[offset] = chunk
                                is_modified = True
                                continue
                            current_chunk = conn.chunks[offset]
                            if current_chunk == chunk:
                                continue
                            current_count = data_count.get(current_chunk, 0)
                            assert count >= current_count  # count is a max()
                            print(f"  ... replacing chunk at offset {offset:#08x}: seen {count} >= {current_count}")
                            conn.chunks[offset] = chunk
                            is_modified = True
                        if is_modified:
                            print("... trying again with chunks from previous transfers...")
                            data = conn.finalize(file_size, file_checksum)

                    if data is not None:
                        if saved_key in self._saved_failed_chunks:
                            del self._saved_failed_chunks[saved_key]
                        if not data:
                            print(f"Not saving empty file {conn.src_file_name!r}")
                        else:
                            out_file = unique_file_name(conn.src_file_name, len(data), file_checksum)
                            if out_file:
                                with open(out_file, 'wb') as stream:
                                    stream.write(data)
                                print(f"Saved {len(data)} bytes from {conn.src_file_name!r} in {out_file!r}")
                    del self._active_connections[conn_triple]

            else:
                print(f"Warning: unknown CFDP packet! {cfdp_pkt!r} <{conn_triple}>")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', type=Path,
                        help='Recorded Cosmos streams, received from 127.0.0.1:7779')
    parser.add_argument('-c', '--cosmos', type=str,
                        help='Connect to Cosmos PREIDENTIFIED router, by default at 127.0.0.1:7779')
    parser.add_argument('-d', '--data', action='store_true',
                        help='Show CFDP data PDU')
    args = parser.parse_args()

    processor = SpaceCFDPPacketProcessor(show_data=args.data)

    if args.cosmos:
        matches = re.match(r'^([0-9.]+):([0-9]+)$', args.cosmos)
        if not matches:
            parser.error(f"Unexpected Cosmos addr:port {args.cosmos!r}")
        addr = matches.group(1)
        port = int(matches.group(2))
        stream = socket.create_connection((addr, port))
        for ccsds_pkt in pump_cosmos_ccsds_packets(stream):
            processor.process_space_to_gnd_pkt(ccsds_pkt)
    elif args.files:
        for filepath in args.files:
            with filepath.open('rb') as stream:
                print(f"Processing {filepath}")
                for ccsds_pkt in pump_cosmos_ccsds_packets(stream):
                    processor.process_space_to_gnd_pkt(ccsds_pkt)
    elif sys.stdin.isatty():
        parser.error("stdin is a TTY, not a stream")
    else:
        for ccsds_pkt in pump_cosmos_ccsds_packets(sys.stdin.buffer):
            processor.process_space_to_gnd_pkt(ccsds_pkt)

    if processor.active_connections:
        print(f"Warning: {len(processor.active_connections)} CFDP connections are still active!")
        for conn_triple, state in processor.active_connections.items():
            print(f"* {conn_triple} for {state.src_file_name!r}")
