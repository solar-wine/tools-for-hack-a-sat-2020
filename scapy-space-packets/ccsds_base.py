"""Implement the Space Packet protocol as used by cFE for the Software Bus:

https://github.com/nasa/cFE/blob/6.7.3-bv/fsw/cfe-core/src/sb/cfe_sb_msg_id_util.c refers to:

    "CCSDS Space Packet Protocol 133.0.B-1 with Technical Corrigendum 2, September 2012"

So the relevant specifications are:
* https://web.archive.org/web/20180911191526/https://public.ccsds.org/Pubs/133x0b1c2.pdf
  CCSDS Space Packet Protocol 133.0.B-1
* https://public.ccsds.org/Pubs/133x0b1c2_tc1227.pdf
  Space Packet Protocol Technical Corrigendum 2, September 2012
* https://public.ccsds.org/Pubs/133x0b2.pdf
  CCSDS Space Packet Protocol 133.0-B-2 (Blue Book, June 2020)
"""
from scapy.all import *

from apids import APID_NAMES


class CCSDSPacket(Packet):
    """CCSDS Space packet

    Structures from https://github.com/nasa/cFE/blob/6.7.3-bv/fsw/cfe-core/src/inc/ccsds.h:
        struct CCSDS_PriHdr_t {
            uint16be StreamId;
            uint16be Sequence;
            uint16be Length;
        }
        struct CCSDS_CmdSecHdr_t { // Secondary header for commands
            uint16be Command
        }
        struct CCSDS_TlmSecHdr_t { // Secondary header for telemetry
            uint8  Time[CCSDS_TIME_SIZE];
        }
    """
    name = "CCSDS"
    fields_desc = [
        # CCSDS version = StreamId & 0xe000
        # Version number from https://sanaregistry.org/r/packet_version_number
        # value 0 means "version 1"
        BitEnumField("version", 0, 3, {0: "#1"}),

        # packet type = StreamId & 0x1000
        BitEnumField("pkttype", 1, 1, {0: "TLM", 1: "CMD"}),

        # secondary header present = StreamId & 0x0800
        # Always present of command packets
        BitField("has_sec_header", 1, 1),

        # APID (CCSDS Application ID) = StreamId & 0x07ff
        # https://sanaregistry.org/r/space_packet_protocol_application_process_id
        BitMultiEnumField("apid", 0, 11, APID_NAMES, depends_on=lambda pkt: pkt.pkttype),

        # segmentation flags = Sequence & 0xc000
        # 3 means complete packet (0=continuation, 1=first, 2=last)
        BitField("segm_flags", 3, 2),

        # sequence count = Sequence & 0x3fff
        XBitField("seq_count", 0, 14),

        # packet length word
        ShortField("pkt_length", None),

        # Skip CCSDS_APIDqualifiers_t if MESSAGE_FORMAT_IS_CCSDS_VER_2

        # command function code (high bit is reserved) = Command & 0xff00
        ConditionalField(ByteField("cmd_func_code", 0),
                         lambda pkt: pkt.pkttype == 1 and pkt.has_sec_header),
        # XOR-to-0xff checksum = Command & 0x00ff
        ConditionalField(ByteField("cmd_checksum", 0),
                         lambda pkt: pkt.pkttype == 1 and pkt.has_sec_header),

        # Telemetry time: 32 bits seconds
        ConditionalField(IntField("tlm_time_secs", 0),
                         lambda pkt: pkt.pkttype == 0 and pkt.has_sec_header),
        # Telemetry time: 16 bits subseconds
        ConditionalField(ShortField("tlm_time_subsecs", 0),
                         lambda pkt: pkt.pkttype == 0 and pkt.has_sec_header),
    ]

    def post_build(self, pkt, payload):
        if payload:
            pkt += payload
        # Update length
        if self.pkt_length is None:
            pkt_length = len(pkt) - 7
            pkt = pkt[:4] + pkt_length.to_bytes(2, 'big') + pkt[6:]
        # Update checksum
        if self.pkttype == 1 and self.has_sec_header:
            cksum = 0xff
            for idx, x in enumerate(pkt):
                if idx != 7:
                    cksum ^= x
            pkt = pkt[:7] + cksum.to_bytes(1, 'big') + pkt[8:]
        return pkt
