from scapy.all import *
from ccsds_base import CCSDSPacket


class CFE_TBL_HK_TLM_PKT_TlmPkt(Packet):
    """Housekeeping data (general status) autonomously sent

    app = CFE_TBL
    command = HK_TLM_PKT
    msg_id = CFE_TBL_HK_TLM_MID = 0x0804 = 0x0800 + 0x004
    """
    name = "CFE_TBL_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT         8 UINT "Count of valid commands received."
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT         8 UINT "Count of invalid commands received."
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM NUM_TABLES             16 UINT "Number of Tables Registered."
        ShortField("NUM_TABLES", 0),
        # APPEND_ITEM NUM_LOAD_PEND          16 UINT "Number of Tables pending on Applications for their update."
        ShortField("NUM_LOAD_PEND", 0),
        # APPEND_ITEM VALIDATION_CTR         16 UINT "Number of completed table validations."
        ShortField("VALIDATION_CTR", 0),
        # APPEND_ITEM LAST_VAL_CRC           32 UINT "Data Integrity Value computed for last table validated."
        IntField("LAST_VAL_CRC", 0),
        # APPEND_ITEM LAST_VAL_STATUS        32  INT "Returned status from validation function for last table validated."
        SignedIntField("LAST_VAL_STATUS", 0),
        # APPEND_ITEM LAST_VAL_BUFFER         8 UINT "Indicator of whether table buffer validated was 0=Inactive, 1=Active."
        ByteField("LAST_VAL_BUFFER", 0),
        # STATE Inactive 0
        # STATE Active   1
        # APPEND_ITEM LAST_VAL_TBL_NAME     320 STRING "Name of last table validated."
        StrFixedLenField("LAST_VAL_TBL_NAME", b"", 40),
        # APPEND_ITEM SUCCESS_VAL_CTR         8 UINT "Total number of successful table validations."
        ByteField("SUCCESS_VAL_CTR", 0),
        # APPEND_ITEM FAILED_VAL_CTR          8 UINT "Total number of unsuccessful table validations."
        ByteField("FAILED_VAL_CTR", 0),
        # APPEND_ITEM NUM_VAL_REQUESTS        8 UINT "Number of times Table Services has requested validations from Apps."
        ByteField("NUM_VAL_REQUESTS", 0),
        # APPEND_ITEM NUM_FREE_SHARED_BUFS    8 UINT "Number of free Shared Working Buffers."
        ByteField("NUM_FREE_SHARED_BUFS", 0),
        # APPEND_ITEM BYTE_ALIGN_PAD1         8 UINT "Spare byte to ensure longword alignment."
        ByteField("BYTE_ALIGN_PAD1", 0),
        # APPEND_ITEM MEM_POOL_HANDLE        32 UINT "Handle to TBL's memory pool."
        IntField("MEM_POOL_HANDLE", 0),
        # APPEND_ITEM SPARE1                 16 UINT "TODO - Somethings off by 16. Could it be 48-bit cpuaddr?"
        ShortField("SPARE1", 0),
        # APPEND_ITEM LAST_UPD_TIME_SECONDS  32 UINT "Number of seconds since epoch. (Parent: Time of last table update.)"
        IntField("LAST_UPD_TIME_SECONDS", 0),
        # APPEND_ITEM LAST_UPD_TIME_SUBSECS  32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: Time of last table update.)"
        IntField("LAST_UPD_TIME_SUBSECS", 0),
        # APPEND_ITEM LAST_UPD_TBL_NAME     320 STRING "Name of the last table updated."
        StrFixedLenField("LAST_UPD_TBL_NAME", b"", 40),
        # APPEND_ITEM LAST_FILE_LOADED      512 STRING "Path and Name of last table image file loaded."
        StrFixedLenField("LAST_FILE_LOADED", b"", 64),
        # APPEND_ITEM LAST_FILE_DUMPED      512 STRING "Path and Name of last file dumped to."
        StrFixedLenField("LAST_FILE_DUMPED", b"", 64),
        # APPEND_ITEM LAST_TABLE_LOADED     320 STRING "Name of the last table loaded."
        StrFixedLenField("LAST_TABLE_LOADED", b"", 40),
    ]


bind_layers(CCSDSPacket, CFE_TBL_HK_TLM_PKT_TlmPkt, pkttype=0, apid=4)


class CFE_TBL_TBL_REGISTRY_PKT_TlmPkt(Packet):
    """Table Registry Info Packet sent in response to a SEND_REGISTRY command

    app = CFE_TBL
    command = TBL_REGISTRY_PKT
    msg_id = CFE_TBL_REG_TLM_MID = 0x080c = 0x0800 + 0x00c
    """
    name = "CFE_TBL_TBL_REGISTRY_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM SIZE                     32 UINT "Size, in bytes, of Table."
        IntField("SIZE", 0),
        # APPEND_ITEM CRC                      32 UINT "Most recently calculated CRC of Table."
        IntField("CRC", 0),
        # APPEND_ITEM ACTIVE_BUF_ADDR          32 UINT "Address of Active Buffer."
        IntField("ACTIVE_BUF_ADDR", 0),
        # APPEND_ITEM INACTIVE_BUF_ADDR        32 UINT "Address of Inactive Buffer."
        IntField("INACTIVE_BUF_ADDR", 0),
        # APPEND_ITEM VALIDATION_FUNC_PTR      32 UINT "Ptr to Owner App's function that validates tbl contents."
        IntField("VALIDATION_FUNC_PTR", 0),
        # APPEND_ITEM LAST_UPD_TIME_SECONDS    32 UINT "Number of seconds since epoch. (Parent: Time when Table was last updated.)"
        IntField("LAST_UPD_TIME_SECONDS", 0),
        # APPEND_ITEM LAST_UPD_TIME_SUBSECS    32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: Time when Table was last updated.)"
        IntField("LAST_UPD_TIME_SUBSECS", 0),
        # APPEND_ITEM FILE_CREATE_TIME_SECS    32 UINT "File creation time from last file loaded into table."
        IntField("FILE_CREATE_TIME_SECS", 0),
        # APPEND_ITEM FILE_CREATE_TIME_SUBSECS 32 UINT "File creation time from last file loaded into table."
        IntField("FILE_CREATE_TIME_SUBSECS", 0),
        # APPEND_ITEM TABLE_LOADED_ONCE         8 UINT "Flag indicating whether table has been loaded once or not."
        ByteField("TABLE_LOADED_ONCE", 0),
        # APPEND_ITEM LOAD_PENDING              8 UINT "Flag indicating an inactive buffer is ready to be copied."
        ByteField("LOAD_PENDING", 0),
        # APPEND_ITEM DUMP_ONLY                 8 UINT "Flag indicating Table is NOT to be loaded."
        ByteField("DUMP_ONLY", 0),
        # APPEND_ITEM DBL_BUFFERED              8 UINT "Flag indicating Table has a dedicated inactive buffer."
        ByteField("DBL_BUFFERED", 0),
        # APPEND_ITEM NAME                    320 STRING "Processor specific table name."
        StrFixedLenField("NAME", b"", 40),
        # APPEND_ITEM LAST_FILE_LOADED        512 STRING "Filename of last file loaded into table."
        StrFixedLenField("LAST_FILE_LOADED", b"", 64),
        # APPEND_ITEM OWNER_APP_NAME          176 STRING "Name of owning application."
        StrFixedLenField("OWNER_APP_NAME", b"", 22),
        # APPEND_ITEM CRITICAL                  8 UINT "Indicates whether table is Critical or not."
        ByteField("CRITICAL", 0),
        # APPEND_ITEM BYTE_ALIGN_4              8 UINT "Spare byte to maintain byte alignment."
        ByteField("BYTE_ALIGN_4", 0),
    ]


bind_layers(CCSDSPacket, CFE_TBL_TBL_REGISTRY_PKT_TlmPkt, pkttype=0, apid=12)
