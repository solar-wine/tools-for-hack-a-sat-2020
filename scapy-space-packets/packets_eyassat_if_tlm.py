from scapy.all import *
from ccsds_base import CCSDSPacket


class EYASSAT_IF_HK_TLM_PKT_TlmPkt(Packet):
    """Eyassat_if App

    app = EYASSAT_IF
    command = HK_TLM_PKT
    msg_id = EYASSAT_IF_HK_TLM_MID = 0x09d4 = 0x0800 + 0x1d4
    """
    name = "EYASSAT_IF_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT 16 UINT "Count of valid commands received since startup or the last reset counter command"
        ShortField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT 16 UINT "Count of invalid commands received since startup or the last reset counter command"
        ShortField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM LAST_TBL_ACTION 8 UINT  "Last table action: 1=Register, 2=Load, 3=Dump"
        ByteField("LAST_TBL_ACTION", 0),
        # APPEND_ITEM LAST_TBL_STATUS 8 UINT  "Last table action status: 0=Undefined, 1=Invalid, 2=Valid"
        ByteField("LAST_TBL_STATUS", 0),
        # APPEND_ITEM EXOBJ_EXEC_CNT  16 UINT "Count of example object executions"
        ShortField("EXOBJ_EXEC_CNT", 0),
        # APPEND_ITEM CMD_BUFFER_HEAD  8 UINT "Position of Command Buffer Head Pointer"
        ByteField("CMD_BUFFER_HEAD", 0),
        # APPEND_ITEM CMD_BUFFER_TAIL  8 UINT "Position of Command Buffer Tail Pointer"
        ByteField("CMD_BUFFER_TAIL", 0),
        # APPEND_ITEM PAD 16 UINT "Pad to 24 bytes"
        ShortField("PAD", 0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_HK_TLM_PKT_TlmPkt, pkttype=0, apid=468)


class EYASSAT_IF_INTERNAL_TlmPkt(Packet):
    """Internal Telemetry

    app = EYASSAT_IF
    command = INTERNAL
    msg_id = EYASSAT_IF_INTERNAL_TLM_MID = 0x09d5 = 0x0800 + 0x1d5
    """
    name = "EYASSAT_IF_INTERNAL_TlmPkt"
    fields_desc = [
        # APPEND_ITEM TIME_STRING 64 STRING "Time String"
        StrFixedLenField("TIME_STRING", b"", 8),
        # APPEND_ITEM CALL_SIGN 24 STRING "Simulator Call Sign"
        StrFixedLenField("CALL_SIGN", b"", 3),
        # APPEND_ITEM PACKET_ID 8 UINT "Packet Id"
        ByteField("PACKET_ID", 0),
        # APPEND_ITEM TLM_DELAY 8 UINT "Telemetry Delay in Seconds"
        ByteField("TLM_DELAY", 0),
        # UNITS SECONDS S
        # APPEND_ITEM PWR_TLM 8 UINT "Power Board Telemetry On/Off"
        ByteField("PWR_TLM", 0),
        # STATE ON 1
        # STATE OFF 0
        # APPEND_ITEM ADCS_TLM 8 UINT "ADCS Board Telemetry On/Off"
        ByteField("ADCS_TLM", 0),
        # STATE ON 1
        # STATE OFF 0
        # APPEND_ITEM EXP_TLM 8 UINT "Experiment Board Telemetry On/Off"
        ByteField("EXP_TLM", 0),
        # STATE ON 1
        # STATE OFF 0
        # APPEND_ITEM CMD_TIMEOUT 16 INT "Command Timeout in Seconds"
        SignedShortField("CMD_TIMEOUT", 0),
        # UNITS SECONDS S
        # APPEND_ITEM PAD 16 UINT "Pad to 32 bytes"
        ShortField("PAD", 0),
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_INTERNAL_TlmPkt, pkttype=0, apid=469)


class EYASSAT_IF_TEMPS_TlmPkt(Packet):
    """Temperature Telemetry

    app = EYASSAT_IF
    command = TEMPS
    msg_id = EYASSAT_IF_TEMPS_TLM_MID = 0x09d6 = 0x0800 + 0x1d6
    """
    name = "EYASSAT_IF_TEMPS_TlmPkt"
    fields_desc = [
        # APPEND_ITEM TIME_STRING 64 STRING "Time String"
        StrFixedLenField("TIME_STRING", b"", 8),
        # APPEND_ITEM CALL_SIGN 24 STRING "Simulator Call Sign"
        StrFixedLenField("CALL_SIGN", b"", 3),
        # APPEND_ITEM PACKET_ID 8 UINT "Packet Id"
        ByteField("PACKET_ID", 0),
        # APPEND_ITEM DH_TEMP 32 FLOAT "DH Board Temperature"
        IEEEFloatField("DH_TEMP", 0.0),
        # UNITS Celcius C
        # LIMITS DEFAULT 1 ENABLED 20.0 21.0 34.0 35.0
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM EXP_TEMP 32 FLOAT "Experiment Temperature"
        IEEEFloatField("EXP_TEMP", 0.0),
        # UNITS Celcius C
        # LIMITS DEFAULT 1 ENABLED 20.0 21.0 34.0 35.0
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM REF_TEMP 32 FLOAT "Reference Temperature"
        IEEEFloatField("REF_TEMP", 0.0),
        # UNITS Celcius C
        # LIMITS DEFAULT 1 ENABLED 20.0 21.0 34.0 35.0
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM PANEL_A_TEMP 32 FLOAT "Thermal Panel A Temperature"
        IEEEFloatField("PANEL_A_TEMP", 0.0),
        # UNITS Celcius C
        # LIMITS DEFAULT 1 ENABLED 20.0 21.0 34.0 35.0
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM PANEL_B_TEMP 32 FLOAT "Thermal Panel B Temperature"
        IEEEFloatField("PANEL_B_TEMP", 0.0),
        # UNITS Celcius C
        # LIMITS DEFAULT 1 ENABLED 20.0 21.0 34.0 35.0
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM BASE_TEMP 32 FLOAT "Base of 2 Copper Rods Temperature"
        IEEEFloatField("BASE_TEMP", 0.0),
        # UNITS Celcius C
        # LIMITS DEFAULT 1 ENABLED 20.0 21.0 34.0 35.0
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM TOP_A_TEMP 32 FLOAT "Top of Copper Rod Temperature"
        IEEEFloatField("TOP_A_TEMP", 0.0),
        # UNITS Celcius C
        # LIMITS DEFAULT 1 ENABLED 20.0 21.0 34.0 35.0
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM TOP_B_TEMP 32 FLOAT "Top of Heat Pipe Temperature"
        IEEEFloatField("TOP_B_TEMP", 0.0),
        # UNITS Celcius C
        # LIMITS DEFAULT 1 ENABLED 20.0 21.0 34.0 35.0
        # FORMAT_STRING "%.2f"
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_TEMPS_TlmPkt, pkttype=0, apid=470)


class EYASSAT_IF_POWER_TlmPkt(Packet):
    """Power Telemetry

    app = EYASSAT_IF
    command = POWER
    msg_id = EYASSAT_IF_POWER_TLM_MID = 0x09d7 = 0x0800 + 0x1d7
    """
    name = "EYASSAT_IF_POWER_TlmPkt"
    fields_desc = [
        # APPEND_ITEM TIME_STRING 64 STRING "Time String"
        StrFixedLenField("TIME_STRING", b"", 8),
        # APPEND_ITEM CALL_SIGN 24 STRING "Simulator Call Sign"
        StrFixedLenField("CALL_SIGN", b"", 3),
        # APPEND_ITEM PACKET_ID 8 UINT "Packet Id"
        ByteField("PACKET_ID", 0),
        # APPEND_ITEM SEP_STATUS 8 UINT "Seperation Status"
        ByteField("SEP_STATUS", 0),
        # STATE TRUE 1
        # STATE FALSE 0
        # APPEND_ITEM PAD 8 UINT "Pad"
        ByteField("PAD", 0),
        # APPEND_ITEM SWITCH_STATUS 16 UINT "Switch Status Register"
        ShortField("SWITCH_STATUS", 0),
        # FORMAT_STRING "0x%04X"
        # APPEND_ITEM V_BATT 32 FLOAT "Battery Voltage"
        IEEEFloatField("V_BATT", 0.0),
        # UNITS Volts V
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM I_BATT 32 FLOAT "Battery Current"
        IEEEFloatField("I_BATT", 0.0),
        # UNITS Milliamps mA
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM V_SA 32 FLOAT "Solar Array Voltage"
        IEEEFloatField("V_SA", 0.0),
        # UNITS Volts V
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM I_SA 32 FLOAT "Solar Array Current"
        IEEEFloatField("I_SA", 0.0),
        # UNITS Milliamps mA
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM I_MB 32 FLOAT "Main Bus Current"
        IEEEFloatField("I_MB", 0.0),
        # UNITS Milliamps mA
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM V_5V 32 FLOAT "5V Bus Voltage"
        IEEEFloatField("V_5V", 0.0),
        # UNITS Volts V
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM I_5V 32 FLOAT "5V Bus Current"
        IEEEFloatField("I_5V", 0.0),
        # UNITS Milliamps mA
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM V_3V 32 FLOAT "3.3V Bus Voltage"
        IEEEFloatField("V_3V", 0.0),
        # UNITS Volts V
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM I_3V 32 FLOAT "3.3V Bus Current"
        IEEEFloatField("I_3V", 0.0),
        # UNITS Milliamps mA
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM BATT_TEMP 32 FLOAT "Battery Temperature"
        IEEEFloatField("BATT_TEMP", 0.0),
        # UNITS Celcius C
        # LIMITS DEFAULT 1 ENABLED 20.0 21.0 34.0 35.0
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM SA1_TEMP 32 FLOAT "Solar Array 1 Temperature"
        IEEEFloatField("SA1_TEMP", 0.0),
        # UNITS Celcius C
        # LIMITS DEFAULT 1 ENABLED 20.0 21.0 34.0 35.0
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM SA2_TEMP 32 FLOAT "Solar Array 2 Temperature"
        IEEEFloatField("SA2_TEMP", 0.0),
        # UNITS Celcius C
        # LIMITS DEFAULT 1 ENABLED 20.0 21.0 34.0 35.0
        # FORMAT_STRING "%.2f"
        # ITEM PWR_3V 0 0 DERIVED "3.3V Power On/Off Flag"
        # READ_CONVERSION bit_on_off_conversion.rb 0x0001
        # ITEM PWR_ADCS 0 0 DERIVED "ADCS Power On/Off Flag"
        # READ_CONVERSION bit_on_off_conversion.rb 0x0002
        # ITEM PWR_EXP 0 0 DERIVED "Experiment Power On/Off Flag"
        # READ_CONVERSION bit_on_off_conversion.rb 0x0004
        # ITEM PWR_HTR1 0 0 DERIVED "Heater 1 Power On/Off Flag"
        # READ_CONVERSION bit_on_off_conversion.rb 0x0008
        # ITEM PWR_HTR2 0 0 DERIVED "Heater 2 Power On/Off Flag"
        # READ_CONVERSION bit_on_off_conversion.rb 0x0010
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_POWER_TlmPkt, pkttype=0, apid=471)


class EYASSAT_IF_ADCS_TlmPkt(Packet):
    """ADCS Telemetry

    app = EYASSAT_IF
    command = ADCS
    msg_id = EYASSAT_IF_ADCS_TLM_MID = 0x09d9 = 0x0800 + 0x1d9
    """
    name = "EYASSAT_IF_ADCS_TlmPkt"
    fields_desc = [
        # APPEND_ITEM TIME_STRING 64 STRING "Time String"
        StrFixedLenField("TIME_STRING", b"", 8),
        # APPEND_ITEM CALL_SIGN 24 STRING "Simulator Call Sign"
        StrFixedLenField("CALL_SIGN", b"", 3),
        # APPEND_ITEM PACKET_ID 8 UINT "Packet Id"
        ByteField("PACKET_ID", 0),
        # APPEND_ITEM X_ROD 8 INT "Torque X Status"
        SignedByteField("X_ROD", 0),
        # STATE OFF 0
        # STATE POS 1
        # STATE NEG -1
        # APPEND_ITEM Y_ROD 8 INT "Torque Y Status"
        SignedByteField("Y_ROD", 0),
        # STATE OFF 0
        # STATE POS 1
        # STATE NEG -1
        # APPEND_ITEM CTRL_MODE 8 UINT "Control Mode"
        ByteField("CTRL_MODE", 0),
        # APPEND_ITEM PAD      24 UINT "Pad Bits"
        X3BytesField("PAD", 0),
        # APPEND_ITEM SUN_TOP 16 UINT "Top Sun Sensor Reading"
        ShortField("SUN_TOP", 0),
        # APPEND_ITEM SUN_BOTTOM 16 UINT "Bottom Sun Sensor Reading"
        ShortField("SUN_BOTTOM", 0),
        # APPEND_ITEM PWM 16 UINT "Pulse Width Modulation"
        ShortField("PWM", 0),
        # APPEND_ITEM SUN_YAW_ANG 32 FLOAT "Yaw Angle of the Sun as seen by the yaw sensor"
        IEEEFloatField("SUN_YAW_ANG", 0.0),
        # UNITS Degrees Deg
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM YAW 32 FLOAT "Yaw angle based on Magnetometer"
        IEEEFloatField("YAW", 0.0),
        # UNITS Degrees Deg
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM PITCH 32 FLOAT "Pitch angle based on Magnetometer"
        IEEEFloatField("PITCH", 0.0),
        # UNITS Degrees Deg
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM ROLL 32 FLOAT "Roll angle based on Magnetometer"
        IEEEFloatField("ROLL", 0.0),
        # UNITS Degrees Deg
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM MAG_X 32 FLOAT "Magnetometer X Reading"
        IEEEFloatField("MAG_X", 0.0),
        # UNITS mGauss mG
        # FORMAT_STRING "%4.2f"
        # APPEND_ITEM MAG_Y 32 FLOAT "Magnetometer Y Reading"
        IEEEFloatField("MAG_Y", 0.0),
        # UNITS mGauss mG
        # FORMAT_STRING "%4.2f"
        # APPEND_ITEM MAG_Z 32 FLOAT "Magnetometer Z Reading"
        IEEEFloatField("MAG_Z", 0.0),
        # UNITS mGauss mG
        # FORMAT_STRING "%4.2f"
        # APPEND_ITEM ACC_X 32 FLOAT "Accelerometer X Reading"
        IEEEFloatField("ACC_X", 0.0),
        # FORMAT_STRING "%1.3f"
        # APPEND_ITEM ACC_Y 32 FLOAT "Accelerometer Y Reading"
        IEEEFloatField("ACC_Y", 0.0),
        # FORMAT_STRING "%1.3f"
        # APPEND_ITEM ACC_Z 32 FLOAT "Accelerometer Z Reading"
        IEEEFloatField("ACC_Z", 0.0),
        # FORMAT_STRING "%1.3f"
        # APPEND_ITEM ROT_X 32 FLOAT "Angular Rotation X Reading"
        IEEEFloatField("ROT_X", 0.0),
        # UNITS degrees/sec dps
        # FORMAT_STRING "%3.3f"
        # APPEND_ITEM ROT_Y 32 FLOAT "Angular Rotation Y Reading"
        IEEEFloatField("ROT_Y", 0.0),
        # UNITS degrees/sec dps
        # FORMAT_STRING "%3.3f"
        # APPEND_ITEM ROT_Z 32 FLOAT "Angular Rotation Z Reading"
        IEEEFloatField("ROT_Z", 0.0),
        # UNITS degrees/sec dps
        # FORMAT_STRING "%3.3f"
        # APPEND_ITEM ACT_WHEEL_SPD 32 FLOAT "Actual Wheel Speed"
        IEEEFloatField("ACT_WHEEL_SPD", 0.0),
        # UNITS "Rotations Per Seconds" RPS
        # LIMITS DEFAULT 1 ENABLED -10 -8.0 8.0 10.0
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM CMD_WHEEL_SPD 32 FLOAT "Commanded Wheel Speed"
        IEEEFloatField("CMD_WHEEL_SPD", 0.0),
        # UNITS "Rotations Per Seconds" RPS
        # LIMITS DEFAULT 1 ENABLED -10 -8.0 8.0 10.0
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM WHEEL_ANG_MOM 32 FLOAT "Wheel Angular Momentum"
        IEEEFloatField("WHEEL_ANG_MOM", 0.0),
        # UNITS "Newton Meter Seconds" NMS
        # FORMAT_STRING "%.6f"
        # APPEND_ITEM DELTA_T 32 FLOAT "Integration Time"
        IEEEFloatField("DELTA_T", 0.0),
        # UNITS Seconds S
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM YAW_CMD 32 FLOAT "Commanded yaw angle offset for sun and mag pointing"
        IEEEFloatField("YAW_CMD", 0.0),
        # UNITS Degrees Deg
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM POINTING_ERROR 32 FLOAT "Pointing Error - degrees from commanded yaw angle"
        IEEEFloatField("POINTING_ERROR", 0.0),
        # UNITS Degrees Deg
        # FORMAT_STRING "%.1f"
        # APPEND_ITEM DEADBAND 32 FLOAT "Deadband for deadband pointing algorithm"
        IEEEFloatField("DEADBAND", 0.0),
        # FORMAT_STRING "%2.1f"
        # APPEND_ITEM EXTRA 32 FLOAT "Extra PWM value for deadband pointing algorithm"
        IEEEFloatField("EXTRA", 0.0),
        # FORMAT_STRING "%2.1f"
        # APPEND_ITEM KP 32 FLOAT "Wheel/Attitude control P coefficient"
        IEEEFloatField("KP", 0.0),
        # FORMAT_STRING "%1.1f"
        # APPEND_ITEM KI 32 FLOAT "Wheel control I coefficient"
        IEEEFloatField("KI", 0.0),
        # FORMAT_STRING "%1.1f"
        # APPEND_ITEM KD 32 FLOAT "Wheel/Attitude control P coefficient"
        IEEEFloatField("KD", 0.0),
        # FORMAT_STRING "%1.1f"
        # APPEND_ITEM DEADBAND_SCALE_FACTOR 32 FLOAT "Scaling factor applied to PWM when in PD pointing mode within deadband"
        IEEEFloatField("DEADBAND_SCALE_FACTOR", 0.0),
        # FORMAT_STRING "%1.2f"
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_ADCS_TlmPkt, pkttype=0, apid=473)


class EYASSAT_IF_CAL_TBL_TlmPkt(Packet):
    """ADCS Magnetometer/Gryo Calibration Table Telemetry

    app = EYASSAT_IF
    command = CAL_TBL
    msg_id = EYASSAT_IF_CAL_TBL_TLM_MID = 0x09da = 0x0800 + 0x1da
    """
    name = "EYASSAT_IF_CAL_TBL_TlmPkt"
    fields_desc = [
        # APPEND_ITEM PAD 32 UINT "Pad to 8 byte alignment"
        IntField("PAD", 0),
        # APPEND_ITEM MAG_CAL_X 64 FLOAT "Magnetometer X Calibration Offset"
        IEEEDoubleField("MAG_CAL_X", 0.0),
        # UNITS mGauss mG
        # FORMAT_STRING "%4.2f"
        # APPEND_ITEM MAG_CAL_Y 64 FLOAT "Magnetometer Y Calibration Offset"
        IEEEDoubleField("MAG_CAL_Y", 0.0),
        # UNITS mGauss mG
        # FORMAT_STRING "%4.2f"
        # APPEND_ITEM MAG_CAL_Z 64 FLOAT "Magnetometer Z Calibration Offset"
        IEEEDoubleField("MAG_CAL_Z", 0.0),
        # UNITS mGauss mG
        # FORMAT_STRING "%4.2f"
        # APPEND_ITEM ROT_CAL_X 64 FLOAT "Gyro Angular Rotation X Offset"
        IEEEDoubleField("ROT_CAL_X", 0.0),
        # UNITS degrees/sec dps
        # FORMAT_STRING "%3.3f"
        # APPEND_ITEM ROT_CAL_Y 64 FLOAT "Gyro Angular Rotation Y Offset"
        IEEEDoubleField("ROT_CAL_Y", 0.0),
        # UNITS degrees/sec dps
        # FORMAT_STRING "%3.3f"
        # APPEND_ITEM ROT_CAL_Z 64 FLOAT "Gyro Angular Rotation Z Offset"
        IEEEDoubleField("ROT_CAL_Z", 0.0),
        # UNITS degrees/sec dps
        # FORMAT_STRING "%3.3f"
    ]


bind_layers(CCSDSPacket, EYASSAT_IF_CAL_TBL_TlmPkt, pkttype=0, apid=474)
