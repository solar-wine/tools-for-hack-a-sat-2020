from scapy.all import *
from ccsds_base import CCSDSPacket


class CS_NOOP_CmdPkt(Packet):
    """Implements the Noop command that insures the CS task is alive

    app = CS
    command = NOOP
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "CS_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_NOOP_CmdPkt, pkttype=1, apid=159, cmd_func_code=0)


class CS_RESET_CTRS_CmdPkt(Packet):
    """Resets the CS housekeeping counters

    app = CS
    command = RESET_CTRS
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "CS_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_RESET_CTRS_CmdPkt, pkttype=1, apid=159, cmd_func_code=1)


class CS_ONESHOT_CmdPkt(Packet):
    """Computes a checksum on the given address and size of memory specified in the command. This command spawns a child task to complete the checksum.

    app = CS
    command = ONESHOT
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 2
    data_len = 8 bytes
    """
    name = "CS_ONESHOT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ADDRESS 32 UINT MIN_UINT32 MAX_UINT32 0 "Address to start checksum."
        IntField("ADDRESS", 0),
        # APPEND_PARAMETER SIZE 32 UINT MIN_UINT32 MAX_UINT32 0 "Number of bytes to checksum."
        IntField("SIZE", 0),
    ]


bind_layers(CCSDSPacket, CS_ONESHOT_CmdPkt, pkttype=1, apid=159, cmd_func_code=2)


class CS_CANCEL_ONESHOT_CmdPkt(Packet):
    """Cancels a one shot calculation that is already in progress.

    app = CS
    command = CANCEL_ONESHOT
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 3
    data_len = 0 bytes
    """
    name = "CS_CANCEL_ONESHOT_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_CANCEL_ONESHOT_CmdPkt, pkttype=1, apid=159, cmd_func_code=3)


class CS_ENABLE_ALL_CS_CmdPkt(Packet):
    """Allows CS to continue background checking

    app = CS
    command = ENABLE_ALL_CS
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 4
    data_len = 0 bytes
    """
    name = "CS_ENABLE_ALL_CS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_ENABLE_ALL_CS_CmdPkt, pkttype=1, apid=159, cmd_func_code=4)


class CS_DISABLE_ALL_CS_CmdPkt(Packet):
    """Disables all background checking

    app = CS
    command = DISABLE_ALL_CS
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 5
    data_len = 0 bytes
    """
    name = "CS_DISABLE_ALL_CS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_DISABLE_ALL_CS_CmdPkt, pkttype=1, apid=159, cmd_func_code=5)


class CS_ENABLE_CFECORE_CmdPkt(Packet):
    """Enables background checking on the cFE core code segment

    app = CS
    command = ENABLE_CFECORE
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 6
    data_len = 0 bytes
    """
    name = "CS_ENABLE_CFECORE_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_ENABLE_CFECORE_CmdPkt, pkttype=1, apid=159, cmd_func_code=6)


class CS_DISABLE_CFECORE_CmdPkt(Packet):
    """Disables background checking on the cFE core code segment

    app = CS
    command = DISABLE_CFECORE
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 7
    data_len = 0 bytes
    """
    name = "CS_DISABLE_CFECORE_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_DISABLE_CFECORE_CmdPkt, pkttype=1, apid=159, cmd_func_code=7)


class CS_REPORT_BASELINE_CFECORE_CmdPkt(Packet):
    """Reports the baseline checksum of the cFE core that has already been calculated.

    app = CS
    command = REPORT_BASELINE_CFECORE
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 8
    data_len = 0 bytes
    """
    name = "CS_REPORT_BASELINE_CFECORE_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_REPORT_BASELINE_CFECORE_CmdPkt, pkttype=1, apid=159, cmd_func_code=8)


class CS_RECOMPUTE_BASELINE_CFECORE_CmdPkt(Packet):
    """Recomputesthe baseline checksum of the cFE core and use the new value as the baseline.

    app = CS
    command = RECOMPUTE_BASELINE_CFECORE
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 9
    data_len = 0 bytes
    """
    name = "CS_RECOMPUTE_BASELINE_CFECORE_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_RECOMPUTE_BASELINE_CFECORE_CmdPkt, pkttype=1, apid=159, cmd_func_code=9)


class CS_ENABLE_OS_CmdPkt(Packet):
    """Enables background checking on the OS code segment

    app = CS
    command = ENABLE_OS
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 10
    data_len = 0 bytes
    """
    name = "CS_ENABLE_OS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_ENABLE_OS_CmdPkt, pkttype=1, apid=159, cmd_func_code=10)


class CS_DISABLE_OS_CmdPkt(Packet):
    """Disables background checking on the OS code segment code segment

    app = CS
    command = DISABLE_OS
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 11
    data_len = 0 bytes
    """
    name = "CS_DISABLE_OS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_DISABLE_OS_CmdPkt, pkttype=1, apid=159, cmd_func_code=11)


class CS_REPORT_BASELINE_OS_CmdPkt(Packet):
    """Reports the baseline checksum of the OS code segment that has already been calculated.

    app = CS
    command = REPORT_BASELINE_OS
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 12
    data_len = 0 bytes
    """
    name = "CS_REPORT_BASELINE_OS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_REPORT_BASELINE_OS_CmdPkt, pkttype=1, apid=159, cmd_func_code=12)


class CS_RECOMPUTE_BASELINE_OS_CmdPkt(Packet):
    """Recomputesthe baseline checksum of the OS code segment and use the new value as the baseline.

    app = CS
    command = RECOMPUTE_BASELINE_OS
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 13
    data_len = 0 bytes
    """
    name = "CS_RECOMPUTE_BASELINE_OS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_RECOMPUTE_BASELINE_OS_CmdPkt, pkttype=1, apid=159, cmd_func_code=13)


class CS_ENABLE_EEPROM_CmdPkt(Packet):
    """Allow the Eeprom table to checksummed in the background

    app = CS
    command = ENABLE_EEPROM
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 14
    data_len = 0 bytes
    """
    name = "CS_ENABLE_EEPROM_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_ENABLE_EEPROM_CmdPkt, pkttype=1, apid=159, cmd_func_code=14)


class CS_DISABLE_EEPROM_CmdPkt(Packet):
    """Disable the Eeprom table background checksumming

    app = CS
    command = DISABLE_EEPROM
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 15
    data_len = 0 bytes
    """
    name = "CS_DISABLE_EEPROM_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_DISABLE_EEPROM_CmdPkt, pkttype=1, apid=159, cmd_func_code=15)


class CS_REPORT_BASELINE_EEPROM_CmdPkt(Packet):
    """Reports the baseline checksum of the Eeprom table entry that has already been calculated.

    app = CS
    command = REPORT_BASELINE_EEPROM
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 16
    data_len = 2 bytes
    """
    name = "CS_REPORT_BASELINE_EEPROM_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ENTRYID 16 UINT MIN_UINT16 MAX_UINT16 0 "EntryID to perform a command on."
        ShortField("ENTRYID", 0),
    ]


bind_layers(CCSDSPacket, CS_REPORT_BASELINE_EEPROM_CmdPkt, pkttype=1, apid=159, cmd_func_code=16)


class CS_RECOMPUTE_BASELINE_EEPROM_CmdPkt(Packet):
    """Recompute the baseline checksum of the Eeprom table entry and use that value as the new baseline. This command spawns a child task to do the recompute.

    app = CS
    command = RECOMPUTE_BASELINE_EEPROM
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 17
    data_len = 2 bytes
    """
    name = "CS_RECOMPUTE_BASELINE_EEPROM_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ENTRYID 16 UINT MIN_UINT16 MAX_UINT16 0 "EntryID to perform a command on."
        ShortField("ENTRYID", 0),
    ]


bind_layers(CCSDSPacket, CS_RECOMPUTE_BASELINE_EEPROM_CmdPkt, pkttype=1, apid=159, cmd_func_code=17)


class CS_ENABLE_ENTRY_EEPROM_CmdPkt(Packet):
    """Allow the Eeprom entry to checksummed in the background

    app = CS
    command = ENABLE_ENTRY_EEPROM
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 18
    data_len = 2 bytes
    """
    name = "CS_ENABLE_ENTRY_EEPROM_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ENTRYID 16 UINT MIN_UINT16 MAX_UINT16 0 "EntryID to perform a command on."
        ShortField("ENTRYID", 0),
    ]


bind_layers(CCSDSPacket, CS_ENABLE_ENTRY_EEPROM_CmdPkt, pkttype=1, apid=159, cmd_func_code=18)


class CS_DISABLE_ENTRY_EEPROM_CmdPkt(Packet):
    """Disable the Eeprom entry background checksumming

    app = CS
    command = DISABLE_ENTRY_EEPROM
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 19
    data_len = 2 bytes
    """
    name = "CS_DISABLE_ENTRY_EEPROM_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ENTRYID 16 UINT MIN_UINT16 MAX_UINT16 0 "EntryID to perform a command on."
        ShortField("ENTRYID", 0),
    ]


bind_layers(CCSDSPacket, CS_DISABLE_ENTRY_EEPROM_CmdPkt, pkttype=1, apid=159, cmd_func_code=19)


class CS_GET_ENTRY_ID_EEPROM_CmdPkt(Packet):
    """Gets the Entry ID of an Eeprom address to use in subsequent commands.

    app = CS
    command = GET_ENTRY_ID_EEPROM
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 20
    data_len = 4 bytes
    """
    name = "CS_GET_ENTRY_ID_EEPROM_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ADDRESS 32 UINT MIN_UINT32 MAX_UINT32 0 "Address to get the ID for."
        IntField("ADDRESS", 0),
    ]


bind_layers(CCSDSPacket, CS_GET_ENTRY_ID_EEPROM_CmdPkt, pkttype=1, apid=159, cmd_func_code=20)


class CS_ENABLE_MEMORY_CmdPkt(Packet):
    """Allow the Memory table to checksummed in the background

    app = CS
    command = ENABLE_MEMORY
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 21
    data_len = 0 bytes
    """
    name = "CS_ENABLE_MEMORY_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_ENABLE_MEMORY_CmdPkt, pkttype=1, apid=159, cmd_func_code=21)


class CS_DISABLE_MEMORY_CmdPkt(Packet):
    """Disable the Memory table background checksumming

    app = CS
    command = DISABLE_MEMORY
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 22
    data_len = 0 bytes
    """
    name = "CS_DISABLE_MEMORY_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_DISABLE_MEMORY_CmdPkt, pkttype=1, apid=159, cmd_func_code=22)


class CS_REPORT_BASELINE_MEMORY_CmdPkt(Packet):
    """Reports the baseline checksum of the Memory table entry that has already been calculated.

    app = CS
    command = REPORT_BASELINE_MEMORY
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 23
    data_len = 2 bytes
    """
    name = "CS_REPORT_BASELINE_MEMORY_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ENTRYID 16 UINT MIN_UINT16 MAX_UINT16 0 "EntryID to perform a command on."
        ShortField("ENTRYID", 0),
    ]


bind_layers(CCSDSPacket, CS_REPORT_BASELINE_MEMORY_CmdPkt, pkttype=1, apid=159, cmd_func_code=23)


class CS_RECOMPUTE_BASELINE_MEMORY_CmdPkt(Packet):
    """Recompute the baseline checksum of the Memory table entry and use that value as the new baseline. This command spawns a child task to do the recompute.

    app = CS
    command = RECOMPUTE_BASELINE_MEMORY
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 24
    data_len = 2 bytes
    """
    name = "CS_RECOMPUTE_BASELINE_MEMORY_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ENTRYID 16 UINT MIN_UINT16 MAX_UINT16 0 "EntryID to perform a command on."
        ShortField("ENTRYID", 0),
    ]


bind_layers(CCSDSPacket, CS_RECOMPUTE_BASELINE_MEMORY_CmdPkt, pkttype=1, apid=159, cmd_func_code=24)


class CS_ENABLE_ENTRY_MEMORY_CmdPkt(Packet):
    """Allow the Memory entry to checksummed in the background

    app = CS
    command = ENABLE_ENTRY_MEMORY
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 25
    data_len = 2 bytes
    """
    name = "CS_ENABLE_ENTRY_MEMORY_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ENTRYID 16 UINT MIN_UINT16 MAX_UINT16 0 "EntryID to perform a command on."
        ShortField("ENTRYID", 0),
    ]


bind_layers(CCSDSPacket, CS_ENABLE_ENTRY_MEMORY_CmdPkt, pkttype=1, apid=159, cmd_func_code=25)


class CS_DISABLE_ENTRY_MEMORY_CmdPkt(Packet):
    """Disable the Memory entry background checksumming

    app = CS
    command = DISABLE_ENTRY_MEMORY
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 26
    data_len = 2 bytes
    """
    name = "CS_DISABLE_ENTRY_MEMORY_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ENTRYID 16 UINT MIN_UINT16 MAX_UINT16 0 "EntryID to perform a command on."
        ShortField("ENTRYID", 0),
    ]


bind_layers(CCSDSPacket, CS_DISABLE_ENTRY_MEMORY_CmdPkt, pkttype=1, apid=159, cmd_func_code=26)


class CS_GET_ENTRY_ID_MEMORY_CmdPkt(Packet):
    """Gets the Entry ID of a Memory address to use in subsequent commands.

    app = CS
    command = GET_ENTRY_ID_MEMORY
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 27
    data_len = 4 bytes
    """
    name = "CS_GET_ENTRY_ID_MEMORY_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ADDRESS 32 UINT MIN_UINT32 MAX_UINT32 0 "Address to get the ID for."
        IntField("ADDRESS", 0),
    ]


bind_layers(CCSDSPacket, CS_GET_ENTRY_ID_MEMORY_CmdPkt, pkttype=1, apid=159, cmd_func_code=27)


class CS_ENABLE_TABLES_CmdPkt(Packet):
    """Allow the Tables table to checksummed in the background

    app = CS
    command = ENABLE_TABLES
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 28
    data_len = 0 bytes
    """
    name = "CS_ENABLE_TABLES_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_ENABLE_TABLES_CmdPkt, pkttype=1, apid=159, cmd_func_code=28)


class CS_DISABLE_TABLES_CmdPkt(Packet):
    """Disable the Tables table background checksumming

    app = CS
    command = DISABLE_TABLES
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 29
    data_len = 0 bytes
    """
    name = "CS_DISABLE_TABLES_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_DISABLE_TABLES_CmdPkt, pkttype=1, apid=159, cmd_func_code=29)


class CS_REPORT_BASELINE_TABLE_CmdPkt(Packet):
    """Reports the baseline checksum of the table that has already been calculated.

    app = CS
    command = REPORT_BASELINE_TABLE
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 30
    data_len = 38 bytes
    """
    name = "CS_REPORT_BASELINE_TABLE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER NAME 304 STRING "default" "Table name to perform a command on."
        StrFixedLenField("NAME", b"default", 38),
    ]


bind_layers(CCSDSPacket, CS_REPORT_BASELINE_TABLE_CmdPkt, pkttype=1, apid=159, cmd_func_code=30)


class CS_RECOMPUTE_BASELINE_TABLE_CmdPkt(Packet):
    """Recompute the baseline checksum of the table and use that value as the new baseline. This command spawns a child task to do the recompute.

    app = CS
    command = RECOMPUTE_BASELINE_TABLE
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 31
    data_len = 38 bytes
    """
    name = "CS_RECOMPUTE_BASELINE_TABLE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER NAME 304 STRING "default" "Table name to perform a command on."
        StrFixedLenField("NAME", b"default", 38),
    ]


bind_layers(CCSDSPacket, CS_RECOMPUTE_BASELINE_TABLE_CmdPkt, pkttype=1, apid=159, cmd_func_code=31)


class CS_ENABLE_NAME_TABLE_CmdPkt(Packet):
    """Allow the table to checksummed in the background

    app = CS
    command = ENABLE_NAME_TABLE
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 32
    data_len = 38 bytes
    """
    name = "CS_ENABLE_NAME_TABLE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER NAME 304 STRING "default" "Table name to perform a command on."
        StrFixedLenField("NAME", b"default", 38),
    ]


bind_layers(CCSDSPacket, CS_ENABLE_NAME_TABLE_CmdPkt, pkttype=1, apid=159, cmd_func_code=32)


class CS_DISABLE_NAME_TABLE_CmdPkt(Packet):
    """Disable background checking of the table

    app = CS
    command = DISABLE_NAME_TABLE
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 33
    data_len = 38 bytes
    """
    name = "CS_DISABLE_NAME_TABLE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER NAME 304 STRING "default" "Table name to perform a command on."
        StrFixedLenField("NAME", b"default", 38),
    ]


bind_layers(CCSDSPacket, CS_DISABLE_NAME_TABLE_CmdPkt, pkttype=1, apid=159, cmd_func_code=33)


class CS_ENABLE_APPS_CmdPkt(Packet):
    """Allow the App table to checksummed in the background

    app = CS
    command = ENABLE_APPS
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 34
    data_len = 0 bytes
    """
    name = "CS_ENABLE_APPS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_ENABLE_APPS_CmdPkt, pkttype=1, apid=159, cmd_func_code=34)


class CS_DISABLE_APPS_CmdPkt(Packet):
    """Disable the App table background checksumming

    app = CS
    command = DISABLE_APPS
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 35
    data_len = 0 bytes
    """
    name = "CS_DISABLE_APPS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CS_DISABLE_APPS_CmdPkt, pkttype=1, apid=159, cmd_func_code=35)


class CS_REPORT_BASELINE_APP_CmdPkt(Packet):
    """Reports the baseline checksum of the app that has already been calculated.

    app = CS
    command = REPORT_BASELINE_APP
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 36
    data_len = 20 bytes
    """
    name = "CS_REPORT_BASELINE_APP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER NAME 160 STRING "default" "App name to perform a command on."
        StrFixedLenField("NAME", b"default", 20),
    ]


bind_layers(CCSDSPacket, CS_REPORT_BASELINE_APP_CmdPkt, pkttype=1, apid=159, cmd_func_code=36)


class CS_RECOMPUTE_BASELINE_APP_CmdPkt(Packet):
    """Recompute the baseline checksum of the app and use that value as the new baseline. This command spawns a child task to do the recompute.

    app = CS
    command = RECOMPUTE_BASELINE_APP
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 37
    data_len = 20 bytes
    """
    name = "CS_RECOMPUTE_BASELINE_APP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER NAME 160 STRING "default" "App name to perform a command on."
        StrFixedLenField("NAME", b"default", 20),
    ]


bind_layers(CCSDSPacket, CS_RECOMPUTE_BASELINE_APP_CmdPkt, pkttype=1, apid=159, cmd_func_code=37)


class CS_ENABLE_NAME_APP_CmdPkt(Packet):
    """Allow the app to checksummed in the background

    app = CS
    command = ENABLE_NAME_APP
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 38
    data_len = 20 bytes
    """
    name = "CS_ENABLE_NAME_APP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER NAME 160 STRING "default" "App name to perform a command on."
        StrFixedLenField("NAME", b"default", 20),
    ]


bind_layers(CCSDSPacket, CS_ENABLE_NAME_APP_CmdPkt, pkttype=1, apid=159, cmd_func_code=38)


class CS_DISABLE_NAME_APP_CmdPkt(Packet):
    """Disable background checking of the app

    app = CS
    command = DISABLE_NAME_APP
    msg_id = CS_CMD_MID = 0x189f = 0x1800 + 0x09f
    cmd_func_code = 39
    data_len = 20 bytes
    """
    name = "CS_DISABLE_NAME_APP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER NAME 160 STRING "default" "App name to perform a command on."
        StrFixedLenField("NAME", b"default", 20),
    ]


bind_layers(CCSDSPacket, CS_DISABLE_NAME_APP_CmdPkt, pkttype=1, apid=159, cmd_func_code=39)
