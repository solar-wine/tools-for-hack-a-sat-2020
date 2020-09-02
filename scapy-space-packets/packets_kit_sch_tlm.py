from scapy.all import *
from ccsds_base import CCSDSPacket


class KIT_SCH_HK_TLM_PKT_TlmPkt(Packet):
    """Scheduler Housekeeping Packet

    app = KIT_SCH
    command = HK_TLM_PKT
    msg_id = KIT_SCH_HK_TLM_MID = 0x0899 = 0x0800 + 0x099
    """
    name = "KIT_SCH_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT 16 UINT        "Command Count"
        ShortField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT 16 UINT        "Error Count"
        ShortField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM MSG_TBL_LOAD_STATUS 8 UINT     "0=Undefined, 1=Invalid, 1=Valid"
        ByteField("MSG_TBL_LOAD_STATUS", 0),
        # APPEND_ITEM SCH_TBL_LOAD_STATUS 8 UINT     "0=Undefined, 1=Invalid, 1=Valid"
        ByteField("SCH_TBL_LOAD_STATUS", 0),
        # APPEND_ITEM MSG_TBL_LOAD_ATTR_ERRS 16 UINT  "Count of attribute errors in last msg table load"
        ShortField("MSG_TBL_LOAD_ATTR_ERRS", 0),
        # APPEND_ITEM SCH_TBL_LOAD_ATTR_ERRS 16 UINT  "Count of attribute errors in last msg table load"
        ShortField("SCH_TBL_LOAD_ATTR_ERRS", 0),
        # APPEND_ITEM SLOTS_PROCESSED_CNT      32 UINT "Total # of Schedule Slots (Minor Frames) Processed."
        IntField("SLOTS_PROCESSED_CNT", 0),
        # APPEND_ITEM SCH_ACTIVITY_SUCCESS_CNT 32 UINT "Number of successfully performed activities."
        IntField("SCH_ACTIVITY_SUCCESS_CNT", 0),
        # APPEND_ITEM SCH_ACTIVITY_FAILURE_CNT 32 UINT "Number of unsuccessful activities attempted."
        IntField("SCH_ACTIVITY_FAILURE_CNT", 0),
        # APPEND_ITEM VALID_MAJOR_FRAME_CNT    32 UINT "Number of valid major frames processed."
        IntField("VALID_MAJOR_FRAME_CNT", 0),
        # APPEND_ITEM MISSED_MAJOR_FRAME_CNT   32 UINT "Number of missing Major Frame tones"
        IntField("MISSED_MAJOR_FRAME_CNT", 0),
        # APPEND_ITEM UNEXPECT_MAJOR_FRAME_CNT 32 UINT "Number of unexpected Major Frame tones"
        IntField("UNEXPECT_MAJOR_FRAME_CNT", 0),
        # APPEND_ITEM SCH_TBL_PASS_CNT         32 UINT "Number of times Schedule Table has been processed"
        IntField("SCH_TBL_PASS_CNT", 0),
        # APPEND_ITEM CONSEC_NOISY_FRAME_CNT   32 UINT "Number of times tone arrives in wrong slot?"
        IntField("CONSEC_NOISY_FRAME_CNT", 0),
        # APPEND_ITEM SKIPPED_SLOT_CNT         16 UINT "Number of times that slots were skipped."
        ShortField("SKIPPED_SLOT_CNT", 0),
        # APPEND_ITEM MULTIPLE_SLOTS_CNT       16 UINT "Number of times that multiple slots processed."
        ShortField("MULTIPLE_SLOTS_CNT", 0),
        # APPEND_ITEM SAME_SLOT_CNT            16 UINT "Number of times SCH woke up in the same slot as last time"
        ShortField("SAME_SLOT_CNT", 0),
        # APPEND_ITEM SYNC_ATTEMPTS_LEFT       16 UINT "Remaining attempts to resynch major frame?"
        ShortField("SYNC_ATTEMPTS_LEFT", 0),
        # APPEND_ITEM LAST_SYNC_MET_SLOT       16 UINT "Slot number where Time Sync last occurred."
        ShortField("LAST_SYNC_MET_SLOT", 0),
        # APPEND_ITEM IGNORE_MAJOR_FRAME        8 UINT "Major Frame too noisy to trust."
        ByteField("IGNORE_MAJOR_FRAME", 0),
        # APPEND_ITEM UNEXPECTED_MAJOR_FRAME    8 UINT ""
        ByteField("UNEXPECTED_MAJOR_FRAME", 0),
    ]


bind_layers(CCSDSPacket, KIT_SCH_HK_TLM_PKT_TlmPkt, pkttype=0, apid=153)
