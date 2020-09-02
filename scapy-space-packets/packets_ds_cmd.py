from scapy.all import *
from ccsds_base import CCSDSPacket


class DS_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = DS
    command = NOOP
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "DS_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, DS_NOOP_CmdPkt, pkttype=1, apid=187, cmd_func_code=0)


class DS_RESET_CTRS_CmdPkt(Packet):
    """Reset counters

    app = DS
    command = RESET_CTRS
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "DS_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, DS_RESET_CTRS_CmdPkt, pkttype=1, apid=187, cmd_func_code=1)


class DS_SET_APP_STATE_CmdPkt(Packet):
    """Enable/Disable the DS application packet storing

    app = DS
    command = SET_APP_STATE
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 2
    data_len = 2 bytes
    """
    name = "DS_SET_APP_STATE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER APP_STATE 16 UINT MIN_UINT16 MAX_UINT16 1 "0=Disable, 1=Enable packet storing"
        ShortField("APP_STATE", 1),
    ]


bind_layers(CCSDSPacket, DS_SET_APP_STATE_CmdPkt, pkttype=1, apid=187, cmd_func_code=2)


class DS_SET_FILTER_FILE_CmdPkt(Packet):
    """Modify the Destination File selection for the commanded entry in the Packet Filter Table.

    app = DS
    command = SET_FILTER_FILE
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 3
    data_len = 6 bytes
    """
    name = "DS_SET_FILTER_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MSG_ID           16 UINT MIN_UINT16 MAX_UINT16 0 "Message ID of existing entry in Packet Filter Table"
        ShortField("MSG_ID", 0),
        # APPEND_PARAMETER FILTER_PARAM_IDX 16 UINT MIN_UINT16 MAX_UINT16 0 "Index into Filter Parmeter Array"
        ShortField("FILTER_PARAM_IDX", 0),
        # APPEND_PARAMETER FILE_TBL_IDX     16 UINT MIN_UINT16 MAX_UINT16 0 "Index into Destination File Table"
        ShortField("FILE_TBL_IDX", 0),
    ]


bind_layers(CCSDSPacket, DS_SET_FILTER_FILE_CmdPkt, pkttype=1, apid=187, cmd_func_code=3)


class DS_SET_FILTER_TYPE_CmdPkt(Packet):
    """Modify the Filter Type (pkt count or time) for the commanded entry in the Packet Filter Table.

    app = DS
    command = SET_FILTER_TYPE
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 4
    data_len = 6 bytes
    """
    name = "DS_SET_FILTER_TYPE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MSG_ID           16 UINT MIN_UINT16 MAX_UINT16 0 "Message ID of existing entry in Packet Filter Table."
        ShortField("MSG_ID", 0),
        # APPEND_PARAMETER FILTER_PARAM_IDX 16 UINT MIN_UINT16 MAX_UINT16 0 "Index into Filter Parameter Array"
        ShortField("FILTER_PARAM_IDX", 0),
        # APPEND_PARAMETER FILTER_TYPE      16 UINT MIN_UINT16 MAX_UINT16 0 "Filter type (packet sequence count or time)."
        ShortField("FILTER_TYPE", 0),
    ]


bind_layers(CCSDSPacket, DS_SET_FILTER_TYPE_CmdPkt, pkttype=1, apid=187, cmd_func_code=4)


class DS_SET_FILTER_PARAM_CmdPkt(Packet):
    """Modify the Algorithm Parameters for the commanded entry in the Packet Filter Table. N of X messages will be stored starting at offset O

    app = DS
    command = SET_FILTER_PARAM
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 5
    data_len = 10 bytes
    """
    name = "DS_SET_FILTER_PARAM_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MSG_ID           16 UINT MIN_UINT16 MAX_UINT16 0 "Message ID of existing entry in Packet Filter Table."
        ShortField("MSG_ID", 0),
        # APPEND_PARAMETER FILTER_PARAM_IDX 16 UINT MIN_UINT16 MAX_UINT16 0 "Index into Filter Parameter Array"
        ShortField("FILTER_PARAM_IDX", 0),
        # APPEND_PARAMETER Algorithm_N      16 UINT MIN_UINT16 MAX_UINT16 0 "Algorithm value N (pass this many)"
        ShortField("Algorithm_N", 0),
        # APPEND_PARAMETER Algorithm_X      16 UINT MIN_UINT16 MAX_UINT16 0 "Algorithm value X (out of this many)"
        ShortField("Algorithm_X", 0),
        # APPEND_PARAMETER Algorithm_O      16 UINT MIN_UINT16 MAX_UINT16 0 "Algorithm value O (at this offset)"
        ShortField("Algorithm_O", 0),
    ]


bind_layers(CCSDSPacket, DS_SET_FILTER_PARAM_CmdPkt, pkttype=1, apid=187, cmd_func_code=5)


class DS_SET_FILE_TYPE_CmdPkt(Packet):
    """Set file name to use sequence count or time in the name for commanded entry in the Destination File Table.

    app = DS
    command = SET_FILE_TYPE
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 6
    data_len = 4 bytes
    """
    name = "DS_SET_FILE_TYPE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILE_TBL_IDX  16 UINT MIN_UINT16 MAX_UINT16 0 "Index into Destination File Table"
        ShortField("FILE_TBL_IDX", 0),
        # APPEND_PARAMETER FILENAME_TYPE 16 UINT MIN_UINT16 MAX_UINT16 0 "1=Count, 2=Time"
        ShortField("FILENAME_TYPE", 0),
    ]


bind_layers(CCSDSPacket, DS_SET_FILE_TYPE_CmdPkt, pkttype=1, apid=187, cmd_func_code=6)


class DS_SET_FILE_STATE_CmdPkt(Packet):
    """Default to enable for the indicated entry in the Destination File Table.

    app = DS
    command = SET_FILE_STATE
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 7
    data_len = 4 bytes
    """
    name = "DS_SET_FILE_STATE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILE_TBL_IDX 16 UINT MIN_UINT16 MAX_UINT16 0 "Index into Destination File Table"
        ShortField("FILE_TBL_IDX", 0),
        # APPEND_PARAMETER FILE_STATE   16 UINT MIN_UINT16 MAX_UINT16 1 "0=Disable, 1=Enable destination storage file"
        ShortField("FILE_STATE", 1),
    ]


bind_layers(CCSDSPacket, DS_SET_FILE_STATE_CmdPkt, pkttype=1, apid=187, cmd_func_code=7)


class DS_SET_FILE_PATH_NAME_CmdPkt(Packet):
    """Modify the Pathname portion of the filename for the commanded entry in the Destination File Table.

    app = DS
    command = SET_FILE_PATH_NAME
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 8
    data_len = 68 bytes
    """
    name = "DS_SET_FILE_PATH_NAME_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILE_TBL_IDX 32 UINT MIN_UINT32 MAX_UINT32 0 "Index into Destination File Table"
        IntField("FILE_TBL_IDX", 0),
        # APPEND_PARAMETER PATH_NAME    512 STRING "default" "Path name portion of filename."
        StrFixedLenField("PATH_NAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, DS_SET_FILE_PATH_NAME_CmdPkt, pkttype=1, apid=187, cmd_func_code=8)


class DS_SET_FILE_BASE_NAME_CmdPkt(Packet):
    """Modify the Basename portion of the filename for the commanded entry in the Destination File Table.

    app = DS
    command = SET_FILE_BASE_NAME
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 9
    data_len = 68 bytes
    """
    name = "DS_SET_FILE_BASE_NAME_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILE_TBL_IDX 32 UINT MIN_UINT32 MAX_UINT32 0 "Index into Destination File Table"
        IntField("FILE_TBL_IDX", 0),
        # APPEND_PARAMETER BASE_NAME    512 STRING "default" "Base name portion of filename"
        StrFixedLenField("BASE_NAME", b"default", 64),
    ]


bind_layers(CCSDSPacket, DS_SET_FILE_BASE_NAME_CmdPkt, pkttype=1, apid=187, cmd_func_code=9)


class DS_SET_FILE_EXT_CmdPkt(Packet):
    """Modify the Extension portion of the filename for the indicated entry in the Destination File Table.

    app = DS
    command = SET_FILE_EXT
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 10
    data_len = 12 bytes
    """
    name = "DS_SET_FILE_EXT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILE_TBL_IDX 32 UINT MIN_UINT32 MAX_UINT32 0 "Index into Destination File Table"
        IntField("FILE_TBL_IDX", 0),
        # APPEND_PARAMETER EXTENSION    64 STRING "default" "Extension portion of filename"
        StrFixedLenField("EXTENSION", b"default", 8),
    ]


bind_layers(CCSDSPacket, DS_SET_FILE_EXT_CmdPkt, pkttype=1, apid=187, cmd_func_code=10)


class DS_SET_FILE_MAX_SIZE_CmdPkt(Packet):
    """Modify the max file size for the commanded entry in the Destination File Table.

    app = DS
    command = SET_FILE_MAX_SIZE
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 11
    data_len = 8 bytes
    """
    name = "DS_SET_FILE_MAX_SIZE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILE_TBL_IDX  32 UINT MIN_UINT32 MAX_UINT32 0 "Index into Destination File Table."
        IntField("FILE_TBL_IDX", 0),
        # APPEND_PARAMETER MAX_FILE_SIZE 32 UINT MIN_UINT32 MAX_UINT32 0 "Max file size (bytes) before re-open"
        IntField("MAX_FILE_SIZE", 0),
    ]


bind_layers(CCSDSPacket, DS_SET_FILE_MAX_SIZE_CmdPkt, pkttype=1, apid=187, cmd_func_code=11)


class DS_SET_FILE_MAX_AGE_CmdPkt(Packet):
    """Modify the max file age for the commanded entry in the Destination File Table.

    app = DS
    command = SET_FILE_MAX_AGE
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 12
    data_len = 8 bytes
    """
    name = "DS_SET_FILE_MAX_AGE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILE_TBL_IDX 32 UINT MIN_UINT32 MAX_UINT32 0 "Index into Destination File Table."
        IntField("FILE_TBL_IDX", 0),
        # APPEND_PARAMETER MAX_FILE_AGE 32 UINT MIN_UINT32 MAX_UINT32 0 "Max file age (seconds) before re-open"
        IntField("MAX_FILE_AGE", 0),
    ]


bind_layers(CCSDSPacket, DS_SET_FILE_MAX_AGE_CmdPkt, pkttype=1, apid=187, cmd_func_code=12)


class DS_SET_FILE_COUNT_CmdPkt(Packet):
    """Set the sequence count value for the commanded entry in the Destination File Table

    app = DS
    command = SET_FILE_COUNT
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 13
    data_len = 8 bytes
    """
    name = "DS_SET_FILE_COUNT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILE_TBL_IDX 32 UINT MIN_UINT32 MAX_UINT32 0 "Index into Destination File Table"
        IntField("FILE_TBL_IDX", 0),
        # APPEND_PARAMETER SEQUENCE_CNT 32 UINT MIN_UINT32 MAX_UINT32 0 "Sequence count portion of filename"
        IntField("SEQUENCE_CNT", 0),
    ]


bind_layers(CCSDSPacket, DS_SET_FILE_COUNT_CmdPkt, pkttype=1, apid=187, cmd_func_code=13)


class DS_CLOSE_FILE_CmdPkt(Packet):
    """Close the commanded Destination File.

    app = DS
    command = CLOSE_FILE
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 14
    data_len = 4 bytes
    """
    name = "DS_CLOSE_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILE_TBL_IDX 32 UINT MIN_UINT32 MAX_UINT32 0 "Index into Destination File Table"
        IntField("FILE_TBL_IDX", 0),
    ]


bind_layers(CCSDSPacket, DS_CLOSE_FILE_CmdPkt, pkttype=1, apid=187, cmd_func_code=14)


class DS_SEND_FILE_INFO_CmdPkt(Packet):
    """Send the DS File Info Packet.

    app = DS
    command = SEND_FILE_INFO
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 15
    data_len = 0 bytes
    """
    name = "DS_SEND_FILE_INFO_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, DS_SEND_FILE_INFO_CmdPkt, pkttype=1, apid=187, cmd_func_code=15)


class DS_ADD_FILTER_MID_CmdPkt(Packet):
    """Insert the commanded Message ID to an unused Packet Filter Table entry

    app = DS
    command = ADD_FILTER_MID
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 16
    data_len = 2 bytes
    """
    name = "DS_ADD_FILTER_MID_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MSG_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "Message ID to add to Packet Filter Table"
        ShortField("MSG_ID", 0),
    ]


bind_layers(CCSDSPacket, DS_ADD_FILTER_MID_CmdPkt, pkttype=1, apid=187, cmd_func_code=16)


class DS_CLOSE_ALL_CmdPkt(Packet):
    """Close all open Destination Files. NOTE: Using this command may incur a performance hit based upon the number and size of the files being closed.

    app = DS
    command = CLOSE_ALL
    msg_id = DS_CMD_MID = 0x18bb = 0x1800 + 0x0bb
    cmd_func_code = 17
    data_len = 0 bytes
    """
    name = "DS_CLOSE_ALL_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, DS_CLOSE_ALL_CmdPkt, pkttype=1, apid=187, cmd_func_code=17)
