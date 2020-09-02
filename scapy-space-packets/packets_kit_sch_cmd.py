from scapy.all import *
from ccsds_base import CCSDSPacket


class KIT_SCH_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = KIT_SCH
    command = NOOP
    msg_id = KIT_SCH_CMD_MID = 0x1895 = 0x1800 + 0x095
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "KIT_SCH_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, KIT_SCH_NOOP_CmdPkt, pkttype=1, apid=149, cmd_func_code=0)


class KIT_SCH_RESET_CTRS_CmdPkt(Packet):
    """Reset application to a known state

    app = KIT_SCH
    command = RESET_CTRS
    msg_id = KIT_SCH_CMD_MID = 0x1895 = 0x1800 + 0x095
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "KIT_SCH_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, KIT_SCH_RESET_CTRS_CmdPkt, pkttype=1, apid=149, cmd_func_code=1)


class KIT_SCH_LOAD_TBL_CmdPkt(Packet):
    """Load Table

    app = KIT_SCH
    command = LOAD_TBL
    msg_id = KIT_SCH_CMD_MID = 0x1895 = 0x1800 + 0x095
    cmd_func_code = 2
    data_len = 66 bytes
    """
    name = "KIT_SCH_LOAD_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ID    8  UINT 0 1 0 "Table ID: 0=Message 1=Schedule"
        ByteField("ID", 0),
        # APPEND_PARAMETER TYPE  8  UINT 0 1 1 "0=Replace Table, 1=Update Records"
        ByteField("TYPE", 1),
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/kit_sch_msg_tbl.json" "Message Table"
        StrFixedLenField("FILENAME", b"/cf/kit_sch_msg_tbl.json", 64),
    ]


bind_layers(CCSDSPacket, KIT_SCH_LOAD_TBL_CmdPkt, pkttype=1, apid=149, cmd_func_code=2)


class KIT_SCH_DUMP_TBL_CmdPkt(Packet):
    """Dump Table

    app = KIT_SCH
    command = DUMP_TBL
    msg_id = KIT_SCH_CMD_MID = 0x1895 = 0x1800 + 0x095
    cmd_func_code = 3
    data_len = 66 bytes
    """
    name = "KIT_SCH_DUMP_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ID    8  UINT 0 1 0 "Table ID: 0=Message 1=Schedule"
        ByteField("ID", 0),
        # APPEND_PARAMETER TYPE  8  UINT 0 1 1 "Unused"
        ByteField("TYPE", 1),
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/kit_sch_msg_tbl~.json" "Full path/file name to receive table dump. 20 char max for file name without extension"
        StrFixedLenField("FILENAME", b"/cf/kit_sch_msg_tbl~.json", 64),
    ]


bind_layers(CCSDSPacket, KIT_SCH_DUMP_TBL_CmdPkt, pkttype=1, apid=149, cmd_func_code=3)


class KIT_SCH_CFG_SCH_ENTRY_CmdPkt(Packet):
    """Enable/disable a single activity in the Schedule Definition Table

    app = KIT_SCH
    command = CFG_SCH_ENTRY
    msg_id = KIT_SCH_CMD_MID = 0x1895 = 0x1800 + 0x095
    cmd_func_code = 4
    data_len = 5 bytes
    """
    name = "KIT_SCH_CFG_SCH_ENTRY_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SLOT     16 UINT MIN_UINT16 MAX_UINT16 0 "Scheduler slot number (0..N) whose state is to change."
        ShortField("SLOT", 0),
        # APPEND_PARAMETER ACTIVITY 16 UINT MIN_UINT16 MAX_UINT16 0 "Activity index (0..M) whose state is to change."
        ShortField("ACTIVITY", 0),
        # APPEND_PARAMETER CONFIG    8 UINT 0 1 1 "0=Disable, 1=Enable"
        ByteField("CONFIG", 1),
    ]


bind_layers(CCSDSPacket, KIT_SCH_CFG_SCH_ENTRY_CmdPkt, pkttype=1, apid=149, cmd_func_code=4)


class KIT_SCH_LOAD_SCH_ENTRY_CmdPkt(Packet):
    """Load a scheduler table entry

    app = KIT_SCH
    command = LOAD_SCH_ENTRY
    msg_id = KIT_SCH_CMD_MID = 0x1895 = 0x1800 + 0x095
    cmd_func_code = 5
    data_len = 12 bytes
    """
    name = "KIT_SCH_LOAD_SCH_ENTRY_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SLOT        16 UINT MIN_UINT16 MAX_UINT16 0 "Scheduler slot number (0..N) whose state is to change."
        ShortField("SLOT", 0),
        # APPEND_PARAMETER ACTIVITY    16 UINT MIN_UINT16 MAX_UINT16 0 "Activity index (0..M) whose state is to change."
        ShortField("ACTIVITY", 0),
        # APPEND_PARAMETER CONFIG      16 UINT          0          1 1 "0=Disable, 1=Enable"
        ShortField("CONFIG", 1),
        # APPEND_PARAMETER FREQ        16 UINT MIN_UINT16 MAX_UINT16 1 "Scheduler cycles between execution. 1=Send every execution"
        ShortField("FREQ", 1),
        # APPEND_PARAMETER OFFSET      16 UINT MIN_UINT16 MAX_UINT16 0 "Number of schedler cycles to wait before first execution"
        ShortField("OFFSET", 0),
        # APPEND_PARAMETER MSG_TBL_IDX 16 UINT MIN_UINT16 MAX_UINT16 0 "Index into message table"
        ShortField("MSG_TBL_IDX", 0),
    ]


bind_layers(CCSDSPacket, KIT_SCH_LOAD_SCH_ENTRY_CmdPkt, pkttype=1, apid=149, cmd_func_code=5)


class KIT_SCH_LOAD_MSG_ENTRY_CmdPkt(Packet):
    """Load a message table entry. Doesn't accept parameters

    app = KIT_SCH
    command = LOAD_MSG_ENTRY
    msg_id = KIT_SCH_CMD_MID = 0x1895 = 0x1800 + 0x095
    cmd_func_code = 6
    data_len = 4 bytes
    """
    name = "KIT_SCH_LOAD_MSG_ENTRY_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MSG_TBL_IDX 16 UINT MIN_UINT16 MAX_UINT16 0 "Index into message table"
        ShortField("MSG_TBL_IDX", 0),
        # APPEND_PARAMETER MSG_ID      16 UINT MIN_UINT16 MAX_UINT16 0 "Complete first word of CCSDS primary header"
        ShortField("MSG_ID", 0),
    ]


bind_layers(CCSDSPacket, KIT_SCH_LOAD_MSG_ENTRY_CmdPkt, pkttype=1, apid=149, cmd_func_code=6)
