"""Packets that are not described in COSMOS files or too complex (like FM packets)"""
import struct
from scapy.all import *
from ccsds_base import CCSDSPacket


class CosmosPreidentifiedPkt(Packet):
    """Cosmos PREIDENTIFIED protocol"""
    name = "CosmosPreidentifiedPkt"
    fields_desc = [
        # Flags: COSMOS4_STORED_FLAG_MASK = 0x80
        BitField("cosmos4_stored_flag", 0, 1),
        # Flags: COSMOS4_EXTRA_FLAG_MASK = 0x40
        BitField("cosmos4_extra_flag", 0, 1),
        BitField("flags", 0, 6),

        IntField("time_seconds", 0),
        IntField("time_microseconds", 0),

        FieldLenField("target_name_len", None, length_of="target_name", fmt="B"),
        StrLenField("target_name", b"", length_from=lambda pkt: pkt.target_name_len),

        FieldLenField("packet_name_len", None, length_of="packet_name", fmt="B"),
        StrLenField("packet_name", b"", length_from=lambda pkt: pkt.packet_name_len),

        FieldLenField("data_len", None, length_of="data", fmt="I"),
        StrLenField("data", b"", length_from=lambda pkt: pkt.data_len),
    ]

    def packet_size(self):
        """Compute the size of a received packet"""
        return 15 + self.target_name_len + self.packet_name_len + self.data_len


def pump_cosmos_ccsds_packets(stream):
    """Decode all packets from a Cosmos "Preidentified router" stream

    stream can be either a input stream (like an opened file) or a socket
    Returns the CCSDS packets, as a generator.
    """
    use_recv = hasattr(stream, 'recv')
    buffer = b''
    while True:
        if use_recv:
            data = stream.recv(4096)
        else:
            data = stream.read(4096)
        if not data:
            break
        buffer += data
        while len(buffer) >= 15:
            try:
                cosmos_pkt = CosmosPreidentifiedPkt(buffer)
                pkt_size = cosmos_pkt.packet_size()
            except Exception:
                break
            if pkt_size > len(buffer):
                break
            cosmos_pkt = CosmosPreidentifiedPkt(buffer[:pkt_size])
            buffer = buffer[pkt_size:]

            if cosmos_pkt.target_name in (b'CFDP', b'SYSTEM'):
                # Cosmos internal packets
                continue
            try:
                ccsds_pkt = CCSDSPacket(cosmos_pkt.data)
            except struct.error as exc:
                print(f"Warning: exception while decoding a CCSDSPacket: {exc}", file=sys.stderr)
                continue
            yield ccsds_pkt


def _gen_FM_DIR_LIST_PKT_files_fields():
    for idx in range(20):  # FswConfigParam::FM_DIR_LIST_PKT_ENTRIES
        # append_items << "APPEND_ITEM FILE#{i}_NAME     512 STRING \"File Name\""        << "\n"
        yield StrFixedLenField(f"FILE{idx}_NAME", b"", 64)
        # append_items << "APPEND_ITEM FILE#{i}_SIZE      32 UINT   \"Size in bytes\""    << "\n"
        yield IntField(f"FILE{idx}_SIZE", 0)
        # append_items << "APPEND_ITEM FILE#{i}_MOD_TIME  32 UINT   \"Time of last mod\"" << "\n"
        yield IntField(f"FILE{idx}_MOD_TIME", 0)
        # append_items << "APPEND_ITEM FILE#{i}_MODE      32 UINT   \"Permissions\""      << "\n"
        yield IntField(f"FILE{idx}_MODE", 0)


class FM_DIR_LIST_PKT_TlmPkt(Packet):
    """Get File Info telemetry packet

    app = FM
    command = DIR_LIST_PKT
    msg_id = FM_DIR_LIST_TLM_MID = 0x088c = 0x0800 + 0x08c
    """
    name = "FM_DIR_LIST_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM DIRNAME 512 STRING "Directory Name"
        StrFixedLenField("DIRNAME", b"", 64),
        # APPEND_ITEM TOTALFILES 32 UINT "Number of files in the directory"
        IntField("TOTALFILES", 0),
        # APPEND_ITEM PACKETFILES 32 UINT "Number of files in this packet"
        IntField("PACKETFILES", 0),
        # APPEND_ITEM FIRSTFILE 32 UINT "Index into directory files of first packet file"
        IntField("FIRSTFILE", 0),
    ] + list(_gen_FM_DIR_LIST_PKT_files_fields())


bind_layers(CCSDSPacket, FM_DIR_LIST_PKT_TlmPkt, pkttype=0, apid=140)


class CFDP_TlmPkt(Packet):
    """Packet received from CFDP subsystem, when transmitting files

    Official spec: https://public.ccsds.org/Pubs/727x0b4.pdf
    cf. function m__gen_pdu_header in https://github.com/nasa/CF/blob/master/fsw/src/PRI/pdu.c
    """
    name = "CFDP_TlmPkt"
    fields_desc = [
        # CCSDS version = first_byte & 0xe0
        BitEnumField("version", 0, 3, {0: "#1"}),

        # PDU type = first_byte & 0x10
        # 0 = File Directive, 1 = File Data
        BitEnumField("pdu_type", 0, 1, {0: "Directive", 1: "Data"}),

        # Direction = first_byte & 0x08
        # 0 = toward file receiver, 1 = toward file sender
        BitEnumField("direction", 0, 1, {0: "receiver", 1: "sender"}),

        # Transmission mode = first_byte & 0x04
        # 0 = acknowledged, 1 = unacknowledged
        BitEnumField("trans_mode", 0, 1, {0: "ack", 1: "unack"}),

        # CRC flag = first_byte & 0x02
        # 0 = CRC not present, 1 = CRC present
        BitField("crc_flag", 0, 1),

        # Reserved for future use = first_byte & 0x01
        BitField("_rfu", 0, 1),

        # PDU Data field length, in octets
        ShortField("data_len", None),

        # Reserved for future use = fourth_byte & 0x80
        BitField("_rfu480", 0, 1),

        # Length of entity IDs = fourth_byte & 0x70
        BitField("entity_ids_len", 0, 3),

        # Reserved for future use = fourth_byte & 0x08
        BitField("_rfu408", 0, 1),

        # Length of Transaction sequence number = fourth_byte & 0x07
        BitField("trans_seq_len", 0, 3),

        # Source entity ID
        StrLenField("src_id", b"", length_from=lambda pkt: pkt.entity_ids_len + 1),

        # Transaction sequence number
        StrLenField("trans_seq", b"", length_from=lambda pkt: pkt.trans_seq_len + 1),

        # Destination entity ID
        StrLenField("dst_id", b"", length_from=lambda pkt: pkt.entity_ids_len + 1),

        # For File Directive: File Directive Code
        ConditionalField(
            ByteEnumField("directive_code", 0, {
                0x04: "EOF",
                0x05: "Finished",
                0x06: "ACK",
                0x07: "Metadata",
                0x08: "NAK",
                0x09: "Prompt",
                0x0c: "Keep Alive",
            }),
            lambda pkt: pkt.pdu_type == 0),

        # For File Data: file offset
        ConditionalField(IntField("data_file_offset", 0), lambda pkt: pkt.pdu_type == 1),

        # For File Data: file payload
        ConditionalField(StrLenField("data", b"", length_from=lambda pkt: pkt.data_len - 4),
                         lambda pkt: pkt.pdu_type == 1),
    ]


bind_layers(CCSDSPacket, CFDP_TlmPkt, pkttype=0, apid=2045)


class CFDP_EOF_PDU(Packet):
    """CFDP End Of File PDU"""
    name = "CFDP_EOF_PDU"
    fields_desc = [
        # Condition Code = first_byte & 0xf0
        BitField("cond_code", 0, 4),

        # Spare = first_byte & 0x0f
        BitField("spare", 0, 4),

        # File checksum
        XIntField("file_checksum", 0),

        # File size
        IntField("file_size", 0),

        # TODO: fault location as TLV, in the remaining bytes
    ]


bind_layers(CFDP_TlmPkt, CFDP_EOF_PDU, pdu_type=0, directive_code=0x04)


class CFDP_MD_PDU(Packet):
    """CFDP Metadata PDU"""
    name = "CFDP_MD_PDU"
    fields_desc = [
        # Segmentation control = first_byte & 0x80
        # 0 = Record boundaries respected, 1 = Record boundaries not respected
        BitField("segm_ctrl", 0, 1),

        # Reserved for future use = first_byte & 0x7f
        BitField("_rfu", 0, 7),

        # File size
        IntField("file_size", 0),

        # Source file name
        FieldLenField("src_file_name_len", None, length_of="src_file_name", fmt="B"),
        StrLenField("src_file_name", b"", length_from=lambda pkt: pkt.src_file_name_len),

        # Destination file name
        FieldLenField("dst_file_name_len", None, length_of="dst_file_name", fmt="B"),
        StrLenField("dst_file_name", b"", length_from=lambda pkt: pkt.dst_file_name_len),

        # TODO: options as TLV, in the remaining bytes
    ]


bind_layers(CFDP_TlmPkt, CFDP_MD_PDU, pdu_type=0, directive_code=0x07)


def cfdp_checksum(data):
    """Compute the checksum used by CFDP

    NASA Implementation:
    https://github.com/nasa/CF/blob/cbda7b9cad82e0d37cd0080e21f79b18eb571b17/fsw/src/PRI/aaa.c#L249
    """
    checksum = 0
    for offset in range(0, len(data), 4):
        data_block = data[offset:min(len(data), offset + 4)]
        if len(data_block) < 4:
            data_block += b'\x00' * (4 - len(data_block))
        checksum = (checksum + int.from_bytes(data_block, 'big')) & 0xffffffff
    return checksum
