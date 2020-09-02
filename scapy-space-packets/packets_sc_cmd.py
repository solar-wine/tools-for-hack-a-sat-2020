from scapy.all import *
from ccsds_base import CCSDSPacket


class SC_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = SC
    command = NOOP
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "SC_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, SC_NOOP_CmdPkt, pkttype=1, apid=169, cmd_func_code=0)


class SC_RESET_CTRS_CmdPkt(Packet):
    """Resets the SC housekeeping counters

    app = SC
    command = RESET_CTRS
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "SC_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, SC_RESET_CTRS_CmdPkt, pkttype=1, apid=169, cmd_func_code=1)


class SC_START_ATS_CmdPkt(Packet):
    """Starts the specified ATS

    app = SC
    command = START_ATS
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 2
    data_len = 2 bytes
    """
    name = "SC_START_ATS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ATS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "The ID of the ATS to start, 1 = ATS_A, 2 = ATS_B."
        ShortField("ATS_ID", 0),
    ]


bind_layers(CCSDSPacket, SC_START_ATS_CmdPkt, pkttype=1, apid=169, cmd_func_code=2)


class SC_STOP_ATS_CmdPkt(Packet):
    """Stops the active ATS

    app = SC
    command = STOP_ATS
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 3
    data_len = 0 bytes
    """
    name = "SC_STOP_ATS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, SC_STOP_ATS_CmdPkt, pkttype=1, apid=169, cmd_func_code=3)


class SC_START_RTS_CmdPkt(Packet):
    """Starts the specified RTS

    app = SC
    command = START_RTS
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 4
    data_len = 2 bytes
    """
    name = "SC_START_RTS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER RTS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "The ID of the RTS to start, 1 through SC_NUMBER_OF_RTS."
        ShortField("RTS_ID", 0),
    ]


bind_layers(CCSDSPacket, SC_START_RTS_CmdPkt, pkttype=1, apid=169, cmd_func_code=4)


class SC_STOP_RTS_CmdPkt(Packet):
    """Stops the specified RTS

    app = SC
    command = STOP_RTS
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 5
    data_len = 2 bytes
    """
    name = "SC_STOP_RTS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER RTS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "The ID of the RTS to start, 1 through SC_NUMBER_OF_RTS."
        ShortField("RTS_ID", 0),
    ]


bind_layers(CCSDSPacket, SC_STOP_RTS_CmdPkt, pkttype=1, apid=169, cmd_func_code=5)


class SC_DISABLE_RTS_CmdPkt(Packet):
    """Disables the specified RTS

    app = SC
    command = DISABLE_RTS
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 6
    data_len = 2 bytes
    """
    name = "SC_DISABLE_RTS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER RTS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "The ID of the RTS to start, 1 through SC_NUMBER_OF_RTS."
        ShortField("RTS_ID", 0),
    ]


bind_layers(CCSDSPacket, SC_DISABLE_RTS_CmdPkt, pkttype=1, apid=169, cmd_func_code=6)


class SC_ENABLE_RTS_CmdPkt(Packet):
    """Enables the specified RTS

    app = SC
    command = ENABLE_RTS
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 7
    data_len = 2 bytes
    """
    name = "SC_ENABLE_RTS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER RTS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "The ID of the RTS to start, 1 through SC_NUMBER_OF_RTS."
        ShortField("RTS_ID", 0),
    ]


bind_layers(CCSDSPacket, SC_ENABLE_RTS_CmdPkt, pkttype=1, apid=169, cmd_func_code=7)


class SC_SWITCH_ATS_CmdPkt(Packet):
    """Switches the running ATS and the ATS no running

    app = SC
    command = SWITCH_ATS
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 8
    data_len = 0 bytes
    """
    name = "SC_SWITCH_ATS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, SC_SWITCH_ATS_CmdPkt, pkttype=1, apid=169, cmd_func_code=8)


class SC_JUMP_ATS_CmdPkt(Packet):
    """Moves the 'current time' pointer in the ATS to another time

    app = SC
    command = JUMP_ATS
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 9
    data_len = 4 bytes
    """
    name = "SC_JUMP_ATS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER NEW_TIME 32 UINT MIN_UINT32 MAX_UINT32 0 "the time to 'jump' to"
        IntField("NEW_TIME", 0),
    ]


bind_layers(CCSDSPacket, SC_JUMP_ATS_CmdPkt, pkttype=1, apid=169, cmd_func_code=9)


class SC_CONT_ATS_CmdPkt(Packet):
    """Sets the flag which specifies whether or not to continue processing an ATS if one of the commands in the ATS fails checksum validation before being sent out.

    app = SC
    command = CONT_ATS
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 10
    data_len = 2 bytes
    """
    name = "SC_CONT_ATS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CONTINUE_STATE 16 UINT MIN_UINT16 MAX_UINT16 0 "TRUE or FALSE, to continue ATS after a failure."
        ShortField("CONTINUE_STATE", 0),
    ]


bind_layers(CCSDSPacket, SC_CONT_ATS_CmdPkt, pkttype=1, apid=169, cmd_func_code=10)


class SC_APPEND_ATS_CmdPkt(Packet):
    """Adds contents of the Append table to the specified ATS table

    app = SC
    command = APPEND_ATS
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 11
    data_len = 2 bytes
    """
    name = "SC_APPEND_ATS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ATS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "The ID of the ATS to append to, 1 = ATS_A, 2 = ATS_B."
        ShortField("ATS_ID", 0),
    ]


bind_layers(CCSDSPacket, SC_APPEND_ATS_CmdPkt, pkttype=1, apid=169, cmd_func_code=11)


class SC_START_RTS_GROUP_CmdPkt(Packet):
    """The load state for an RTS may be LOADED or NOT LOADED. The enable state for an RTS may be ENABLED or DISABLED. The run state for an RTS may be STARTED or STOPPED. This command STARTS each RTS in the specified group that is currently LOADED, ENABLED and STOPPED.

    app = SC
    command = START_RTS_GROUP
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 13
    data_len = 4 bytes
    """
    name = "SC_START_RTS_GROUP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FIRST_RTS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "ID of the first RTS to act on, 1 through SC_NUMBER_OF_RTS."
        ShortField("FIRST_RTS_ID", 0),
        # APPEND_PARAMETER LAST_RTS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "ID of the last RTS to act on, 1 through SC_NUMBER_OF_RTS."
        ShortField("LAST_RTS_ID", 0),
    ]


bind_layers(CCSDSPacket, SC_START_RTS_GROUP_CmdPkt, pkttype=1, apid=169, cmd_func_code=13)


class SC_STOP_RTS_GROUP_CmdPkt(Packet):
    """The load state for an RTS may be LOADED or NOT LOADED. The enable state for an RTS may be ENABLED or DISABLED. The run state for an RTS may be STARTED or STOPPED. This command STOPS each RTS in the specified group that is currently STARTED.

    app = SC
    command = STOP_RTS_GROUP
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 14
    data_len = 4 bytes
    """
    name = "SC_STOP_RTS_GROUP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FIRST_RTS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "ID of the first RTS to act on, 1 through SC_NUMBER_OF_RTS."
        ShortField("FIRST_RTS_ID", 0),
        # APPEND_PARAMETER LAST_RTS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "ID of the last RTS to act on, 1 through SC_NUMBER_OF_RTS."
        ShortField("LAST_RTS_ID", 0),
    ]


bind_layers(CCSDSPacket, SC_STOP_RTS_GROUP_CmdPkt, pkttype=1, apid=169, cmd_func_code=14)


class SC_DISABLE_RTS_GROUP_CmdPkt(Packet):
    """The enable state for an RTS may be ENABLED or DISABLED. This command sets the enable state for the specified group of RTS to DISABLED.

    app = SC
    command = DISABLE_RTS_GROUP
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 15
    data_len = 4 bytes
    """
    name = "SC_DISABLE_RTS_GROUP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FIRST_RTS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "ID of the first RTS to act on, 1 through SC_NUMBER_OF_RTS."
        ShortField("FIRST_RTS_ID", 0),
        # APPEND_PARAMETER LAST_RTS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "ID of the last RTS to act on, 1 through SC_NUMBER_OF_RTS."
        ShortField("LAST_RTS_ID", 0),
    ]


bind_layers(CCSDSPacket, SC_DISABLE_RTS_GROUP_CmdPkt, pkttype=1, apid=169, cmd_func_code=15)


class SC_ENABLE_RTS_GROUP_CmdPkt(Packet):
    """The enable state for an RTS may be ENABLED or DISABLED. This command sets the enable state for the specified group of RTS to ENABLED.

    app = SC
    command = ENABLE_RTS_GROUP
    msg_id = SC_CMD_MID = 0x18a9 = 0x1800 + 0x0a9
    cmd_func_code = 16
    data_len = 4 bytes
    """
    name = "SC_ENABLE_RTS_GROUP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FIRST_RTS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "ID of the first RTS to act on, 1 through SC_NUMBER_OF_RTS."
        ShortField("FIRST_RTS_ID", 0),
        # APPEND_PARAMETER LAST_RTS_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "ID of the last RTS to act on, 1 through SC_NUMBER_OF_RTS."
        ShortField("LAST_RTS_ID", 0),
    ]


bind_layers(CCSDSPacket, SC_ENABLE_RTS_GROUP_CmdPkt, pkttype=1, apid=169, cmd_func_code=16)
