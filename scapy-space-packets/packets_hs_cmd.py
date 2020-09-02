from scapy.all import *
from ccsds_base import CCSDSPacket


class HS_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = HS
    command = NOOP
    msg_id = HS_CMD_MID = 0x18ae = 0x1800 + 0x0ae
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "HS_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HS_NOOP_CmdPkt, pkttype=1, apid=174, cmd_func_code=0)


class HS_RESET_CTRS_CmdPkt(Packet):
    """Resets the HS housekeeping counters

    app = HS
    command = RESET_CTRS
    msg_id = HS_CMD_MID = 0x18ae = 0x1800 + 0x0ae
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "HS_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HS_RESET_CTRS_CmdPkt, pkttype=1, apid=174, cmd_func_code=1)


class HS_ENABLE_APP_MON_CmdPkt(Packet):
    """Enables the Critical Applications Monitor

    app = HS
    command = ENABLE_APP_MON
    msg_id = HS_CMD_MID = 0x18ae = 0x1800 + 0x0ae
    cmd_func_code = 2
    data_len = 0 bytes
    """
    name = "HS_ENABLE_APP_MON_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HS_ENABLE_APP_MON_CmdPkt, pkttype=1, apid=174, cmd_func_code=2)


class HS_DISABLE_APP_MON_CmdPkt(Packet):
    """Disables the Critical Applications Monitor

    app = HS
    command = DISABLE_APP_MON
    msg_id = HS_CMD_MID = 0x18ae = 0x1800 + 0x0ae
    cmd_func_code = 3
    data_len = 0 bytes
    """
    name = "HS_DISABLE_APP_MON_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HS_DISABLE_APP_MON_CmdPkt, pkttype=1, apid=174, cmd_func_code=3)


class HS_ENABLE_EVENT_MON_CmdPkt(Packet):
    """Enables the Critical Events Monitor

    app = HS
    command = ENABLE_EVENT_MON
    msg_id = HS_CMD_MID = 0x18ae = 0x1800 + 0x0ae
    cmd_func_code = 4
    data_len = 0 bytes
    """
    name = "HS_ENABLE_EVENT_MON_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HS_ENABLE_EVENT_MON_CmdPkt, pkttype=1, apid=174, cmd_func_code=4)


class HS_DISABLE_EVENT_MON_CmdPkt(Packet):
    """Disables the Critical Events Monitor

    app = HS
    command = DISABLE_EVENT_MON
    msg_id = HS_CMD_MID = 0x18ae = 0x1800 + 0x0ae
    cmd_func_code = 5
    data_len = 0 bytes
    """
    name = "HS_DISABLE_EVENT_MON_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HS_DISABLE_EVENT_MON_CmdPkt, pkttype=1, apid=174, cmd_func_code=5)


class HS_ENABLE_ALIVENESS_CmdPkt(Packet):
    """Enables the Aliveness Indicator UART output

    app = HS
    command = ENABLE_ALIVENESS
    msg_id = HS_CMD_MID = 0x18ae = 0x1800 + 0x0ae
    cmd_func_code = 6
    data_len = 0 bytes
    """
    name = "HS_ENABLE_ALIVENESS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HS_ENABLE_ALIVENESS_CmdPkt, pkttype=1, apid=174, cmd_func_code=6)


class HS_DISABLE_ALIVENESS_CmdPkt(Packet):
    """Disables the Aliveness Indicator UART output

    app = HS
    command = DISABLE_ALIVENESS
    msg_id = HS_CMD_MID = 0x18ae = 0x1800 + 0x0ae
    cmd_func_code = 7
    data_len = 0 bytes
    """
    name = "HS_DISABLE_ALIVENESS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HS_DISABLE_ALIVENESS_CmdPkt, pkttype=1, apid=174, cmd_func_code=7)


class HS_RESET_RESETS_PERFORMED_CmdPkt(Packet):
    """Resets the count of HS performed resets maintained by HS

    app = HS
    command = RESET_RESETS_PERFORMED
    msg_id = HS_CMD_MID = 0x18ae = 0x1800 + 0x0ae
    cmd_func_code = 8
    data_len = 0 bytes
    """
    name = "HS_RESET_RESETS_PERFORMED_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HS_RESET_RESETS_PERFORMED_CmdPkt, pkttype=1, apid=174, cmd_func_code=8)


class HS_SET_MAX_RESETS_CmdPkt(Packet):
    """Sets the max allowable count of processor resets to the provided value

    app = HS
    command = SET_MAX_RESETS
    msg_id = HS_CMD_MID = 0x18ae = 0x1800 + 0x0ae
    cmd_func_code = 9
    data_len = 2 bytes
    """
    name = "HS_SET_MAX_RESETS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MAXRESETS 16 UINT MIN_UINT16 MAX_UINT16 0 " "
        ShortField("MAXRESETS", 0),
    ]


bind_layers(CCSDSPacket, HS_SET_MAX_RESETS_CmdPkt, pkttype=1, apid=174, cmd_func_code=9)


class HS_ENABLE_CPU_HOG_CmdPkt(Packet):
    """Enables the CPU Hogging Indicator Event Message

    app = HS
    command = ENABLE_CPU_HOG
    msg_id = HS_CMD_MID = 0x18ae = 0x1800 + 0x0ae
    cmd_func_code = 10
    data_len = 0 bytes
    """
    name = "HS_ENABLE_CPU_HOG_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HS_ENABLE_CPU_HOG_CmdPkt, pkttype=1, apid=174, cmd_func_code=10)


class HS_DISABLE_CPU_HOG_CmdPkt(Packet):
    """Disables the CPU Hogging Indicator Event Message

    app = HS
    command = DISABLE_CPU_HOG
    msg_id = HS_CMD_MID = 0x18ae = 0x1800 + 0x0ae
    cmd_func_code = 11
    data_len = 0 bytes
    """
    name = "HS_DISABLE_CPU_HOG_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HS_DISABLE_CPU_HOG_CmdPkt, pkttype=1, apid=174, cmd_func_code=11)
