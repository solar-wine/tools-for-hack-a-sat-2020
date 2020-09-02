from scapy.all import *
from ccsds_base import CCSDSPacket


class CFE_TIME_HK_TLM_PKT_TlmPkt(Packet):
    """Housekeeping data (general status) autonomously sent

    app = CFE_TIME
    command = HK_TLM_PKT
    msg_id = CFE_TIME_HK_TLM_MID = 0x0805 = 0x0800 + 0x005
    """
    name = "CFE_TIME_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT    8 UINT "Time Command Execution Counter."
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT    8 UINT "Time Command Error Counter."
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM CLOCK_STATE_FLAGS 16 UINT "State Flags. See cfe_time_msg.h. Will need to bit bust."
        ShortField("CLOCK_STATE_FLAGS", 0),
        # FORMAT_STRING  "0x%04X"
        # APPEND_ITEM CLOCK_STATE_API   16  INT "API State"
        SignedShortField("CLOCK_STATE_API", 0),
        # STATE Invalid -1
        # STATE Valid    0
        # STATE FlyWheel 1
        # APPEND_ITEM LEAP_SECONDS      16  INT "Leaps Seconds."
        SignedShortField("LEAP_SECONDS", 0),
        # APPEND_ITEM MET_SECONDS       32 UINT "MET (seconds)."
        IntField("MET_SECONDS", 0),
        # APPEND_ITEM MET_SUBSECS       32 UINT "MET (sub-seconds)."
        IntField("MET_SUBSECS", 0),
        # APPEND_ITEM STCF_SECONDS      32 UINT "STCF (seconds)."
        IntField("STCF_SECONDS", 0),
        # APPEND_ITEM STCF_SUBSECS      32 UINT "STCF (sub-seconds)."
        IntField("STCF_SUBSECS", 0),
        # APPEND_ITEM 1HZADJ_SECONDS    32 UINT "1 Hz SCTF adjustment (seconds)."
        IntField("1HZADJ_SECONDS", 0),
        # APPEND_ITEM 1HZADJ_SUBSECS    32 UINT "1 Hz SCTF adjustment (sub-seconds)."
        IntField("1HZADJ_SUBSECS", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_HK_TLM_PKT_TlmPkt, pkttype=0, apid=5)


class CFE_TIME_DIAG_TLM_PKT_TlmPkt(Packet):
    """Time Services Diagnostics Packet sent in response to a SEND_DIAG command

    app = CFE_TIME
    command = DIAG_TLM_PKT
    msg_id = CFE_TIME_DIAG_TLM_MID = 0x0806 = 0x0800 + 0x006
    """
    name = "CFE_TIME_DIAG_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM MET_AT_TONE_SECONDS        32 UINT "Number of seconds since epoch. (Parent: MET at time of tone.)"
        IntField("MET_AT_TONE_SECONDS", 0),
        # APPEND_ITEM MET_AT_TONE_SUBSECONDS     32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: MET at time of tone.)"
        IntField("MET_AT_TONE_SUBSECONDS", 0),
        # APPEND_ITEM STCF_AT_TONE_SECONDS       32 UINT "Number of seconds since epoch. (Parent: STCF at time of tone.)"
        IntField("STCF_AT_TONE_SECONDS", 0),
        # APPEND_ITEM STCF_AT_TONE_SUBSECONDS    32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: STCF at time of tone.)"
        IntField("STCF_AT_TONE_SUBSECONDS", 0),
        # APPEND_ITEM DELAY_AT_TONE_SECONDS      32 UINT "Number of seconds since epoch. (Parent: Adjustment for slow tone detection.)"
        IntField("DELAY_AT_TONE_SECONDS", 0),
        # APPEND_ITEM DELAY_AT_TONE_SUBSECONDS   32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: Adjustment for slow tone detection.)"
        IntField("DELAY_AT_TONE_SUBSECONDS", 0),
        # APPEND_ITEM LATCH_AT_TONE_SECONDS      32 UINT "Number of seconds since epoch. (Parent: Local clock latched at time of tone.)"
        IntField("LATCH_AT_TONE_SECONDS", 0),
        # APPEND_ITEM LATCH_AT_TONE_SUBSECONDS   32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: Local clock latched at time of tone.)"
        IntField("LATCH_AT_TONE_SUBSECONDS", 0),
        # APPEND_ITEM LEAP_SEC_AT_TONE           16 INT "Leap Seconds at time of tone."
        SignedShortField("LEAP_SEC_AT_TONE", 0),
        # APPEND_ITEM CLOCK_STATE_API            16 INT "Clock state as per API."
        SignedShortField("CLOCK_STATE_API", 0),
        # STATE Invalid -1
        # STATE Valid    0
        # STATE FlyWheel 1
        # APPEND_ITEM TIME_SINCE_TONE_SECONDS    32 UINT "Number of seconds since epoch. (Parent: Time elapsed since the tone.)"
        IntField("TIME_SINCE_TONE_SECONDS", 0),
        # APPEND_ITEM TIME_SINCE_TONE_SUBSECONDS 32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: Time elapsed since the tone.)"
        IntField("TIME_SINCE_TONE_SUBSECONDS", 0),
        # APPEND_ITEM LATCH_CURRENT_SECONDS      32 UINT "Number of seconds since epoch. (Parent: Local clock latched just 'now'.)"
        IntField("LATCH_CURRENT_SECONDS", 0),
        # APPEND_ITEM LATCH_CURRENT_SUBSECONDS   32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: Local clock latched just 'now'.)"
        IntField("LATCH_CURRENT_SUBSECONDS", 0),
        # APPEND_ITEM MET_CURRENT_SECONDS        32 UINT "Number of seconds since epoch. (Parent: MET at this instant.)"
        IntField("MET_CURRENT_SECONDS", 0),
        # APPEND_ITEM MET_CURRENT_SUBSECONDS     32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: MET at this instant.)"
        IntField("MET_CURRENT_SUBSECONDS", 0),
        # APPEND_ITEM TAI_CURRENT_SECONDS        32 UINT "Number of seconds since epoch. (Parent: TAI at this instant.)"
        IntField("TAI_CURRENT_SECONDS", 0),
        # APPEND_ITEM TAI_CURRENT_SUBSECONDS     32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: TAI at this instant.)"
        IntField("TAI_CURRENT_SUBSECONDS", 0),
        # APPEND_ITEM UTC_CURRENT_SECONDS        32 UINT "Number of seconds since epoch. (Parent: UTC at this instant.)"
        IntField("UTC_CURRENT_SECONDS", 0),
        # APPEND_ITEM UTC_CURRENT_SUBSECONDS     32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: UTC at this instant.)"
        IntField("UTC_CURRENT_SUBSECONDS", 0),
        # APPEND_ITEM CLOCK_SET_STATE            16 INT "Time has been 'set'."
        SignedShortField("CLOCK_SET_STATE", 0),
        # STATE Not_Set 0
        # STATE Was_Set 1
        # APPEND_ITEM CLOCK_FLY_STATE            16 INT "Current fly-wheel state."
        SignedShortField("CLOCK_FLY_STATE", 0),
        # STATE No_Fly 0
        # STATE Is_Fly 1
        # APPEND_ITEM CLOCK_SOURCE               16 INT "Internal vs external, etc."
        SignedShortField("CLOCK_SOURCE", 0),
        # STATE Internal 1
        # STATE External 2
        # APPEND_ITEM CLOCK_SIGNAL               16 INT "Primary vs redundant, etc."
        SignedShortField("CLOCK_SIGNAL", 0),
        # APPEND_ITEM SERVER_FLY_STATE           16 INT "Used by clients only."
        SignedShortField("SERVER_FLY_STATE", 0),
        # APPEND_ITEM FORCED_TO_FLY              16 INT "Commanded into fly-wheel."
        SignedShortField("FORCED_TO_FLY", 0),
        # APPEND_ITEM CLOCK_STATE_FLAGS          16 UINT "Clock State Flags."
        ShortField("CLOCK_STATE_FLAGS", 0),
        # APPEND_ITEM ONE_TIME_DIRECTION         16 INT "One time STCF adjustment direction (Add = 1, Sub = 2)."
        SignedShortField("ONE_TIME_DIRECTION", 0),
        # APPEND_ITEM ONE_HZ_DIRECTION           16 INT "1Hz STCF adjustment direction"
        SignedShortField("ONE_HZ_DIRECTION", 0),
        # APPEND_ITEM DELAY_DIRECTION            16 INT "Client latency adjustment direction."
        SignedShortField("DELAY_DIRECTION", 0),
        # APPEND_ITEM ONE_TIME_ADJUST_SECONDS    32 UINT "Number of seconds since epoch. (Parent: Previous one-time STCF adjustment.)"
        IntField("ONE_TIME_ADJUST_SECONDS", 0),
        # APPEND_ITEM ONE_TIME_ADJUST_SUBSECONDS 32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: Previous one-time STCF adjustment.)"
        IntField("ONE_TIME_ADJUST_SUBSECONDS", 0),
        # APPEND_ITEM ONE_HZ_ADJUST_SECONDS        32 UINT "Number of seconds since epoch. (Parent: Current 1Hz STCF adjustment.)"
        IntField("ONE_HZ_ADJUST_SECONDS", 0),
        # APPEND_ITEM ONE_HZ_ADJUST_SUBSECONDS     32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: Current 1Hz STCF adjustment.)"
        IntField("ONE_HZ_ADJUST_SUBSECONDS", 0),
        # APPEND_ITEM LATCH_TONE_SIGNAL_SECONDS    32 UINT "Number of seconds since epoch. (Parent: Local Clock latched at most recent tone signal.)"
        IntField("LATCH_TONE_SIGNAL_SECONDS", 0),
        # APPEND_ITEM LATCH_TONE_SIGNAL_SUBSECONDS 32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: Local Clock latched at most recent tone signal.)"
        IntField("LATCH_TONE_SIGNAL_SUBSECONDS", 0),
        # APPEND_ITEM LATCH_TONE_DATA_SECONDS      32 UINT "Number of seconds since epoch. (Parent: Local Clock latched at arrival of tone data.)"
        IntField("LATCH_TONE_DATA_SECONDS", 0),
        # APPEND_ITEM LATCH_TONE_DATA_SUBSECONDS   32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: Local Clock latched at arrival of tone data.)"
        IntField("LATCH_TONE_DATA_SUBSECONDS", 0),
        # APPEND_ITEM TONE_MATCH_COUNT           32 UINT "Tone signal / data verification count."
        IntField("TONE_MATCH_COUNT", 0),
        # APPEND_ITEM TONE_MATCH_ERRORS          32 UINT "Tone signal / data verification error count."
        IntField("TONE_MATCH_ERRORS", 0),
        # APPEND_ITEM TONE_SIGNAL_COUNT          32 UINT "Tone signal detected SB message count."
        IntField("TONE_SIGNAL_COUNT", 0),
        # APPEND_ITEM TONE_DATA_COUNT            32 UINT "Time at the tone data SB message count."
        IntField("TONE_DATA_COUNT", 0),
        # APPEND_ITEM TONE_INT_COUNT             32 UINT "Tone signal ISR execution count."
        IntField("TONE_INT_COUNT", 0),
        # APPEND_ITEM TONE_INT_ERRORS            32 UINT "Tone signal ISR error count."
        IntField("TONE_INT_ERRORS", 0),
        # APPEND_ITEM TONE_TASK_COUNT            32 UINT "Tone task execution count."
        IntField("TONE_TASK_COUNT", 0),
        # APPEND_ITEM VERSION_COUNT              32 UINT "Count of mods to time at tone reference data (version)."
        IntField("VERSION_COUNT", 0),
        # APPEND_ITEM LOCAL_INT_COUNT            32 UINT "Local 1Hz ISR execution count."
        IntField("LOCAL_INT_COUNT", 0),
        # APPEND_ITEM LOCAL_TASK_COUNT           32 UINT "Local 1Hz task execution count."
        IntField("LOCAL_TASK_COUNT", 0),
        # APPEND_ITEM VIRTUAL_MET                32 UINT "Software MET."
        IntField("VIRTUAL_MET", 0),
        # APPEND_ITEM MIN_ELAPSED                32 UINT "Min tone signal / data pkt arrival window (Sub-seconds)."
        IntField("MIN_ELAPSED", 0),
        # APPEND_ITEM MAX_ELAPSED                32 UINT "Max tone signal / data pkt arrival window (Sub-seconds)."
        IntField("MAX_ELAPSED", 0),
        # APPEND_ITEM MAX_LOCAL_CLOCK_SECONDS    32 UINT "Number of seconds since epoch. (Parent: Max local clock value before rollover.)"
        IntField("MAX_LOCAL_CLOCK_SECONDS", 0),
        # APPEND_ITEM MAX_LOCAL_CLOCK_SUBSECONDS 32 UINT "Number of subseconds since epoch (LSB = 2^(-32) seconds). (Parent: Max local clock value before rollover.)"
        IntField("MAX_LOCAL_CLOCK_SUBSECONDS", 0),
        # APPEND_ITEM TONE_OVER_LIMIT            32 UINT "Max between tone signal interrupts."
        IntField("TONE_OVER_LIMIT", 0),
        # APPEND_ITEM TONE_UNDER_LIMIT           32 UINT "Min between tone signal interrupts."
        IntField("TONE_UNDER_LIMIT", 0),
        # APPEND_ITEM DATA_STORE_STATUS          32 UINT "Data Store status (preserved across processor reset)."
        IntField("DATA_STORE_STATUS", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_DIAG_TLM_PKT_TlmPkt, pkttype=0, apid=6)
