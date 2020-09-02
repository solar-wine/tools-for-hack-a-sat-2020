from scapy.all import *
from ccsds_base import CCSDSPacket


class CFE_TIME_NOOP_CmdPkt(Packet):
    """Generate an information event message with app version

    app = CFE_TIME
    command = NOOP
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "CFE_TIME_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_TIME_NOOP_CmdPkt, pkttype=1, apid=5, cmd_func_code=0)


class CFE_TIME_RESET_CTRS_CmdPkt(Packet):
    """Reset the following counters: Valid/Invalid command counters, Tone Signal Detected SB Msg Counter, Time at the Tone Data SB Msg Counter Tone Signal/Data Verify Counter Tone Signal/Data Error Counter ($sc_$cpu_TIME_DVerifyER)Tone Signal Interrupt Counter ($sc_$cpu_TIME_DTsISRCNT)Tone Signal Interrupt Error Counter ($sc_$cpu_TIME_DTsISRERR)Tone Signal Task Counter ($sc_$cpu_TIME_DTsTaskCNT)Local 1 Hz Interrupt Counter ($sc_$cpu_TIME_D1HzISRCNT)Local 1 Hz Task Counter ($sc_$cpu_TIME_D1HzTaskCNT)Reference Time Version Counter ($sc_$cpu_TIME_DVersionCNT)

    app = CFE_TIME
    command = RESET_CTRS
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "CFE_TIME_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_TIME_RESET_CTRS_CmdPkt, pkttype=1, apid=5, cmd_func_code=1)


class CFE_TIME_SEND_DIAG_CmdPkt(Packet):
    """ Send a single copy of the diagnostic . Refer to CFE_TIME_DiagPacket_t for a description of the Time Service diagnostic message contents.

    app = CFE_TIME
    command = SEND_DIAG
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 2
    data_len = 0 bytes
    """
    name = "CFE_TIME_SEND_DIAG_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_TIME_SEND_DIAG_CmdPkt, pkttype=1, apid=5, cmd_func_code=2)


class CFE_TIME_SET_SOURCE_CmdPkt(Packet):
    """This command selects the Time Service clock source. Although the list of potential clock sources is mission specific and defined via configuration parameters, this command provides a common method for switching between the local processor clock and an external source for time data. When commanded to accept external time data (GPS, MET, spacecraft time, etc.), the Time Server will enable input via an API function specific to the configuration definitions for the particular source. When commanded to use internal time data, the Time Server will ignore the external data. However, the Time Server will continue to use the API function as the trigger to generate a 'time at the tone' command packet regardless of the internal/external command selection. \n\nNotes: \n\tOperating in FLYWHEEL mode is not considered a choice related to clock source, but rather an element of the clock state. See below for a description of the CFE_TIME_SET_STATE_CC command.This command is only valid when the CFE_TIME_CFG_SOURCE configuration parameter in the cfe_platform_cfg.h file has been set to TRUE.

    app = CFE_TIME
    command = SET_SOURCE
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 3
    data_len = 2 bytes
    """
    name = "CFE_TIME_SET_SOURCE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TIME_SOURCE 16 INT MIN_INT16 MAX_INT16 0 "CFE_TIME_USE_INTERN=Internal Source, CFE_TIME_USE_EXTERN=External Source"
        SignedShortField("TIME_SOURCE", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_SET_SOURCE_CmdPkt, pkttype=1, apid=5, cmd_func_code=3)


class CFE_TIME_SET_STATE_CmdPkt(Packet):
    """This command indirectly affects the Time Service on-board determination of clock state. Clock state is a combination of factors, most significantly whether the spacecraft time has been accurately set, and whether Time Service is operating in FLYWHEEL mode.\nThis command may be used to notify the Time Server that spacecraft time is now correct, or that time is no longer correct. This information will be distributed to Time Clients, and in turn, to any interested sub-systems.\nAlso, this command may be used to force a Time Server or Time Client into FLYWHEEL mode. Use of FLYWHEEL mode is mainly for debug purposes although in extreme circumstances, it may be of value to force Time Service not to rely on normal time updates. Note that when commanded into FLYWHEEL mode, the Time Service will remain so until receipt of another 'set state' command setting the state into a mode other than FLYWHEEL. \nNote also that setting the clock state to VALID or INVALID on a Time Client that is currently getting time updates from the Time Server will have very limited effect. As soon as the Time Client receives the next time update, the VALID/INVALID selection will be set to that of the Time Server. However, setting a Time Client to FLYWHEEL cannot be overridden by the Time Server since the Time Client will ignore time updates from the Time Server while in FLYWHEEL mode.

    app = CFE_TIME
    command = SET_STATE
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 4
    data_len = 2 bytes
    """
    name = "CFE_TIME_SET_STATE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CLOCK_STATE 16 INT MIN_INT16 MAX_INT16 0 "CFE_TIME_INVALID=Spacecraft time has not been accurately set, CFE_TIME_VALID=Spacecraft clock has been accurately set, CFE_TIME_FLYWHEEL=Force into FLYWHEEL mode"
        SignedShortField("CLOCK_STATE", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_SET_STATE_CmdPkt, pkttype=1, apid=5, cmd_func_code=4)


class CFE_TIME_ADD_CLOCK_LAT_CmdPkt(Packet):
    """This command is used to factor out a known, predictable latency between the Time Server and a particular Time Client. The correction is applied (added) to the current time calculation for Time Clients, so this command has no meaning for Time Servers. Each Time Client can have a unique latency setting. The latency value is a positive number of seconds and microseconds that represent the deviation from the time maintained by the Time Server.

    app = CFE_TIME
    command = ADD_CLOCK_LAT
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 5
    data_len = 8 bytes
    """
    name = "CFE_TIME_ADD_CLOCK_LAT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SECONDS      32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("SECONDS", 0),
        # APPEND_PARAMETER MICROSECONDS 32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("MICROSECONDS", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_ADD_CLOCK_LAT_CmdPkt, pkttype=1, apid=5, cmd_func_code=5)


class CFE_TIME_SUB_CLOCK_LAT_CmdPkt(Packet):
    """This command is used to factor out a known, predictable latency between the Time Server and a particular Time Client. The correction is applied (subtracted) to the current time calculation for Time Clients, so this command has no meaning for Time Servers. Each Time Client can have a unique latency setting. The latency value is a positive number of seconds and microseconds that represent the deviation from the time maintained by the Time Server. \nNote that it is unimaginable that the seconds value will ever be anything but zero.

    app = CFE_TIME
    command = SUB_CLOCK_LAT
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 6
    data_len = 8 bytes
    """
    name = "CFE_TIME_SUB_CLOCK_LAT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SECONDS      32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("SECONDS", 0),
        # APPEND_PARAMETER MICROSECONDS 32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("MICROSECONDS", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_SUB_CLOCK_LAT_CmdPkt, pkttype=1, apid=5, cmd_func_code=6)


class CFE_TIME_SET_CLOCK_CmdPkt(Packet):
    """This command sets the spacecraft clock to a new value, regardless of the current setting (time jam). The new time value represents the desired offset from the mission-defined time epoch and takes effect immediately upon execution of this command. Time Service will calculate a new STCF value based on the current MET and the desired new time using one of the following: \n\nIf Time Service is configured to compute current time as TAI\n\nSTCF = (new time) - (current MET)  (current time) = (current MET) + STCF \n\nIf Time Service is configured to compute current time as UTC STCF = ((new time) - (current MET)) + (Leap Seconds)  (current time) = ((curent MET) + STCF) - (Leap Seconds)

    app = CFE_TIME
    command = SET_CLOCK
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 7
    data_len = 8 bytes
    """
    name = "CFE_TIME_SET_CLOCK_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SECONDS      32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("SECONDS", 0),
        # APPEND_PARAMETER MICROSECONDS 32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("MICROSECONDS", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_SET_CLOCK_CmdPkt, pkttype=1, apid=5, cmd_func_code=7)


class CFE_TIME_SET_CLOCK_MET_CmdPkt(Packet):
    """This command sets the Mission Elapsed Timer (MET) to the specified value. Note that the MET (as implemented for cFE Time Service) is a logical representation and not a physical timer. Thus, setting the MET is not dependent on whether the hardware supports a MET register that can be written to. Note also that Time Service 'assumes' that during normal operation, the MET is synchronized to the tone signal. Therefore, unless operating in FLYWHEEL mode, the sub-seconds portion of the MET will be set to zero at the next tone signal interrupt. The new MET takes effect immediately upon execution of this command.

    app = CFE_TIME
    command = SET_CLOCK_MET
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 8
    data_len = 8 bytes
    """
    name = "CFE_TIME_SET_CLOCK_MET_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SECONDS      32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("SECONDS", 0),
        # APPEND_PARAMETER MICROSECONDS 32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("MICROSECONDS", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_SET_CLOCK_MET_CmdPkt, pkttype=1, apid=5, cmd_func_code=8)


class CFE_TIME_SET_CLOCK_STCF_CmdPkt(Packet):
    """This command sets the Spacecraft Time Correlation Factor (STCF) to the specified value. This command differs from the previously described SET CLOCK in the nature of the command argument. This command sets the STCF value directly, rather than extracting the STCF from a value representing the total of MET, STCF and optionally, Leap Seconds. The new STCF takes effect immediately upon execution of this command.

    app = CFE_TIME
    command = SET_CLOCK_STCF
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 9
    data_len = 8 bytes
    """
    name = "CFE_TIME_SET_CLOCK_STCF_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SECONDS      32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("SECONDS", 0),
        # APPEND_PARAMETER MICROSECONDS 32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("MICROSECONDS", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_SET_CLOCK_STCF_CmdPkt, pkttype=1, apid=5, cmd_func_code=9)


class CFE_TIME_SET_CLOCK_LEAP_CmdPkt(Packet):
    """This command sets the spacecraft Leap Seconds to the specified value. Leap Seconds may be positive or negative, and there is no limit to the value except, of course, the limit imposed by the 16 bit signed integer data type. The new Leap Seconds value takes effect immediately upon execution of this command.

    app = CFE_TIME
    command = SET_CLOCK_LEAP
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 10
    data_len = 8 bytes
    """
    name = "CFE_TIME_SET_CLOCK_LEAP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SECONDS      32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("SECONDS", 0),
        # APPEND_PARAMETER MICROSECONDS 32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("MICROSECONDS", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_SET_CLOCK_LEAP_CmdPkt, pkttype=1, apid=5, cmd_func_code=10)


class CFE_TIME_ADD_STCF_ADJ_CmdPkt(Packet):
    """This command adjusts the Spacecraft Time Correlation Factor (STCF) by adding the specified value. The new STCF takes effect immediately upon execution of this command.

    app = CFE_TIME
    command = ADD_STCF_ADJ
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 11
    data_len = 8 bytes
    """
    name = "CFE_TIME_ADD_STCF_ADJ_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SECONDS      32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("SECONDS", 0),
        # APPEND_PARAMETER MICROSECONDS 32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("MICROSECONDS", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_ADD_STCF_ADJ_CmdPkt, pkttype=1, apid=5, cmd_func_code=11)


class CFE_TIME_SUB_STCF_ADJ_CmdPkt(Packet):
    """This command adjusts the Spacecraft Time Correlation Factor (STCF) by subtracting the specified value. The new STCF takes effect immediately upon execution of this command.

    app = CFE_TIME
    command = SUB_STCF_ADJ
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 12
    data_len = 8 bytes
    """
    name = "CFE_TIME_SUB_STCF_ADJ_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SECONDS      32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("SECONDS", 0),
        # APPEND_PARAMETER MICROSECONDS 32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("MICROSECONDS", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_SUB_STCF_ADJ_CmdPkt, pkttype=1, apid=5, cmd_func_code=12)


class CFE_TIME_ADD_1HZ_STCF_ADJ_CmdPkt(Packet):
    """This command has been updated to take actual sub-seconds (1/2^32 seconds) rather than micro-seconds as an input argument. This change occurred after the determination was made that one micro-second is too large an increment for a constant 1Hz adjustment. This command continuously adjusts the Spacecraft Time Correlation Factor (STCF) every second, by adding the specified value. The adjustment to the STCF is applied in the Time Service local 1Hz interrupt handler. As the local 1Hz interrupt is not synchronized to the tone signal, one cannot say when the adjustment will occur, other than once a second, at about the same time relative to the tone. There was some debate about whether the maximum 1Hz clock drift correction factor would ever need to exceed some small fraction of a second. But, the decision was made to provide the capability to make 1Hz adjustments greater than one second and leave it to the ground system to provide mission specific limits.

    app = CFE_TIME
    command = ADD_1HZ_STCF_ADJ
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 13
    data_len = 8 bytes
    """
    name = "CFE_TIME_ADD_1HZ_STCF_ADJ_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SECONDS    32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("SECONDS", 0),
        # APPEND_PARAMETER SUBSECONDS 32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("SUBSECONDS", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_ADD_1HZ_STCF_ADJ_CmdPkt, pkttype=1, apid=5, cmd_func_code=13)


class CFE_TIME_SUB_1HZ_STCF_ADJ_CmdPkt(Packet):
    """This command has been updated to take actual sub-seconds (1/2^32 seconds) rather than micro-seconds as an input argument. This change occurred after the determination was made that one micro-second is too large an increment for a constant 1Hz adjustment. This command continuously adjusts the Spacecraft Time Correlation Factor (STCF) every second, by subtracting the specified value. The adjustment to the STCF is applied in the Time Service local 1Hz interrupt handler. As the local 1Hz interrupt is not synchronized to the tone signal, one cannot say when the adjustment will occur, other than once a second, at about the same time relative to the tone. There was some debate about whether the maximum 1Hz clock drift correction factor would to ever need exceed some small fraction of a second. But, the decision was made to provide the capability to make 1Hz adjustments greater than one second and leave it to the ground system to provide mission specific limits.

    app = CFE_TIME
    command = SUB_1HZ_STCF_ADJ
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 14
    data_len = 8 bytes
    """
    name = "CFE_TIME_SUB_1HZ_STCF_ADJ_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SECONDS    32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("SECONDS", 0),
        # APPEND_PARAMETER SUBSECONDS 32 UINT MIN_UINT32 MAX_UINT32 0 " "
        IntField("SUBSECONDS", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_SUB_1HZ_STCF_ADJ_CmdPkt, pkttype=1, apid=5, cmd_func_code=14)


class CFE_TIME_SET_SIGNAL_CmdPkt(Packet):
    """This command selects the Time Service tone signal source. Although the list of potential tone signal sources is mission specific, a common choice is the selection of primary or redundant tone signal. The selection may be available to both the Time Server and Time Clients, depending on hardware configuration. \nNotes:\n\tThis command is only valid when the CFE_TIME_CFG_SIGNAL configuration parameter in the cfe_platform_cfg.h file has been set to TRUE.

    app = CFE_TIME
    command = SET_SIGNAL
    msg_id = CFE_TIME_CMD_MID = 0x1805 = 0x1800 + 0x005
    cmd_func_code = 15
    data_len = 2 bytes
    """
    name = "CFE_TIME_SET_SIGNAL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TONE_SOURCE 16 INT MIN_INT16 MAX_INT16 0 "CFE_TIME_TONE_PRI=Primary Source, CFE_TIME_TONE_RED=Redundant Source"
        SignedShortField("TONE_SOURCE", 0),
    ]


bind_layers(CCSDSPacket, CFE_TIME_SET_SIGNAL_CmdPkt, pkttype=1, apid=5, cmd_func_code=15)
