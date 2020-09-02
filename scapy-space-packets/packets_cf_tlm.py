from scapy.all import *
from ccsds_base import CCSDSPacket


class CF_HK_TLM_PKT_TlmPkt(Packet):
    """CFDP housekeeping Packet

    app = CF
    command = HK_TLM_PKT
    msg_id = CF_HK_TLM_MID = 0x08b0 = 0x0800 + 0x0b0
    """
    name = "CF_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT                  16 UINT "Count of valid commands received."
        ShortField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT                  16 UINT "Count of invalid commands received."
        ShortField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM APP_WAKEUPFORFILEPROC            32 UINT "(Parent: )"
        IntField("APP_WAKEUPFORFILEPROC", 0),
        # APPEND_ITEM APP_ENGINECYCLECOUNT             32 UINT "(Parent: )"
        IntField("APP_ENGINECYCLECOUNT", 0),
        # APPEND_ITEM APP_MEMINUSE                     32 UINT "(Parent: )"
        IntField("APP_MEMINUSE", 0),
        # APPEND_ITEM APP_PEAKMEMINUSE                 32 UINT "(Parent: )"
        IntField("APP_PEAKMEMINUSE", 0),
        # APPEND_ITEM APP_LOWMEMORYMARK                32 UINT "(Parent: )"
        IntField("APP_LOWMEMORYMARK", 0),
        # APPEND_ITEM APP_MAXMEMNEEDED                 32 UINT "(Parent: )"
        IntField("APP_MAXMEMNEEDED", 0),
        # APPEND_ITEM APP_MEMALLOCATED                 32 UINT "(Parent: )"
        IntField("APP_MEMALLOCATED", 0),
        # APPEND_ITEM APP_BUFFERPOOLHANDLE             32 UINT "(Parent: )"
        IntField("APP_BUFFERPOOLHANDLE", 0),
        # APPEND_ITEM APP_QNODESALLOCATED              32 UINT "(Parent: )"
        IntField("APP_QNODESALLOCATED", 0),
        # APPEND_ITEM APP_QNODESDEALLOCATED            32 UINT "(Parent: )"
        IntField("APP_QNODESDEALLOCATED", 0),
        # APPEND_ITEM APP_PDUSRECEIVED                 32 UINT "(Parent: )"
        IntField("APP_PDUSRECEIVED", 0),
        # APPEND_ITEM APP_PDUSREJECTED                 32 UINT "(Parent: )"
        IntField("APP_PDUSREJECTED", 0),
        # APPEND_ITEM APP_TOTALINPROGTRANS             32 UINT "(Parent: )"
        IntField("APP_TOTALINPROGTRANS", 0),
        # APPEND_ITEM APP_TOTALFAILEDTRANS             32 UINT "(Parent: )"
        IntField("APP_TOTALFAILEDTRANS", 0),
        # APPEND_ITEM APP_TOTALABANDONTRANS            32 UINT "(Parent: )"
        IntField("APP_TOTALABANDONTRANS", 0),
        # APPEND_ITEM APP_TOTALSUCCESSTRANS            32 UINT "(Parent: )"
        IntField("APP_TOTALSUCCESSTRANS", 0),
        # APPEND_ITEM APP_TOTALCOMPLETEDTRANS          32 UINT "(Parent: )"
        IntField("APP_TOTALCOMPLETEDTRANS", 0),
        # APPEND_ITEM APP_LASTFAILEDTRANS             160 STRING "(Parent: )"
        StrFixedLenField("APP_LASTFAILEDTRANS", b"", 20),
        # APPEND_ITEM AUTOSUSPEND_ENFLAG               32 UINT "(Parent: )"
        IntField("AUTOSUSPEND_ENFLAG", 0),
        # APPEND_ITEM AUTOSUSPEND_LOWFREEMARK          32 UINT "(Parent: )"
        IntField("AUTOSUSPEND_LOWFREEMARK", 0),
        # APPEND_ITEM COND_POSACKNUM                    8 UINT "(Parent: )"
        ByteField("COND_POSACKNUM", 0),
        # APPEND_ITEM COND_FILESTOREREJNUM              8 UINT "(Parent: )"
        ByteField("COND_FILESTOREREJNUM", 0),
        # APPEND_ITEM COND_FILECHECKSUMNUM              8 UINT "(Parent: )"
        ByteField("COND_FILECHECKSUMNUM", 0),
        # APPEND_ITEM COND_FILESIZENUM                  8 UINT "(Parent: )"
        ByteField("COND_FILESIZENUM", 0),
        # APPEND_ITEM COND_NAKLIMITNUM                  8 UINT "(Parent: )"
        ByteField("COND_NAKLIMITNUM", 0),
        # APPEND_ITEM COND_INACTIVENUM                  8 UINT "(Parent: )"
        ByteField("COND_INACTIVENUM", 0),
        # APPEND_ITEM COND_SUSPENDNUM                   8 UINT "(Parent: )"
        ByteField("COND_SUSPENDNUM", 0),
        # APPEND_ITEM COND_CANCELNUM                    8 UINT "(Parent: )"
        ByteField("COND_CANCELNUM", 0),
        # APPEND_ITEM ENG_FLIGHTENGINEENTITYID        128 STRING "(Parent: )"
        StrFixedLenField("ENG_FLIGHTENGINEENTITYID", b"", 16),
        # APPEND_ITEM ENG_FLAGS                        32 UINT "(Parent: )"
        IntField("ENG_FLAGS", 0),
        # APPEND_ITEM ENG_MACHINESALLOCATED            32 UINT "(Parent: )"
        IntField("ENG_MACHINESALLOCATED", 0),
        # APPEND_ITEM ENG_MACHINESDEALLOCATED          32 UINT "(Parent: )"
        IntField("ENG_MACHINESDEALLOCATED", 0),
        # APPEND_ITEM ANY_PARTNERS_FROZEN               8 UINT "Are any partners frozen"
        ByteField("ANY_PARTNERS_FROZEN", 0),
        # APPEND_ARRAY_ITEM ENG_SPARE                   8 UINT 24 "(Parent: )"
        StrFixedLenField("ENG_SPARE", b"", 3),  # FIXME: XNBytesField should be better, if supported
        # APPEND_ITEM HOW_MANY_SENDERS                 32 UINT "active Senders?"
        IntField("HOW_MANY_SENDERS", 0),
        # APPEND_ITEM HOW_MANY_RECEIVERS               32 UINT "active Receivers?"
        IntField("HOW_MANY_RECEIVERS", 0),
        # APPEND_ITEM HOW_MANY_FROZEN                  32 UINT  "trans are frozen?"
        IntField("HOW_MANY_FROZEN", 0),
        # APPEND_ITEM HOW_MANY_SUSPENDED               32 UINT "trans are suspended?"
        IntField("HOW_MANY_SUSPENDED", 0),
        # APPEND_ITEM TOTAL_SENT                       32 UINT "files sent succesfully"
        IntField("TOTAL_SENT", 0),
        # APPEND_ITEM TOTAL_RECEIVED                   32 UINT "files received successfully"
        IntField("TOTAL_RECEIVED", 0),
        # APPEND_ITEM TOTAL_UNSUCCESSFUL_SENDERS       32 UINT "total unsuccessful senders"
        IntField("TOTAL_UNSUCCESSFUL_SENDERS", 0),
        # APPEND_ITEM TOTAL_UNSUCCESSFUL_RECEIVERS     32 UINT "total unsuccessful receivers"
        IntField("TOTAL_UNSUCCESSFUL_RECEIVERS", 0),
        # APPEND_ITEM UP_METACOUNT                     32 UINT "(Parent: )"
        IntField("UP_METACOUNT", 0),
        # APPEND_ITEM UP_UPLINKACTIVEQFILECNT          32 UINT "(Parent: )"
        IntField("UP_UPLINKACTIVEQFILECNT", 0),
        # APPEND_ITEM UP_SUCCESSCOUNTER                32 UINT "(Parent: )"
        IntField("UP_SUCCESSCOUNTER", 0),
        # APPEND_ITEM UP_FAILEDCOUNTER                 32 UINT "(Parent: )"
        IntField("UP_FAILEDCOUNTER", 0),
        # APPEND_ITEM UP_LASTFILEUPLINKED             512 STRING "(Parent: )"
        StrFixedLenField("UP_LASTFILEUPLINKED", b"", 64),
        # APPEND_ITEM CH0_PDU_SENT                     32 UINT "PDUsSent"
        IntField("CH0_PDU_SENT", 0),
        # APPEND_ITEM CH0_FILES_SENT                   32 UINT "Files Sent"
        IntField("CH0_FILES_SENT", 0),
        # APPEND_ITEM CH0_SUCCESS_COUNTER              32 UINT "Success Counter"
        IntField("CH0_SUCCESS_COUNTER", 0),
        # APPEND_ITEM CH0_FAILED_COUNTER               32 UINT "Failed Counter"
        IntField("CH0_FAILED_COUNTER", 0),
        # APPEND_ITEM CH0_PENDING_Q_FILECNT            32 UINT "PendingQFileCnt"
        IntField("CH0_PENDING_Q_FILECNT", 0),
        # APPEND_ITEM CH0_ACTIVE_Q_FILECNT             32 UINT "ActiveQFileCnt"
        IntField("CH0_ACTIVE_Q_FILECNT", 0),
        # APPEND_ITEM CH0_HISTORY_Q_FILECNT            32 UINT "HIstoryQFileCnt"
        IntField("CH0_HISTORY_Q_FILECNT", 0),
        # APPEND_ITEM CH0_FLAGS                        32 UINT "0=ChanDequeue enabled,1=Chan Blast In progress"
        IntField("CH0_FLAGS", 0),
        # APPEND_ITEM CH0_RED_LIGHT_CNTR               32 UINT "RedLightCntr"
        IntField("CH0_RED_LIGHT_CNTR", 0),
        # APPEND_ITEM CH0_GREEN_LIGHT_CNTR             32 UINT "GreenLightCntr"
        IntField("CH0_GREEN_LIGHT_CNTR", 0),
        # APPEND_ITEM CH0_POLL_DIRS_CHECKED            32 UINT "PollDirsChecked"
        IntField("CH0_POLL_DIRS_CHECKED", 0),
        # APPEND_ITEM CH0_PENDING_Q_CHECKED            32 UINT "PendingQChecked"
        IntField("CH0_PENDING_Q_CHECKED", 0),
        # APPEND_ITEM CH0_SEM_VALUE                    32 UINT "SemValue"
        IntField("CH0_SEM_VALUE", 0),
        # APPEND_ITEM CH1_PDU_SENT                     32 UINT "PDUsSent"
        IntField("CH1_PDU_SENT", 0),
        # APPEND_ITEM CH1_FILES_SENT                   32 UINT "Files Sent"
        IntField("CH1_FILES_SENT", 0),
        # APPEND_ITEM CH1_SUCCESS_COUNTER              32 UINT "Success Counter"
        IntField("CH1_SUCCESS_COUNTER", 0),
        # APPEND_ITEM CH1_FAILED_COUNTER               32 UINT "Failed Counter"
        IntField("CH1_FAILED_COUNTER", 0),
        # APPEND_ITEM CH1_PENDING_Q_FILECNT            32 UINT "PendingQFileCnt"
        IntField("CH1_PENDING_Q_FILECNT", 0),
        # APPEND_ITEM CH1_ACTIVE_Q_FILECNT             32 UINT "ActiveQFileCnt"
        IntField("CH1_ACTIVE_Q_FILECNT", 0),
        # APPEND_ITEM CH1_HISTORY_Q_FILECNT            32 UINT "HIstoryQFileCnt"
        IntField("CH1_HISTORY_Q_FILECNT", 0),
        # APPEND_ITEM CH1_FLAGS                        32 UINT "0=ChanDequeue enabled,1=Chan Blast In progress"
        IntField("CH1_FLAGS", 0),
        # APPEND_ITEM CH1_RED_LIGHT_CNTR               32 UINT "RedLightCntr"
        IntField("CH1_RED_LIGHT_CNTR", 0),
        # APPEND_ITEM CH1_GREEN_LIGHT_CNTR             32 UINT "GreenLightCntr"
        IntField("CH1_GREEN_LIGHT_CNTR", 0),
        # APPEND_ITEM CH1_POLL_DIRS_CHECKED            32 UINT "PollDirsChecked"
        IntField("CH1_POLL_DIRS_CHECKED", 0),
        # APPEND_ITEM CH1_PENDING_Q_CHECKED            32 UINT "PendingQChecked"
        IntField("CH1_PENDING_Q_CHECKED", 0),
        # APPEND_ITEM CH1_SEM_VALUE                    32 UINT "SemValue"
        IntField("CH1_SEM_VALUE", 0),
    ]


bind_layers(CCSDSPacket, CF_HK_TLM_PKT_TlmPkt, pkttype=0, apid=176)


class CF_TRANS_DIAG_PKT_TlmPkt(Packet):
    """Active Transaction Diagnostic Packet

    app = CF
    command = TRANS_DIAG_PKT
    msg_id = CF_TRANS_TLM_MID = 0x08b1 = 0x0800 + 0x0b1
    """
    name = "CF_TRANS_DIAG_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM TRANS_LEN       8 UINT ""
        ByteField("TRANS_LEN", 0),
        # APPEND_ITEM TRANS_Val       8 UINT ""
        ByteField("TRANS_Val", 0),
        # APPEND_ITEM NAKS            8 UINT "How many Nak PDUs have been sent/recd?"
        ByteField("NAKS", 0),
        # APPEND_ITEM PART_LEN        8 UINT ""
        ByteField("PART_LEN", 0),
        # APPEND_ITEM PART_VAL        8 UINT "Who is this transaction with?"
        ByteField("PART_VAL", 0),
        # APPEND_ITEM PHASE           8 UINT "Either 1, 2, 3, or 4"
        ByteField("PHASE", 0),
        # APPEND_ITEM SPARE_1         8 UINT ""
        ByteField("SPARE_1", 0),
        # APPEND_ITEM SPARE_2         8 UINT ""
        ByteField("SPARE_2", 0),
        # APPEND_ITEM FLAGS          32 UINT ""
        IntField("FLAGS", 0),
        # APPEND_ITEM TRANS_NUM      32 UINT ""
        IntField("TRANS_NUM", 0),
        # APPEND_ITEM ATTEMPTS       32 UINT "How many attempts to send current PDU?"
        IntField("ATTEMPTS", 0),
        # APPEND_ITEM COND_CODE      32 UINT ""
        IntField("COND_CODE", 0),
        # APPEND_ITEM DELI_CODE      32 UINT ""
        IntField("DELI_CODE", 0),
        # APPEND_ITEM FD_OFFSET      32 UINT "Offset of last Filedata sent/received"
        IntField("FD_OFFSET", 0),
        # APPEND_ITEM FD_LEN         32 UINT "Length of last Filedata sent/received"
        IntField("FD_LEN", 0),
        # APPEND_ITEM CHECKSUM       32 UINT ""
        IntField("CHECKSUM", 0),
        # APPEND_ITEM FINAL_STAT     32 UINT ""
        IntField("FINAL_STAT", 0),
        # APPEND_ITEM FILE_SIZE      32 UINT ""
        IntField("FILE_SIZE", 0),
        # APPEND_ITEM RCVD_FILE_SIZE 32 UINT ""
        IntField("RCVD_FILE_SIZE", 0),
        # APPEND_ITEM ROLE           32 UINT "(e.g. Receiver Class 1)"
        IntField("ROLE", 0),
        # APPEND_ITEM STATE          32 UINT ""
        IntField("STATE", 0),
        # APPEND_ITEM START_TIME     32 UINT "When was this transaction started?"
        IntField("START_TIME", 0),
        # APPEND_ITEM SRC_FILE      512 STRING ""
        StrFixedLenField("SRC_FILE", b"", 64),
        # APPEND_ITEM DST_FILE      512 STRING ""
        StrFixedLenField("DST_FILE", b"", 64),
        # APPEND_ITEM TMP_FILE      512 STRING ""
        StrFixedLenField("TMP_FILE", b"", 64),
        # APPEND_ITEM APP_STATUS          32 UINT ""
        IntField("APP_STATUS", 0),
        # APPEND_ITEM APP_COND_CODE       32 UINT ""
        IntField("APP_COND_CODE", 0),
        # APPEND_ITEM APP_PRIORITY        32 UINT "applies only to playback files"
        IntField("APP_PRIORITY", 0),
        # APPEND_ITEM APP_CLASS           32 UINT ""
        IntField("APP_CLASS", 0),
        # APPEND_ITEM APP_CHAN_NUM        32 UINT "applies only to playback files"
        IntField("APP_CHAN_NUM", 0),
        # APPEND_ITEM APP_SOURCE          32 UINT "from poll dir,playbackfile cmd or playback dir cmd"
        IntField("APP_SOURCE", 0),
        # APPEND_ITEM APP_NODE_TYPE       32 UINT ""
        IntField("APP_NODE_TYPE", 0),
        # APPEND_ITEM APP_TRANS_NUM       32 UINT ""
        IntField("APP_TRANS_NUM", 0),
        # APPEND_ITEM APP_SRC_ENTITY_ID  128 STRING ""
        StrFixedLenField("APP_SRC_ENTITY_ID", b"", 16),
        # APPEND_ITEM APP_SRC_FILE       512 STRING ""
        StrFixedLenField("APP_SRC_FILE", b"", 64),
        # APPEND_ITEM APP_DST_FILE       512 STRING ""
        StrFixedLenField("APP_DST_FILE", b"", 64),
    ]


bind_layers(CCSDSPacket, CF_TRANS_DIAG_PKT_TlmPkt, pkttype=0, apid=177)


class CF_CONFIG_PKT_TlmPkt(Packet):
    """Configuration Packet

    app = CF
    command = CONFIG_PKT
    msg_id = CF_CONFIG_TLM_MID = 0x08b2 = 0x0800 + 0x0b2
    """
    name = "CF_CONFIG_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM ENG_CYC_PER_WAKEUP    32 UINT ""
        IntField("ENG_CYC_PER_WAKEUP", 0),
        # APPEND_ITEM ACK_LIM               32 UINT ""
        IntField("ACK_LIM", 0),
        # APPEND_ITEM ACK_TIMEOUT           32 UINT ""
        IntField("ACK_TIMEOUT", 0),
        # APPEND_ITEM NAK_LIM               32 UINT ""
        IntField("NAK_LIM", 0),
        # APPEND_ITEM NACK_TIMEOUT          32 UINT ""
        IntField("NACK_TIMEOUT", 0),
        # APPEND_ITEM INACT_TIMEOUT         32 UINT ""
        IntField("INACT_TIMEOUT", 0),
        # APPEND_ITEM DEF_OUT_CHUNK_SIZE    32 UINT ""
        IntField("DEF_OUT_CHUNK_SIZE", 0),
        # APPEND_ITEM PIPE_DEPTH            32 UINT ""
        IntField("PIPE_DEPTH", 0),
        # APPEND_ITEM MAX_SIMULT_TRANS      32 UINT ""
        IntField("MAX_SIMULT_TRANS", 0),
        # APPEND_ITEM IN_PDU_BUF_SIZE       32 UINT ""
        IntField("IN_PDU_BUF_SIZE", 0),
        # APPEND_ITEM OUT_PDU_BUF_SIZE      32 UINT ""
        IntField("OUT_PDU_BUF_SIZE", 0),
        # APPEND_ITEM NUM_IN_CHAN           32 UINT ""
        IntField("NUM_IN_CHAN", 0),
        # APPEND_ITEM MAX_PLAYBACK_CHAN     32 UINT ""
        IntField("MAX_PLAYBACK_CHAN", 0),
        # APPEND_ITEM MAX_POLL_DIR_PER_CHAN 32 UINT ""
        IntField("MAX_POLL_DIR_PER_CHAN", 0),
        # APPEND_ITEM MM_POOL_BYTES         32 UINT ""
        IntField("MM_POOL_BYTES", 0),
        # APPEND_ITEM DEBUG_COMPILED_IN     32 UINT ""
        IntField("DEBUG_COMPILED_IN", 0),
        # APPEND_ITEM SAVE_INCOMP_FILES     64 STRING ""
        StrFixedLenField("SAVE_INCOMP_FILES", b"", 8),
        # APPEND_ITEM PIPE_NAME            160 STRING ""
        StrFixedLenField("PIPE_NAME", b"", 20),
        # APPEND_ITEM TMP_FILE_PREFIX      512 STRING ""
        StrFixedLenField("TMP_FILE_PREFIX", b"", 64),
        # APPEND_ITEM CFG_TBL_NAME         512 STRING ""
        StrFixedLenField("CFG_TBL_NAME", b"", 64),
        # APPEND_ITEM CFG_TBL_FILENAME     512 STRING ""
        StrFixedLenField("CFG_TBL_FILENAME", b"", 64),
        # APPEND_ITEM DEF_Q_INFO_FILEENAME 512 STRING ""
        StrFixedLenField("DEF_Q_INFO_FILEENAME", b"", 64),
    ]


bind_layers(CCSDSPacket, CF_CONFIG_PKT_TlmPkt, pkttype=0, apid=178)
