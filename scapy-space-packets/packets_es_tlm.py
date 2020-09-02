from scapy.all import *
from ccsds_base import CCSDSPacket


class CFE_ES_HK_TLM_PKT_TlmPkt(Packet):
    """Housekeeping data (general status) autonomously sent

    app = CFE_ES
    command = HK_TLM_PKT
    msg_id = CFE_ES_HK_TLM_MID = 0x0800 = 0x0800 + 0x000
    """
    name = "CFE_ES_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT     8 UINT "The ES Application Command Counter."
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT     8 UINT "The ES Application Command Error Counter."
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM CFE_CORE_CHECKSUM  16 UINT "Checksum of cFE Core Code."
        ShortField("CFE_CORE_CHECKSUM", 0),
        # APPEND_ITEM CFE_MAJOR_VER       8 UINT "Major Version Number of cFE."
        ByteField("CFE_MAJOR_VER", 0),
        # APPEND_ITEM CFE_MINOR_VER       8 UINT "Minor Version Number of cFE."
        ByteField("CFE_MINOR_VER", 0),
        # APPEND_ITEM CFE_REV             8 UINT "Sub-Minor Version Number of cFE."
        ByteField("CFE_REV", 0),
        # APPEND_ITEM CFE_MISSION_REV     8 UINT "Mission Version Number of cFE."
        ByteField("CFE_MISSION_REV", 0),
        # APPEND_ITEM OSAL_MAJOR_VER      8 UINT "OS Abstraction Layer Major Version Number."
        ByteField("OSAL_MAJOR_VER", 0),
        # APPEND_ITEM OSAL_MINOR_VER      8 UINT "OS Abstraction Layer Minor Version Number."
        ByteField("OSAL_MINOR_VER", 0),
        # APPEND_ITEM OSAL_REVISION       8 UINT "OS Abstraction Layer Revision Number."
        ByteField("OSAL_REVISION", 0),
        # APPEND_ITEM OSAL_MISSION_REV    8 UINT "OS Abstraction Layer MissionRevision Number."
        ByteField("OSAL_MISSION_REV", 0),
        # APPEND_ITEM SYSLOG_BYTES_USED  32 UINT "Total number of bytes used in system log."
        IntField("SYSLOG_BYTES_USED", 0),
        # APPEND_ITEM SYSLOG_SIZE        32 UINT "Total size of the system log."
        IntField("SYSLOG_SIZE", 0),
        # APPEND_ITEM SYSLOG_ENTRIES     32 UINT "Number of entries in the system log."
        IntField("SYSLOG_ENTRIES", 0),
        # APPEND_ITEM SYSLOG_MODE        32 UINT "Write/Overwrite Mode."
        IntField("SYSLOG_MODE", 0),
        # APPEND_ITEM ERLOG_INDEX        32 UINT "Current index of the ER Log (wraps around)."
        IntField("ERLOG_INDEX", 0),
        # APPEND_ITEM ERLOG_ENTRIES      32 UINT "Number of entries made in the ER Log since the power on."
        IntField("ERLOG_ENTRIES", 0),
        # APPEND_ITEM REG_CORE_APPS      32 UINT "Number of Applications registered with ES."
        IntField("REG_CORE_APPS", 0),
        # APPEND_ITEM REG_EXT_APPS       32 UINT "Number of Applications registered with ES."
        IntField("REG_EXT_APPS", 0),
        # APPEND_ITEM REG_TASKS          32 UINT "Number of Tasks ( main AND child tasks ) registered with ES."
        IntField("REG_TASKS", 0),
        # APPEND_ITEM REG_LIBS           32 UINT "Number of Libraries registered with ES."
        IntField("REG_LIBS", 0),
        # APPEND_ITEM RESET_TYPE         32 UINT "Reset type ( PROCESSOR or POWERON ). Defined in cfe_psp.h"
        IntField("RESET_TYPE", 0),
        # STATE Processor 1
        # STATE PowerOn   2
        # APPEND_ITEM RESET_SUBTYPE      32 UINT "Reset Sub Type."
        IntField("RESET_SUBTYPE", 0),
        # APPEND_ITEM PROC_RESETS        32 UINT "Number of processor resets since last power on."
        IntField("PROC_RESETS", 0),
        # APPEND_ITEM MAX_PROC_RESETS    32 UINT "Max processor resets before a power on is done."
        IntField("MAX_PROC_RESETS", 0),
        # APPEND_ITEM BOOT_SOURCE        32 UINT "Boot source ( as provided from BSP )."
        IntField("BOOT_SOURCE", 0),
        # APPEND_ITEM PERF_STATE         32 UINT "Current state of Performance Analyzer."
        IntField("PERF_STATE", 0),
        # APPEND_ITEM PERF_MODE          32 UINT "Current mode of Performance Analyzer."
        IntField("PERF_MODE", 0),
        # APPEND_ITEM PERF_TRIG_COUNT    32 UINT "Number of Times Perfomance Analyzer has Triggered."
        IntField("PERF_TRIG_COUNT", 0),
        # APPEND_ITEM PERF_FILTER_MASK0  32 UINT "Current Setting of Performance Analyzer Filter Masks."
        IntField("PERF_FILTER_MASK0", 0),
        # APPEND_ITEM PERF_FILTER_MASK1  32 UINT "Current Setting of Performance Analyzer Filter Masks."
        IntField("PERF_FILTER_MASK1", 0),
        # APPEND_ITEM PERF_FILTER_MASK2  32 UINT "Current Setting of Performance Analyzer Filter Masks."
        IntField("PERF_FILTER_MASK2", 0),
        # APPEND_ITEM PERF_FILTER_MASK3  32 UINT "Current Setting of Performance Analyzer Filter Masks."
        IntField("PERF_FILTER_MASK3", 0),
        # APPEND_ITEM PERF_TRIG_MASK0    32 UINT "Current Setting of Performance Analyzer Trigger Masks."
        IntField("PERF_TRIG_MASK0", 0),
        # APPEND_ITEM PERF_TRIG_MASK1    32 UINT "Current Setting of Performance Analyzer Trigger Masks."
        IntField("PERF_TRIG_MASK1", 0),
        # APPEND_ITEM PERF_TRIG_MASK2    32 UINT "Current Setting of Performance Analyzer Trigger Masks."
        IntField("PERF_TRIG_MASK2", 0),
        # APPEND_ITEM PERF_TRIG_MASK3    32 UINT "Current Setting of Performance Analyzer Trigger Masks."
        IntField("PERF_TRIG_MASK3", 0),
        # APPEND_ITEM PERF_DATA_START    32 UINT "Identifies First Stored Entry in Performance Analyzer Log."
        IntField("PERF_DATA_START", 0),
        # APPEND_ITEM PERF_DATA_END      32 UINT "Identifies Last Stored Entry in Performance Analyzer Log."
        IntField("PERF_DATA_END", 0),
        # APPEND_ITEM PERF_DATA_COUNT    32 UINT "Number of Entries Put Into the Performance Analyzer Log."
        IntField("PERF_DATA_COUNT", 0),
        # APPEND_ITEM PERF_DATA_TO_WRITE 32 UINT "Number of Performance Analyzer Log Entries Left to be Written to Log Dump File."
        IntField("PERF_DATA_TO_WRITE", 0),
        # APPEND_ITEM HEAP_BYTES_FREE    32 UINT "Number of free bytes remaining in the OS heap."
        IntField("HEAP_BYTES_FREE", 0),
        # APPEND_ITEM HEAP_BLOCKS_FREE   32 UINT "Number of free blocks remaining in the OS heap."
        IntField("HEAP_BLOCKS_FREE", 0),
        # APPEND_ITEM HEAP_MAX_BLOCKSIZE 32 UINT "Number of bytes in the largest free block."
        IntField("HEAP_MAX_BLOCKSIZE", 0),
    ]


bind_layers(CCSDSPacket, CFE_ES_HK_TLM_PKT_TlmPkt, pkttype=0, apid=0)


class CFE_ES_APP_INFO_TLM_PKT_TlmPkt(Packet):
    """Single Application Information Packet (CFE_ES_AppInfo_t) sent in response to a SEND_APP_INFO command

    app = CFE_ES
    command = APP_INFO_TLM_PKT
    msg_id = CFE_ES_APP_TLM_MID = 0x080b = 0x0800 + 0x00b
    """
    name = "CFE_ES_APP_INFO_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM APP_ID              32 UINT   "Application Identifier assigned by ES"
        IntField("APP_ID", 0),
        # APPEND_ITEM TYPE                32 UINT   "App type: CORE or EXTERNAL"
        IntField("TYPE", 0),
        # APPEND_ITEM NAME               160 STRING "Registered Name of the Application"
        StrFixedLenField("NAME", b"", 20),
        # APPEND_ITEM ENTRY_POINT        160 STRING "Entry Point label for the Application"
        StrFixedLenField("ENTRY_POINT", b"", 20),
        # APPEND_ITEM FILENAME           512 STRING "Filename of the file containing the Application"
        StrFixedLenField("FILENAME", b"", 64),
        # APPEND_ITEM STACK_SIZE          32 UINT   "Stack Size of the Application"
        IntField("STACK_SIZE", 0),
        # APPEND_ITEM MODULE_ID           32 UINT   "The ID of the Loadable Module for the Application"
        IntField("MODULE_ID", 0),
        # APPEND_ITEM ADDR__ARE_VALID     32 UINT   "Indicates that the Code, Data, and BSS addresses/sizes are valid"
        IntField("ADDR__ARE_VALID", 0),
        # APPEND_ITEM CODE_ADDR           32 UINT   "Address of the Application Code Segment"
        IntField("CODE_ADDR", 0),
        # APPEND_ITEM CODE_SIZE           32 UINT   "Code Size of the Application"
        IntField("CODE_SIZE", 0),
        # APPEND_ITEM DATA_ADDR           32 UINT   "Address of the Application Data Segment"
        IntField("DATA_ADDR", 0),
        # APPEND_ITEM DATA_SIZE           32 UINT   "Data Size of the Application"
        IntField("DATA_SIZE", 0),
        # APPEND_ITEM BSS_ADDR            32 UINT   "Address of the Application BSS Segment"
        IntField("BSS_ADDR", 0),
        # APPEND_ITEM BSS_SIZE            32 UINT   "BSS Size of the Application"
        IntField("BSS_SIZE", 0),
        # APPEND_ITEM START_ADDR          32 UINT   "Start Address of the Application"
        IntField("START_ADDR", 0),
        # APPEND_ITEM EXCEPTION_ACTION    16 UINT   "What should occur if Application has an exception (Restart Application OR Restart Processor)"
        ShortField("EXCEPTION_ACTION", 0),
        # APPEND_ITEM PRIORITY            16 UINT   "The Priority of the Application"
        ShortField("PRIORITY", 0),
        # APPEND_ITEM MAIN_TASK_ID        32 UINT   "App's Main Task ID"
        IntField("MAIN_TASK_ID", 0),
        # APPEND_ITEM EXECUTION_COUNTER   32 UINT   "App's Main Task Execution Counter"
        IntField("EXECUTION_COUNTER", 0),
        # APPEND_ITEM MAIN_TASK_NAME     160 STRING "App's Main Task ID"
        StrFixedLenField("MAIN_TASK_NAME", b"", 20),
        # APPEND_ITEM NUM_OF_CHILD_TASKS  32 UINT   "Number of Child tasks"
        IntField("NUM_OF_CHILD_TASKS", 0),
    ]


bind_layers(CCSDSPacket, CFE_ES_APP_INFO_TLM_PKT_TlmPkt, pkttype=0, apid=11)


class CFE_ES_MEM_POOL_STATS_TLM_PKT_TlmPkt(Packet):
    """Memory Pool Statistics Packet sent in response to a SEND_MEM_POOL_STATS command

    app = CFE_ES
    command = MEM_POOL_STATS_TLM_PKT
    msg_id = CFE_ES_MEMSTATS_TLM_MID = 0x0810 = 0x0800 + 0x010
    """
    name = "CFE_ES_MEM_POOL_STATS_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM POOL_HANDLE                32 UINT      "Handle of memory pool whose stats are being telemetered."
        IntField("POOL_HANDLE", 0),
        # APPEND_ITEM POOL_STATS_POOL_SIZE       32 UINT      "Size of Memory Pool (in bytes). (Parent: For more info, see CFE_ES_MemPoolStats_t.)"
        IntField("POOL_STATS_POOL_SIZE", 0),
        # APPEND_ITEM POOL_STATS_NUM_BLOCKS_REQ  32 UINT      "Number of times a memory block has been allocated. (Parent: For more info, see CFE_ES_MemPoolStats_t.)"
        IntField("POOL_STATS_NUM_BLOCKS_REQ", 0),
        # APPEND_ITEM POOL_STATS_CHECK_ERR_CTR   32 UINT      "Number of errors detected when freeing a memory block. (Parent: For more info, see CFE_ES_MemPoolStats_t.)"
        IntField("POOL_STATS_CHECK_ERR_CTR", 0),
        # APPEND_ITEM POOL_STATS_NUM_FREE_BYTES  32 UINT      "Number of bytes never allocated to a block. (Parent: For more info, see CFE_ES_MemPoolStats_t.)"
        IntField("POOL_STATS_NUM_FREE_BYTES", 0),
        # APPEND_ARRAY_ITEM POOLSTATS_BLOCKSTATS 96 UINT 1632 "Contains stats on each block size. (Parent: For more info, see CFE_ES_MemPoolStats_t.)"
        StrFixedLenField("POOLSTATS_BLOCKSTATS__0", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__1", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__2", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__3", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__4", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__5", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__6", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__7", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__8", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__9", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__10", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__11", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__12", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__13", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__14", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__15", b"", 12),  # FIXME: XNBytesField should be better, if supported
        StrFixedLenField("POOLSTATS_BLOCKSTATS__16", b"", 12),  # FIXME: XNBytesField should be better, if supported
    ]


bind_layers(CCSDSPacket, CFE_ES_MEM_POOL_STATS_TLM_PKT_TlmPkt, pkttype=0, apid=16)


class CFE_ES_SHELL_TLM_PKT_TlmPkt(Packet):
    """OS Shell Output Packet sent in response to a ES_SHELL command

    app = CFE_ES
    command = SHELL_TLM_PKT
    msg_id = CFE_ES_SHELL_TLM_MID = 0x080f = 0x0800 + 0x00f
    """
    name = "CFE_ES_SHELL_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ARRAY_ITEM SHELL_OUTPUT 8 UINT 512 "ASCII text string containing output from OS Shell that was received in response to an OS Shell Command."
        StrFixedLenField("SHELL_OUTPUT", b"", 64),  # FIXME: XNBytesField should be better, if supported
    ]


bind_layers(CCSDSPacket, CFE_ES_SHELL_TLM_PKT_TlmPkt, pkttype=0, apid=15)
