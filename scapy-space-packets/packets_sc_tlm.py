from scapy.all import *
from ccsds_base import CCSDSPacket


class SC_HK_TLM_PKT_TlmPkt(Packet):
    """Housekeeping Packet Structure

    app = SC
    command = HK_TLM_PKT
    msg_id = SC_HK_TLM_MID = 0x08aa = 0x0800 + 0x0aa
    """
    name = "SC_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM ATS_NUMBER          8 UINT "Current ATS number 1 = ATS A, 2 = ATS B"
        ByteField("ATS_NUMBER", 0),
        # APPEND_ITEM ATP_STATE           8 UINT "Current ATP state valid values are: 2 = IDLE, 5 = EXECUTING"
        ByteField("ATP_STATE", 0),
        # APPEND_ITEM CONT_ATS_ON_FAIL    8 UINT "In the event of ATS execution failure (ats command fails checksum) , the ATS execution will continue if this flag is set to TRUE and will stop if this flag is set to FALSE"
        ByteField("CONT_ATS_ON_FAIL", 0),
        # APPEND_ITEM CMD_ERROR_COUNT     8 UINT "Counts Request Errors"
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM CMD_VALID_COUNT     8 UINT "Counts Ground Requests"
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM PADDING8            8 UINT ""
        ByteField("PADDING8", 0),
        # APPEND_ITEM SWITCH_PEND_FLAG   16 UINT "Is an ats switch pending? 0 = NO, 1 = YES This means that the ATS switch is waiting until a safe time"
        ShortField("SWITCH_PEND_FLAG", 0),
        # APPEND_ITEM NUM_RTS_ACTIVE     16 UINT "Number of RTSs currently active"
        ShortField("NUM_RTS_ACTIVE", 0),
        # APPEND_ITEM RTS_NUMBER         16 UINT "Next RTS number"
        ShortField("RTS_NUMBER", 0),
        # APPEND_ITEM RTS_ACTIVE_CTR     16 UINT "Increments when an RTS is started without error"
        ShortField("RTS_ACTIVE_CTR", 0),
        # APPEND_ITEM RTS_ACTIVE_ERR_CTR 16 UINT "Increments when an attempt to start an RTS fails"
        ShortField("RTS_ACTIVE_ERR_CTR", 0),
        # APPEND_ITEM ATS_CMD_CTR        16 UINT "Total ATS cmd cnter counts commands sent by the ATS"
        ShortField("ATS_CMD_CTR", 0),
        # APPEND_ITEM ATS_CMD_ERR_CTR    16 UINT "Total ATS cmd Error ctr command errors in the ATS"
        ShortField("ATS_CMD_ERR_CTR", 0),
        # APPEND_ITEM RTS_CMD_CTR        16 UINT "Counts TOTAL rts cmds that were sent out from ALL active RTSs"
        ShortField("RTS_CMD_CTR", 0),
        # APPEND_ITEM RTS_CMD_ERR_CTR    16 UINT "Counts TOTAL number of errs from ALL RTSs that are active"
        ShortField("RTS_CMD_ERR_CTR", 0),
        # APPEND_ITEM LAST_ATS_ERR_SEQ   16 UINT "Last ATS Errant Sequence Num Values: 1 or 2"
        ShortField("LAST_ATS_ERR_SEQ", 0),
        # APPEND_ITEM LAST_ATS_ERR_CMD   16 UINT "Last ATS Errant Command Num"
        ShortField("LAST_ATS_ERR_CMD", 0),
        # APPEND_ITEM LAST_RTS_ERR_SEQ   16 UINT "Last RTS Errant Sequence Num"
        ShortField("LAST_RTS_ERR_SEQ", 0),
        # APPEND_ITEM LAST_RTS_ERR_CMD   16 UINT "The OFFSET in the RTS buffer of the command that had an error It will be a WORD value i.e. 1st command had an error, this value would be 0, if the 2nd command started at int8 10 in the buffer, this value would be 5"
        ShortField("LAST_RTS_ERR_CMD", 0),
        # APPEND_ITEM APPEND_CMD_ARG     16 UINT "ATS selection argument from most recent Append ATS command"
        ShortField("APPEND_CMD_ARG", 0),
        # APPEND_ITEM APPEND_ENTRY_COUNT 16 UINT "Number of cmd entries in current Append ATS table"
        ShortField("APPEND_ENTRY_COUNT", 0),
        # APPEND_ITEM APPEND_BYTE_COUNT  16 UINT "Size of cmd entries in current Append ATS table"
        ShortField("APPEND_BYTE_COUNT", 0),
        # APPEND_ITEM APPEND_LOAD_COUNT  16 UINT "Total number of Append ATS table loads"
        ShortField("APPEND_LOAD_COUNT", 0),
        # APPEND_ITEM ATP_CMD_NUMBER     32 UINT "current command number"
        IntField("ATP_CMD_NUMBER", 0),
        # APPEND_ITEM ATP_1_FREE_BYTES   32 UINT "Free Bytes in ATS 1"
        IntField("ATP_1_FREE_BYTES", 0),
        # APPEND_ITEM ATP_2_FREE_BYTES   32 UINT "Free Bytes in ATS 2"
        IntField("ATP_2_FREE_BYTES", 0),
        # APPEND_ITEM NEXT_RTS_TIME      32 UINT "Next RTS cmd Absolute Time"
        IntField("NEXT_RTS_TIME", 0),
        # APPEND_ITEM NEXT_ATS_TIME      32 UINT "Next ATS Command Time (seconds)"
        IntField("NEXT_ATS_TIME", 0),
        # APPEND_ITEM RTS_W1_EXE_STATUS  16 UINT "RTS executing status bit map where each uint16 represents 16 RTS numbers. Note: array index numbers and bit numbers use base zero indexing, but RTS numbers use base one indexing. Thus, the LSB (bit zero) of uint16 array index zero represents RTS number 1, and bit one of uint16 array index zero represents RTS number 2, etc. If an RTS is IDLE, then the corresponding bit is zero. If an RTS is EXECUTING, then the corresponding bit is one"
        ShortField("RTS_W1_EXE_STATUS", 0),
        # ITEM RTS_8_EXE 576 1 UINT
        # ITEM RTS_7_EXE 577 1 UINT
        # ITEM RTS_6_EXE 578 1 UINT
        # STATE IDLE 0
        # STATE EXEC 1
        # ITEM RTS_5_EXE 579 1 UINT
        # ITEM RTS_4_EXE 580 1 UINT
        # ITEM RTS_3_EXE 581 1 UINT
        # ITEM RTS_2_EXE 582 1 UINT
        # ITEM RTS_1_EXE 583 1 UINT
        # APPEND_ITEM RTS_W2_EXE_STATUS  16 UINT "RTS executing status bit map where each uint16 represents 16 RTS numbers. Note: array index numbers and bit numbers use base zero indexing, but RTS numbers use base one indexing. Thus, the LSB (bit zero) of uint16 array index zero represents RTS number 1, and bit one of uint16 array index zero represents RTS number 2, etc. If an RTS is IDLE, then the corresponding bit is zero. If an RTS is EXECUTING, then the corresponding bit is one"
        ShortField("RTS_W2_EXE_STATUS", 0),
        # APPEND_ITEM RTS_W3_EXE_STATUS  16 UINT "RTS executing status bit map where each uint16 represents 16 RTS numbers. Note: array index numbers and bit numbers use base zero indexing, but RTS numbers use base one indexing. Thus, the LSB (bit zero) of uint16 array index zero represents RTS number 1, and bit one of uint16 array index zero represents RTS number 2, etc. If an RTS is IDLE, then the corresponding bit is zero. If an RTS is EXECUTING, then the corresponding bit is one"
        ShortField("RTS_W3_EXE_STATUS", 0),
        # APPEND_ITEM RTS_W4_EXE_STATUS  16 UINT "RTS executing status bit map where each uint16 represents 16 RTS numbers. Note: array index numbers and bit numbers use base zero indexing, but RTS numbers use base one indexing. Thus, the LSB (bit zero) of uint16 array index zero represents RTS number 1, and bit one of uint16 array index zero represents RTS number 2, etc. If an RTS is IDLE, then the corresponding bit is zero. If an RTS is EXECUTING, then the corresponding bit is one"
        ShortField("RTS_W4_EXE_STATUS", 0),
        # APPEND_ITEM RTS_W1_DIS_STATUS  16 UINT "RTS disabled status bit map where each uint16 represents 16 RTS numbers. Note: array index numbers and bit numbers use base zero indexing, but RTS numbers use base one indexing. Thus, the LSB (bit zero) of uint16 array index zero represents RTS number 1, and bit one of uint16 array index zero represents RTS number 2, etc. If an RTS is ENABLED, then the corresponding bit is zero. If an RTS is DISABLED, then the corresponding bit is one"
        ShortField("RTS_W1_DIS_STATUS", 0),
        # ITEM RTS_8_DIS 640 1 UINT
        # ITEM RTS_7_DIS 641 1 UINT
        # ITEM RTS_6_DIS 642 1 UINT
        # STATE FALSE 0
        # STATE TRUE  1
        # ITEM RTS_5_DIS 643 1 UINT
        # ITEM RTS_4_DIS 644 1 UINT
        # ITEM RTS_3_DIS 645 1 UINT
        # ITEM RTS_2_DIS 646 1 UINT
        # ITEM RTS_1_DIS 647 1 UINT
        # APPEND_ITEM RTS_W2_DIS_STATUS  16 UINT "RTS disabled status bit map where each uint16 represents 16 RTS numbers. Note: array index numbers and bit numbers use base zero indexing, but RTS numbers use base one indexing. Thus, the LSB (bit zero) of uint16 array index zero represents RTS number 1, and bit one of uint16 array index zero represents RTS number 2, etc. If an RTS is ENABLED, then the corresponding bit is zero. If an RTS is DISABLED, then the corresponding bit is one"
        ShortField("RTS_W2_DIS_STATUS", 0),
        # APPEND_ITEM RTS_W3_DIS_STATUS  16 UINT "RTS disabled status bit map where each uint16 represents 16 RTS numbers. Note: array index numbers and bit numbers use base zero indexing, but RTS numbers use base one indexing. Thus, the LSB (bit zero) of uint16 array index zero represents RTS number 1, and bit one of uint16 array index zero represents RTS number 2, etc. If an RTS is ENABLED, then the corresponding bit is zero. If an RTS is DISABLED, then the corresponding bit is one"
        ShortField("RTS_W3_DIS_STATUS", 0),
        # APPEND_ITEM RTS_W4_DIS_STATUS  16 UINT "RTS disabled status bit map where each uint16 represents 16 RTS numbers. Note: array index numbers and bit numbers use base zero indexing, but RTS numbers use base one indexing. Thus, the LSB (bit zero) of uint16 array index zero represents RTS number 1, and bit one of uint16 array index zero represents RTS number 2, etc. If an RTS is ENABLED, then the corresponding bit is zero. If an RTS is DISABLED, then the corresponding bit is one"
        ShortField("RTS_W4_DIS_STATUS", 0),
    ]


bind_layers(CCSDSPacket, SC_HK_TLM_PKT_TlmPkt, pkttype=0, apid=170)
