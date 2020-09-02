from scapy.all import *
from ccsds_base import CCSDSPacket


class HK_HK_TLM_PKT_TlmPkt(Packet):
    """Housekeeping telemetry packet

    app = HK
    command = HK_TLM_PKT
    msg_id = HK_HK_TLM_MID = 0x089b = 0x0800 + 0x09b
    """
    name = "HK_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT 8 UINT "Application command counter"
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT 8 UINT "Application command error counter"
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM PADDING_16                 16 UINT "Padding to align to 32-bit"
        ShortField("PADDING_16", 0),
        # APPEND_ITEM COMBINE_PKT_SENT_CNT       16 UINT "Count of combined tlm pkts sent"
        ShortField("COMBINE_PKT_SENT_CNT", 0),
        # APPEND_ITEM MISSING_DATA_CNT           16 UINT "Count of combined tlm pkts sent"
        ShortField("MISSING_DATA_CNT", 0),
        # APPEND_ITEM MEM_POOL_HANDLE            32 UINT "Memory pool handle used to get mempool diagnostics"
        IntField("MEM_POOL_HANDLE", 0),
    ]


bind_layers(CCSDSPacket, HK_HK_TLM_PKT_TlmPkt, pkttype=0, apid=155)


class HK_COMBO_PKT_1_TlmPkt(Packet):
    """Housekeeping Combined Packet 1

    app = HK
    command = COMBO_PKT_1
    msg_id = HK_COMBINED_PKT1_MID = 0x089c = 0x0800 + 0x09c
    """
    name = "HK_COMBO_PKT_1_TlmPkt"
    fields_desc = [
        # APPEND_ITEM EVS_CMD_VALID_COUNT   8 UINT "EVS Command Valid Counter."
        ByteField("EVS_CMD_VALID_COUNT", 0),
        # APPEND_ITEM EVS_CMD_ERROR_COUNT   8 UINT "EVS Command Error Counter."
        ByteField("EVS_CMD_ERROR_COUNT", 0),
        # APPEND_ITEM EVS_MSG_FORMAT_MODE                    8 UINT "EVS Event message format mode (short/long)."
        ByteField("EVS_MSG_FORMAT_MODE", 0),
        # APPEND_ITEM EVS_MSG_TRUNC_CNT                      8 UINT "EVS Event message truncation counter."
        ByteField("EVS_MSG_TRUNC_CNT", 0),
        # APPEND_ITEM TIME_CMD_VALID_COUNT  8 UINT "TIME Command Valid Counter."
        ByteField("TIME_CMD_VALID_COUNT", 0),
        # APPEND_ITEM TIME_CMD_ERROR_COUNT  8 UINT "TIME Command Error Counter."
        ByteField("TIME_CMD_ERROR_COUNT", 0),
        # APPEND_ITEM TIME_CLK_STATE_FLAGS                  16 UINT "TIME State Flags."
        ShortField("TIME_CLK_STATE_FLAGS", 0),
        # APPEND_ITEM SB_CMD_VALID_COUNT    8 UINT "SB Command Valid Counter."
        ByteField("SB_CMD_VALID_COUNT", 0),
        # APPEND_ITEM SB_CMD_ERROR_COUNT    8 UINT "SB Command Error Counter."
        ByteField("SB_CMD_ERROR_COUNT", 0),
        # APPEND_ITEM SB_NO_SUBSCRIBERS_CNT                  8 UINT "SB Count pkts sent with no subscribers."
        ByteField("SB_NO_SUBSCRIBERS_CNT", 0),
        # APPEND_ITEM SB_MSG_SEND_ERR_CNT                    8 UINT "SB Count of message send errors."
        ByteField("SB_MSG_SEND_ERR_CNT", 0),
        # APPEND_ITEM ES_CMD_VALID_COUNT    8 UINT "ES Command Valid Counter."
        ByteField("ES_CMD_VALID_COUNT", 0),
        # APPEND_ITEM ES_CMD_ERROR_COUNT    8 UINT "ES Command Error Counter."
        ByteField("ES_CMD_ERROR_COUNT", 0),
        # APPEND_ITEM ES_CFE_CORE_CHECKSUM                  16 UINT "ES Checksum of cFE Core Code."
        ShortField("ES_CFE_CORE_CHECKSUM", 0),
        # APPEND_ITEM TBL_CMD_VALID_COUNT   8 UINT "TBL Command Valid Counter."
        ByteField("TBL_CMD_VALID_COUNT", 0),
        # APPEND_ITEM TBL_CMD_ERROR_COUNT   8 UINT "TBL Command Error Counter."
        ByteField("TBL_CMD_ERROR_COUNT", 0),
        # APPEND_ITEM TBL_NUM_REG_TABLES                    16 UINT "TBL Number of Tables Registered."
        ShortField("TBL_NUM_REG_TABLES", 0),
    ]


bind_layers(CCSDSPacket, HK_COMBO_PKT_1_TlmPkt, pkttype=0, apid=156)


class HK_COMBO_PKT_2_TlmPkt(Packet):
    """Housekeeping Combined Packet 2

    app = HK
    command = COMBO_PKT_2
    msg_id = HK_COMBINED_PKT2_MID = 0x089d = 0x0800 + 0x09d
    """
    name = "HK_COMBO_PKT_2_TlmPkt"
    fields_desc = [
        # APPEND_ITEM INSTR_STATE 8 UINT  ""
        ByteField("INSTR_STATE", 0),
        # STATE OFF          0
        # STATE INITIALIZING 1
        # STATE READY        2
        # APPEND_ITEM SCI_STATE 8 UINT  ""
        ByteField("SCI_STATE", 0),
        # STATE OFF    0
        # STATE START  1
        # STATE STOP   2
        # STATE ON     3
        # APPEND_ITEM FAULT  8 UINT  ""
        ByteField("FAULT", 0),
        # STATE FALSE   0
        # STATE TRUE    1
        # APPEND_ITEM SPARE  8 UINT  ""
        ByteField("SPARE", 0),
        # APPEND_ITEM CTRL_MODE       16 UINT "Control Mode"
        ShortField("CTRL_MODE", 0),
        # STATE Init 1
        # STATE TBD  2
        # APPEND_ITEM WBN_1       32 FLOAT "wbn[0]"
        IEEEFloatField("WBN_1", 0.0),
        # FORMAT_STRING "%.6f"
        # APPEND_ITEM WBN_2       32 FLOAT "wbn[1]"
        IEEEFloatField("WBN_2", 0.0),
        # FORMAT_STRING "%.6f"
        # APPEND_ITEM WBN_3       32 FLOAT "wbn[2]"
        IEEEFloatField("WBN_3", 0.0),
        # FORMAT_STRING "%.6f"
        # APPEND_ITEM QBR_1       32 FLOAT "qbr[0]"
        IEEEFloatField("QBR_1", 0.0),
        # FORMAT_STRING "%.6f"
        # APPEND_ITEM QBR_2       32 FLOAT "qbr[1]"
        IEEEFloatField("QBR_2", 0.0),
        # FORMAT_STRING "%.6f"
        # APPEND_ITEM QBR_3       32 FLOAT "qbr[2]"
        IEEEFloatField("QBR_3", 0.0),
        # FORMAT_STRING "%.6f"
        # APPEND_ITEM QBR_4       32 FLOAT "qbr[3]"
        IEEEFloatField("QBR_4", 0.0),
        # FORMAT_STRING "%.6f"
        # APPEND_ITEM ATT_ERR_X   32 FLOAT "qbr[0]*2.0"
        IEEEFloatField("ATT_ERR_X", 0.0),
        # FORMAT_STRING "%.6f"
        # APPEND_ITEM ATT_ERR_Y   32 FLOAT "qbr[1]*2.0"
        IEEEFloatField("ATT_ERR_Y", 0.0),
        # FORMAT_STRING "%.6f"
        # APPEND_ITEM ATT_ERR_Z   32 FLOAT "qbr[2]*2.0"
        IEEEFloatField("ATT_ERR_Z", 0.0),
        # FORMAT_STRING "%.6f"
    ]


bind_layers(CCSDSPacket, HK_COMBO_PKT_2_TlmPkt, pkttype=0, apid=157)
