from scapy.all import *
from ccsds_base import CCSDSPacket


class EYASSAT_IF_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = EYASSAT_IF
    command = NOOP
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "EYASSAT_IF_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_NOOP_CmdPkt, pkttype=1, apid=469, cmd_func_code=0)


class EYASSAT_IF_RESET_CTRS_CmdPkt(Packet):
    """Reset command counters

    app = EYASSAT_IF
    command = RESET_CTRS
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "EYASSAT_IF_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_RESET_CTRS_CmdPkt, pkttype=1, apid=469, cmd_func_code=1)


class EYASSAT_IF_LOAD_TBL_CmdPkt(Packet):
    """Load example object table

    app = EYASSAT_IF
    command = LOAD_TBL
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 2
    data_len = 66 bytes
    """
    name = "EYASSAT_IF_LOAD_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ID    8  UINT 0 2 0 "Table ID. 0 is first table registered"
        ByteField("ID", 0),
        # APPEND_PARAMETER TYPE  8  UINT 0 1 1 "0=Replace Table, 1=Update Records"
        ByteField("TYPE", 1),
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/es_adcs_tbl.json" "Full path and file name of table to be loaded"
        StrFixedLenField("FILENAME", b"/cf/es_adcs_tbl.json", 64),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_LOAD_TBL_CmdPkt, pkttype=1, apid=469, cmd_func_code=2)


class EYASSAT_IF_DUMP_TBL_CmdPkt(Packet):
    """Dump example object table

    app = EYASSAT_IF
    command = DUMP_TBL
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 3
    data_len = 66 bytes
    """
    name = "EYASSAT_IF_DUMP_TBL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER ID   8 UINT 0 1 0 "Table ID. 0 is first table registered"
        ByteField("ID", 0),
        # APPEND_PARAMETER TYPE 8 UINT 0 1 0 "Unused"
        ByteField("TYPE", 0),
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/es_adcs_tbl~.json" "Full path and file name to receive table dump"
        StrFixedLenField("FILENAME", b"/cf/es_adcs_tbl~.json", 64),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_DUMP_TBL_CmdPkt, pkttype=1, apid=469, cmd_func_code=3)


class EYASSAT_IF_HOUR_CmdPkt(Packet):
    """Set Hour

    app = EYASSAT_IF
    command = HOUR
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_HOUR_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "ch" "Command Code"
        StrFixedLenField("CODE", b"ch", 2),
        # APPEND_PARAMETER HOUR 8 UINT 0 23 0 "Hour"
        ByteField("HOUR", 0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_HOUR_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_MINUTE_CmdPkt(Packet):
    """Set Minute

    app = EYASSAT_IF
    command = MINUTE
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_MINUTE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "cm" "Command Code"
        StrFixedLenField("CODE", b"cm", 2),
        # APPEND_PARAMETER MINUTE 8 UINT 0 59 0 "Minute"
        ByteField("MINUTE", 0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_MINUTE_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_SECOND_CmdPkt(Packet):
    """Set Second

    app = EYASSAT_IF
    command = SECOND
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_SECOND_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "cs" "Command Code"
        StrFixedLenField("CODE", b"cs", 2),
        # APPEND_PARAMETER SECOND 8 UINT 0 59 0 "Second"
        ByteField("SECOND", 0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_SECOND_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_CALL_SIGN_CmdPkt(Packet):
    """Set Call Sign

    app = EYASSAT_IF
    command = CALL_SIGN
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_CALL_SIGN_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "is" "Command Code"
        StrFixedLenField("CODE", b"is", 2),
        # APPEND_PARAMETER CALL_SIGN 8 UINT 0 9 0 "Call Sign"
        ByteField("CALL_SIGN", 0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_CALL_SIGN_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_TLM_DELAY_CmdPkt(Packet):
    """Set Telemetry Delay

    app = EYASSAT_IF
    command = TLM_DELAY
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_TLM_DELAY_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "id" "Command Code"
        StrFixedLenField("CODE", b"id", 2),
        # APPEND_PARAMETER DELAY 8 UINT 2 60 2 "Delay in Seconds"
        ByteField("DELAY", 2),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_TLM_DELAY_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_CMD_TIMEOUT_CmdPkt(Packet):
    """Set Command Timeout

    app = EYASSAT_IF
    command = CMD_TIMEOUT
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 5
    data_len = 4 bytes
    """
    name = "EYASSAT_IF_CMD_TIMEOUT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "it" "Command Code"
        StrFixedLenField("CODE", b"it", 2),
        # APPEND_PARAMETER TIMEOUT 16 INT 1 32767 1 "Command Timeout in Seconds"
        SignedShortField("TIMEOUT", 1),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_CMD_TIMEOUT_CmdPkt, pkttype=1, apid=469, cmd_func_code=5)


class EYASSAT_IF_UART0_CmdPkt(Packet):
    """Enable or Disable UART 0

    app = EYASSAT_IF
    command = UART0
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_UART0_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "iu" "Command Code"
        StrFixedLenField("CODE", b"iu", 2),
        # APPEND_PARAMETER ENABLE 8 UINT 0 1 1 "Enable Flag"
        ByteField("ENABLE", 1),
        # STATE TRUE 1
        # STATE FALSE 0
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_UART0_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_PWR_TLM_CmdPkt(Packet):
    """Control Power Telemetry

    app = EYASSAT_IF
    command = PWR_TLM
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_PWR_TLM_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "dp" "Command Code"
        StrFixedLenField("CODE", b"dp", 2),
        # APPEND_PARAMETER ENABLE 8 UINT 0 1 1 "Enable Flag"
        ByteField("ENABLE", 1),
        # STATE ON 1
        # STATE OFF 0
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_PWR_TLM_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_ADCS_TLM_CmdPkt(Packet):
    """Control ADCS Telemetry

    app = EYASSAT_IF
    command = ADCS_TLM
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_ADCS_TLM_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "da" "Command Code"
        StrFixedLenField("CODE", b"da", 2),
        # APPEND_PARAMETER ENABLE 8 UINT 0 1 1 "Enable Flag"
        ByteField("ENABLE", 1),
        # STATE ON 1
        # STATE OFF 0
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_TLM_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_PWR_RQST_CmdPkt(Packet):
    """Power Telemetry Request from UART

    app = EYASSAT_IF
    command = PWR_RQST
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 7
    data_len = 2 bytes
    """
    name = "EYASSAT_IF_PWR_RQST_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "pt" "Command Code"
        StrFixedLenField("CODE", b"pt", 2),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_PWR_RQST_CmdPkt, pkttype=1, apid=469, cmd_func_code=7)


class EYASSAT_IF_PWR_RESET_CmdPkt(Packet):
    """Power Reset from UART

    app = EYASSAT_IF
    command = PWR_RESET
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 7
    data_len = 2 bytes
    """
    name = "EYASSAT_IF_PWR_RESET_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "pr" "Command Code"
        StrFixedLenField("CODE", b"pr", 2),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_PWR_RESET_CmdPkt, pkttype=1, apid=469, cmd_func_code=7)


class EYASSAT_IF_PWR_SCALE_CmdPkt(Packet):
    """Enable or Disable Scaling Power Telemetry

    app = EYASSAT_IF
    command = PWR_SCALE
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_PWR_SCALE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "ps" "Command Code"
        StrFixedLenField("CODE", b"ps", 2),
        # APPEND_PARAMETER ENABLE 8 UINT 0 1 1 "Enable Flag"
        ByteField("ENABLE", 1),
        # STATE TRUE 1
        # STATE FALSE 0
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_PWR_SCALE_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_PWR_3V_CmdPkt(Packet):
    """Control 3.3V Power

    app = EYASSAT_IF
    command = PWR_3V
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_PWR_3V_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "p1" "Command Code"
        StrFixedLenField("CODE", b"p1", 2),
        # APPEND_PARAMETER STATE 8 UINT 0 1 1 "On/Off Flag"
        ByteField("STATE", 1),
        # STATE ON 1
        # STATE OFF 0
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_PWR_3V_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_PWR_ADCS_CmdPkt(Packet):
    """Control ADCS Power

    app = EYASSAT_IF
    command = PWR_ADCS
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_PWR_ADCS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "p2" "Command Code"
        StrFixedLenField("CODE", b"p2", 2),
        # APPEND_PARAMETER STATE 8 UINT 0 1 1 "On/Off Flag"
        ByteField("STATE", 1),
        # STATE ON 1
        # STATE OFF 0
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_PWR_ADCS_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_PWR_EXP_CmdPkt(Packet):
    """Control Experiment Power

    app = EYASSAT_IF
    command = PWR_EXP
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_PWR_EXP_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "p3" "Command Code"
        StrFixedLenField("CODE", b"p3", 2),
        # APPEND_PARAMETER STATE 8 UINT 0 1 1 "On/Off Flag"
        ByteField("STATE", 1),
        # STATE ON 1
        # STATE OFF 0
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_PWR_EXP_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_PWR_HTR1_CmdPkt(Packet):
    """Control Heater 1 Power

    app = EYASSAT_IF
    command = PWR_HTR1
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_PWR_HTR1_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "p4" "Command Code"
        StrFixedLenField("CODE", b"p4", 2),
        # APPEND_PARAMETER STATE 8 UINT 0 1 1 "On/Off Flag"
        ByteField("STATE", 1),
        # STATE ON 1
        # STATE OFF 0
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_PWR_HTR1_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_PWR_HTR2_CmdPkt(Packet):
    """Control Heater 2 Power

    app = EYASSAT_IF
    command = PWR_HTR2
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 4
    data_len = 3 bytes
    """
    name = "EYASSAT_IF_PWR_HTR2_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "p5" "Command Code"
        StrFixedLenField("CODE", b"p5", 2),
        # APPEND_PARAMETER STATE 8 UINT 0 1 1 "On/Off Flag"
        ByteField("STATE", 1),
        # STATE ON 1
        # STATE OFF 0
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_PWR_HTR2_CmdPkt, pkttype=1, apid=469, cmd_func_code=4)


class EYASSAT_IF_ADCS_RQST_CmdPkt(Packet):
    """ADCS Telemetry Request from UART

    app = EYASSAT_IF
    command = ADCS_RQST
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 7
    data_len = 2 bytes
    """
    name = "EYASSAT_IF_ADCS_RQST_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "at" "Command Code"
        StrFixedLenField("CODE", b"at", 2),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_RQST_CmdPkt, pkttype=1, apid=469, cmd_func_code=7)


class EYASSAT_IF_ADCS_RESET_CmdPkt(Packet):
    """ADCS Reset from UART

    app = EYASSAT_IF
    command = ADCS_RESET
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 7
    data_len = 2 bytes
    """
    name = "EYASSAT_IF_ADCS_RESET_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "ar" "Command Code"
        StrFixedLenField("CODE", b"ar", 2),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_RESET_CmdPkt, pkttype=1, apid=469, cmd_func_code=7)


class EYASSAT_IF_ADCS_ENABLE_IMU_CmdPkt(Packet):
    """ADCS Enable 9DOF IMU

    app = EYASSAT_IF
    command = ADCS_ENABLE_IMU
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 7
    data_len = 2 bytes
    """
    name = "EYASSAT_IF_ADCS_ENABLE_IMU_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "a9" "Command Code"
        StrFixedLenField("CODE", b"a9", 2),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_ENABLE_IMU_CmdPkt, pkttype=1, apid=469, cmd_func_code=7)


class EYASSAT_IF_CONNECT_CmdPkt(Packet):
    """Connect to the EyasSat UART port

    app = EYASSAT_IF
    command = CONNECT
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 8
    data_len = 0 bytes
    """
    name = "EYASSAT_IF_CONNECT_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_CONNECT_CmdPkt, pkttype=1, apid=469, cmd_func_code=8)


class EYASSAT_IF_DISCONNECT_CmdPkt(Packet):
    """Disconnect from the EyasSat UART port

    app = EYASSAT_IF
    command = DISCONNECT
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 9
    data_len = 0 bytes
    """
    name = "EYASSAT_IF_DISCONNECT_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_DISCONNECT_CmdPkt, pkttype=1, apid=469, cmd_func_code=9)


class EYASSAT_IF_ADCS_X_ROD_CmdPkt(Packet):
    """Set Torquer X

    app = EYASSAT_IF
    command = ADCS_X_ROD
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 12
    data_len = 4 bytes
    """
    name = "EYASSAT_IF_ADCS_X_ROD_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "ax" "Command Code"
        StrFixedLenField("CODE", b"ax", 2),
        # APPEND_PARAMETER X_ROD 16 INT 0 2 0 "Direction"
        SignedShortField("X_ROD", 0),
        # STATE OFF 0
        # STATE POS 1
        # STATE NEG 2
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_X_ROD_CmdPkt, pkttype=1, apid=469, cmd_func_code=12)


class EYASSAT_IF_ADCS_Y_ROD_CmdPkt(Packet):
    """Set Torquer Y

    app = EYASSAT_IF
    command = ADCS_Y_ROD
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 12
    data_len = 4 bytes
    """
    name = "EYASSAT_IF_ADCS_Y_ROD_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "ay" "Command Code"
        StrFixedLenField("CODE", b"ay", 2),
        # APPEND_PARAMETER Y_ROD 16 INT 0 2 0 "Direction"
        SignedShortField("Y_ROD", 0),
        # STATE OFF 0
        # STATE POS 1
        # STATE NEG 2
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_Y_ROD_CmdPkt, pkttype=1, apid=469, cmd_func_code=12)


class EYASSAT_IF_ADCS_PWM_BASELINE_CmdPkt(Packet):
    """Set PWM Baseline Output for Earth/Sun pointing

    app = EYASSAT_IF
    command = ADCS_PWM_BASELINE
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 5
    data_len = 4 bytes
    """
    name = "EYASSAT_IF_ADCS_PWM_BASELINE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "am" "Command Code"
        StrFixedLenField("CODE", b"am", 2),
        # APPEND_PARAMETER PWM 16 INT 0 250 0 "Output Value"
        SignedShortField("PWM", 0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_PWM_BASELINE_CmdPkt, pkttype=1, apid=469, cmd_func_code=5)


class EYASSAT_IF_ADCS_WHEEL_SPD_CmdPkt(Packet):
    """Set Wheel Speed

    app = EYASSAT_IF
    command = ADCS_WHEEL_SPD
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 6
    data_len = 6 bytes
    """
    name = "EYASSAT_IF_ADCS_WHEEL_SPD_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "aw" "Command Code"
        StrFixedLenField("CODE", b"aw", 2),
        # APPEND_PARAMETER SPD 32 FLOAT -8.0 8.0 0.0 "Commanded Speed"
        IEEEFloatField("SPD", 0.0),
        # UNITS "Rotations Per Second" RPS
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_WHEEL_SPD_CmdPkt, pkttype=1, apid=469, cmd_func_code=6)


class EYASSAT_IF_ADCS_DELTA_T_CmdPkt(Packet):
    """Integration Time in Loop

    app = EYASSAT_IF
    command = ADCS_DELTA_T
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 6
    data_len = 6 bytes
    """
    name = "EYASSAT_IF_ADCS_DELTA_T_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "al" "Command Code"
        StrFixedLenField("CODE", b"al", 2),
        # APPEND_PARAMETER DELTA_T 32 FLOAT MIN MAX 1.0 "Integration Time"
        IEEEFloatField("DELTA_T", 1.0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_DELTA_T_CmdPkt, pkttype=1, apid=469, cmd_func_code=6)


class EYASSAT_IF_ADCS_CTRL_ALG_CmdPkt(Packet):
    """Set Control Algorithm

    app = EYASSAT_IF
    command = ADCS_CTRL_ALG
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 5
    data_len = 4 bytes
    """
    name = "EYASSAT_IF_ADCS_CTRL_ALG_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "ac" "Command Code"
        StrFixedLenField("CODE", b"ac", 2),
        # APPEND_PARAMETER CTRL_ALG 16 INT 0 7 0 "Commanded control algorithm"
        SignedShortField("CTRL_ALG", 0),
        # STATE DEFAULT 0
        # STATE PID 1
        # STATE PDSUN 2
        # STATE PDMAG 3
        # STATE DBSUN 4
        # STATE DBMAG 5
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_CTRL_ALG_CmdPkt, pkttype=1, apid=469, cmd_func_code=5)


class EYASSAT_IF_ADCS_YAW_CMD_CmdPkt(Packet):
    """Offset to point from earth

    app = EYASSAT_IF
    command = ADCS_YAW_CMD
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 6
    data_len = 6 bytes
    """
    name = "EYASSAT_IF_ADCS_YAW_CMD_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "ao" "Command Code"
        StrFixedLenField("CODE", b"ao", 2),
        # APPEND_PARAMETER YAW_CMD 32 FLOAT 0.0 360.0 0.0 "Commanded offset"
        IEEEFloatField("YAW_CMD", 0.0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_YAW_CMD_CmdPkt, pkttype=1, apid=469, cmd_func_code=6)


class EYASSAT_IF_ADCS_P_CONST_CmdPkt(Packet):
    """Proportional Constant for PID algorithm

    app = EYASSAT_IF
    command = ADCS_P_CONST
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 6
    data_len = 6 bytes
    """
    name = "EYASSAT_IF_ADCS_P_CONST_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "ap" "Command Code"
        StrFixedLenField("CODE", b"ap", 2),
        # APPEND_PARAMETER P_CONST 32 FLOAT MIN MAX 5.0 "Commanded constant"
        IEEEFloatField("P_CONST", 5.0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_P_CONST_CmdPkt, pkttype=1, apid=469, cmd_func_code=6)


class EYASSAT_IF_ADCS_I_CONST_CmdPkt(Packet):
    """Integral Constant for PID algorithm

    app = EYASSAT_IF
    command = ADCS_I_CONST
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 6
    data_len = 6 bytes
    """
    name = "EYASSAT_IF_ADCS_I_CONST_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "ai" "Command Code"
        StrFixedLenField("CODE", b"ai", 2),
        # APPEND_PARAMETER I_CONST 32 FLOAT MIN MAX 2.0 "Commanded constant"
        IEEEFloatField("I_CONST", 2.0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_I_CONST_CmdPkt, pkttype=1, apid=469, cmd_func_code=6)


class EYASSAT_IF_ADCS_D_CONST_CmdPkt(Packet):
    """Differential Constant for PID algorithm

    app = EYASSAT_IF
    command = ADCS_D_CONST
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 6
    data_len = 6 bytes
    """
    name = "EYASSAT_IF_ADCS_D_CONST_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "ad" "Command Code"
        StrFixedLenField("CODE", b"ad", 2),
        # APPEND_PARAMETER D_CONST 32 FLOAT MIN MAX 2.0 "Commanded constant"
        IEEEFloatField("D_CONST", 2.0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_D_CONST_CmdPkt, pkttype=1, apid=469, cmd_func_code=6)


class EYASSAT_IF_ADCS_EXTRA_CmdPkt(Packet):
    """Kick value for sun point mode

    app = EYASSAT_IF
    command = ADCS_EXTRA
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 6
    data_len = 6 bytes
    """
    name = "EYASSAT_IF_ADCS_EXTRA_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "ae" "Command Code"
        StrFixedLenField("CODE", b"ae", 2),
        # APPEND_PARAMETER EXTRA 32 FLOAT MIN MAX 20.0 "Kick value for sun point mode"
        IEEEFloatField("EXTRA", 20.0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_EXTRA_CmdPkt, pkttype=1, apid=469, cmd_func_code=6)


class EYASSAT_IF_ADCS_DEADBAND_CmdPkt(Packet):
    """Deadband value for deadband point mode

    app = EYASSAT_IF
    command = ADCS_DEADBAND
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 6
    data_len = 6 bytes
    """
    name = "EYASSAT_IF_ADCS_DEADBAND_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "ab" "Command Code"
        StrFixedLenField("CODE", b"ab", 2),
        # APPEND_PARAMETER DEADBAND 32 FLOAT MIN MAX 10.0 "Deadband value for deadband point mode"
        IEEEFloatField("DEADBAND", 10.0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_DEADBAND_CmdPkt, pkttype=1, apid=469, cmd_func_code=6)


class ADCS_MAG_CAL_CmdPkt(Packet):
    """Calibration values for magnetometer

    app = ADCS
    command = MAG_CAL
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 10
    data_len = 12 bytes
    """
    name = "ADCS_MAG_CAL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MAGCALX 32 FLOAT MIN MAX 0.0 "Mag cal offset for x axis"
        IEEEFloatField("MAGCALX", 0.0),
        # APPEND_PARAMETER MAGCALY 32 FLOAT MIN MAX 0.0 "Mag cal offset for y axis"
        IEEEFloatField("MAGCALY", 0.0),
        # APPEND_PARAMETER MAGCALZ 32 FLOAT MIN MAX 0.0 "Mag cal offset for z axis"
        IEEEFloatField("MAGCALZ", 0.0),
    ]


bind_layers(CCSDSPacket, ADCS_MAG_CAL_CmdPkt, pkttype=1, apid=469, cmd_func_code=10)


class ADCS_GYRO_CAL_CmdPkt(Packet):
    """Calibration values for gyro

    app = ADCS
    command = GYRO_CAL
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 11
    data_len = 12 bytes
    """
    name = "ADCS_GYRO_CAL_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER GYROCALX 32 FLOAT MIN MAX 0.0 "Gyro cal offset for x axis"
        IEEEFloatField("GYROCALX", 0.0),
        # APPEND_PARAMETER GYROCALY 32 FLOAT MIN MAX 0.0 "Gyro cal offset for y axis"
        IEEEFloatField("GYROCALY", 0.0),
        # APPEND_PARAMETER GYROCALZ 32 FLOAT MIN MAX 0.0 "Gyro cal offset for z axis"
        IEEEFloatField("GYROCALZ", 0.0),
    ]


bind_layers(CCSDSPacket, ADCS_GYRO_CAL_CmdPkt, pkttype=1, apid=469, cmd_func_code=11)


class EYASSAT_IF_ADCS_DEADBAND_SCALE_FACTOR_CmdPkt(Packet):
    """Scaling factor applied to PWM when in PD pointing mode within deadband

    app = EYASSAT_IF
    command = ADCS_DEADBAND_SCALE_FACTOR
    msg_id = EYASSAT_IF_CMD_MID = 0x19d5 = 0x1800 + 0x1d5
    cmd_func_code = 6
    data_len = 6 bytes
    """
    name = "EYASSAT_IF_ADCS_DEADBAND_SCALE_FACTOR_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CODE 16 STRING "as" "Command Code"
        StrFixedLenField("CODE", b"as", 2),
        # APPEND_PARAMETER DEADBAND 32 FLOAT 0 1.0 0.25 "Deadband scale factor PD point mode"
        IEEEFloatField("DEADBAND", 0.25),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_DEADBAND_SCALE_FACTOR_CmdPkt, pkttype=1, apid=469, cmd_func_code=6)
