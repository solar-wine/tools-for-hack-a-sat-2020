from scapy.all import *
from ccsds_base import CCSDSPacket


class CFE_EVS_HK_TLM_PKT_TlmPkt(Packet):
    """Housekeeping data (general status) autonomously sent

    app = CFE_EVS
    command = HK_TLM_PKT
    msg_id = CFE_EVS_HK_TLM_MID = 0x0801 = 0x0800 + 0x001
    """
    name = "CFE_EVS_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT 8 UINT "EVS Command Counter."
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT 8 UINT "EVS Command Error Counter."
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM MSG_FMT_MODE    8 UINT "Event message format mode (short/long)."
        ByteField("MSG_FMT_MODE", 0),
        # STATE Short 0
        # STATE Long  1
        # APPEND_ITEM MSG_TRUNC_CTR   8 UINT "Event message truncation counter."
        ByteField("MSG_TRUNC_CTR", 0),
        # APPEND_ITEM UNREG_APP_CTR   8 UINT "Unregistered application message send counter."
        ByteField("UNREG_APP_CTR", 0),
        # APPEND_ITEM OUTPUT_PORT     8 UINT "Output port mask."
        ByteField("OUTPUT_PORT", 0),
        # APPEND_ITEM LOG_FULL_FLAG   8 UINT "Local event log full flag."
        ByteField("LOG_FULL_FLAG", 0),
        # STATE False 0
        # STATE True  1
        # APPEND_ITEM LOG_MODE        8 UINT "Local event logging mode (overwrite/discard)."
        ByteField("LOG_MODE", 0),
        # STATE Overwrite 0
        # STATE Discard   1
        # APPEND_ITEM MSG_SEND_CTR   16 UINT "Event message send counter."
        ShortField("MSG_SEND_CTR", 0),
        # APPEND_ITEM LOG_OVFL_CTR   16 UINT "Local event log overflow counter."
        ShortField("LOG_OVFL_CTR", 0),
        # APPEND_ITEM LOG_ENA         8 UINT "Current event log enable/disable state."
        ByteField("LOG_ENA", 0),
        # APPEND_ITEM SPARE1          8 UINT "Padding for 32 bit boundary."
        ByteField("SPARE1", 0),
        # APPEND_ITEM SPARE2          8 UINT "Padding for 32 bit boundary."
        ByteField("SPARE2", 0),
        # APPEND_ITEM SPARE3          8 UINT "Padding for 32 bit boundary."
        ByteField("SPARE3", 0),
        # APPEND_ARRAY_ITEM APPDATA  16 UINT 1024 "Array of registered application table data."
        ShortField("APPDATA__0", 0),
        ShortField("APPDATA__1", 0),
        ShortField("APPDATA__2", 0),
        ShortField("APPDATA__3", 0),
        ShortField("APPDATA__4", 0),
        ShortField("APPDATA__5", 0),
        ShortField("APPDATA__6", 0),
        ShortField("APPDATA__7", 0),
        ShortField("APPDATA__8", 0),
        ShortField("APPDATA__9", 0),
        ShortField("APPDATA__10", 0),
        ShortField("APPDATA__11", 0),
        ShortField("APPDATA__12", 0),
        ShortField("APPDATA__13", 0),
        ShortField("APPDATA__14", 0),
        ShortField("APPDATA__15", 0),
        ShortField("APPDATA__16", 0),
        ShortField("APPDATA__17", 0),
        ShortField("APPDATA__18", 0),
        ShortField("APPDATA__19", 0),
        ShortField("APPDATA__20", 0),
        ShortField("APPDATA__21", 0),
        ShortField("APPDATA__22", 0),
        ShortField("APPDATA__23", 0),
        ShortField("APPDATA__24", 0),
        ShortField("APPDATA__25", 0),
        ShortField("APPDATA__26", 0),
        ShortField("APPDATA__27", 0),
        ShortField("APPDATA__28", 0),
        ShortField("APPDATA__29", 0),
        ShortField("APPDATA__30", 0),
        ShortField("APPDATA__31", 0),
        ShortField("APPDATA__32", 0),
        ShortField("APPDATA__33", 0),
        ShortField("APPDATA__34", 0),
        ShortField("APPDATA__35", 0),
        ShortField("APPDATA__36", 0),
        ShortField("APPDATA__37", 0),
        ShortField("APPDATA__38", 0),
        ShortField("APPDATA__39", 0),
        ShortField("APPDATA__40", 0),
        ShortField("APPDATA__41", 0),
        ShortField("APPDATA__42", 0),
        ShortField("APPDATA__43", 0),
        ShortField("APPDATA__44", 0),
        ShortField("APPDATA__45", 0),
        ShortField("APPDATA__46", 0),
        ShortField("APPDATA__47", 0),
        ShortField("APPDATA__48", 0),
        ShortField("APPDATA__49", 0),
        ShortField("APPDATA__50", 0),
        ShortField("APPDATA__51", 0),
        ShortField("APPDATA__52", 0),
        ShortField("APPDATA__53", 0),
        ShortField("APPDATA__54", 0),
        ShortField("APPDATA__55", 0),
        ShortField("APPDATA__56", 0),
        ShortField("APPDATA__57", 0),
        ShortField("APPDATA__58", 0),
        ShortField("APPDATA__59", 0),
        ShortField("APPDATA__60", 0),
        ShortField("APPDATA__61", 0),
        ShortField("APPDATA__62", 0),
        ShortField("APPDATA__63", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_HK_TLM_PKT_TlmPkt, pkttype=0, apid=1)


class CFE_EVS_EVENT_MSG_PKT_TlmPkt(Packet):
    """Event Message Telemetry Packet

    app = CFE_EVS
    command = EVENT_MSG_PKT
    msg_id = CFE_EVS_EVENT_MSG_MID = 0x0808 = 0x0800 + 0x008
    """
    name = "CFE_EVS_EVENT_MSG_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM PKT_ID_APP_NAME      160 STRING "Application name"
        StrFixedLenField("PKT_ID_APP_NAME", b"", 20),
        # APPEND_ITEM PKT_ID_EVENT_ID       16 UINT   "Numerical event identifier"
        ShortField("PKT_ID_EVENT_ID", 0),
        # APPEND_ITEM PKT_ID_EVENT_TYPE     16 UINT   "Numerical event type identifier"
        ShortField("PKT_ID_EVENT_TYPE", 0),
        # APPEND_ITEM PKT_ID_SPACECRAFT_ID  32 UINT   "Spacecraft identifier"
        IntField("PKT_ID_SPACECRAFT_ID", 0),
        # APPEND_ITEM PKT_ID_PROCESSOR_ID   32 UINT   "Numerical processor identifier"
        IntField("PKT_ID_PROCESSOR_ID", 0),
        # APPEND_ITEM MESSAGE 976 STRING "Message text string"
        StrFixedLenField("MESSAGE", b"", 122),
        # APPEND_ITEM SPARE1 8 UINT "Structure padding."
        ByteField("SPARE1", 0),
        # APPEND_ITEM SPARE2 8 UINT "Structure padding."
        ByteField("SPARE2", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_EVENT_MSG_PKT_TlmPkt, pkttype=0, apid=8)
