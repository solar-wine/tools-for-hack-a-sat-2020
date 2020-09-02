from scapy.all import *
from ccsds_base import CCSDSPacket


class LC_NOOP_CmdPkt(Packet):
    """Implements the Noop command that insures the LC task is alive

    app = LC
    command = NOOP
    msg_id = LC_CMD_MID = 0x18a4 = 0x1800 + 0x0a4
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "LC_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, LC_NOOP_CmdPkt, pkttype=1, apid=164, cmd_func_code=0)


class LC_RESET_CTRS_CmdPkt(Packet):
    """Resets the LC housekeeping counters

    app = LC
    command = RESET_CTRS
    msg_id = LC_CMD_MID = 0x18a4 = 0x1800 + 0x0a4
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "LC_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, LC_RESET_CTRS_CmdPkt, pkttype=1, apid=164, cmd_func_code=1)


class LC_SET_APP_STATE_CmdPkt(Packet):
    """Sets the operational state of the LC application

    app = LC
    command = SET_APP_STATE
    msg_id = LC_CMD_MID = 0x18a4 = 0x1800 + 0x0a4
    cmd_func_code = 2
    data_len = 4 bytes
    """
    name = "LC_SET_APP_STATE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER NEW_STATE 16 UINT MIN_UINT16 MAX_UINT16 0 "1=Active, 2=Passive, 3=Disabled"
        ShortField("NEW_STATE", 0),
        # APPEND_PARAMETER PADDING   16 UINT MIN_UINT16 MAX_UINT16 0 "Structure padding"
        ShortField("PADDING", 0),
    ]


bind_layers(CCSDSPacket, LC_SET_APP_STATE_CmdPkt, pkttype=1, apid=164, cmd_func_code=2)


class LC_SET_AP_STATE_CmdPkt(Packet):
    """Set actionpoint state

    app = LC
    command = SET_AP_STATE
    msg_id = LC_CMD_MID = 0x18a4 = 0x1800 + 0x0a4
    cmd_func_code = 3
    data_len = 4 bytes
    """
    name = "LC_SET_AP_STATE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER AP_ID     16 UINT MIN_UINT16 MAX_UINT16 0 "Which actionpoint(s) to change"
        ShortField("AP_ID", 0),
        # APPEND_PARAMETER NEW_STATE 16 UINT MIN_UINT16 MAX_UINT16 0 "1=Active, 2=Passive, 3=Disabled"
        ShortField("NEW_STATE", 0),
    ]


bind_layers(CCSDSPacket, LC_SET_AP_STATE_CmdPkt, pkttype=1, apid=164, cmd_func_code=3)


class LC_SET_AP_PERM_OFF_CmdPkt(Packet):
    """Set the specified actionpoint's state to LC_APSTATE_PERMOFF

    app = LC
    command = SET_AP_PERM_OFF
    msg_id = LC_CMD_MID = 0x18a4 = 0x1800 + 0x0a4
    cmd_func_code = 4
    data_len = 4 bytes
    """
    name = "LC_SET_AP_PERM_OFF_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER AP_ID   16 UINT MIN_UINT16 MAX_UINT16 0 "Which actionpoint to change"
        ShortField("AP_ID", 0),
        # APPEND_PARAMETER PADDING 16 UINT MIN_UINT16 MAX_UINT16 0 "Structure padding"
        ShortField("PADDING", 0),
    ]


bind_layers(CCSDSPacket, LC_SET_AP_PERM_OFF_CmdPkt, pkttype=1, apid=164, cmd_func_code=4)


class LC_RESET_AP_STATS_CmdPkt(Packet):
    """Resets actionpoint statistics

    app = LC
    command = RESET_AP_STATS
    msg_id = LC_CMD_MID = 0x18a4 = 0x1800 + 0x0a4
    cmd_func_code = 5
    data_len = 4 bytes
    """
    name = "LC_RESET_AP_STATS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER AP_ID   16 UINT MIN_UINT16 MAX_UINT16 0 "Which actionpoint(s) to change"
        ShortField("AP_ID", 0),
        # APPEND_PARAMETER PADDING 16 UINT MIN_UINT16 MAX_UINT16 0 "Structure padding"
        ShortField("PADDING", 0),
    ]


bind_layers(CCSDSPacket, LC_RESET_AP_STATS_CmdPkt, pkttype=1, apid=164, cmd_func_code=5)


class LC_RESET_WP_STATS_CmdPkt(Packet):
    """Resets watchpoint statistics

    app = LC
    command = RESET_WP_STATS
    msg_id = LC_CMD_MID = 0x18a4 = 0x1800 + 0x0a4
    cmd_func_code = 6
    data_len = 4 bytes
    """
    name = "LC_RESET_WP_STATS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER WP_ID   16 UINT MIN_UINT16 MAX_UINT16 0 "Which watchpoint(s) to change"
        ShortField("WP_ID", 0),
        # APPEND_PARAMETER PADDING 16 UINT MIN_UINT16 MAX_UINT16 0 "Structure padding"
        ShortField("PADDING", 0),
    ]


bind_layers(CCSDSPacket, LC_RESET_WP_STATS_CmdPkt, pkttype=1, apid=164, cmd_func_code=6)
