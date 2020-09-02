from scapy.all import *
from ccsds_base import CCSDSPacket


class MM_HK_TLM_PKT_TlmPkt(Packet):
    """Housekeeping Packet

    app = MM
    command = HK_TLM_PKT
    msg_id = MM_HK_TLM_MID = 0x0887 = 0x0800 + 0x087
    """
    name = "MM_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT  8 UINT "Valid Command Count"
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT  8 UINT "Error Command Count"
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM LAST_ACTION      8 UINT "Last command action executed"
        ByteField("LAST_ACTION", 0),
        # STATE NONE          0
        # STATE MEM_PEEK      1
        # STATE MEM_POKE      2
        # STATE LD_FR_FILE    3
        # STATE LD_NO_INT     4
        # STATE DMP_TO_FILE   5
        # STATE DMP_TO_EVENT  6
        # STATE MEM_FILL      7
        # STATE SYM_LOOKUP    8
        # STATE SYM_TO_FILE   9
        # STATE EE_WR_ENA    10
        # STATE EE_WR_DIS    11
        # STATE NOOP         12
        # STATE RESET        13
        # APPEND_ITEM MEM_TYPE         8 UINT "Memory type for last command"
        ByteField("MEM_TYPE", 0),
        # APPEND_ITEM ADDRESS         32 UINT "Fully resolved address used for last command"
        IntField("ADDRESS", 0),
        # APPEND_ITEM FILL_PATTERN    32 UINT "Fill pattern used if memory fill command was issued"
        IntField("FILL_PATTERN", 0),
        # APPEND_ITEM BYTES_PROCESSED 32 UINT "Bytes processed for last command"
        IntField("BYTES_PROCESSED", 0),
        # APPEND_ITEM FILENAME 512 STRING "Name of the data file used for last command, where applicable"
        StrFixedLenField("FILENAME", b"", 64),
    ]


bind_layers(CCSDSPacket, MM_HK_TLM_PKT_TlmPkt, pkttype=0, apid=135)
