from scapy.all import *
from ccsds_base import CCSDSPacket


class UART_TO_CI_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = UART_TO_CI
    command = NOOP
    msg_id = UART_TO_CI_CMD_MID = 0x19d7 = 0x1800 + 0x1d7
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "UART_TO_CI_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, UART_TO_CI_NOOP_CmdPkt, pkttype=1, apid=471, cmd_func_code=0)


class UART_TO_CI_RESET_CTRS_CmdPkt(Packet):
    """Reset Counters

    app = UART_TO_CI
    command = RESET_CTRS
    msg_id = UART_TO_CI_CMD_MID = 0x19d7 = 0x1800 + 0x1d7
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "UART_TO_CI_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, UART_TO_CI_RESET_CTRS_CmdPkt, pkttype=1, apid=471, cmd_func_code=1)


class UART_TO_CI_LOAD_TBL_CmdPkt(Packet):
    """Load Packet Table

    app = UART_TO_CI
    command = LOAD_TBL
    msg_id = UART_TO_CI_CMD_MID = 0x19d7 = 0x1800 + 0x1d7
    cmd_func_code = 2
    data_len = 66 bytes
    """
    name = "UART_TO_CI_LOAD_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ID    8  UINT 0 1 0 "Table ID: 0=Packet"
        ByteField("ID", 0),
        # APPEND_PARAMETER TYPE  8  UINT 0 1 1 "0=Replace Table, 1=Update Records"
        ByteField("TYPE", 1),
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/kit_to_pkt_tbl.json" "Full path and file name of table to be loaded"
        StrFixedLenField("FILENAME", b"/cf/kit_to_pkt_tbl.json", 64),
    ]


bind_layers(CCSDSPacket, UART_TO_CI_LOAD_TBL_CmdPkt, pkttype=1, apid=471, cmd_func_code=2)


class UART_TO_CI_DUMP_TBL_CmdPkt(Packet):
    """Dump Packet Table

    app = UART_TO_CI
    command = DUMP_TBL
    msg_id = UART_TO_CI_CMD_MID = 0x19d7 = 0x1800 + 0x1d7
    cmd_func_code = 3
    data_len = 66 bytes
    """
    name = "UART_TO_CI_DUMP_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ID    8  UINT 0 1 0 "0=Packet Table"
        ByteField("ID", 0),
        # APPEND_PARAMETER TYPE  8  UINT 0 1 1 "Unused"
        ByteField("TYPE", 1),
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/kit_to_pkt_tbl~.json" "Full path and file name to receive table dump"
        StrFixedLenField("FILENAME", b"/cf/kit_to_pkt_tbl~.json", 64),
    ]


bind_layers(CCSDSPacket, UART_TO_CI_DUMP_TBL_CmdPkt, pkttype=1, apid=471, cmd_func_code=3)


class UART_TO_CI_ADD_PKT_CmdPkt(Packet):
    """Add an individual packet to packet table

    app = UART_TO_CI
    command = ADD_PKT
    msg_id = UART_TO_CI_CMD_MID = 0x19d7 = 0x1800 + 0x1d7
    cmd_func_code = 4
    data_len = 5 bytes
    """
    name = "UART_TO_CI_ADD_PKT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MSG_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "First word of CCSDS primary header"
        ShortField("MSG_ID", 0),
        # APPEND_PARAMETER QOS_RELIABILITY 8 UINT MIN_UINT8 MAX_UINT8 0 "Quality of Service: Reliability"
        ByteField("QOS_RELIABILITY", 0),
        # APPEND_PARAMETER QOS_PRIORITY    8 UINT MIN_UINT8 MAX_UINT8 0 "Quality of Service: Priority"
        ByteField("QOS_PRIORITY", 0),
        # APPEND_PARAMETER BUF_LIM         8 UINT MIN_UINT8 MAX_UINT8 4 "TO input buffer limit"
        ByteField("BUF_LIM", 4),
    ]


bind_layers(CCSDSPacket, UART_TO_CI_ADD_PKT_CmdPkt, pkttype=1, apid=471, cmd_func_code=4)


class UART_TO_CI_REMOVE_PKT_CmdPkt(Packet):
    """Remove all packets

    app = UART_TO_CI
    command = REMOVE_PKT
    msg_id = UART_TO_CI_CMD_MID = 0x19d7 = 0x1800 + 0x1d7
    cmd_func_code = 5
    data_len = 2 bytes
    """
    name = "UART_TO_CI_REMOVE_PKT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MSG_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "First word of CCSDS primary header"
        ShortField("MSG_ID", 0),
    ]


bind_layers(CCSDSPacket, UART_TO_CI_REMOVE_PKT_CmdPkt, pkttype=1, apid=471, cmd_func_code=5)


class UART_TO_CI_REMOVE_ALL_PKTS_CmdPkt(Packet):
    """Remove all packets

    app = UART_TO_CI
    command = REMOVE_ALL_PKTS
    msg_id = UART_TO_CI_CMD_MID = 0x19d7 = 0x1800 + 0x1d7
    cmd_func_code = 6
    data_len = 0 bytes
    """
    name = "UART_TO_CI_REMOVE_ALL_PKTS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, UART_TO_CI_REMOVE_ALL_PKTS_CmdPkt, pkttype=1, apid=471, cmd_func_code=6)


class UART_TO_CI_ENABLE_TELEMETRY_CmdPkt(Packet):
    """Tell TO to start sending telemetry

    app = UART_TO_CI
    command = ENABLE_TELEMETRY
    msg_id = UART_TO_CI_CMD_MID = 0x19d7 = 0x1800 + 0x1d7
    cmd_func_code = 7
    data_len = 0 bytes
    """
    name = "UART_TO_CI_ENABLE_TELEMETRY_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, UART_TO_CI_ENABLE_TELEMETRY_CmdPkt, pkttype=1, apid=471, cmd_func_code=7)


class UART_TO_CI_DISABLE_TELEMETRY_CmdPkt(Packet):
    """Disable telemetry downlink

    app = UART_TO_CI
    command = DISABLE_TELEMETRY
    msg_id = UART_TO_CI_CMD_MID = 0x19d7 = 0x1800 + 0x1d7
    cmd_func_code = 8
    data_len = 0 bytes
    """
    name = "UART_TO_CI_DISABLE_TELEMETRY_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, UART_TO_CI_DISABLE_TELEMETRY_CmdPkt, pkttype=1, apid=471, cmd_func_code=8)
