#!/usr/bin/env python3
import IPython
import argparse
import json
from pathlib import Path
import re
import socket
import time
from datetime import datetime

from scapy.all import *
import recover_cfdp_downloads


from apids import APID_NAMES
from all_packets import *


# Synchronisation pattern for UART_TO_CI
UART_SYNC_PATTERN = b'\xde\xad\xbe\xef'


# Sanity checks on Scapy packet constructors, on UART_TO_CI:ENABLE_TELEMETRY command packet
assert bytes(CCSDSPacket(apid=0x1d7, cmd_func_code=7)) == b'\x19\xd7\xc0\x00\x00\x01\x07\xf7'
assert bytes(CCSDSPacket() / UART_TO_CI_ENABLE_TELEMETRY_CmdPkt()) == b'\x19\xd7\xc0\x00\x00\x01\x07\xf7'


def build_kit_to_enable_telemetry():
    """
    Send a KIT_TO ENABLE_TELEMETRY command, for "That's not on my calendar" challenge

    Dump from COSMOS:

        00000000: 18 80 C0 00 00 11 07 9A 31 32 37 2E 30 2E 30 2E
        00000010: 31 00 00 00 00 00 00 00
    """
    # The payload is the local IP address where telemetry data is sent
    # Func code 7 = KIT_TO_ENABLE_OUTPUT_CMD_FC
    pkt = CCSDSPacket(apid=0x80, cmd_func_code=7) / b'127.0.0.1\x00\x00\x00\x00\x00\x00\x00'
    payload = bytes(pkt)
    assert payload.hex() == '1880c0000011079a3132372e302e302e3100000000000000', "Sanity check failed"
    return payload


def safe_bytes2line(data):
    """Converts bytes to text that can be safely printed on a line on a terminal"""
    if all(32 <= x < 127 for x in data):
        return data.decode('ascii')
    return repr(data)


def show_ccsds_packet(self, pkt, show_hk, hide_ee):
    """Display a received CCSDS packet on the console"""
    apid_name = pkt.fieldtype['apid'].i2repr(pkt, pkt.apid)
    # Change to a less-visible color when showing Housekeeping messages
    is_hk = apid_name.endswith('_HK_TLM') or apid_name.startswith('HK_COMBINED_PKT') or apid_name == 'PL_IF_PL_STATUS_TLM'  # noqa
    if is_hk and not show_hk:
        # Do not show housekeeping telemetry messages
        return

    is_ee = apid_name in (
        'EPHEM_TLM_EPHEM',
        'EYASSAT_IF_ADCS_TLM',
        'EYASSAT_IF_CAL_TBL_TLM',
        'EYASSAT_IF_INTERNAL_TLM',
        'EYASSAT_IF_POWER_TLM',
        'EYASSAT_IF_TEMPS_TLM',
    )
    if is_ee and hide_ee:
        # Do not show Ephem and Eyassat_if regular telemetry packets
        return

    if apid_name == 'CFE_EVS_LONG_EVENT_MSG':
        # Log message
        assert isinstance(pkt.payload, CFE_EVS_EVENT_MSG_PKT_TlmPkt)
        app_name = safe_bytes2line(pkt.payload.PKT_ID_APP_NAME.rstrip(b'\0'))
        msg = safe_bytes2line(pkt.payload.MESSAGE.rstrip(b'\0'))
        print(f"[< {apid_name}={pkt.apid:#x} {pkt.seq_count:#x}] [{pkt.payload.PKT_ID_SPACECRAFT_ID}/{pkt.payload.PKT_ID_PROCESSOR_ID}/{app_name} {pkt.payload.PKT_ID_EVENT_TYPE}.{pkt.payload.PKT_ID_EVENT_ID}] {msg}")  # noqa
        return

    if apid_name == 'FM_DIR_LIST_TLM':
        # Show the result of a "ls" command
        assert isinstance(pkt.payload, FM_DIR_LIST_PKT_TlmPkt)
        dirname = safe_bytes2line(pkt.payload.DIRNAME.rstrip(b'\0'))
        packet_files = pkt.payload.PACKETFILES
        total_files = pkt.payload.TOTALFILES
        first_file = pkt.payload.FIRSTFILE
        print(f"[< {apid_name}={pkt.apid:#x} {pkt.seq_count:#x}] ls {dirname}: {packet_files}/{total_files} from {first_file}")  # noqa
        for file_idx in range(packet_files):
            file_name = safe_bytes2line(getattr(pkt.payload, f'FILE{file_idx}_NAME').rstrip(b'\0'))
            file_size = getattr(pkt.payload, f'FILE{file_idx}_SIZE')
            file_mod_time = getattr(pkt.payload, f'FILE{file_idx}_MOD_TIME')
            file_mode = getattr(pkt.payload, f'FILE{file_idx}_MODE')
            print(f"  {file_size} {file_mode} {file_mod_time} {file_name}")
        return

    # By default, use repr(pkt.payload)
    print("{}[< {}={:#x} {:#x}] {}{}".format(
        "\033[34m" if is_hk else "",
        apid_name,
        pkt.apid,
        pkt.seq_count,
        repr(pkt.payload),
        "\033[m" if is_hk else "",))


class Codec(Sink):
    def __init__(self, show_hk=False, hide_ee=False, add_sync=False):
        super().__init__()
        self.show_hk = show_hk
        self.hide_ee = hide_ee
        self.add_sync = add_sync
        self._buf = b""

    def push(self, msg: bytes):
        self._buf += msg
        # print(f"\033[35mReceiving {len(msg)}/{len(self._buf)} bytes: {msg[:42].hex()}\033[m")
        while True:
            if self.add_sync:
                if len(self._buf) < 10:
                    return
                if not self._buf.startswith(UART_SYNC_PATTERN):
                    # Drop bytes until the synchronisation pattern appears
                    try:
                        drop_bytes = self._buf.index(UART_SYNC_PATTERN)
                    except ValueError:
                        drop_bytes = len(self._buf)
                    assert drop_bytes != 0
                    print(f"[<] Dropping {drop_bytes} bytes: {self._buf[:drop_bytes].hex()}")
                    self._buf = self._buf[drop_bytes:]
                    continue

                current_ccsds_buffer = self._buf[4:]
            else:
                current_ccsds_buffer = self._buf

            pkt = CCSDSPacket(current_ccsds_buffer)
            pkt_size = pkt.pkt_length + 7
            if pkt_size > len(current_ccsds_buffer):
                return
            pkt = CCSDSPacket(current_ccsds_buffer[:pkt_size])
            self._buf = current_ccsds_buffer[pkt_size:]

            # Show packet only if some fields changed from the reference
            if pkt.version != 0 or pkt.pkttype != 0 or pkt.has_sec_header != 1 or pkt.segm_flags != 3:
                print("UNEXPECTED HEADER FIELDS in received CCSDS packet:")
                pkt.show()

            try:
                show_ccsds_packet(self, pkt, show_hk=self.show_hk, hide_ee=self.hide_ee)
            except Exception as exc:
                print(f"ERROR: Exception while showing a packet: {exc!r}")
                raise
            self._high_send(pkt)

    def high_push(self, msg: Packet):
        msg_bytes = bytes(msg)
        if self.add_sync:
            # Add 4 bytes of synchronisation
            msg_bytes = UART_SYNC_PATTERN + msg_bytes
        self._send(msg_bytes)


class FileRecorder(Sink):
    def __init__(self):
        super().__init__()
        self.processor = recover_cfdp_downloads.SpaceCFDPPacketProcessor()

    def high_push(self, msg: Packet):
        self.processor.process_space_to_gnd_pkt(msg)


class CosmosCodec(Sink):
    """Implement Cosmos PREIDENTIFIED protocol

    Documentation:
        https://cosmosrb.com/docs/chaining/
    Source:
        https://github.com/BallAerospace/COSMOS/blob/v4.4.2/lib/cosmos/interfaces/protocols/preidentified_protocol.rb
        https://github.com/BallAerospace/COSMOS/blob/v4.4.2/spec/interfaces/protocols/preidentified_protocol_spec.rb
    """
    def __init__(self, show_hk=False, hide_ee=False):
        super().__init__()
        self.show_hk = show_hk
        self.hide_ee = hide_ee
        self._buf = b""

    def push(self, msg: bytes):
        self._buf += msg
        # print(f"\033[35mReceiving {len(msg)}/{len(self._buf)} bytes: {msg[:42].hex()}\033[m")
        while len(self._buf) >= 15:
            try:
                pkt = CosmosPreidentifiedPkt(self._buf)
                pkt_size = pkt.packet_size()
            except Exception:
                break
            if pkt_size > len(self._buf):
                break
            pkt = CosmosPreidentifiedPkt(self._buf[:pkt_size])
            self._buf = self._buf[pkt_size:]

            try:
                self.show_packet(pkt)
            except Exception as exc:
                print(f"ERROR: Exception while showing a packet: {exc!r}")
                raise

    def high_push(self, msg: Packet):
        # Craft a fake Cosmos packet, to encapsulated the CCSDS packet
        # target_name = 'FAKE'
        # packet_name = 'FAKE'
        target_name = 'CFE_ES'
        packet_name = 'NOOP'
        for pktclass in COSMOS_TARGET_PACKETS_REV:
            if msg.haslayer(pktclass):
                target_name, packet_name = COSMOS_TARGET_PACKETS_REV[pktclass]
                break
        if target_name == 'PDU' and packet_name == 'CF_SPACE_TO_GND_PDU':
            # Nope, it is ground to space (otherwise Cosmos fails to route the packet)
            packet_name = 'CF_GND_TO_SPACE_PDU'
        cosmos_pkt = CosmosPreidentifiedPkt(
            target_name=target_name,
            packet_name=packet_name,
            data=bytes(msg))
        msg_bytes = bytes(cosmos_pkt)
        self._send(msg_bytes)

    def show_packet(self, pkt):
        """Display a received Cosmos packet on the console"""
        target_name = pkt.target_name.decode('utf-8', 'replace')
        packet_name = pkt.packet_name.decode('utf-8', 'replace')
        apid_name = target_name + '_' + packet_name

        if target_name in ('CFDP', 'SYSTEM'):
            # Cosmos special packets
            if apid_name == 'CFDP_CFDP_ENGINE_HK' and not self.show_hk:
                return

            if apid_name == 'SYSTEM_META':
                payload_pkt = SYSTEM_META_TlmPkt(pkt.data)
            elif apid_name == 'SYSTEM_LIMITS_CHANGE':
                payload_pkt = SYSTEM_LIMITS_CHANGE_TlmPkt(pkt.data)
            else:
                payload_pkt = pkt.data
            print(f"[< {apid_name}] {payload_pkt!r}")
            return

        # Get the class associated with the target and packet
        if target_name == 'UNKNOWN' and packet_name == 'UNKNOWN':
            # Decode a CCSDS packet unknown to COSMOS
            pkt_class = None
        else:
            try:
                pkt_class = COSMOS_TARGET_PACKETS[target_name][packet_name]
            except KeyError:
                if self.show_hk:
                    print(f"WARNING: unknown received packet for {target_name}/{packet_name}: {pkt.data!r}")
                return

        ccsds_pkt = CCSDSPacket(pkt.data)
        payload = ccsds_pkt.payload
        if pkt_class is not None and not isinstance(payload, pkt_class):
            print(f"WARNING: mismatched CCSDS decoding: expected {pkt_class!r}, found {ccsds_pkt!r}")

        self._high_send(ccsds_pkt)
        show_ccsds_packet(self, ccsds_pkt, show_hk=self.show_hk, hide_ee=self.hide_ee)


class UnixStreamSourceSink(Source):
    """Use a Unix socket as source and sink
    TODO: upstream this to https://github.com/secdev/scapy/blob/master/scapy/scapypipes.py ?
    """
    def __init__(self, unix_path, name=None):
        Source.__init__(self, name=name)
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(unix_path)
        self.last_recv_time = time.monotonic()

    def push(self, msg):
        # Wait a little bit since the last time some data was received, in order to prevent comm desync
        elapsed_since_recv = time.monotonic() - self.last_recv_time
        while elapsed_since_recv < 1.:
            print(f"\033[35mWaiting before sending {len(msg)} bytes (last recv was {elapsed_since_recv} second ago)\033[m")  # noqa
            time.sleep(1. - elapsed_since_recv)
            elapsed_since_recv = time.monotonic() - self.last_recv_time

        print(f"\033[35mSending {len(msg)} bytes: {msg.hex()}\033[m")
        sent = self.sock.send(msg)
        if sent != len(msg):
            print(f"\033[33;1mWARNING: only {sent}/{len(msg)} bytes were sent to the socket. Sending the remaining...\033[m")  # noqa
            # self.sock.sendall(msg[sent:])
            self.push(msg[sent:])

    def fileno(self):
        return self.sock.fileno()

    def deliver(self):
        # Improve stability by waiting a little bit before receiving data
        # (merge small packets together)
        self.last_recv_time = time.monotonic()
        time.sleep(.005)
        data = self.sock.recv(4096)
        self.last_recv_time = time.monotonic()
        self._send(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--scapy-pipes', action='store_true')
    parser.add_argument('-H', '--show-hk', action='store_true',
                        help='Show Housekeeping telemetry packets')
    parser.add_argument('-E', '--hide-ephem-eyassat', action='store_true',
                        help='Hide Ephem and Eyassat_if regular telemetry packets')
    parser.add_argument('-t', '--tcp', type=str,
                        help='Connect to a TCP/IPv4 socket for communications such as 127.0.0.1:54321')
    parser.add_argument('-x', '--unix', type=Path,
                        help='Communicate to a UNIX socket to communicate instead of TCP')
    parser.add_argument('-s', '--sync', action='store_true',
                        help='Add synchronisation pattern for UART_TO_CI')
    parser.add_argument('-P', '--patch-alignsyncword', action='store_true',
                        help='Fix a bug in alignSyncWord by patching UART_TO_CI app')
    parser.add_argument('-c', '--cosmos', type=str,
                        help='Connect to Cosmos PREIDENTIFIED router, by default at 127.0.0.1:7779')
    parser.add_argument('-w', '--write-files', action='store_true',
                        help='Write files received from space')
    args = parser.parse_args()

    if args.cosmos:
        matches = re.match(r'^([0-9.]+):([0-9]+)$', args.cosmos)
        if not matches:
            parser.error(f"Unexpected Cosmos addr:port {args.cosmos!r}")
        addr = matches.group(1)
        port = int(matches.group(2))
        client = TCPConnectPipe(name="client", addr=addr, port=port)
    elif args.tcp:
        matches = re.match(r'^([0-9.]+):([0-9]+)$', args.tcp)
        if not matches:
            parser.error(f"Unexpected TCP/IPv4 addr:port {args.tcp!r}")
        addr = matches.group(1)
        port = int(matches.group(2))
        client = TCPConnectPipe(name="client", addr=addr, port=port)
    elif args.unix:
        client = UnixStreamSourceSink(str(args.unix), name="client")
    else:
        parser.error("Missing target: use -t/--tcp, -x/--unix or -c/--cosmos to specify one")

    if args.cosmos:
        codec = CosmosCodec(show_hk=args.show_hk, hide_ee=args.hide_ephem_eyassat)
    else:
        codec = Codec(show_hk=args.show_hk, hide_ee=args.hide_ephem_eyassat, add_sync=args.sync)

    display = ConsoleSink(name="display")
    client > codec
    codec > client
    # codec >> display  # codec already displays packets
    if args.write_files:
        file_recorder = FileRecorder()
        codec >> file_recorder

    pt = PipeEngine(codec)
    # pt.graph(type="png", target="> scapy-pipes.png")
    pt.start()

    def send_noops(fast=False):
        """Send many NOOP commands (function code 0)

        Usually these commands display build versions in the event log"""
        for apid_val, apid_name in sorted(APID_NAMES[1].items()):
            if apid_name.endswith('_CMD'):
                if not fast:
                    print("Sending NOOP_CC on {}={:#05x}".format(apid_name, apid_val))
                codec.high_push(CCSDSPacket(pkttype=1, apid=apid_val, cmd_func_code=0))
                if not fast:
                    time.sleep(1)

    def sh(cmd, filename=b'/cf/cmd.tmp'):
        """Send a CFE_ES_SHELL_CC command"""
        if not isinstance(cmd, bytes):
            cmd = cmd.encode()
        if not isinstance(filename, bytes):
            filename = filename.encode()
        pkt = CCSDSPacket() / CFE_ES_SHELL_CmdPkt(CMD_STRING=cmd, OUTPUT_FILENAME=filename)
        codec.high_push(pkt)

    def toggle_hk():
        """Toggle show/hide housekeeping telemetry packets"""
        codec.show_hk = not codec.show_hk

    def toggle_ee():
        """Toggle show/hide Ephem and Eyassat_if regular telemetry packets"""
        codec.hide_ee = not codec.hide_ee

    def enable_telemetry():
        codec.high_push(CCSDSPacket() / UART_TO_CI_ENABLE_TELEMETRY_CmdPkt())

    def disable_telemetry():
        codec.high_push(CCSDSPacket() / UART_TO_CI_DISABLE_TELEMETRY_CmdPkt())

    def ls(dirname=b'/cf', idx=0):
        """List a directory, like '/cf/../etc'

        The result is read using FM_DIR_LIST_TLM packets.

        idx is the index of the first directory entry to put into the TLM packet
        """
        if isinstance(dirname, str):
            dirname = dirname.encode()
        assert isinstance(dirname, bytes)
        codec.high_push(CCSDSPacket() / FM_SEND_DIR_PKT_CmdPkt(DIRECTORY=dirname, DIR_LIST_OFFSET=idx))

    def rm(filename):
        """Remove a file"""
        codec.high_push(CCSDSPacket() / FM_DELETE_FILE_CmdPkt(FILENAME=filename))

    def concat(src1, src2, dst):
        """Concat two files into a destination file"""
        codec.high_push(CCSDSPacket() / FM_CONCAT_FILES_CmdPkt(SOURCE1=src1, SOURCE2=src2, TARGET=dst))

    def file_info(filename):
        """Get information about a file, including its size (in FM_FILE_INFO_TLM)"""
        codec.high_push(CCSDSPacket() / FM_SEND_FILE_INFO_CmdPkt(FILENAME=filename))

    def file_play_cfdp(filename):
        """Put a filename in the CFPD playback queue.

        The file is transmitted through CF_SPACE_TO_GND_PDU packets in chunks of 216 bytes
        """
        codec.high_push(CCSDSPacket() / CF_PLAYBACK_FILE_CmdPkt(SRC_FILENAME=filename))

    def file_upload_cfdp(dst_file_name, data, block_size=400):
        """Upload a file using CFDP

        /eeprom/cf_cfgtable.tbl configures CF with (structure cf_config_table_t):
            (CF_AppData.Tbl)->FlightEntityId = "0.24" (b'\\x00\\x18') for the satellite
        (substructure cf_out_channel_entry_t -> cf_polling_dir_entry_t)
            (CF_AppData.Tbl)->OuCh[0...1].PollDir[0...7].PeerEntityId = "0.21" (b'\\x00\\x15') for the ground
        """
        assert isinstance(data, bytes)  # Ensure no "str" is given to the function
        metadata_pdu = CFDP_MD_PDU(
            segm_ctrl=1,
            file_size=len(data),
            src_file_name='cosmos/temp',
            dst_file_name=dst_file_name)
        metadata_bytes = bytes(metadata_pdu)
        cfdp_packet = CFDP_TlmPkt(
            pdu_type=0,  # File Directive PDU
            direction=0,
            trans_mode=1,
            crc_flag=0,
            data_len=len(metadata_bytes) + 1,
            entity_ids_len=1,
            trans_seq_len=3,
            src_id=b'\x00\x15',
            trans_seq=b'\x00\x00\x00\x01',
            dst_id=b'\x00\x18',
            directive_code=0x07)  # Metadata
        codec.high_push(CCSDSPacket(pkttype=1, apid=0x7fd) / cfdp_packet / metadata_bytes)
        time.sleep(1)  # Give time to the sat to receive the metadata packet

        for offset in range(0, len(data), block_size):
            data_block = data[offset:min(len(data), offset + block_size)]
            cfdp_packet = CFDP_TlmPkt(
                pdu_type=1,  # Data PDU
                direction=0,
                trans_mode=1,
                crc_flag=0,
                data_len=len(data_block) + 4,
                entity_ids_len=1,
                trans_seq_len=3,
                src_id=b'\x00\x15',
                trans_seq=b'\x00\x00\x00\x01',
                dst_id=b'\x00\x18',
                data_file_offset=offset,
                data=data_block)
            codec.high_push(CCSDSPacket(pkttype=1, apid=0x7fd) / cfdp_packet)
            time.sleep(1)

        checksum = cfdp_checksum(data)
        eof_pdu = CFDP_EOF_PDU(
            cond_code=0,
            file_checksum=checksum,
            file_size=len(data))
        eof_bytes = bytes(eof_pdu)
        cfdp_packet = CFDP_TlmPkt(
            pdu_type=0,  # File Directive PDU
            direction=0,
            trans_mode=1,
            crc_flag=0,
            data_len=len(eof_bytes) + 1,
            entity_ids_len=1,
            trans_seq_len=3,
            src_id=b'\x00\x15',
            trans_seq=b'\x00\x00\x00\x01',
            dst_id=b'\x00\x18',
            directive_code=0x04)  # EOF
        codec.high_push(CCSDSPacket(pkttype=1, apid=0x7fd) / cfdp_packet / eof_bytes)

    def file_upload_cfdp_file(dst_file_name, local_file_path, block_size=400):
        with open(local_file_path, 'rb') as stream:
            data = stream.read()
        print(f"Sending {local_file_path!r} to {dst_file_name!r}: {len(data)} in {len(data) / block_size} chunks")
        return file_upload_cfdp(dst_file_name, data, block_size=block_size)

    def file_upload_cfdp_json(dst_file_name, local_file_path, block_size=400):
        with open(local_file_path, 'rb') as stream:
            json_data = json.load(stream)
        data = json.dumps(json_data).encode('ascii')
        print(f"Sending {local_file_path!r} to {dst_file_name!r}: {len(data)} in {len(data) / block_size} chunks")
        return file_upload_cfdp(dst_file_name, data, block_size=block_size)

    def file_upload_cfdp_chunked(dst_file_name, local_file_path, block_size=400, chunk_size=5000):
        """
        Split file into 5k chunks, upload them, concat them
        """
        with open(local_file_path, 'rb') as f:
            contents = f.read()
        nbchunks = 0
        chunknames = []
        if len(contents) <= chunk_size:
            print("Uploading a single chunk...")
            file_upload_cfdp(dst_file_name, contents, block_size=block_size)
            return
        # upload chunks
        while True:
            if len(contents) == 0:
                break
            chunkname = "%s.%d" % (dst_file_name, nbchunks)
            print(f"Uploading chunk #{nbchunks} dstname={chunkname} {contents[:chunk_size]}...")
            chunknames.append(chunkname)
            file_upload_cfdp(chunkname, contents[:chunk_size], block_size=block_size)
            time.sleep(1)
            contents = contents[chunk_size:]
            nbchunks += 1
        # concat
        for i in range(1, nbchunks):
            if i == 1:
                s1 = chunknames[i - 1]
            else:
                s1 = chunknames[i - 1] + 'c'
            s2 = chunknames[i]
            if i == nbchunks - 1:
                # final chunk
                dst = dst_file_name
            else:
                dst = s2 + 'c'
            print(f"Concatenating '{s1}' + '{s2}' -> '{dst}'")
            concat(s1, s2, dst)
            time.sleep(1)

    def dlsym(symbol):
        """Resolve a symbol using OS_SymbolLookup()

        The result is display in the event log (thanks to CFE_EVS_SendEvent()):
        [< CFE_EVS_LONG_EVENT_MSG=8 0x50] [42/3/MM 2.45] Symbol Lookup Command: Name = 'system' Addr = 0x400F61D0
        [< CFE_EVS_LONG_EVENT_MSG=8 0x73] [42/3/MM 2.45] Symbol Lookup Command: Name = 'hard_reset' Addr = 0x40001000
        """
        codec.high_push(CCSDSPacket() / MM_LOOKUP_SYMBOL_CmdPkt(SYMBOL_NAME=symbol))

    def mem_read32(addr):
        """Read 32 bits at a given address.

        For example for the APB memory:
        [< CFE_EVS_LONG_EVENT_MSG=8 0x45] [42/3/MM 2.9] Peek Command: Addr = 0x800FF000 Size = 32 bits Data = 0x0100D040
        """
        codec.high_push(CCSDSPacket() / MM_PEEK_MEM_CmdPkt(
            DATA_SIZE=32,
            ADDR_SYMBOL_NAME='hard_reset',  # hard_reset is a symbol always at 0x40001000
            ADDR_OFFSET=(addr - 0x40001000) & 0xfffffffc))

    def mem_write32(addr, data):
        """Write 32 bits at a given address."""
        if isinstance(data, bytes):
            assert len(data) == 4
            int_data = int.from_bytes(data, 'big')
        elif isinstance(data, int):
            assert 0 <= data <= 0xffffffff
            int_data = data
        else:
            raise ValueError(f"Unsupported data {data!r}")
        codec.high_push(CCSDSPacket() / MM_POKE_MEM_CmdPkt(
            DATA_SIZE=32,
            DATA=int_data,
            ADDR_SYMBOL_NAME='hard_reset',  # hard_reset is a symbol always at 0x40001000
            ADDR_OFFSET=(addr - 0x40001000) & 0xfffffffc))

    def mem_crc(addr, size):
        """Compute a checksum of the memory"""
        codec.high_push(CCSDSPacket() / CS_ONESHOT_CmdPkt(
            ADDRESS=addr, SIZE=size))

    def patch_alignsyncword():
        """Patch function alignSyncWord in uart_to_ci.obj in order to change:
            00010b78  0a bf ff 9b   bcs LAB_000109e4
            if (end - 4 <= dropped_bytes) return 0; // with an int underflow if end < 4
        to:
            00010b78  0c bf ff 9b   bneg LAB_000109e4
            // if (-1 < (int)(dropped_bytes - (end - 4))) return 0;

        In memory, this is located at alignSyncWord+444 = 0x40fca748
        (alignSyncWord is at 0x40FCA58C)
        """
        # Read the previous opcode
        # [42/3/MM 2.9] Peek Command: Addr = 0x40FCA748 Size = 32 bits Data = 0x0ABFFF9B
        codec.high_push(CCSDSPacket() / MM_PEEK_MEM_CmdPkt(
            DATA_SIZE=32, ADDR_SYMBOL_NAME='alignSyncWord', ADDR_OFFSET=444))
        # Write the previous opcode
        # [42/3/MM 2.10] Poke Command: Addr = 0x40FCA748, Size = 8 bits, Data = 0x0C
        codec.high_push(CCSDSPacket() / MM_POKE_MEM_CmdPkt(
            DATA_SIZE=8, ADDR_SYMBOL_NAME='alignSyncWord', ADDR_OFFSET=444, DATA=0x0c))

    # Attitude control related functions
    def disable_reaction_wheel():
        codec.high_push(
            CCSDSPacket() / EYASSAT_IF_ADCS_CTRL_ALG_CmdPkt(CTRL_ALG=0))

    def follow_the_sun(angle=0.0):
        codec.high_push(
            CCSDSPacket() / EYASSAT_IF_ADCS_CTRL_ALG_CmdPkt(CTRL_ALG=2))
        codec.high_push(
            CCSDSPacket() / EYASSAT_IF_ADCS_YAW_CMD_CmdPkt(YAW_CMD=angle))

    def set_wheel_speed(speed=0.0):
        codec.high_push(
            CCSDSPacket() / EYASSAT_IF_ADCS_CTRL_ALG_CmdPkt(CTRL_ALG=1))
        codec.high_push(
            CCSDSPacket() / EYASSAT_IF_ADCS_WHEEL_SPD_CmdPkt(SPD=speed))

    def set_wheel_pwm(pwm=0):
        """
        pass values between -250 and +250
        Using this bypasses the regulation routine
        """
        codec.high_push(
            CCSDSPacket() / EYASSAT_IF_ADCS_PWM_BASELINE_CmdPkt(PWM=pwm))

    def set_magnetorquers(x=0, y=0):
        if x not in [-1, 0, 1, 2] or y not in [-1, 0, 1, 2]:
            print("invalid values for magnetorquers")
            return
        if x == -1:
            x = 2
        if y == -1:
            y = 2
        codec.high_push(
            CCSDSPacket() / EYASSAT_IF_ADCS_X_ROD_CmdPkt(X_ROD=x))
        codec.high_push(
            CCSDSPacket() / EYASSAT_IF_ADCS_Y_ROD_CmdPkt(Y_ROD=y))

    def set_controller_settings(
            p=None, i=None, d=None, alg=None, delta_t=None, extra=None,
            deadband=None, deadband_scale=None):
        if p is not None:
            codec.high_push(
                CCSDSPacket() / EYASSAT_IF_ADCS_P_CONST_CmdPkt(P_CONST=p))
        time.sleep(0.5)
        if i is not None:
            codec.high_push(
                CCSDSPacket() / EYASSAT_IF_ADCS_I_CONST_CmdPkt(I_CONST=i))
        time.sleep(0.5)
        if d is not None:
            codec.high_push(
                CCSDSPacket() / EYASSAT_IF_ADCS_D_CONST_CmdPkt(D_CONST=d))
        time.sleep(0.5)
        if alg is not None:
            codec.high_push(
                CCSDSPacket() / EYASSAT_IF_ADCS_CTRL_ALG_CmdPkt(CTRL_ALG=alg))
        time.sleep(0.5)
        if delta_t is not None:
            codec.high_push(
                CCSDSPacket() / EYASSAT_IF_ADCS_DELTA_T_CmdPkt(DELTA_T=delta_t))
        time.sleep(0.5)
        if extra is not None:
            codec.high_push(
                CCSDSPacket() / EYASSAT_IF_ADCS_EXTRA_CmdPkt(EXTRA=extra))
        time.sleep(0.5)
        if deadband is not None:
            codec.high_push(
                CCSDSPacket() / EYASSAT_IF_ADCS_DEADBAND_CmdPkt(DEADBAND=deadband))
        time.sleep(0.5)
        if deadband_scale is not None:
            codec.high_push(
                CCSDSPacket() / EYASSAT_IF_ADCS_DEADBAND_SCALE_FACTOR_CmdPkt(DEADBAND=deadband_scale))

    def set_eyassat_time(hour=None, minute=None, second=None):
        curtime = datetime.utcnow()
        if hour is None:
            hour = curtime.hour
        codec.high_push(
            CCSDSPacket() / EYASSAT_IF_HOUR_CmdPkt(HOUR=hour))
        time.sleep(0.2)
        if minute is None:
            minute = curtime.minute
        codec.high_push(
            CCSDSPacket() / EYASSAT_IF_MINUTE_CmdPkt(MINUTE=minute))
        time.sleep(0.2)
        if second is None:
            second = curtime.second
        codec.high_push(
            CCSDSPacket() / EYASSAT_IF_SECOND_CmdPkt(SECOND=second))

    def eyassat_load_tbl(filename=b"/cf/es_adcs_tbl.json", loadtype=1):
        """Load TBL:
        ID : "Table ID. 0 is first table registered"
        TYPE : "0=Replace Table, 1=Update Records"
        """
        codec.high_push(
            CCSDSPacket() / EYASSAT_IF_LOAD_TBL_CmdPkt(ID=0, TYPE=loadtype, FILENAME=filename))

    def cosmos_enable_radio():
        """Send a Cosmos PREIDENTIFIED PACKET to set the RADIO to RATE=LOW (0), POWER=HIGH (1)"""
        if not isinstance(codec, CosmosCodec):
            print("CLI error: not connected to COSMOS!")
            return
        codec._send(bytes(CosmosPreidentifiedPkt(target_name='RADIO', packet_name='CONFIG', data=b'RSC:\x00\x01')))

    def cosmos_adcs_recalibrate(filename):
        """Load a new ADCS calibration file on the satellite"""
        try:
            f = open(filename, "rb")
            file_upload_cfdp("/cf/es_adcs_tbl.json", f.read())
            codec.high_push(CCSDSPacket() / EYASSAT_IF_LOAD_TBL_CmdPkt())
        except Exception as exc:
            print(f"ERROR: Exception Error uploading calibration file: {exc!r}")
            raise

    def implant_dump(symbol, addr=0, size=58):
        codec.high_push(CCSDSPacket() / IMP_CmdPkt() / IMP_DUMP_SubPkt(SYMBOL=symbol, address=addr, size=size))

    def implant_unlock(password):
        codec.high_push(CCSDSPacket() / IMP_CmdPkt() / IMP_CHECK_SubPkt(password=password))

    def implant_pwn_exec():
        # Unlock the sat through an overflow in exec
        codec.high_push(CCSDSPacket() / IMP_CmdPkt() / IMP_EXEC_SubPkt(
            subcmds=b'\x06\xbc\x40\x06\xB3\x44' + b'\x03\x00'*5 + b'\x06\xbc\x40\x06\xB3\x44' + b'\x03\x00'*5 + b'\0' * (64-6-6-20) + struct.pack('>I', 62)))  # noqa

    def power_pl_if(onoff):
        codec.high_push(CCSDSPacket() / PL_IF_POWER_CmdPkt(ON_OFF=onoff))

    def uart_w(cmd):
        if not isinstance(cmd, bytes):
            cmd = cmd.encode()
        for i, c in enumerate(cmd):
            codec.high_push(CCSDSPacket() / MM_POKE_MEM_CmdPkt(DATA_SIZE=8, DATA=c, ADDR_SYMBOL_NAME='SOLARWINE_Cmdline', ADDR_OFFSET=i))  # noqa
            time.sleep(.5)
        codec.high_push(CCSDSPacket() / MM_POKE_MEM_CmdPkt(DATA_SIZE=32, DATA=len(cmd), ADDR_SYMBOL_NAME='SOLARWINE_Cmdsize', ADDR_OFFSET=0))  # noqa
        time.sleep(.5)
        codec.high_push(CCSDSPacket() / MM_PEEK_MEM_CmdPkt(DATA_SIZE=8, ADDR_SYMBOL_NAME='SOLARWINE_Cmdsize', ADDR_OFFSET=0))  # noqa

    def uart_w4(cmd):
        if not isinstance(cmd, bytes):
            cmd = cmd.encode()
        size_cmd = len(cmd) - (len(cmd) % 4)
        for i in range(0, size_cmd, 4):
            codec.high_push(CCSDSPacket() / MM_POKE_MEM_CmdPkt(
                DATA_SIZE=32,
                DATA=struct.unpack('>I', cmd[i:i + 4])[0],
                ADDR_SYMBOL_NAME='SOLARWINE_Cmdline',
                ADDR_OFFSET=i))
            time.sleep(1)
        for i in range(size_cmd, len(cmd)):
            codec.high_push(CCSDSPacket() / MM_POKE_MEM_CmdPkt(DATA_SIZE=8, DATA=cmd[i],ADDR_SYMBOL_NAME='SOLARWINE_Cmdline', ADDR_OFFSET=i))  # noqa
            time.sleep(1)
        codec.high_push(CCSDSPacket() / MM_POKE_MEM_CmdPkt(DATA_SIZE=32, DATA=len(cmd), ADDR_SYMBOL_NAME='SOLARWINE_Cmdsize', ADDR_OFFSET=0))  # noqa
        time.sleep(1)
        codec.high_push(CCSDSPacket() / MM_PEEK_MEM_CmdPkt(DATA_SIZE=8, ADDR_SYMBOL_NAME='SOLARWINE_Cmdsize', ADDR_OFFSET=0))  # noqa

    if not args.cosmos:  # Do not send packets when connecting to a Cosmos instance
        # codec.high_push(build_kit_to_enable_telemetry())  # "That's not on my calendar" challenge
        enable_telemetry()  # Hack-A-Sat final

        if args.patch_alignsyncword:
            patch_alignsyncword()

        # send_noops(fast=True)
        # sh('id -nu')

    IPython.embed()
