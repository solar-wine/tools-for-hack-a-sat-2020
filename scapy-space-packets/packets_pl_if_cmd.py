from scapy.all import *
from ccsds_base import CCSDSPacket


class PL_IF_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = PL_IF
    command = NOOP
    msg_id = PL_IF_CMD_MID = 0x19d9 = 0x1800 + 0x1d9
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "PL_IF_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, PL_IF_NOOP_CmdPkt, pkttype=1, apid=473, cmd_func_code=0)


class PL_IF_RESET_CTRS_CmdPkt(Packet):
    """Reset command counters

    app = PL_IF
    command = RESET_CTRS
    msg_id = PL_IF_CMD_MID = 0x19d9 = 0x1800 + 0x1d9
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "PL_IF_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, PL_IF_RESET_CTRS_CmdPkt, pkttype=1, apid=473, cmd_func_code=1)


class PL_IF_LOAD_TBL_CmdPkt(Packet):
    """Load example object table

    app = PL_IF
    command = LOAD_TBL
    msg_id = PL_IF_CMD_MID = 0x19d9 = 0x1800 + 0x1d9
    cmd_func_code = 2
    data_len = 66 bytes
    """
    name = "PL_IF_LOAD_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ID    8  UINT 0 2 0 "Table ID. 0 is first table registered"
        ByteField("ID", 0),
        # APPEND_PARAMETER TYPE  8  UINT 0 1 1 "0=Replace Table, 1=Update Records"
        ByteField("TYPE", 1),
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/pl_if_extbl.json" "Full path and file name of table to be loaded"
        StrFixedLenField("FILENAME", b"/cf/pl_if_extbl.json", 64),
    ]


bind_layers(CCSDSPacket, PL_IF_LOAD_TBL_CmdPkt, pkttype=1, apid=473, cmd_func_code=2)


class PL_IF_DUMP_TBL_CmdPkt(Packet):
    """Dump example object table

    app = PL_IF
    command = DUMP_TBL
    msg_id = PL_IF_CMD_MID = 0x19d9 = 0x1800 + 0x1d9
    cmd_func_code = 3
    data_len = 66 bytes
    """
    name = "PL_IF_DUMP_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ID   8 UINT 0 1 0 "Table ID. 0 is first table registered"
        ByteField("ID", 0),
        # APPEND_PARAMETER TYPE 8 UINT 0 1 0 "Unused"
        ByteField("TYPE", 0),
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/pl_if_extbl~.json" "Full path and file name to receive table dump"
        StrFixedLenField("FILENAME", b"/cf/pl_if_extbl~.json", 64),
    ]


bind_layers(CCSDSPacket, PL_IF_DUMP_TBL_CmdPkt, pkttype=1, apid=473, cmd_func_code=3)


class PL_IF_POWER_CmdPkt(Packet):
    """Enable/Disable Payload Power

    app = PL_IF
    command = POWER
    msg_id = PL_IF_CMD_MID = 0x19d9 = 0x1800 + 0x1d9
    cmd_func_code = 5
    data_len = 1 bytes
    """
    name = "PL_IF_POWER_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ON_OFF 8 UINT 0 1 1 "Set Power On/Off"
        ByteField("ON_OFF", 1),
        # STATE ON 1
        # STATE OFF 0
    ]


bind_layers(CCSDSPacket, PL_IF_POWER_CmdPkt, pkttype=1, apid=473, cmd_func_code=5)


class PL_IF_TAKE_IMG_CmdPkt(Packet):
    """Command the payload to take an image

    app = PL_IF
    command = TAKE_IMG
    msg_id = PL_IF_CMD_MID = 0x19d9 = 0x1800 + 0x1d9
    cmd_func_code = 7
    data_len = 1 bytes
    """
    name = "PL_IF_TAKE_IMG_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TAKE_IMG 8 UINT 0 0 0 "Take Image"
        ByteField("TAKE_IMG", 0),
    ]


bind_layers(CCSDSPacket, PL_IF_TAKE_IMG_CmdPkt, pkttype=1, apid=473, cmd_func_code=7)


class PL_IF_DLINK_IMG_CmdPkt(Packet):
    """Command the payload to downlink an image

    app = PL_IF
    command = DLINK_IMG
    msg_id = PL_IF_CMD_MID = 0x19d9 = 0x1800 + 0x1d9
    cmd_func_code = 7
    data_len = 1 bytes
    """
    name = "PL_IF_DLINK_IMG_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER DLINK_IMG 8 UINT 48 48 48 "Downlink Image"
        ByteField("DLINK_IMG", 48),
    ]


bind_layers(CCSDSPacket, PL_IF_DLINK_IMG_CmdPkt, pkttype=1, apid=473, cmd_func_code=7)


class PL_IF_REBOOT_CmdPkt(Packet):
    """Command the payload to reboot

    app = PL_IF
    command = REBOOT
    msg_id = PL_IF_CMD_MID = 0x19d9 = 0x1800 + 0x1d9
    cmd_func_code = 7
    data_len = 1 bytes
    """
    name = "PL_IF_REBOOT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER REBOOT 8 UINT 1 1 1 "Reboot"
        ByteField("REBOOT", 1),
    ]


bind_layers(CCSDSPacket, PL_IF_REBOOT_CmdPkt, pkttype=1, apid=473, cmd_func_code=7)


class PL_IF_STOP_CmdPkt(Packet):
    """Command the payload to stop the program

    app = PL_IF
    command = STOP
    msg_id = PL_IF_CMD_MID = 0x19d9 = 0x1800 + 0x1d9
    cmd_func_code = 7
    data_len = 1 bytes
    """
    name = "PL_IF_STOP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER STOP 8 UINT 2 2 2 "Stop"
        ByteField("STOP", 2),
    ]


bind_layers(CCSDSPacket, PL_IF_STOP_CmdPkt, pkttype=1, apid=473, cmd_func_code=7)


class PL_IF_GET_IMAGE_SIZE_CmdPkt(Packet):
    """Get the current image size from PL

    app = PL_IF
    command = GET_IMAGE_SIZE
    msg_id = PL_IF_CMD_MID = 0x19d9 = 0x1800 + 0x1d9
    cmd_func_code = 7
    data_len = 1 bytes
    """
    name = "PL_IF_GET_IMAGE_SIZE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER IMAGE_SIZE 8 UINT 5 5 5 "Get Image Size"
        ByteField("IMAGE_SIZE", 5),
    ]


bind_layers(CCSDSPacket, PL_IF_GET_IMAGE_SIZE_CmdPkt, pkttype=1, apid=473, cmd_func_code=7)
