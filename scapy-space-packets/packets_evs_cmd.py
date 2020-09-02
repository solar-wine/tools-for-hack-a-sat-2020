from scapy.all import *
from ccsds_base import CCSDSPacket


class CFE_EVS_NOOP_CmdPkt(Packet):
    """Increment the command execution counter and send event message to verify Event Service app response.

    app = CFE_EVS
    command = NOOP
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "CFE_EVS_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_EVS_NOOP_CmdPkt, pkttype=1, apid=1, cmd_func_code=0)


class CFE_EVS_RESET_CTRS_CmdPkt(Packet):
    """Resets the command counters

    app = CFE_EVS
    command = RESET_CTRS
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "CFE_EVS_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_EVS_RESET_CTRS_CmdPkt, pkttype=1, apid=1, cmd_func_code=1)


class CFE_EVS_ENA_EVENT_TYPE_CmdPkt(Packet):
    """This command enables the command specified Event Type allowing event messages of this type to be sent through Event Service. An Event Type is defined to be a classification of an Event Message such as debug, informational, error and critical. This command is a global enable of a particular event type, it applies to all applications.

    app = CFE_EVS
    command = ENA_EVENT_TYPE
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 2
    data_len = 2 bytes
    """
    name = "CFE_EVS_ENA_EVENT_TYPE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER BITMASK  8 UINT MIN_UINT8 MAX_UINT8 0 "Event type bitmask (3..0) = (Critical, Error, Info, Debug)"
        ByteField("BITMASK", 0),
        # APPEND_PARAMETER SPARE    8 UINT MIN_UINT8 MAX_UINT8 0 "Pad to even byte"
        ByteField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_ENA_EVENT_TYPE_CmdPkt, pkttype=1, apid=1, cmd_func_code=2)


class CFE_EVS_DIS_EVENT_TYPE_CmdPkt(Packet):
    """This command disables the command specified Event Type preventing event messages of this type to be sent through Event Service. An Event Type is defined to be a classification of an Event Message such as debug, informational, error and critical. This command is a global disable of a particular event type, it applies to all applications.

    app = CFE_EVS
    command = DIS_EVENT_TYPE
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 3
    data_len = 2 bytes
    """
    name = "CFE_EVS_DIS_EVENT_TYPE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER BITMASK 8 UINT MIN_UINT8 MAX_UINT8 0 "Event type bitmask (3..0) = (Critical, Error, Info, Debug)"
        ByteField("BITMASK", 0),
        # APPEND_PARAMETER SPARE   8 UINT MIN_UINT8 MAX_UINT8 0 "Pad to even byte"
        ByteField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_DIS_EVENT_TYPE_CmdPkt, pkttype=1, apid=1, cmd_func_code=3)


class CFE_EVS_SET_EVENT_FMT_CmdPkt(Packet):
    """This command sets the event format mode to the command specified value. The event format mode may be either short or long. A short event format detaches the Event Data from the event message and only includes the following information in the event packet: Processor ID, Application ID, Event ID, and Event Type. Refer to section 5.3.3.4 for a description of the Event Service event packet contents. Event Data is defined to be data describing an Event that is supplied to the cFE Event Service. ASCII text strings are used as the primary format for Event Data because heritage ground systems use string compares as the basis for their automated alert systems. Two systems, ANSR and SERS were looked at for interface definitions. The short event format is used to accommodate experiences with limited telemetry bandwidth. The long event format includes all event information included within the short format along with the Event Data.

    app = CFE_EVS
    command = SET_EVENT_FMT
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 4
    data_len = 2 bytes
    """
    name = "CFE_EVS_SET_EVENT_FMT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MODE  8 UINT MIN_UINT8 MAX_UINT8 0 "Format Mode: 0=Short, 1=Long"
        ByteField("MODE", 0),
        # APPEND_PARAMETER SPARE 8 UINT MIN_UINT8 MAX_UINT8 0 "Pad to even byte"
        ByteField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_SET_EVENT_FMT_CmdPkt, pkttype=1, apid=1, cmd_func_code=4)


class CFE_EVS_ENA_APP_EVENT_TYPE_CmdPkt(Packet):
    """This command enables the command specified event type for the command specified application, allowing the application to send event messages of the command specified event type through Event Service. An Event Type is defined to be a classification of an Event Message such as debug, informational, critical, and error. Note: In order for this command to take effect, applications must be registered for Event Service.

    app = CFE_EVS
    command = ENA_APP_EVENT_TYPE
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 5
    data_len = 22 bytes
    """
    name = "CFE_EVS_ENA_APP_EVENT_TYPE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING                   "default" "Application name to use in the command"
        StrFixedLenField("APP_NAME", b"default", 20),
        # APPEND_PARAMETER BITMASK    8 UINT MIN_UINT8 MAX_UINT8 0x0F      "Event type bitmask (3..0) = (Critical, Error, Info, Debug)"
        ByteField("BITMASK", 0x0F),
        # APPEND_PARAMETER SPARE      8 UINT MIN_UINT8 MAX_UINT8 0         "Pad to even byte"
        ByteField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_ENA_APP_EVENT_TYPE_CmdPkt, pkttype=1, apid=1, cmd_func_code=5)


class CFE_EVS_DIS_APP_EVENT_TYPE_CmdPkt(Packet):
    """This command disables the command specified event type for the command specified application, preventing the application from sending event messages of the command specified event type through Event Service. An Event Type is defined to be a classification of an Event Message such as debug, informational, critical, and error. Note: In order for this command to take effect, applications must be registered for Event Service.

    app = CFE_EVS
    command = DIS_APP_EVENT_TYPE
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 6
    data_len = 22 bytes
    """
    name = "CFE_EVS_DIS_APP_EVENT_TYPE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING                   "default" "Application name to use in the command"
        StrFixedLenField("APP_NAME", b"default", 20),
        # APPEND_PARAMETER BITMASK    8 UINT MIN_UINT8 MAX_UINT8 0         "Event type bitmask (3..0) = (Critical, Error, Info, Debug)"
        ByteField("BITMASK", 0),
        # APPEND_PARAMETER SPARE      8 UINT MIN_UINT8 MAX_UINT8 0         "Pad to even byte."
        ByteField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_DIS_APP_EVENT_TYPE_CmdPkt, pkttype=1, apid=1, cmd_func_code=6)


class CFE_EVS_ENA_APP_EVENT_GEN_CmdPkt(Packet):
    """This command enables the command specified application to send events through the Event Service. Note: In order for this command to take effect, applications must be registered for Event Service.

    app = CFE_EVS
    command = ENA_APP_EVENT_GEN
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 7
    data_len = 20 bytes
    """
    name = "CFE_EVS_ENA_APP_EVENT_GEN_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING "default" "Application name"
        StrFixedLenField("APP_NAME", b"default", 20),
    ]


bind_layers(CCSDSPacket, CFE_EVS_ENA_APP_EVENT_GEN_CmdPkt, pkttype=1, apid=1, cmd_func_code=7)


class CFE_EVS_DIS_APP_EVENT_GEN_CmdPkt(Packet):
    """This command disables the command specified application from sending events through Event Service. Note: In order for this command to take effect, applications must be registered for Event Service.

    app = CFE_EVS
    command = DIS_APP_EVENT_GEN
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 8
    data_len = 20 bytes
    """
    name = "CFE_EVS_DIS_APP_EVENT_GEN_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING "default" "Application name"
        StrFixedLenField("APP_NAME", b"default", 20),
    ]


bind_layers(CCSDSPacket, CFE_EVS_DIS_APP_EVENT_GEN_CmdPkt, pkttype=1, apid=1, cmd_func_code=8)


class CFE_EVS_RESET_APP_CTRS_CmdPkt(Packet):
    """This command sets the command specified application's event counter to zero. Note: In order for this command to take effect, applications must be registered for Event Service.

    app = CFE_EVS
    command = RESET_APP_CTRS
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 9
    data_len = 20 bytes
    """
    name = "CFE_EVS_RESET_APP_CTRS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING "default" "Application name"
        StrFixedLenField("APP_NAME", b"default", 20),
    ]


bind_layers(CCSDSPacket, CFE_EVS_RESET_APP_CTRS_CmdPkt, pkttype=1, apid=1, cmd_func_code=9)


class CFE_EVS_SET_FILTER_MASK_CmdPkt(Packet):
    """This command sets the command specified application's event filter mask to the command specified value for the command specified event. Note: In order for this command to take effect, applications must be registered for Event Service.

    app = CFE_EVS
    command = SET_FILTER_MASK
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 10
    data_len = 24 bytes
    """
    name = "CFE_EVS_SET_FILTER_MASK_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING                    "default" "Application name"
        StrFixedLenField("APP_NAME", b"default", 20),
        # APPEND_PARAMETER EVENT_ID  16 UINT MIN_UINT16 MAX_UINT16 0        "Event ID"
        ShortField("EVENT_ID", 0),
        # APPEND_PARAMETER MASK      16 UINT MIN_UINT16 MAX_UINT16 0        "Mask"
        ShortField("MASK", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_SET_FILTER_MASK_CmdPkt, pkttype=1, apid=1, cmd_func_code=10)


class CFE_EVS_ENA_PORT_CmdPkt(Packet):
    """This command enables the command specified port to output event messages

    app = CFE_EVS
    command = ENA_PORT
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 11
    data_len = 2 bytes
    """
    name = "CFE_EVS_ENA_PORT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER BITMASK 8 UINT MIN_UINT8 MAX_UINT8 0 "BitMask"
        ByteField("BITMASK", 0),
        # APPEND_PARAMETER SPARE   8 UINT MIN_UINT8 MAX_UINT8 0 "Pad to even byte."
        ByteField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_ENA_PORT_CmdPkt, pkttype=1, apid=1, cmd_func_code=11)


class CFE_EVS_DIS_PORT_CmdPkt(Packet):
    """This command disables the specified port from outputting event messages.

    app = CFE_EVS
    command = DIS_PORT
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 12
    data_len = 2 bytes
    """
    name = "CFE_EVS_DIS_PORT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER BITMASK 8 UINT MIN_UINT8 MAX_UINT8 0 "BitMask"
        ByteField("BITMASK", 0),
        # APPEND_PARAMETER SPARE   8 UINT MIN_UINT8 MAX_UINT8 0 "Pad to even byte."
        ByteField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_DIS_PORT_CmdPkt, pkttype=1, apid=1, cmd_func_code=12)


class CFE_EVS_RESET_FILTER_CTR_CmdPkt(Packet):
    """This command resets the command specified application's event filter for the command specified event ID. Note: In order for this command to take effect, applications must be registered for Event Service.

    app = CFE_EVS
    command = RESET_FILTER_CTR
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 13
    data_len = 22 bytes
    """
    name = "CFE_EVS_RESET_FILTER_CTR_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING                     "default" "Application name to use in the command."
        StrFixedLenField("APP_NAME", b"default", 20),
        # APPEND_PARAMETER EVENT_ID  16 UINT MIN_UINT16 MAX_UINT16 0         "Event ID to use in the command."
        ShortField("EVENT_ID", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_RESET_FILTER_CTR_CmdPkt, pkttype=1, apid=1, cmd_func_code=13)


class CFE_EVS_RESET_ALL_FILTERS_CmdPkt(Packet):
    """This command resets all of the command specified applications event filters. Note: In order for this command to take effect, applications must be registered for Event Service.

    app = CFE_EVS
    command = RESET_ALL_FILTERS
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 14
    data_len = 20 bytes
    """
    name = "CFE_EVS_RESET_ALL_FILTERS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING "default" "Application name to use in the command."
        StrFixedLenField("APP_NAME", b"default", 20),
    ]


bind_layers(CCSDSPacket, CFE_EVS_RESET_ALL_FILTERS_CmdPkt, pkttype=1, apid=1, cmd_func_code=14)


class CFE_EVS_ADD_EVENT_FILTER_CmdPkt(Packet):
    """This command adds the given filter for the given application identifier and event identifier. Note: In order for this command to take effect, applications must be registered for Event Service.

    app = CFE_EVS
    command = ADD_EVENT_FILTER
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 15
    data_len = 24 bytes
    """
    name = "CFE_EVS_ADD_EVENT_FILTER_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING                     "default"  "Application name to use in the command."
        StrFixedLenField("APP_NAME", b"default", 20),
        # APPEND_PARAMETER EVENT_ID  16 UINT MIN_UINT16 MAX_UINT16         0  "Event ID to use in the command."
        ShortField("EVENT_ID", 0),
        # APPEND_PARAMETER MASK      16 UINT MIN_UINT16 MAX_UINT16         0  "Mask to use in the command."
        ShortField("MASK", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_ADD_EVENT_FILTER_CmdPkt, pkttype=1, apid=1, cmd_func_code=15)


class CFE_EVS_DEL_EVENT_FILTER_CmdPkt(Packet):
    """This command removes the given filter for the given application identifier and event identifier. Note: In order for this command to take effect, applications must be registered for Event Service.

    app = CFE_EVS
    command = DEL_EVENT_FILTER
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 16
    data_len = 22 bytes
    """
    name = "CFE_EVS_DEL_EVENT_FILTER_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_NAME 160 STRING "default" "Application name to use in the command."
        StrFixedLenField("APP_NAME", b"default", 20),
        # APPEND_PARAMETER EVENT_ID  16 UINT MIN_UINT16 MAX_UINT16 0 "Event ID to use in the command."
        ShortField("EVENT_ID", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_DEL_EVENT_FILTER_CmdPkt, pkttype=1, apid=1, cmd_func_code=16)


class CFE_EVS_WRITE_APP_INFO_TO_FILE_CmdPkt(Packet):
    """Write application registry & status to a file

    app = CFE_EVS
    command = WRITE_APP_INFO_TO_FILE
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 17
    data_len = 64 bytes
    """
    name = "CFE_EVS_WRITE_APP_INFO_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/cfe_evs_app.dat" "Full path/filename where applicaton data is to be written"
        StrFixedLenField("FILENAME", b"/cf/cfe_evs_app.dat", 64),
    ]


bind_layers(CCSDSPacket, CFE_EVS_WRITE_APP_INFO_TO_FILE_CmdPkt, pkttype=1, apid=1, cmd_func_code=17)


class CFE_EVS_WRITE_LOG_TO_FILE_CmdPkt(Packet):
    """Write the contents of the local event log to a file.

    app = CFE_EVS
    command = WRITE_LOG_TO_FILE
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 18
    data_len = 64 bytes
    """
    name = "CFE_EVS_WRITE_LOG_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/cfe_evs.log" "Full path/filename where log data is to be written"
        StrFixedLenField("FILENAME", b"/cf/cfe_evs.log", 64),
    ]


bind_layers(CCSDSPacket, CFE_EVS_WRITE_LOG_TO_FILE_CmdPkt, pkttype=1, apid=1, cmd_func_code=18)


class CFE_EVS_SET_LOG_MODE_CmdPkt(Packet):
    """Sets the logging mode to the command specified value.

    app = CFE_EVS
    command = SET_LOG_MODE
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 19
    data_len = 2 bytes
    """
    name = "CFE_EVS_SET_LOG_MODE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MODE  8 UINT MIN_UINT8 MAX_UINT8 0 "0=Overwrite, 1=Discard"
        ByteField("MODE", 0),
        # APPEND_PARAMETER SPARE 8 UINT MIN_UINT8 MAX_UINT8 0 "Pad to even byte."
        ByteField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, CFE_EVS_SET_LOG_MODE_CmdPkt, pkttype=1, apid=1, cmd_func_code=19)


class CFE_EVS_CLEAR_LOG_CmdPkt(Packet):
    """Clears the contents of the local event log.

    app = CFE_EVS
    command = CLEAR_LOG
    msg_id = CFE_EVS_CMD_MID = 0x1801 = 0x1800 + 0x001
    cmd_func_code = 20
    data_len = 0 bytes
    """
    name = "CFE_EVS_CLEAR_LOG_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_EVS_CLEAR_LOG_CmdPkt, pkttype=1, apid=1, cmd_func_code=20)
