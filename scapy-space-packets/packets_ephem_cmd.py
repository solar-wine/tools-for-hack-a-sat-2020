from scapy.all import *
from ccsds_base import CCSDSPacket


class EPHEM_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = EPHEM
    command = NOOP
    msg_id = EPHEM_CMD_MID = 0x19dc = 0x1800 + 0x1dc
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "EPHEM_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, EPHEM_NOOP_CmdPkt, pkttype=1, apid=476, cmd_func_code=0)


class EPHEM_RESET_CTRS_CmdPkt(Packet):
    """Reset command counters

    app = EPHEM
    command = RESET_CTRS
    msg_id = EPHEM_CMD_MID = 0x19dc = 0x1800 + 0x1dc
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "EPHEM_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, EPHEM_RESET_CTRS_CmdPkt, pkttype=1, apid=476, cmd_func_code=1)


class EPHEM_LOAD_TBL_CmdPkt(Packet):
    """Load example object table

    app = EPHEM
    command = LOAD_TBL
    msg_id = EPHEM_CMD_MID = 0x19dc = 0x1800 + 0x1dc
    cmd_func_code = 2
    data_len = 66 bytes
    """
    name = "EPHEM_LOAD_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ID    8  UINT 0 2 0 "Table ID. 0 is first table registered"
        ByteField("ID", 0),
        # APPEND_PARAMETER TYPE  8  UINT 0 1 1 "0=Replace Table, 1=Update Records"
        ByteField("TYPE", 1),
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/ephem_extbl.json" "Full path and file name of table to be loaded"
        StrFixedLenField("FILENAME", b"/cf/ephem_extbl.json", 64),
    ]


bind_layers(CCSDSPacket, EPHEM_LOAD_TBL_CmdPkt, pkttype=1, apid=476, cmd_func_code=2)


class EPHEM_DUMP_TBL_CmdPkt(Packet):
    """Dump example object table

    app = EPHEM
    command = DUMP_TBL
    msg_id = EPHEM_CMD_MID = 0x19dc = 0x1800 + 0x1dc
    cmd_func_code = 3
    data_len = 66 bytes
    """
    name = "EPHEM_DUMP_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ID   8 UINT 0 1 0 "Table ID. 0 is first table registered"
        ByteField("ID", 0),
        # APPEND_PARAMETER TYPE 8 UINT 0 1 0 "Unused"
        ByteField("TYPE", 0),
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/ephem_extbl~.json" "Full path and file name to receive table dump"
        StrFixedLenField("FILENAME", b"/cf/ephem_extbl~.json", 64),
    ]


bind_layers(CCSDSPacket, EPHEM_DUMP_TBL_CmdPkt, pkttype=1, apid=476, cmd_func_code=3)


class EPHEM_EXOBJ_STUB_CmdPkt(Packet):
    """Stub command for the example object

    app = EPHEM
    command = EXOBJ_STUB
    msg_id = EPHEM_CMD_MID = 0x19dc = 0x1800 + 0x1dc
    cmd_func_code = 4
    data_len = 2 bytes
    """
    name = "EPHEM_EXOBJ_STUB_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER PARAMETER 16 UINT MIN_UINT16 MAX_UINT16 1 "Example integer parameter"
        ShortField("PARAMETER", 1),
    ]


bind_layers(CCSDSPacket, EPHEM_EXOBJ_STUB_CmdPkt, pkttype=1, apid=476, cmd_func_code=4)
