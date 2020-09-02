from scapy.all import *
from ccsds_base import CCSDSPacket


class HK_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = HK
    command = NOOP
    msg_id = HK_CMD_MID = 0x189a = 0x1800 + 0x09a
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "HK_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HK_NOOP_CmdPkt, pkttype=1, apid=154, cmd_func_code=0)


class HK_RESET_CTRS_CmdPkt(Packet):
    """Resets HK TLM counters

    app = HK
    command = RESET_CTRS
    msg_id = HK_CMD_MID = 0x189a = 0x1800 + 0x09a
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "HK_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, HK_RESET_CTRS_CmdPkt, pkttype=1, apid=154, cmd_func_code=1)
