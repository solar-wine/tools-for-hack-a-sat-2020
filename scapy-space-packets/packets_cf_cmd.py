from scapy.all import *
from ccsds_base import CCSDSPacket


class CF_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = CF
    command = NOOP
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "CF_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CF_NOOP_CmdPkt, pkttype=1, apid=179, cmd_func_code=0)


class CF_RESET_CTRS_CmdPkt(Packet):
    """Resets HK TLM parent and child task counters

    app = CF
    command = RESET_CTRS
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 1
    data_len = 4 bytes
    """
    name = "CF_RESET_CTRS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER VALUE 8 UINT MIN_UINT8 MAX_UINT8 0 "0=all, 1=cmd, 2=fault 3=up 4=down"
        ByteField("VALUE", 0),
        # APPEND_PARAMETER SPARE_1    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_1", 0),
        # APPEND_PARAMETER SPARE_2    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_2", 0),
        # APPEND_PARAMETER SPARE_3    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_3", 0),
    ]


bind_layers(CCSDSPacket, CF_RESET_CTRS_CmdPkt, pkttype=1, apid=179, cmd_func_code=1)


class CF_PLAYBACK_FILE_CmdPkt(Packet):
    """Put the specified file in the playback queue

    app = CF
    command = PLAYBACK_FILE
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 2
    data_len = 148 bytes
    """
    name = "CF_PLAYBACK_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CLASS           8 UINT MIN_UINT8 MAX_UINT8 1 "Class_1(1), Class_2(2)"
        ByteField("CLASS", 1),
        # APPEND_PARAMETER CHANNEL         8 UINT MIN_UINT8 MAX_UINT8 0 "Chan_0(0), Chan_1(1)"
        ByteField("CHANNEL", 0),
        # APPEND_PARAMETER PRIORITY        8 UINT MIN_UINT8 MAX_UINT8 0 "Priority – 00 (highest priority) – 0xff (lowest priority)"
        ByteField("PRIORITY", 0),
        # APPEND_PARAMETER PRESERVE        8 UINT MIN_UINT8 MAX_UINT8 1 "Delete_File(0), Keep_File(1)"
        ByteField("PRESERVE", 1),
        # APPEND_PARAMETER PEER_ID       128 STRING "0.21" "Entity ID of ground engine to receive file (ex 0.23)"
        StrFixedLenField("PEER_ID", b"0.21", 16),
        # APPEND_PARAMETER SRC_FILENAME  512 STRING "/cf/cf_test.txt"  "Complete target /path/filename"
        StrFixedLenField("SRC_FILENAME", b"/cf/cf_test.txt", 64),
        # APPEND_PARAMETER DEST_FILENAME 512 STRING "cosmos/cfs_kit/file_server/osk_tmp.txt" "Complete target /path/filename"
        StrFixedLenField("DEST_FILENAME", b"cosmos/cfs_kit/file_server/osk_tmp.txt", 64),
    ]


bind_layers(CCSDSPacket, CF_PLAYBACK_FILE_CmdPkt, pkttype=1, apid=179, cmd_func_code=2)


class CF_PLAYBACK_DIR_CmdPkt(Packet):
    """Put all of the files in the specified directory in the playback queue

    app = CF
    command = PLAYBACK_DIR
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 3
    data_len = 148 bytes
    """
    name = "CF_PLAYBACK_DIR_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CLASS           8 UINT MIN_UINT8 MAX_UINT8 1 "Class_1(1), Class_2(2)"
        ByteField("CLASS", 1),
        # APPEND_PARAMETER CHANNEL         8 UINT MIN_UINT8 MAX_UINT8 0 "Chan_0(0), Chan_1(1)"
        ByteField("CHANNEL", 0),
        # APPEND_PARAMETER PRIORITY        8 UINT MIN_UINT8 MAX_UINT8 0 "Priority – 00 (highest priority) – 0xff (lowest priority)"
        ByteField("PRIORITY", 0),
        # APPEND_PARAMETER PRESERVE        8 UINT MIN_UINT8 MAX_UINT8 0 "Delete_File(0), Keep_File(1)"
        ByteField("PRESERVE", 0),
        # APPEND_PARAMETER PEER_ID       128 STRING "0.21" "Entity ID of ground engine to receive file (ex 0.23)"
        StrFixedLenField("PEER_ID", b"0.21", 16),
        # APPEND_PARAMETER SRC_FILENAME  512 STRING "osk_tmp_bin.dat"   "Complete target /path/filename"
        StrFixedLenField("SRC_FILENAME", b"osk_tmp_bin.dat", 64),
        # APPEND_PARAMETER DEST_FILENAME 512 STRING "osk_tmp_bin.dat"   "Complete target /path/filename"
        StrFixedLenField("DEST_FILENAME", b"osk_tmp_bin.dat", 64),
    ]


bind_layers(CCSDSPacket, CF_PLAYBACK_DIR_CmdPkt, pkttype=1, apid=179, cmd_func_code=3)


class CF_SET_MIB_CmdPkt(Packet):
    """TODO

    app = CF
    command = SET_MIB
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 10
    data_len = 48 bytes
    """
    name = "CF_SET_MIB_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER PARAM  256 STRING "param"  "TODO"
        StrFixedLenField("PARAM", b"param", 32),
        # APPEND_PARAMETER VALUE  128 STRING "value"  "TODO"
        StrFixedLenField("VALUE", b"value", 16),
    ]


bind_layers(CCSDSPacket, CF_SET_MIB_CmdPkt, pkttype=1, apid=179, cmd_func_code=10)


class CF_GET_MIB_CmdPkt(Packet):
    """TODO

    app = CF
    command = GET_MIB
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 11
    data_len = 32 bytes
    """
    name = "CF_GET_MIB_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER PARAM  256 STRING "param"  "TODO"
        StrFixedLenField("PARAM", b"param", 32),
    ]


bind_layers(CCSDSPacket, CF_GET_MIB_CmdPkt, pkttype=1, apid=179, cmd_func_code=11)


class CF_SEND_TRANS_DIAG_DATA_CmdPkt(Packet):
    """Create/send diagnostic data on a particular transaction.

    app = CF
    command = SEND_TRANS_DIAG_DATA
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 12
    data_len = 64 bytes
    """
    name = "CF_SEND_TRANS_DIAG_DATA_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TRANS 512 STRING "default" "Transaction ID (0.24_4) or Filename (/path/filename) of the transaction to suspend"
        StrFixedLenField("TRANS", b"default", 64),
    ]


bind_layers(CCSDSPacket, CF_SEND_TRANS_DIAG_DATA_CmdPkt, pkttype=1, apid=179, cmd_func_code=12)


class CF_SEND_CFG_PARAMS_CmdPkt(Packet):
    """Create/send a configuration telemetry packet

    app = CF
    command = SEND_CFG_PARAMS
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 14
    data_len = 0 bytes
    """
    name = "CF_SEND_CFG_PARAMS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, CF_SEND_CFG_PARAMS_CmdPkt, pkttype=1, apid=179, cmd_func_code=14)


class CF_WRITE_QUEUE_INFO_CmdPkt(Packet):
    """TODO

    app = CF
    command = WRITE_QUEUE_INFO
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 15
    data_len = 68 bytes
    """
    name = "CF_WRITE_QUEUE_INFO_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TYPE       8 UINT MIN_UINT8 MAX_UINT8 1 "1=Up, 2=Down"
        ByteField("TYPE", 1),
        # APPEND_PARAMETER CHANNEL    8 UINT MIN_UINT8 MAX_UINT8 0 "Chan_0(0), Chan_1(1)"
        ByteField("CHANNEL", 0),
        # APPEND_PARAMETER QUEUE      8 UINT MIN_UINT8 MAX_UINT8 0 "0=pending, 1=active, 2=history"
        ByteField("QUEUE", 0),
        # APPEND_PARAMETER SPARE      8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE", 0),
        # APPEND_PARAMETER FILENAME 512 STRING "osk_tmp_bin.dat"   "Complete target /path/filename"
        StrFixedLenField("FILENAME", b"osk_tmp_bin.dat", 64),
    ]


bind_layers(CCSDSPacket, CF_WRITE_QUEUE_INFO_CmdPkt, pkttype=1, apid=179, cmd_func_code=15)


class CF_ENA_DEQUEUE_CmdPkt(Packet):
    """TODO

    app = CF
    command = ENA_DEQUEUE
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 16
    data_len = 4 bytes
    """
    name = "CF_ENA_DEQUEUE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CHANNEL    8 UINT MIN_UINT8 MAX_UINT8 0 "Chan_0(0), Chan_1(1)"
        ByteField("CHANNEL", 0),
        # APPEND_PARAMETER SPARE_1    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_1", 0),
        # APPEND_PARAMETER SPARE_2    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_2", 0),
        # APPEND_PARAMETER SPARE_3    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_3", 0),
    ]


bind_layers(CCSDSPacket, CF_ENA_DEQUEUE_CmdPkt, pkttype=1, apid=179, cmd_func_code=16)


class CF_DIS_DEQUEUE_CmdPkt(Packet):
    """TODO

    app = CF
    command = DIS_DEQUEUE
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 17
    data_len = 4 bytes
    """
    name = "CF_DIS_DEQUEUE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CHANNEL    8 UINT MIN_UINT8 MAX_UINT8 0 "Chan_0(0), Chan_1(1)"
        ByteField("CHANNEL", 0),
        # APPEND_PARAMETER SPARE_1    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_1", 0),
        # APPEND_PARAMETER SPARE_2    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_2", 0),
        # APPEND_PARAMETER SPARE_3    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_3", 0),
    ]


bind_layers(CCSDSPacket, CF_DIS_DEQUEUE_CmdPkt, pkttype=1, apid=179, cmd_func_code=17)


class CF_ENA_DIR_POLLING_CmdPkt(Packet):
    """TODO

    app = CF
    command = ENA_DIR_POLLING
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 18
    data_len = 4 bytes
    """
    name = "CF_ENA_DIR_POLLING_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CHANNEL    8 UINT MIN_UINT8 MAX_UINT8 0 "Chan_0(0), Chan_1(1)"
        ByteField("CHANNEL", 0),
        # APPEND_PARAMETER DIR        8 UINT MIN_UINT8 MAX_UINT8 0 "TODO"
        ByteField("DIR", 0),
        # APPEND_PARAMETER SPARE_1    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_1", 0),
        # APPEND_PARAMETER SPARE_2    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_2", 0),
    ]


bind_layers(CCSDSPacket, CF_ENA_DIR_POLLING_CmdPkt, pkttype=1, apid=179, cmd_func_code=18)


class CF_DIS_DIR_POLLING_CmdPkt(Packet):
    """TODO

    app = CF
    command = DIS_DIR_POLLING
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 19
    data_len = 4 bytes
    """
    name = "CF_DIS_DIR_POLLING_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CHANNEL    8 UINT MIN_UINT8 MAX_UINT8 0 "Chan_0(0), Chan_1(1)"
        ByteField("CHANNEL", 0),
        # APPEND_PARAMETER DIR        8 UINT MIN_UINT8 MAX_UINT8 0 "TODO"
        ByteField("DIR", 0),
        # APPEND_PARAMETER SPARE_1    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_1", 0),
        # APPEND_PARAMETER SPARE_2    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_2", 0),
    ]


bind_layers(CCSDSPacket, CF_DIS_DIR_POLLING_CmdPkt, pkttype=1, apid=179, cmd_func_code=19)


class CF_PURGE_QUEUE_CmdPkt(Packet):
    """TODO

    app = CF
    command = PURGE_QUEUE
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 21
    data_len = 4 bytes
    """
    name = "CF_PURGE_QUEUE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TYPE       8 UINT MIN_UINT8 MAX_UINT8 1 "1=Up, 2=Down"
        ByteField("TYPE", 1),
        # APPEND_PARAMETER CHANNEL    8 UINT MIN_UINT8 MAX_UINT8 0 "Chan_0(0), Chan_1(1)"
        ByteField("CHANNEL", 0),
        # APPEND_PARAMETER QUEUE      8 UINT MIN_UINT8 MAX_UINT8 0 "0=pending, 1=active, 2=history"
        ByteField("QUEUE", 0),
        # APPEND_PARAMETER SPARE      8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, CF_PURGE_QUEUE_CmdPkt, pkttype=1, apid=179, cmd_func_code=21)


class CF_WRITE_ACTIVE_TRANS_CmdPkt(Packet):
    """Create/send an active transaction telemetry packet

    app = CF
    command = WRITE_ACTIVE_TRANS
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 22
    data_len = 66 bytes
    """
    name = "CF_WRITE_ACTIVE_TRANS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TYPE     8 UINT MIN_UINT8 MAX_UINT8 0 "all(0), incoming(1), outgoing(2)"
        ByteField("TYPE", 0),
        # APPEND_PARAMETER SPARE    8 UINT MIN_UINT8 MAX_UINT8 0 "one byte field"
        ByteField("SPARE", 0),
        # APPEND_PARAMETER DEST   512 STRING "osk_tmp_bin.dat"  "Complete target /path/filename"
        StrFixedLenField("DEST", b"osk_tmp_bin.dat", 64),
    ]


bind_layers(CCSDSPacket, CF_WRITE_ACTIVE_TRANS_CmdPkt, pkttype=1, apid=179, cmd_func_code=22)


class CF_KICK_START_CmdPkt(Packet):
    """TODO

    app = CF
    command = KICK_START
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 23
    data_len = 4 bytes
    """
    name = "CF_KICK_START_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER CHANNEL    8 UINT MIN_UINT8 MAX_UINT8 0 "Chan_0(0), Chan_1(1)"
        ByteField("CHANNEL", 0),
        # APPEND_PARAMETER SPARE_1    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_1", 0),
        # APPEND_PARAMETER SPARE_2    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_2", 0),
        # APPEND_PARAMETER SPARE_3    8 UINT MIN_UINT8 MAX_UINT8 0 ""
        ByteField("SPARE_3", 0),
    ]


bind_layers(CCSDSPacket, CF_KICK_START_CmdPkt, pkttype=1, apid=179, cmd_func_code=23)


class CF_QUICK_STAT_CmdPkt(Packet):
    """Send an event message containing status of teh specified transaction

    app = CF
    command = QUICK_STAT
    msg_id = CF_CMD_MID = 0x18b3 = 0x1800 + 0x0b3
    cmd_func_code = 24
    data_len = 64 bytes
    """
    name = "CF_QUICK_STAT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TRANS   512 STRING "osk_tmp_bin.dat"  "Complete target /path/filename"
        StrFixedLenField("TRANS", b"osk_tmp_bin.dat", 64),
    ]


bind_layers(CCSDSPacket, CF_QUICK_STAT_CmdPkt, pkttype=1, apid=179, cmd_func_code=24)
