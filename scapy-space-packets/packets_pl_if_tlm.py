from scapy.all import *
from ccsds_base import CCSDSPacket


class PL_IF_HK_TLM_PKT_TlmPkt(Packet):
    """Pl_if App

    app = PL_IF
    command = HK_TLM_PKT
    msg_id = PL_IF_HK_TLM_MID = 0x09de = 0x0800 + 0x1de
    """
    name = "PL_IF_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT 16 UINT "Count of valid commands received since startup or the last reset counter command"
        ShortField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT 16 UINT "Count of invalid commands received since startup or the last reset counter command"
        ShortField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM LAST_TBL_ACTION 8 UINT  "Last table action: 1=Register, 2=Load, 3=Dump"
        ByteField("LAST_TBL_ACTION", 0),
        # APPEND_ITEM LAST_TBL_STATUS 8 UINT  "Last table action status: 0=Undefined, 1=Invalid, 2=Valid"
        ByteField("LAST_TBL_STATUS", 0),
        # APPEND_ITEM PLIF_OBJ_EXEC_CNT  16 UINT "Count of Pl_if object executions"
        ShortField("PLIF_OBJ_EXEC_CNT", 0),
    ]


bind_layers(CCSDSPacket, PL_IF_HK_TLM_PKT_TlmPkt, pkttype=0, apid=478)


class PL_IF_PL_STATUS_PKT_TlmPkt(Packet):
    """Pl_if PL status packet

    app = PL_IF
    command = PL_STATUS_PKT
    msg_id = PL_IF_PL_STATUS_TLM_MID = 0x09e4 = 0x0800 + 0x1e4
    """
    name = "PL_IF_PL_STATUS_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM BUSY_STATUS 8 UINT "Latest busy status"
        ByteField("BUSY_STATUS", 0),
        # APPEND_ITEM IMG_READY_STATUS 8 UINT "Latest image ready status"
        ByteField("IMG_READY_STATUS", 0),
        # APPEND_ITEM BAD_ADDR_STATUS 8 UINT "Latest bad address status"
        ByteField("BAD_ADDR_STATUS", 0),
        # APPEND_ITEM ALIVE_STATUS 8 UINT "Aliveness status of the payload"
        ByteField("ALIVE_STATUS", 0),
        # APPEND_ITEM DOWNLINK_STATUS 8 UINT "Downlink status of the payload"
        ByteField("DOWNLINK_STATUS", 0),
        # STATE NO_IMAGE 0
        # STATE IN_PROGRESS 1
        # STATE COMPLETE 2
        # APPEND_ITEM PAD 24 UINT "Pad"
        X3BytesField("PAD", 0),
        # APPEND_ITEM IMAGE_SIZE 32 UINT "Image size as reported by the payload"
        IntField("IMAGE_SIZE", 0),
        # APPEND_ITEM CURRENT_DOWNLINK_ADDRESS 32 UINT "Address currently being downlinked from the payload"
        IntField("CURRENT_DOWNLINK_ADDRESS", 0),
    ]


bind_layers(CCSDSPacket, PL_IF_PL_STATUS_PKT_TlmPkt, pkttype=0, apid=484)
