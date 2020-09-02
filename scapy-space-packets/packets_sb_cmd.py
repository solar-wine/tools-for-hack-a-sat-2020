from scapy.all import *
from ccsds_base import CCSDSPacket


class CFE_SB_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = CFE_SB
    command = NOOP
    msg_id = CFE_SB_CMD_MID = 0x1803 = 0x1800 + 0x003
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "CFE_SB_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_SB_NOOP_CmdPkt, pkttype=1, apid=3, cmd_func_code=0)


class CFE_SB_RESET_CTRS_CmdPkt(Packet):
    """Reset command counters

    app = CFE_SB
    command = RESET_CTRS
    msg_id = CFE_SB_CMD_MID = 0x1803 = 0x1800 + 0x003
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "CFE_SB_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_SB_RESET_CTRS_CmdPkt, pkttype=1, apid=3, cmd_func_code=1)


class CFE_SB_SEND_STATS_CmdPkt(Packet):
    """Send a statistics packet containing current utilization figures and high water marks which may be useful for checking the margin of the SB platform configuration settings.

    app = CFE_SB
    command = SEND_STATS
    msg_id = CFE_SB_CMD_MID = 0x1803 = 0x1800 + 0x003
    cmd_func_code = 2
    data_len = 0 bytes
    """
    name = "CFE_SB_SEND_STATS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_SB_SEND_STATS_CmdPkt, pkttype=1, apid=3, cmd_func_code=2)


class SB_WRITE_ROUTING_TO_FILE_CmdPkt(Packet):
    """Create a file containing the software bus routing information. The routing information contains information about every subscription that has been received through the SB subscription APIs. An abosulte path and filename may be specified in the command. If this command field contains an empty string (NULL terminator as the first character) the default file path and name is used. The default file path and name is defined in the platform configuration file as CFE_SB_DEFAULT_ROUTING_FILENAME.

    app = SB
    command = WRITE_ROUTING_TO_FILE
    msg_id = CFE_SB_CMD_MID = 0x1803 = 0x1800 + 0x003
    cmd_func_code = 3
    data_len = 64 bytes
    """
    name = "SB_WRITE_ROUTING_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/cfe_sb_route.dat" "Path and Filename of data to be loaded."
        StrFixedLenField("FILENAME", b"/cf/cfe_sb_route.dat", 64),
    ]


bind_layers(CCSDSPacket, SB_WRITE_ROUTING_TO_FILE_CmdPkt, pkttype=1, apid=3, cmd_func_code=3)


class CFE_SB_ENA_ROUTE_CmdPkt(Packet):
    """This command will enable a particular destination. The destination is specified in terms of MsgID and PipeID. The MsgId and PipeID are parmaters in the command. All destinations are enabled by default. This command is needed only after a CFE_SB_DISABLE_ROUTE_CC command is used.

    app = CFE_SB
    command = ENA_ROUTE
    msg_id = CFE_SB_CMD_MID = 0x1803 = 0x1800 + 0x003
    cmd_func_code = 4
    data_len = 0 bytes
    """
    name = "CFE_SB_ENA_ROUTE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MSG_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "Message ID of route to be enabled or disabled CFE_SB_MsgId_t."
        ShortField("MSG_ID", 0),
        # APPEND_PARAMETER PIPE    8 UINT MIN_UINT8  MAX_UINT8  0 "Pipe ID of route to be enabled or disabled CFE_SB_PipeId_t."
        ByteField("PIPE", 0),
        # APPEND_PARAMETER SPARE   8 UINT MIN_UINT8  MAX_UINT8  0 "Spare byte to make command even number of bytes."
        ByteField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, CFE_SB_ENA_ROUTE_CmdPkt, pkttype=1, apid=3, cmd_func_code=4)


class CFE_SB_DIS_ROUTE_CmdPkt(Packet):
    """This command will disable a particular destination. The destination is specified in terms of MsgID and PipeID. The MsgId and PipeID are parmaters in the command. All destinations are enabled by default.

    app = CFE_SB
    command = DIS_ROUTE
    msg_id = CFE_SB_CMD_MID = 0x1803 = 0x1800 + 0x003
    cmd_func_code = 5
    data_len = 4 bytes
    """
    name = "CFE_SB_DIS_ROUTE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER MSG_ID 16 UINT MIN_UINT16 MAX_UINT16 0 "Message ID of route to be enabled or disabled CFE_SB_MsgId_t."
        ShortField("MSG_ID", 0),
        # APPEND_PARAMETER PIPE    8 UINT MIN_UINT8  MAX_UINT8  0 "Pipe ID of route to be enabled or disabled CFE_SB_PipeId_t."
        ByteField("PIPE", 0),
        # APPEND_PARAMETER SPARE   8 UINT MIN_UINT8  MAX_UINT8  0 "Spare byte to make command even number of bytes."
        ByteField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, CFE_SB_DIS_ROUTE_CmdPkt, pkttype=1, apid=3, cmd_func_code=5)


class CFE_SB_WRITE_PIPE_TO_FILE_CmdPkt(Packet):
    """This command will create a file containing the software bus pipe information. The pipe information contains information about every pipe that has been created through the CFE_SB_CreatePipe API. An abosulte path and filename may be specified in the command. If this command field contains an empty string (NULL terminator as the first character) the default file path and name is used. The default file path and name is defined in the platform configuration file as CFE_SB_DEFAULT_PIPE_FILENAME.

    app = CFE_SB
    command = WRITE_PIPE_TO_FILE
    msg_id = CFE_SB_CMD_MID = 0x1803 = 0x1800 + 0x003
    cmd_func_code = 7
    data_len = 64 bytes
    """
    name = "CFE_SB_WRITE_PIPE_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/cfe_sb_pipe.dat" "Path and Filename of data to be loaded."
        StrFixedLenField("FILENAME", b"/cf/cfe_sb_pipe.dat", 64),
    ]


bind_layers(CCSDSPacket, CFE_SB_WRITE_PIPE_TO_FILE_CmdPkt, pkttype=1, apid=3, cmd_func_code=7)


class CFE_SB_WRITE_MAP_TO_FILE_CmdPkt(Packet):
    """map information. The message map is a lookup table (an array of uint16s)that allows fast access to the correct routing table element during a softeware bus send operation. This is diasgnostic information that may be needed due to the dynamic nature of the cFE software bus. An abosulte path and filename may be specified in the command. If this command field contains an empty string (NULL terminator as the first character) the default file path and name is used. The default file path and name is defined in the platform configuration file as CFE_SB_DEFAULT_MAP_FILENAME.

    app = CFE_SB
    command = WRITE_MAP_TO_FILE
    msg_id = CFE_SB_CMD_MID = 0x1803 = 0x1800 + 0x003
    cmd_func_code = 8
    data_len = 64 bytes
    """
    name = "CFE_SB_WRITE_MAP_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "/cf/cfe_sb_msgmap.dat" "Path and Filename to recieve data"
        StrFixedLenField("FILENAME", b"/cf/cfe_sb_msgmap.dat", 64),
    ]


bind_layers(CCSDSPacket, CFE_SB_WRITE_MAP_TO_FILE_CmdPkt, pkttype=1, apid=3, cmd_func_code=8)


class CFE_SB_ENA_SUB_REPORTING_CmdPkt(Packet):
    """be used only by the CFS SBN (Software Bus Networking) Application. It is not intended to be sent from the ground or used by operations. When subscription reporting is enabled, SB will generate and send a software bus packet for each subscription received. The software bus packet that is sent contains the information received in the subscription API. This subscription report is neeeded by SBN if offboard routing is required.

    app = CFE_SB
    command = ENA_SUB_REPORTING
    msg_id = CFE_SB_CMD_MID = 0x1803 = 0x1800 + 0x003
    cmd_func_code = 9
    data_len = 0 bytes
    """
    name = "CFE_SB_ENA_SUB_REPORTING_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_SB_ENA_SUB_REPORTING_CmdPkt, pkttype=1, apid=3, cmd_func_code=9)


class CFE_SB_DIS_SUB_REPORTING_CmdPkt(Packet):
    """be used only by the CFS SBN (Software Bus Networking) Application. It is not intended to be sent from the ground or used by operations. When subscription reporting is enabled, SB will generate and send a software bus packet for each subscription received. The software bus packet that is sent contains the information received in the subscription API. This subscription report is neeeded by SBN if offboard routing is required.

    app = CFE_SB
    command = DIS_SUB_REPORTING
    msg_id = CFE_SB_CMD_MID = 0x1803 = 0x1800 + 0x003
    cmd_func_code = 10
    data_len = 0 bytes
    """
    name = "CFE_SB_DIS_SUB_REPORTING_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_SB_DIS_SUB_REPORTING_CmdPkt, pkttype=1, apid=3, cmd_func_code=10)


class CFE_SB_SEND_PREV_SUBS_CmdPkt(Packet):
    """regarding all subscriptions previously received by SB. This command is intended to be used only by the CFS SBN(Software Bus Networking) Application. It is not intended to be sent from the ground or used by operations. When this command is received the software bus will generate and send a series of packets containing information about all subscription previously received.

    app = CFE_SB
    command = SEND_PREV_SUBS
    msg_id = CFE_SB_CMD_MID = 0x1803 = 0x1800 + 0x003
    cmd_func_code = 11
    data_len = 0 bytes
    """
    name = "CFE_SB_SEND_PREV_SUBS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CFE_SB_SEND_PREV_SUBS_CmdPkt, pkttype=1, apid=3, cmd_func_code=11)
