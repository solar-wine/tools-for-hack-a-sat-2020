from scapy.all import *
from ccsds_base import CCSDSPacket


class UART_TO_CI_HK_TLM_PKT_TlmPkt(Packet):
    """Telemetry Output Command Ingest Housekeeping Packet

    app = UART_TO_CI
    command = HK_TLM_PKT
    msg_id = UART_TO_CI_HK_TLM_MID = 0x09dc = 0x0800 + 0x1dc
    """
    name = "UART_TO_CI_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT      16 UINT  "Command Count"
        ShortField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT      16 UINT  "Error Count"
        ShortField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM LAST_TBL_LOAD_STATUS  8 UINT  "0=Undefined, 1=No, 1=Yes"
        ByteField("LAST_TBL_LOAD_STATUS", 0),
        # APPEND_ITEM SPARE_BYTE            8 UINT  ""
        ByteField("SPARE_BYTE", 0),
        # APPEND_ITEM LAST_TBL_LOAD_ATTR_ERRS 16 UINT  "Count of attribute errors in last table load"
        ShortField("LAST_TBL_LOAD_ATTR_ERRS", 0),
        # APPEND_ITEM RECV_CMD_CNT         32 UINT "Count of cmd messages received on uart"
        IntField("RECV_CMD_CNT", 0),
        # APPEND_ITEM RECV_CMD_ERR_CNT     32 UINT "Count of erroneous cmd messages received on uart"
        IntField("RECV_CMD_ERR_CNT", 0),
        # APPEND_ITEM SENT_TLM_CNT         32 UINT "Count of tlm messages sent on uart"
        IntField("SENT_TLM_CNT", 0),
        # APPEND_ITEM BAUD_RATE            32 UINT "Configured baud rate for the command and telemetry console"
        IntField("BAUD_RATE", 0),
    ]


bind_layers(CCSDSPacket, UART_TO_CI_HK_TLM_PKT_TlmPkt, pkttype=0, apid=476)
