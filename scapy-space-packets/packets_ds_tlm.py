from scapy.all import *
from ccsds_base import CCSDSPacket


class DS_HK_TLM_PKT_TlmPkt(Packet):
    """DS application housekeeping packet

    app = DS
    command = HK_TLM_PKT
    msg_id = DS_HK_TLM_MID = 0x08b8 = 0x0800 + 0x0b8
    """
    name = "DS_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT       8   UINT "Count of valid commands received"
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT       8   UINT "Count of invalid commands received"
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM DEST_TBL_LOAD_CTR     8   UINT "Count of destination file table loads"
        ByteField("DEST_TBL_LOAD_CTR", 0),
        # APPEND_ITEM DEST_TBL_ERR_CTR      8   UINT "Count of failed attempts to get table data pointer"
        ByteField("DEST_TBL_ERR_CTR", 0),
        # APPEND_ITEM FILTER_TBL_LOAD_CTR   8   UINT "Count of packet filter table loads"
        ByteField("FILTER_TBL_LOAD_CTR", 0),
        # APPEND_ITEM FILTER_TBL_ERR_CTR    8   UINT "Count of failed attempts to get table data pointer"
        ByteField("FILTER_TBL_ERR_CTR", 0),
        # APPEND_ITEM APP_ENA_STATE         8   UINT "Application enable/disable state"
        ByteField("APP_ENA_STATE", 0),
        # STATE DIS 0 Red
        # STATE ENA 1 Green
        # APPEND_ITEM SPARE8                8   UINT "Structure alignment padding"
        ByteField("SPARE8", 0),
        # APPEND_ITEM FILE_WRITE_CTR       16   UINT "Count of good destination file writes"
        ShortField("FILE_WRITE_CTR", 0),
        # APPEND_ITEM FILE_WRITE_ERR_CTR   16   UINT "Count of bad destination file writes"
        ShortField("FILE_WRITE_ERR_CTR", 0),
        # APPEND_ITEM FILE_UPDATE_CTR      16   UINT "Count of good updates to secondary header"
        ShortField("FILE_UPDATE_CTR", 0),
        # APPEND_ITEM FILE_UPDATE_ERR_CTR  16   UINT "Count of bad updates to secondary header"
        ShortField("FILE_UPDATE_ERR_CTR", 0),
        # APPEND_ITEM DIS_PKT_CTR          32   UINT "Count of packets discarded (DS was disabled)"
        IntField("DIS_PKT_CTR", 0),
        # APPEND_ITEM IGNORED_PKT_CTR      32   UINT "Count of packets discarded. Incoming packets will be discarded when:"
        IntField("IGNORED_PKT_CTR", 0),
        # APPEND_ITEM FILTERED_PKT_CTR     32   UINT "Count of packets discarded (failed filter test)"
        IntField("FILTERED_PKT_CTR", 0),
        # APPEND_ITEM PASSED_PKT_CTR       32   UINT "Count of packets that passed filter test"
        IntField("PASSED_PKT_CTR", 0),
        # APPEND_ITEM FILTER_TBL_FILENAME  512 STRING "Name of filter table file"
        StrFixedLenField("FILTER_TBL_FILENAME", b"", 64),
    ]


bind_layers(CCSDSPacket, DS_HK_TLM_PKT_TlmPkt, pkttype=0, apid=184)


# TELEMETRY DS FILE_INFO_PKT BIG_ENDIAN "DS application file info packet"
#   TLMHDR DS_DIAG_TLM_MID
#   <%
#     append_items = ""
#     num_files = Osk::Cfg.get_fsw_cfg_int_param(@APP_PREFIX_STR, @DS_DEST_FILE_CNT)
#     for i in 1..num_files
#       append_items << "APPEND_ITEM FILE#{i}_AGE     32   UINT \"File age in seconds\"" << "\n"
#       append_items << "APPEND_ITEM FILE#{i}_SIZE    32   UINT \"File size in bytes\"" << "\n"
#       append_items << "APPEND_ITEM FILE#{i}_RATE    32   UINT \"Average data rate since HK\"" << "\n"
#       append_items << "APPEND_ITEM FILE#{i}_SEQ_CNT 32   UINT \"Sequence count portion of filename\"" << "\n"
#       append_items << "APPEND_ITEM FILE#{i}_ENABLE  16   UINT \"File op state: 0=Disabled, 1=Enabled\"" << "\n"
#       append_items << "APPEND_ITEM FILE#{i}_OPEN    16   UINT \"0=Closed, 1=Open\"" << "\n"
#       append_items << "APPEND_ITEM FILE#{i}_NAME   512 STRING \"Name of filter table file\"" << "\n"
#     end
#   %>
#   <%= append_items %>
