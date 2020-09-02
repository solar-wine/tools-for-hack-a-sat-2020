from scapy.all import *
from ccsds_base import CCSDSPacket


class CFE_TBL_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = CFE_TBL
    command = NOOP
    msg_id = CFE_TBL_CMD_MID = 0x1804 = 0x1800 + 0x004
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "CFE_TBL_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_TBL_NOOP_CmdPkt, pkttype=1, apid=4, cmd_func_code=0)


class CFE_TBL_RESET_CTRS_CmdPkt(Packet):
    """This command resets the following counters within the Table Services housekeeping telemetry: Command Execution Counter ($sc_$cpu_TBL_CMDPC)Command Error Counter ($sc_$cpu_TBL_CMDEC)Successful Table Validations Counter ($sc_$cpu_TBL_ValSuccessCtr)Failed Table Validations Counter ($sc_$cpu_TBL_ValFailedCtr)Number of Table Validations Requested ($sc_$cpu_TBL_ValReqCtr)

    app = CFE_TBL
    command = RESET_CTRS
    msg_id = CFE_TBL_CMD_MID = 0x1804 = 0x1800 + 0x004
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "CFE_TBL_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_TBL_RESET_CTRS_CmdPkt, pkttype=1, apid=4, cmd_func_code=1)


class CFE_TBL_LOAD_TBL_CmdPkt(Packet):
    """This command loads the contents of the specified file into an inactive buffer for the table specified within the file.

    app = CFE_TBL
    command = LOAD_TBL
    msg_id = CFE_TBL_CMD_MID = 0x1804 = 0x1800 + 0x004
    cmd_func_code = 2
    data_len = 64 bytes
    """
    name = "CFE_TBL_LOAD_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "default" "Filename (and path) of data to be loaded."
        StrFixedLenField("FILENAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, CFE_TBL_LOAD_TBL_CmdPkt, pkttype=1, apid=4, cmd_func_code=2)


class CFE_TBL_DUMP_TBL_CmdPkt(Packet):
    """This command will cause the Table Services to put the contents of the specified table buffer into the command specified file.

    app = CFE_TBL
    command = DUMP_TBL
    msg_id = CFE_TBL_CMD_MID = 0x1804 = 0x1800 + 0x004
    cmd_func_code = 3
    data_len = 106 bytes
    """
    name = "CFE_TBL_DUMP_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ACTIVE_TBL_FLAG  16   UINT MIN_UINT16 MAX_UINT16 0 "CFE_TBL_INACTIVE_BUFFER=Inactive Table, CFE_TBL_ACTIVE_BUFFER=Active Table"
        ShortField("ACTIVE_TBL_FLAG", 0),
        # APPEND_PARAMETER TABLE_NAME      320 STRING "default" "Full name of table to be dumped."
        StrFixedLenField("TABLE_NAME", b"default", 40),
        # APPEND_PARAMETER FILENAME        512 STRING "default" "Full Filename where data is to be written."
        StrFixedLenField("FILENAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, CFE_TBL_DUMP_TBL_CmdPkt, pkttype=1, apid=4, cmd_func_code=3)


class CFE_TBL_VALIDATE_TBL_CmdPkt(Packet):
    """This command will cause Table Services to calculate the Data Integrity Value for the specified table and to notify the owning application that the table's validation function should be executed. The results of both the Data Integrity Value computation and the validation function are reported in Table Services Housekeeping Telemetry.

    app = CFE_TBL
    command = VALIDATE_TBL
    msg_id = CFE_TBL_CMD_MID = 0x1804 = 0x1800 + 0x004
    cmd_func_code = 4
    data_len = 42 bytes
    """
    name = "CFE_TBL_VALIDATE_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ACTIVE_TBL_FLAG  16 UINT MIN_UINT16 MAX_UINT16 0 "CFE_TBL_INACTIVE_BUFFER=Inactive Table, CFE_TBL_ACTIVE_BUFFER=Active Table"
        ShortField("ACTIVE_TBL_FLAG", 0),
        # APPEND_PARAMETER TABLE_NAME      320 STRING "default" "Full Name of Table to be validated."
        StrFixedLenField("TABLE_NAME", b"default", 40),
    ]


bind_layers(CCSDSPacket, CFE_TBL_VALIDATE_TBL_CmdPkt, pkttype=1, apid=4, cmd_func_code=4)


class CFE_TBL_ACTIVATE_TBL_CmdPkt(Packet):
    """This command will cause Table Services to notify a table's owner that an update is pending. The owning application will then update the contents of the active table buffer with the contents of the associated inactive table buffer at a time of their convenience.

    app = CFE_TBL
    command = ACTIVATE_TBL
    msg_id = CFE_TBL_CMD_MID = 0x1804 = 0x1800 + 0x004
    cmd_func_code = 5
    data_len = 40 bytes
    """
    name = "CFE_TBL_ACTIVATE_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TABLE_NAME 320 STRING "default" "Full Name of Table to be activated."
        StrFixedLenField("TABLE_NAME", b"default", 40),
    ]


bind_layers(CCSDSPacket, CFE_TBL_ACTIVATE_TBL_CmdPkt, pkttype=1, apid=4, cmd_func_code=5)


class CFE_TBL_WRITE_REG_TO_FILE_CmdPkt(Packet):
    """This command will cause Table Services to write some of the contents of the Table Registry to the command specified file. This allows the operator to see the current state and configuration of all tables that have been registered with the cFE.

    app = CFE_TBL
    command = WRITE_REG_TO_FILE
    msg_id = CFE_TBL_CMD_MID = 0x1804 = 0x1800 + 0x004
    cmd_func_code = 6
    data_len = 64 bytes
    """
    name = "CFE_TBL_WRITE_REG_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/cfe_tbl_reg.log" "Full Filename where registry data is to be written."
        StrFixedLenField("FILENAME", b"/cf/cfe_tbl_reg.log", 64),
    ]


bind_layers(CCSDSPacket, CFE_TBL_WRITE_REG_TO_FILE_CmdPkt, pkttype=1, apid=4, cmd_func_code=6)


class CFE_TBL_SEND_REGISTRY_CmdPkt(Packet):
    """This command will cause Table Services to telemeter the contents of the Table Registry for the command specified table.

    app = CFE_TBL
    command = SEND_REGISTRY
    msg_id = CFE_TBL_CMD_MID = 0x1804 = 0x1800 + 0x004
    cmd_func_code = 7
    data_len = 40 bytes
    """
    name = "CFE_TBL_SEND_REGISTRY_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TABLE_NAME 320 STRING "default" "Full Name of Table whose registry entry is to be telemetered."
        StrFixedLenField("TABLE_NAME", b"default", 40),
    ]


bind_layers(CCSDSPacket, CFE_TBL_SEND_REGISTRY_CmdPkt, pkttype=1, apid=4, cmd_func_code=7)


class CFE_TBL_DELETE_CDS_CmdPkt(Packet):
    """This command will delete the Critical Data Store (CDS) associated with the specified Critical Table. Note that any table still present in the Table Registry is unable to be deleted from the Critical Data Store. All Applications that are accessing the critical table must release and unregister their access before the CDS can be deleted.

    app = CFE_TBL
    command = DELETE_CDS
    msg_id = CFE_TBL_CMD_MID = 0x1804 = 0x1800 + 0x004
    cmd_func_code = 8
    data_len = 40 bytes
    """
    name = "CFE_TBL_DELETE_CDS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TABLE_NAME 320 STRING "default" "Full Name of Table whose CDS is to be deleted."
        StrFixedLenField("TABLE_NAME", b"default", 40),
    ]


bind_layers(CCSDSPacket, CFE_TBL_DELETE_CDS_CmdPkt, pkttype=1, apid=4, cmd_func_code=8)


class CFE_TBL_ABORT_LOAD_CmdPkt(Packet):
    """This command will cause Table Services to discard the contents of a table buffer that was previously loaded with the data in a file as specified by a Table Load command. For single buffered tables, the allocated shared working buffer is freed and becomes available for other Table Load commands.

    app = CFE_TBL
    command = ABORT_LOAD
    msg_id = CFE_TBL_CMD_MID = 0x1804 = 0x1800 + 0x004
    cmd_func_code = 9
    data_len = 40 bytes
    """
    name = "CFE_TBL_ABORT_LOAD_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TABLE_NAME 320 STRING "default" "Full Name of Table whose load is to be aborted."
        StrFixedLenField("TABLE_NAME", b"default", 40),
    ]


bind_layers(CCSDSPacket, CFE_TBL_ABORT_LOAD_CmdPkt, pkttype=1, apid=4, cmd_func_code=9)
