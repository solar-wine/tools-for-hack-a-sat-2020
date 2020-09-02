from scapy.all import *
from ccsds_base import CCSDSPacket


class CFE_ES_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = CFE_ES
    command = NOOP
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "CFE_ES_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_ES_NOOP_CmdPkt, pkttype=1, apid=6, cmd_func_code=0)


class CFE_ES_RESET_CTRS_CmdPkt(Packet):
    """Reset command counters

    app = CFE_ES
    command = RESET_CTRS
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "CFE_ES_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_ES_RESET_CTRS_CmdPkt, pkttype=1, apid=6, cmd_func_code=1)


class CFE_ES_RESET_CmdPkt(Packet):
    """Restart the cFE in one of two modes: Power-On Reset will cause the cFE to restart as though the power were first applied to the processor. The Processor Reset will attempt to retain the contents of the volatile disk and the contents of the Critical Data Store. NOTE: If a requested Processor Reset should cause the Processor Reset Counter ($sc_$cpu_ES_ProcResetCnt) to exceed OR EQUAL the limit CFE_ES_MAX_PROCESSOR_RESETS (which is reported in housekeeping telemetry as $sc_$cpu_ES_MaxProcResets), the command is AUTOMATICALLY upgraded to a Power-On Reset

    app = CFE_ES
    command = RESET
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 2
    data_len = 2 bytes
    """
    name = "CFE_ES_RESET_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER RESTART_TYPE 16 UINT MIN_UINT16 MAX_UINT16 0 "CFE_ES_PROCESSOR_RESET=Processor Reset or CFE_ES_POWERON_RESET=Power-On Reset"
        ShortField("RESTART_TYPE", 0),
    ]


bind_layers(CCSDSPacket, CFE_ES_RESET_CmdPkt, pkttype=1, apid=6, cmd_func_code=2)


class CFE_ES_SHELL_CmdPkt(Packet):
    """This command passes an ASCII string as a command line to the underlying realtime operating system shell. Any response to the command is both written to the shell command output file and sent as a series of shell command output telemetry packets

    app = CFE_ES
    command = SHELL
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 3
    data_len = 128 bytes
    """
    name = "CFE_ES_SHELL_CmdPkt"
    fields_desc = [
        # APPEND_ARRAY_PARAMETER CMD_STRING        8 UINT 512 "ASCII text string containing shell command to be executed"
        StrFixedLenField("CMD_STRING", b"", 64),
        # APPEND_PARAMETER       OUTPUT_FILENAME 512 STRING   "default" "Filename where shell command output is to be written"
        StrFixedLenField("OUTPUT_FILENAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, CFE_ES_SHELL_CmdPkt, pkttype=1, apid=6, cmd_func_code=3)


class CFE_ES_START_APP_CmdPkt(Packet):
    """This command starts the specified application with the specified start address, stack size, etc options

    app = CFE_ES
    command = START_APP
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 4
    data_len = 112 bytes
    """
    name = "CFE_ES_START_APP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME         160 STRING "APPNAME" "Name of Application to be started"
        StrFixedLenField("APP_NAME", b"APPNAME", 20),
        # APPEND_PARAMETER APP_ENTRY_POINT  160 STRING "APPNAME_AppMain" "Symbolic name of Application's entry point"
        StrFixedLenField("APP_ENTRY_POINT", b"APPNAME_AppMain", 20),
        # APPEND_PARAMETER APP_FILENAME     512 STRING "/cf/appname.so" "Full path and filename of Application's executable image"
        StrFixedLenField("APP_FILENAME", b"/cf/appname.so", 64),
        # APPEND_PARAMETER STACK_SIZE        32 UINT MIN_UINT32 MAX_UINT32 8192 "Desired stack size for the new application"
        IntField("STACK_SIZE", 8192),
        # APPEND_PARAMETER EXCEPTION_ACTION  16 UINT MIN_UINT16 MAX_UINT16 0 "CFE_ES_APP_EXCEPTION_RESTART_APP=On exception, restart Application, CFE_ES_APP_EXCEPTION_PROC_RESTART=On exception, perform a Processor Reset"
        ShortField("EXCEPTION_ACTION", 0),
        # APPEND_PARAMETER PRIORITY          16 UINT MIN_UINT16 MAX_UINT16 0 "The new Applications runtime priority"
        ShortField("PRIORITY", 0),
    ]


bind_layers(CCSDSPacket, CFE_ES_START_APP_CmdPkt, pkttype=1, apid=6, cmd_func_code=4)


class CFE_ES_STOP_APP_CmdPkt(Packet):
    """This command halts and removes the specified Application from the system. NOTE: This command should never be used on the Command Ingest application. This would prevent further commands from entering the system. If Command Ingest needs to be stopped and restarted, use CFE_ES_RESTART_APP_CC or CFE_ES_RELOAD_APP_CC

    app = CFE_ES
    command = STOP_APP
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 5
    data_len = 20 bytes
    """
    name = "CFE_ES_STOP_APP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING "APPNAME" "ASCII text string containing Application Name"
        StrFixedLenField("APP_NAME", b"APPNAME", 20),
    ]


bind_layers(CCSDSPacket, CFE_ES_STOP_APP_CmdPkt, pkttype=1, apid=6, cmd_func_code=5)


class CFE_ES_RESTART_APP_CmdPkt(Packet):
    """This command halts and restarts the specified Application. This command does NOT reload the application from the onboard filesystem

    app = CFE_ES
    command = RESTART_APP
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 6
    data_len = 20 bytes
    """
    name = "CFE_ES_RESTART_APP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING "default" "ASCII text string containing Application Name"
        StrFixedLenField("APP_NAME", b"default", 20),
    ]


bind_layers(CCSDSPacket, CFE_ES_RESTART_APP_CmdPkt, pkttype=1, apid=6, cmd_func_code=6)


class CFE_ES_RELOAD_APP_CmdPkt(Packet):
    """This command halts and removes the specified Application from the system. Then it immediately loads the Application from the command specified file and restarts it. This command is especially useful for restarting a Command Ingest Application since once it has been stopped, no further commands can come in to restart it

    app = CFE_ES
    command = RELOAD_APP
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 7
    data_len = 84 bytes
    """
    name = "CFE_ES_RELOAD_APP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME     160 STRING "default" "ASCII text string containing Application Name"
        StrFixedLenField("APP_NAME", b"default", 20),
        # APPEND_PARAMETER APP_FILENAME 512 STRING "default" "Full path and filename of Application's executable image"
        StrFixedLenField("APP_FILENAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, CFE_ES_RELOAD_APP_CmdPkt, pkttype=1, apid=6, cmd_func_code=7)


class CFE_ES_SEND_APP_INFO_CmdPkt(Packet):
    """Send a telemetry packet containing the command-specified app registry data

    app = CFE_ES
    command = SEND_APP_INFO
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 8
    data_len = 20 bytes
    """
    name = "CFE_ES_SEND_APP_INFO_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING "default" "ASCII text string containing Application Name"
        StrFixedLenField("APP_NAME", b"default", 20),
    ]


bind_layers(CCSDSPacket, CFE_ES_SEND_APP_INFO_CmdPkt, pkttype=1, apid=6, cmd_func_code=8)


class CFE_ES_WRITE_APP_INFO_TO_FILE_CmdPkt(Packet):
    """Write the entire app registry data to the command specified file

    app = CFE_ES
    command = WRITE_APP_INFO_TO_FILE
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 9
    data_len = 64 bytes
    """
    name = "CFE_ES_WRITE_APP_INFO_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/cfe_es_app_info.log" "ASCII text string containing full path and filename of file in which Application data is to be dumped"
        StrFixedLenField("FILENAME", b"/cf/cfe_es_app_info.log", 64),
    ]


bind_layers(CCSDSPacket, CFE_ES_WRITE_APP_INFO_TO_FILE_CmdPkt, pkttype=1, apid=6, cmd_func_code=9)


class CFE_ES_CLEAR_SYSLOG_CmdPkt(Packet):
    """This command clears the contents of the Executive Services System Log

    app = CFE_ES
    command = CLEAR_SYSLOG
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 10
    data_len = 0 bytes
    """
    name = "CFE_ES_CLEAR_SYSLOG_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_ES_CLEAR_SYSLOG_CmdPkt, pkttype=1, apid=6, cmd_func_code=10)


class CFE_ES_WRITE_SYSLOG_TO_FILE_CmdPkt(Packet):
    """This command causes the contents of the Executive Services System Log to be written to a log file

    app = CFE_ES
    command = WRITE_SYSLOG_TO_FILE
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 11
    data_len = 64 bytes
    """
    name = "CFE_ES_WRITE_SYSLOG_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/cfe_es_syslog.log" "ASCII text string containing full path and filename of file in which System Log is to be dumped"
        StrFixedLenField("FILENAME", b"/cf/cfe_es_syslog.log", 64),
    ]


bind_layers(CCSDSPacket, CFE_ES_WRITE_SYSLOG_TO_FILE_CmdPkt, pkttype=1, apid=6, cmd_func_code=11)


class CFE_ES_CLEAR_ERLOG_CmdPkt(Packet):
    """This command causes the contents of the Executive Services Exception and Reset Log to be cleared

    app = CFE_ES
    command = CLEAR_ERLOG
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 12
    data_len = 0 bytes
    """
    name = "CFE_ES_CLEAR_ERLOG_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_ES_CLEAR_ERLOG_CmdPkt, pkttype=1, apid=6, cmd_func_code=12)


class CFE_ES_WRITE_ERLOG_TO_FILE_CmdPkt(Packet):
    """This command causes the contents of the Executive Services Exception and Reset Log to be written to the specified file

    app = CFE_ES
    command = WRITE_ERLOG_TO_FILE
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 13
    data_len = 64 bytes
    """
    name = "CFE_ES_WRITE_ERLOG_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/cfe_erlog.log" "ASCII text string containing full path and filename of file in which ER Log is to be dumped"
        StrFixedLenField("FILENAME", b"/cf/cfe_erlog.log", 64),
    ]


bind_layers(CCSDSPacket, CFE_ES_WRITE_ERLOG_TO_FILE_CmdPkt, pkttype=1, apid=6, cmd_func_code=13)


class CFE_ES_START_LA_DATA_CmdPkt(Packet):
    """This command causes the Performance Analyzer to begin collecting data using the specified trigger mode

    app = CFE_ES
    command = START_LA_DATA
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 14
    data_len = 4 bytes
    """
    name = "CFE_ES_START_LA_DATA_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TRIG_MODE 32 UINT MIN_UINT32 MAX_UINT32 0 "Desired trigger position (Start, Center, End)"
        IntField("TRIG_MODE", 0),
    ]


bind_layers(CCSDSPacket, CFE_ES_START_LA_DATA_CmdPkt, pkttype=1, apid=6, cmd_func_code=14)


class CFE_ES_STOP_LA_DATA_CmdPkt(Packet):
    """This command stops the Performance Analyzer from collecting any more data

    app = CFE_ES
    command = STOP_LA_DATA
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 15
    data_len = 64 bytes
    """
    name = "CFE_ES_STOP_LA_DATA_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER DATA_FILENAME 512 STRING "default" "ASCII text string of full path and filename of file Performance Analyzer data is to be written"
        StrFixedLenField("DATA_FILENAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, CFE_ES_STOP_LA_DATA_CmdPkt, pkttype=1, apid=6, cmd_func_code=15)


class CFE_ES_SET_LA_FILTER_MASK_CmdPkt(Packet):
    """This command sets the Performance Analyzer's Filter Masks

    app = CFE_ES
    command = SET_LA_FILTER_MASK
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 16
    data_len = 8 bytes
    """
    name = "CFE_ES_SET_LA_FILTER_MASK_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILTER_MASK_NUM 32 UINT MIN_UINT32 MAX_UINT32 0 "Index into array of Filter Masks"
        IntField("FILTER_MASK_NUM", 0),
        # APPEND_PARAMETER FILTER_MASK     32 UINT MIN_UINT32 MAX_UINT32 0 "New Mask for specified entry in array of Filter Masks"
        IntField("FILTER_MASK", 0),
    ]


bind_layers(CCSDSPacket, CFE_ES_SET_LA_FILTER_MASK_CmdPkt, pkttype=1, apid=6, cmd_func_code=16)


class CFE_ES_SET_LA_TRIG_MASK_CmdPkt(Packet):
    """This command sets the Performance Analyzer's Trigger Masks

    app = CFE_ES
    command = SET_LA_TRIG_MASK
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 17
    data_len = 8 bytes
    """
    name = "CFE_ES_SET_LA_TRIG_MASK_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TRIG_MASK_NUM 32 UINT MIN_UINT32 MAX_UINT32 0 "Index into array of Trigger Masks"
        IntField("TRIG_MASK_NUM", 0),
        # APPEND_PARAMETER TRIG_MASK     32 UINT MIN_UINT32 MAX_UINT32 0 "New Mask for specified entry in array of Trigger Masks"
        IntField("TRIG_MASK", 0),
    ]


bind_layers(CCSDSPacket, CFE_ES_SET_LA_TRIG_MASK_CmdPkt, pkttype=1, apid=6, cmd_func_code=17)


class CFE_ES_OVERWRITE_SYSLOG_MODE_CmdPkt(Packet):
    """This command allows the user to configure the Executive Services to either discard new System Log messages when it is full or to overwrite the oldest messages

    app = CFE_ES
    command = OVERWRITE_SYSLOG_MODE
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 18
    data_len = 4 bytes
    """
    name = "CFE_ES_OVERWRITE_SYSLOG_MODE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MODE 32 UINT MIN_UINT32 MAX_UINT32 0 "CFE_ES_LOG_DISCARD=Throw away most recent messages, CFE_ES_LOG_OVERWRITE=Overwrite oldest with most recent"
        IntField("MODE", 0),
    ]


bind_layers(CCSDSPacket, CFE_ES_OVERWRITE_SYSLOG_MODE_CmdPkt, pkttype=1, apid=6, cmd_func_code=18)


class CFE_ES_RESET_PR_CNT_CmdPkt(Packet):
    """This command allows the user to reset the Processor Reset Counter to zero. The Processor Reset Counter counts the number of Processor Resets that have occurred so as to identify when a Processor Reset should automatically be upgraded to a full Power-On Reset

    app = CFE_ES
    command = RESET_PR_CNT
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 19
    data_len = 0 bytes
    """
    name = "CFE_ES_RESET_PR_CNT_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_ES_RESET_PR_CNT_CmdPkt, pkttype=1, apid=6, cmd_func_code=19)


class CFE_ES_SET_MAX_PR_CNT_CmdPkt(Packet):
    """This command allows the user to specify the number of Processor Resets that are allowed before the next Processor Reset is upgraded to a Power-On Reset

    app = CFE_ES
    command = SET_MAX_PR_CNT
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 20
    data_len = 2 bytes
    """
    name = "CFE_ES_SET_MAX_PR_CNT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MAX_PROCESSOR_COUNT 16 UINT MIN_UINT16 MAX_UINT16 0 "New maximum number of Processor Resets before an automatic Power-On Reset is performed"
        ShortField("MAX_PROCESSOR_COUNT", 0),
    ]


bind_layers(CCSDSPacket, CFE_ES_SET_MAX_PR_CNT_CmdPkt, pkttype=1, apid=6, cmd_func_code=20)


class CFE_ES_DELETE_CDS_CmdPkt(Packet):
    """This command allows the user to delete a Critical Data Store that was created by an Application that is now no longer executing

    app = CFE_ES
    command = DELETE_CDS
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 21
    data_len = 38 bytes
    """
    name = "CFE_ES_DELETE_CDS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CDS_NAME 304 STRING "default" "ASCII text string containing name of CDS to delete"
        StrFixedLenField("CDS_NAME", b"default", 38),
    ]


bind_layers(CCSDSPacket, CFE_ES_DELETE_CDS_CmdPkt, pkttype=1, apid=6, cmd_func_code=21)


class CFE_ES_SEND_MEM_POOL_STATS_CmdPkt(Packet):
    """This command allows the user to obtain a snapshot of the statistics maintained for a specified memory pool

    app = CFE_ES
    command = SEND_MEM_POOL_STATS
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 22
    data_len = 24 bytes
    """
    name = "CFE_ES_SEND_MEM_POOL_STATS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER RESERVED    160 STRING "default" "RESERVED - should be all zeros"
        StrFixedLenField("RESERVED", b"default", 20),
        # APPEND_PARAMETER POOL_HANDLE  32 UINT MIN_UINT32 MAX_UINT32 0 "Handle of Pool whose statistics are to be telemetered."
        IntField("POOL_HANDLE", 0),
    ]


bind_layers(CCSDSPacket, CFE_ES_SEND_MEM_POOL_STATS_CmdPkt, pkttype=1, apid=6, cmd_func_code=22)


class CFE_ES_WRITE_CDS_REG_TO_FILE_CmdPkt(Packet):
    """This command allows the user to dump the Critical Data Store Registry to an onboard file.

    app = CFE_ES
    command = WRITE_CDS_REG_TO_FILE
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 23
    data_len = 64 bytes
    """
    name = "CFE_ES_WRITE_CDS_REG_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/cfe_cds_reg.log" "ASCII text string of full path and filename of file CDS Registry is to be written."
        StrFixedLenField("FILENAME", b"/cf/cfe_cds_reg.log", 64),
    ]


bind_layers(CCSDSPacket, CFE_ES_WRITE_CDS_REG_TO_FILE_CmdPkt, pkttype=1, apid=6, cmd_func_code=23)


class CFE_ES_WRITE_TASK_INFO_TO_FILE_CmdPkt(Packet):
    """This command takes the information kept by Executive Services on all of the registered tasks and writes it to the specified file.

    app = CFE_ES
    command = WRITE_TASK_INFO_TO_FILE
    msg_id = CFE_ES_CMD_MID = 0x1806 = 0x1800 + 0x006
    cmd_func_code = 24
    data_len = 64 bytes
    """
    name = "CFE_ES_WRITE_TASK_INFO_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/cfe_es_task_info.log" "Full path and filename of file in which Application data is to be dumped."
        StrFixedLenField("FILENAME", b"/cf/cfe_es_task_info.log", 64),
    ]


bind_layers(CCSDSPacket, CFE_ES_WRITE_TASK_INFO_TO_FILE_CmdPkt, pkttype=1, apid=6, cmd_func_code=24)
