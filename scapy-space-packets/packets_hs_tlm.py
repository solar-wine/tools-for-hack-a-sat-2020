from scapy.all import *
from ccsds_base import CCSDSPacket


class HS_HK_TLM_PKT_TlmPkt(Packet):
    """Housekeeping Packet Structure

    app = HS
    command = HK_TLM_PKT
    msg_id = HS_HK_TLM_MID = 0x08ad = 0x0800 + 0x0ad
    """
    name = "HS_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT 8 UINT "HS Application Command Counter."
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT 8 UINT "HS Application Command Error Counter."
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM CURRENTAPPMONSTATE 8 UINT "Status of HS Critical Application Monitor."
        ByteField("CURRENTAPPMONSTATE", 0),
        # APPEND_ITEM CURRENTEVENTMONSTATE 8 UINT "Status of HS Critical Events Monitor."
        ByteField("CURRENTEVENTMONSTATE", 0),
        # APPEND_ITEM CURRENTALIVENESSSTATE 8 UINT "Status of HS Aliveness Indicator."
        ByteField("CURRENTALIVENESSSTATE", 0),
        # APPEND_ITEM CURRENTCPUHOGSTATE 8 UINT "Status of HS Hogging Indicator."
        ByteField("CURRENTCPUHOGSTATE", 0),
        # APPEND_ITEM STATUSFLAGS 8 UINT "Internal HS Error States."
        ByteField("STATUSFLAGS", 0),
        # APPEND_ITEM SPAREBYTES 8 UINT "Alignment Spares."
        ByteField("SPAREBYTES", 0),
        # APPEND_ITEM RESETSPERFORMED 16 UINT "HS Performed Processor Reset Count."
        ShortField("RESETSPERFORMED", 0),
        # APPEND_ITEM MAXRESETS 16 UINT "HS Maximum Processor Reset Count."
        ShortField("MAXRESETS", 0),
        # APPEND_ITEM EVENTSMONITOREDCOUNT 32 UINT "Total count of Event Messages Monitored by the Critical Events Monitor."
        IntField("EVENTSMONITOREDCOUNT", 0),
        # APPEND_ITEM INVALIDEVENTMONCOUNT 32 UINT "Total count of Invalid Event Monitors Monitored by the Critical Events Monitor."
        IntField("INVALIDEVENTMONCOUNT", 0),
        # APPEND_ARRAY_ITEM APPMONENABLES 32 UINT 32 "Enable states of App Monitor Entries."
        StrFixedLenField("APPMONENABLES__0", b"", 4),  # FIXME: XNBytesField should be better, if supported
        # APPEND_ITEM MSGACTEXEC 32 UINT "Number of Software Bus Message Actions Executed."
        IntField("MSGACTEXEC", 0),
        # APPEND_ITEM UTILCPUAVG 32 UINT "Current CPU Utilization Average."
        IntField("UTILCPUAVG", 0),
        # APPEND_ITEM UTILCPUPEAK 32 UINT "Current CPU Utilization Peak."
        IntField("UTILCPUPEAK", 0),
        # APPEND_ARRAY_ITEM EXECCOUNTS 32 UINT 1024 "Execution Counters"
        StrFixedLenField("EXECCOUNTS__0", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__1", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__2", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__3", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__4", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__5", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__6", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__7", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__8", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__9", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__10", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__11", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__12", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__13", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__14", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__15", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__16", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__17", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__18", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__19", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__20", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__21", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__22", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__23", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__24", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__25", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__26", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__27", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__28", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__29", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__30", b"", 4),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("EXECCOUNTS__31", b"", 4),  # FIXME: XNBytesField should be better, if supported
    ]


bind_layers(CCSDSPacket, HS_HK_TLM_PKT_TlmPkt, pkttype=0, apid=173)
