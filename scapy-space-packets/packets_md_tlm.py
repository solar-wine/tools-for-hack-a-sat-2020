from scapy.all import *
from ccsds_base import CCSDSPacket


class MD_HK_TLM_PKT_TlmPkt(Packet):
    """Memory Dwell Housekeeping Telemetry

    app = MD
    command = HK_TLM_PKT
    msg_id = MD_HK_TLM_MID = 0x0890 = 0x0800 + 0x090
    """
    name = "MD_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_ERROR_COUNT  8 UINT "Error Command Count"
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM CMD_VALID_COUNT  8 UINT "Valid Command Count"
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM DWELL_ENA_MASK  16 UINT "Each bit in bit mask enables a table 0x0001=TBL1 enable bit,0x0002=TBL2 enable bit, 0x0004=TBL3 enable bit,0x0008=TBL4 enable bit, etc."
        ShortField("DWELL_ENA_MASK", 0),
        # APPEND_ARRAY_ITEM DWELLTBLADDRCOUNT 16 UINT 64 "Number of dwell addresses in table"
        ShortField("DWELLTBLADDRCOUNT__0", 0),
        ShortField("DWELLTBLADDRCOUNT__1", 0),
        ShortField("DWELLTBLADDRCOUNT__2", 0),
        ShortField("DWELLTBLADDRCOUNT__3", 0),
        # APPEND_ARRAY_ITEM NUMWAITSPERPKT 16 UINT 64 "Number of delay counts in table"
        ShortField("NUMWAITSPERPKT__0", 0),
        ShortField("NUMWAITSPERPKT__1", 0),
        ShortField("NUMWAITSPERPKT__2", 0),
        ShortField("NUMWAITSPERPKT__3", 0),
        # APPEND_ARRAY_ITEM BYTECOUNT 16 UINT 64 "Number of bytes of data specified by table"
        ShortField("BYTECOUNT__0", 0),
        ShortField("BYTECOUNT__1", 0),
        ShortField("BYTECOUNT__2", 0),
        ShortField("BYTECOUNT__3", 0),
        # APPEND_ARRAY_ITEM DWELLPKTOFFSET 16 UINT 64 "Current write offset within dwell pkt data region"
        ShortField("DWELLPKTOFFSET__0", 0),
        ShortField("DWELLPKTOFFSET__1", 0),
        ShortField("DWELLPKTOFFSET__2", 0),
        ShortField("DWELLPKTOFFSET__3", 0),
        # APPEND_ARRAY_ITEM DWELLTBLENTRY 16 UINT 64 "Next dwell table entry to be processed"
        ShortField("DWELLTBLENTRY__0", 0),
        ShortField("DWELLTBLENTRY__1", 0),
        ShortField("DWELLTBLENTRY__2", 0),
        ShortField("DWELLTBLENTRY__3", 0),
        # APPEND_ARRAY_ITEM COUNTDOWN 16 UINT 64 "Current value of countdown timer"
        ShortField("COUNTDOWN__0", 0),
        ShortField("COUNTDOWN__1", 0),
        ShortField("COUNTDOWN__2", 0),
        ShortField("COUNTDOWN__3", 0),
    ]


bind_layers(CCSDSPacket, MD_HK_TLM_PKT_TlmPkt, pkttype=0, apid=144)


class MD_DWELL_PKT_TlmPkt(Packet):
    """Memory Dwell Telemetry Packet format

    app = MD
    command = DWELL_PKT
    msg_id = MD_DWELL_PKT_MID_1 = 0x0891 = 0x0800 + 0x091
    """
    name = "MD_DWELL_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM TABLE_ID 8 UINT "TableId from 1 to MD_NUM_DWELL_TABLES."
        ByteField("TABLE_ID", 0),
        # APPEND_ITEM ADDR_COUNT 8 UINT "Number of addresses being sent - 1..MD_DWELL_TABLE_SIZE valid."
        ByteField("ADDR_COUNT", 0),
        # APPEND_ITEM BYTE_COUNT 16 UINT "Number of bytes of dwell data contained in packet."
        ShortField("BYTE_COUNT", 0),
        # APPEND_ITEM INTERVAL 32 UINT "Number of counts between packet sends."
        IntField("INTERVAL", 0),
        # APPEND_ITEM SIGNATURE 256 STRING "Custom string to identify the dwell packet"
        StrFixedLenField("SIGNATURE", b"", 32),
        # APPEND_ITEM DATA_00_0 8 UINT "Dwell data [0] byte [0]"
        ByteField("DATA_00_0", 0),
        # APPEND_ITEM DATA_00_1 8 UINT "Dwell data [0] byte [1]"
        ByteField("DATA_00_1", 0),
        # APPEND_ITEM DATA_00_2 8 UINT "Dwell data [0] byte [2]"
        ByteField("DATA_00_2", 0),
        # APPEND_ITEM DATA_00_3 8 UINT "Dwell data [0] byte [3]"
        ByteField("DATA_00_3", 0),
        # APPEND_ITEM DATA_01_0 8 UINT "Dwell data [1] byte [0]"
        ByteField("DATA_01_0", 0),
        # APPEND_ITEM DATA_01_1 8 UINT "Dwell data [1] byte [1]"
        ByteField("DATA_01_1", 0),
        # APPEND_ITEM DATA_01_2 8 UINT "Dwell data [1] byte [2]"
        ByteField("DATA_01_2", 0),
        # APPEND_ITEM DATA_01_3 8 UINT "Dwell data [1] byte [3]"
        ByteField("DATA_01_3", 0),
        # APPEND_ITEM DATA_02_0 8 UINT "Dwell data [2] byte [0]"
        ByteField("DATA_02_0", 0),
        # APPEND_ITEM DATA_02_1 8 UINT "Dwell data [2] byte [1]"
        ByteField("DATA_02_1", 0),
        # APPEND_ITEM DATA_02_2 8 UINT "Dwell data [2] byte [2]"
        ByteField("DATA_02_2", 0),
        # APPEND_ITEM DATA_02_3 8 UINT "Dwell data [2] byte [3]"
        ByteField("DATA_02_3", 0),
        # APPEND_ITEM DATA_03_0 8 UINT "Dwell data [3] byte [0]"
        ByteField("DATA_03_0", 0),
        # APPEND_ITEM DATA_03_1 8 UINT "Dwell data [3] byte [1]"
        ByteField("DATA_03_1", 0),
        # APPEND_ITEM DATA_03_2 8 UINT "Dwell data [3] byte [2]"
        ByteField("DATA_03_2", 0),
        # APPEND_ITEM DATA_03_3 8 UINT "Dwell data [3] byte [3]"
        ByteField("DATA_03_3", 0),
    ]


bind_layers(CCSDSPacket, MD_DWELL_PKT_TlmPkt, pkttype=0, apid=145)
