from scapy.all import *
from ccsds_base import CCSDSPacket


class LC_HK_TLM_PKT_TlmPkt(Packet):
    """Housekeeping Packet Structure

    app = LC
    command = HK_TLM_PKT
    msg_id = LC_HK_TLM_MID = 0x08a7 = 0x0800 + 0x0a7
    """
    name = "LC_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT      8 UINT "LC Application Command Counter"
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT      8 UINT "LC Application Command Error Counter"
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM APP_STATE            8 UINT "Current LC application operating state"
        ByteField("APP_STATE", 0),
        # STATE UNDEF    0
        # STATE ACTIVE   1 GREEN
        # STATE PASSIVE  2 YELLOW
        # STATE DISABLED 3 RED
        # APPEND_ITEM PAD8                 8 UINT "8-bit pad"
        ByteField("PAD8", 0),
        # APPEND_ARRAY_ITEM WP_RESULTS     8 UINT 352 "Packed watchpoint results data, 2 bits per watchpoint."
        StrFixedLenField("WP_RESULTS", b"", 44),  # FIXME: XNBytesField should be better, if supported
        # ITEM WP_3_RESULT  128 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_2_RESULT  130 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_1_RESULT  132 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_0_RESULT  134 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_7_RESULT  136 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_6_RESULT  138 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_5_RESULT  140 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_4_RESULT  142 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_11_RESULT 144 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_10_RESULT 146 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_9_RESULT  148 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_8_RESULT  150 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_15_RESULT 152 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_14_RESULT 154 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_13_RESULT 156 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM WP_12_RESULT 158 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # APPEND_ARRAY_ITEM AP_RESULTS     8 UINT 704 "Packed actionpoint results data, 4 bits per actionpoint."
        StrFixedLenField("AP_RESULTS", b"", 88),  # FIXME: XNBytesField should be better, if supported
        # ITEM AP_1_STATE  480 2 UINT
        # STATE UNUSED   0
        # STATE ACTIVE   1
        # STATE PASSIVE  2
        # STATE DISABLED 3
        # ITEM AP_1_RESULT 482 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM AP_0_STATE  484 2 UINT
        # STATE UNUSED   0
        # STATE ACTIVE   1
        # STATE PASSIVE  2
        # STATE DISABLED 3
        # ITEM AP_0_RESULT 486 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM AP_3_STATE  488 2 UINT
        # STATE UNUSED   0
        # STATE ACTIVE   1
        # STATE PASSIVE  2
        # STATE DISABLED 3
        # ITEM AP_3_RESULT 490 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # ITEM AP_2_STATE  492 2 UINT
        # STATE UNUSED   0
        # STATE ACTIVE   1
        # STATE PASSIVE  2
        # STATE DISABLED 3
        # ITEM AP_2_RESULT 494 2 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # STATE ERROR 2
        # STATE STALE 3
        # APPEND_ITEM PASSIVE_RTS_EXE_CNT 16 UINT "Total count of RTS sequences not initiated because the LC state is set to LC_STATE_PASSIVE."
        ShortField("PASSIVE_RTS_EXE_CNT", 0),
        # APPEND_ITEM WPS_IN_USE          16 UINT "How many watchpoints are currently in effect."
        ShortField("WPS_IN_USE", 0),
        # APPEND_ITEM ACTIVE_APS          16 UINT "How many actionpoints are currently active."
        ShortField("ACTIVE_APS", 0),
        # APPEND_ITEM PAD16               16 UINT "16 bit pad"
        ShortField("PAD16", 0),
        # APPEND_ITEM AP_SAMPLE_CNT       32 UINT "Total count of Actionpoints sampled."
        IntField("AP_SAMPLE_CNT", 0),
        # APPEND_ITEM MONITORED_MSG_CNT   32 UINT "Total count of messages monitored for watchpoints."
        IntField("MONITORED_MSG_CNT", 0),
        # APPEND_ITEM RTS_EXE_CNT         32 UINT "Total count of RTS sequences initiated."
        IntField("RTS_EXE_CNT", 0),
    ]


bind_layers(CCSDSPacket, LC_HK_TLM_PKT_TlmPkt, pkttype=0, apid=167)
