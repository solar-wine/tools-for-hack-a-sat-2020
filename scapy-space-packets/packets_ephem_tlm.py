from scapy.all import *
from ccsds_base import CCSDSPacket


class EPHEM_HK_TLM_PKT_TlmPkt(Packet):
    """Ephem App

    app = EPHEM
    command = HK_TLM_PKT
    msg_id = EPHEM_HK_TLM_MID = 0x09e2 = 0x0800 + 0x1e2
    """
    name = "EPHEM_HK_TLM_PKT_TlmPkt"
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
    ]


bind_layers(CCSDSPacket, EPHEM_HK_TLM_PKT_TlmPkt, pkttype=0, apid=482)


class EPHEM_EPHEM_PKT_TlmPkt(Packet):
    """Ephemeris Pkt

    app = EPHEM
    command = EPHEM_PKT
    msg_id = EPHEM_TLM_EPHEM_MID = 0x09e3 = 0x0800 + 0x1e3
    """
    name = "EPHEM_EPHEM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM PAD                   32  UINT   "Pad to 8 byte boundaries"
        IntField("PAD", 0),
        # APPEND_ITEM TIME_STRING           512 STRING "Time string in YYYY-MM-DD-HH:MM:SS.SSS format"
        StrFixedLenField("TIME_STRING", b"", 64),
        # APPEND_ITEM ABSOLUTE_TIME_OFFSET  64 FLOAT "Absolute time offset applied as delta seconds from absolute time dervied from the TLE epoch"
        IEEEDoubleField("ABSOLUTE_TIME_OFFSET", 0.0),
        # UNITS seconds s
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM ABSOLUTE_TIME_EPOCH   64 FLOAT "Seconds since J2000 epoch based on TLE Epoch at startup"
        IEEEDoubleField("ABSOLUTE_TIME_EPOCH", 0.0),
        # UNITS seconds s
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM ABSOLUTE_TIME         64 FLOAT "Current time since J2000 epoch based on TLE data"
        IEEEDoubleField("ABSOLUTE_TIME", 0.0),
        # UNITS seconds s
        # FORMAT_STRING "%.2f"
        # APPEND_ITEM PosN_X      64 FLOAT "X Position in Inertial Frame"
        IEEEDoubleField("PosN_X", 0.0),
        # UNITS Kilometers km
        # APPEND_ITEM PosN_Y      64 FLOAT "Y Position in Inertial Frame"
        IEEEDoubleField("PosN_Y", 0.0),
        # UNITS Kilometers km
        # APPEND_ITEM PosN_Z      64 FLOAT "Z Position in Inertial Frame"
        IEEEDoubleField("PosN_Z", 0.0),
        # UNITS Kilometers km
        # APPEND_ITEM VelN_X      64 FLOAT "X Velocity in Inertial Frame"
        IEEEDoubleField("VelN_X", 0.0),
        # UNITS Kilometers/Sec km/s
        # APPEND_ITEM VelN_Y      64 FLOAT "Y Velocity in Inertial Frame"
        IEEEDoubleField("VelN_Y", 0.0),
        # UNITS Kilometers/Sec km/s
        # APPEND_ITEM VelN_Z      64 FLOAT "Z Velocity in Inertial Frame"
        IEEEDoubleField("VelN_Z", 0.0),
        # UNITS Kilometers/Sec km/s
    ]


bind_layers(CCSDSPacket, EPHEM_EPHEM_PKT_TlmPkt, pkttype=0, apid=483)
