from scapy.all import *
from ccsds_base import CCSDSPacket


class CFE_SB_HK_TLM_PKT_TlmPkt(Packet):
    """Housekeeping data (general status) autonomously sent

    app = CFE_SB
    command = HK_TLM_PKT
    msg_id = CFE_SB_HK_TLM_MID = 0x0803 = 0x0800 + 0x003
    """
    name = "CFE_SB_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT     8 UINT "Count of valid commands received."
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT     8 UINT "Count of invalid commands received."
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM NO_SUBSCRIBE_CNT    8 UINT "Count pkts sent with no subscribers."
        ByteField("NO_SUBSCRIBE_CNT", 0),
        # APPEND_ITEM MSG_SEND_ERR_CNT    8 UINT "Count of message send errors."
        ByteField("MSG_SEND_ERR_CNT", 0),
        # APPEND_ITEM MSG_RECV_ERR_CNT    8 UINT "Count of message receive errors."
        ByteField("MSG_RECV_ERR_CNT", 0),
        # APPEND_ITEM INTERNAL_ERR_CNT    8 UINT "Count of queue read or write errors."
        ByteField("INTERNAL_ERR_CNT", 0),
        # APPEND_ITEM CREATE_PIPE_ERR_CNT 8 UINT "Count of errors in create pipe API."
        ByteField("CREATE_PIPE_ERR_CNT", 0),
        # APPEND_ITEM SUBSCRIBE_ERR_CNT   8 UINT "Count of errors in subscribe API."
        ByteField("SUBSCRIBE_ERR_CNT", 0),
        # APPEND_ITEM SPARE               8 UINT "Spare Byte."
        ByteField("SPARE", 0),
        # APPEND_ITEM DUP_SUBSCRIBE_CNT   8 UINT "Count of duplicate subscriptions."
        ByteField("DUP_SUBSCRIBE_CNT", 0),
        # APPEND_ARRAY_ITEM SPARE2ALIGN   8 UINT 16 "Spare bytes to ensure alignment."
        StrFixedLenField("SPARE2ALIGN", b"", 2),  # FIXME: XNBytesField should be better, if supported
        # APPEND_ITEM PIPE_OVFL_ERR_CNT  16 UINT "Count of pipe overflow errors."
        ShortField("PIPE_OVFL_ERR_CNT", 0),
        # APPEND_ITEM MSG_LIM_ERR_CNT    16 UINT "Count of msg id to pipe errors."
        ShortField("MSG_LIM_ERR_CNT", 0),
        # APPEND_ITEM MEM_POOL_HANDLE    32 UINT "Handle to SB's Memory Pool."
        IntField("MEM_POOL_HANDLE", 0),
        # APPEND_ITEM MEM_IN_USE         32 UINT "Memory in use."
        IntField("MEM_IN_USE", 0),
        # APPEND_ITEM UNMARKED_MEM       32 UINT "cfg param CFE_SB_BUF_MEMORY_BYTES minus Peak Memory in use"
        IntField("UNMARKED_MEM", 0),
    ]


bind_layers(CCSDSPacket, CFE_SB_HK_TLM_PKT_TlmPkt, pkttype=0, apid=3)


class CFE_SB_PREV_SUBSCRIBE_TLM_PKT_TlmPkt(Packet):
    """SB Previous Subscriptions Packet sent in response to a SEND_PREV_SUBS command

    app = CFE_SB
    command = PREV_SUBSCRIBE_TLM_PKT
    msg_id = CFE_SB_ALLSUBS_TLM_MID = 0x080d = 0x0800 + 0x00d
    """
    name = "CFE_SB_PREV_SUBSCRIBE_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM PKT_SEGMENT    32 UINT "Pkt number(starts at 1) in the series."
        IntField("PKT_SEGMENT", 0),
        # APPEND_ITEM TOTAL_SEGMENTS 32 UINT "Total number of pkts needed to complete the request."
        IntField("TOTAL_SEGMENTS", 0),
        # APPEND_ITEM ENTRIES        32 UINT "Number of entries in the pkt."
        IntField("ENTRIES", 0),
        # APPEND_ARRAY_ITEM ENTRY 40 UINT 800 "Array of CFE_SB_SubEntries_t entries."
        StrFixedLenField("ENTRY__0", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__1", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__2", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__3", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__4", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__5", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__6", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__7", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__8", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__9", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__10", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__11", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__12", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__13", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__14", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__15", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__16", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__17", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__18", b"", 5),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("ENTRY__19", b"", 5),  # FIXME: XNBytesField should be better, if supported
    ]


bind_layers(CCSDSPacket, CFE_SB_PREV_SUBSCRIBE_TLM_PKT_TlmPkt, pkttype=0, apid=13)


# TELEMETRY CFE_SB STATS_TLM_PKT BIG_ENDIAN "SB Statistics Telemetry Packet sent in response to a SEND_STATS command"
#   TLMHDR CFE_SB_STATS_TLM_MID
#   APPEND_ITEM MSG_IDS_IN_USE            32 UINT "Current number of MsgIds with a destination."
#   APPEND_ITEM PEAK_MSG_IDS_IN_USE       32 UINT "Peak number of MsgIds with a destination."
#   APPEND_ITEM MAX_MSG_IDS_ALLOWED       32 UINT "cFE Cfg Param CFE_SB_MAX_MSG_IDS"
#   APPEND_ITEM PIPES_IN_USE              32 UINT "Number of pipes currently in use."
#   APPEND_ITEM PEAK_PIPES_IN_USE         32 UINT "Peak number of pipes since last reboot."
#   APPEND_ITEM MAX_PIPES_ALLOWED         32 UINT "cFE Cfg Param CFE_SB_MAX_PIPES"
#   APPEND_ITEM MEM_IN_USE                32 UINT "Memory bytes currently in use for SB msg transfers."
#   APPEND_ITEM PEAK_MEM_IN_USE           32 UINT "Peak memory bytes in use for SB msg transfers."
#   APPEND_ITEM MAX_MEM_ALLOWED           32 UINT "cFE Cfg Param CFE_SB_BUF_MEMORY_BYTES"
#   APPEND_ITEM SUBSCRIPTIONS_IN_USE      32 UINT "Number of current subscriptions."
#   APPEND_ITEM PEAK_SUBSCRIPTIONS_IN_USE 32 UINT "Peak number of subscriptions."
#   APPEND_ITEM MAX_SUBSCRIPTIONS_ALLOWED 32 UINT "product of CFE_SB_MAX_MSG_IDS and CFE_SB_MAX_DEST_PER_PKT"
#   APPEND_ITEM SB_BUFFERS_IN_USE         32 UINT "Number of SB message buffers currently in use."
#   APPEND_ITEM PEAK_SB_BUFFERS_IN_USE    32 UINT "Max number of SB message buffers in use."
#   APPEND_ITEM MAX_PIPE_DEPTH_ALLOWED    32 UINT "cFE Cfg Param CFE_SB_MAX_PIPE_DEPTH"
#   <%
#     max_pipes = Osk::Cfg.get_fsw_cfg_int_param(@APP_PREFIX_STR, "CFE_SB_MAX_PIPES")
#     append_items = ""
#     for i in 0..(max_pipes-1)
#       append_items << "APPEND_ITEM \"PIPE#{i}_ID\"            8 UINT  \"Pipe Identfier\"" << "\n"
#       append_items << "APPEND_ITEM \"PIPE#{i}_SPARE\"         8 UINT  \"Spare for byte alignment\"" << "\n"
#       append_items << "APPEND_ITEM \"PIPE#{i}_DEPTH\"        16 UINT  \"Max messages in pipe\"" << "\n"
#       append_items << "APPEND_ITEM \"PIPE#{i}_IN_USE\"       16 UINT  \"Current messages in pipe\"" << "\n"
#       append_items << "APPEND_ITEM \"PIPE#{i}_PEAK_IN_USE\"  16 UINT  \"Peak # of messages in pipe\"" << "\n"
#     end
#   %>
#   <%= append_items %>


class CFE_SB_SUBSCRIBE_REPORT_TLM_PKT_TlmPkt(Packet):
    """SB Subscription Report Packet used by SB-Network

    app = CFE_SB
    command = SUBSCRIBE_REPORT_TLM_PKT
    msg_id = CFE_SB_ONESUB_TLM_MID = 0x080e = 0x0800 + 0x00e
    """
    name = "CFE_SB_SUBSCRIBE_REPORT_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM SUBTYPE         8 UINT  "Subscription or Unsubscription."
        ByteField("SUBTYPE", 0),
        # APPEND_ITEM MSG_ID         16 UINT  "MsgId subscribed or unsubscribe to."
        ShortField("MSG_ID", 0),
        # APPEND_ITEM QOS_PRIORITY    8 UINT  "Specify high(1) or low(0) message priority for off-board routing, currently unused. (Parent: Quality of Service, used only for interprocessor communication.)"
        ByteField("QOS_PRIORITY", 0),
        # APPEND_ITEM QOS_RELIABILITY 8 UINT  "Specify high(1) or low(0) message transfer reliability for off-board routing, currently unused. (Parent: Quality of Service, used only for interprocessor communication.)"
        ByteField("QOS_RELIABILITY", 0),
        # APPEND_ITEM PIPE            8 UINT  "Destination pipe id to send above msg id."
        ByteField("PIPE", 0),
    ]


bind_layers(CCSDSPacket, CFE_SB_SUBSCRIBE_REPORT_TLM_PKT_TlmPkt, pkttype=0, apid=14)
