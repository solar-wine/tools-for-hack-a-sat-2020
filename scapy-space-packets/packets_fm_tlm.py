from scapy.all import *
from ccsds_base import CCSDSPacket

# https://github.com/nasa/FM/blob/b3ea3d11d972b5b9e52d85ee15589630a0d76761/fsw/src/fm_defs.h
FILENAME_STATUS_ENUM = {
    0: "FM_NAME_IS_INVALID",
    1: "FM_NAME_IS_NOT_IN_USE",
    2: "FM_NAME_IS_FILE_OPEN",
    3: "FM_NAME_IS_FILE_CLOSED",
    4: "FM_NAME_IS_DIRECTORY",
}


class FM_HK_TLM_PKT_TlmPkt(Packet):
    """Housekeeping telemetry packet

    app = FM
    command = HK_TLM_PKT
    msg_id = FM_HK_TLM_MID = 0x088a = 0x0800 + 0x08a
    """
    name = "FM_HK_TLM_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM CMD_VALID_COUNT 8 UINT "Application command counter"
        ByteField("CMD_VALID_COUNT", 0),
        # APPEND_ITEM CMD_ERROR_COUNT 8 UINT "Application command error counter"
        ByteField("CMD_ERROR_COUNT", 0),
        # APPEND_ITEM SPARE              8 UINT "Placeholder for unused command warning counter"
        ByteField("SPARE", 0),
        # APPEND_ITEM NUM_OPEN_FILES     8 UINT "Number of open files in the system"
        ByteField("NUM_OPEN_FILES", 0),
        # APPEND_ITEM CHILD_CMD_CTR      8 UINT "Child task command counter"
        ByteField("CHILD_CMD_CTR", 0),
        # APPEND_ITEM CHILD_CMD_ERR_CTR  8 UINT "Child task command error counter"
        ByteField("CHILD_CMD_ERR_CTR", 0),
        # APPEND_ITEM CHILD_CMD_WARN_CTR 8 UINT "Child task command warning counter"
        ByteField("CHILD_CMD_WARN_CTR", 0),
        # APPEND_ITEM CHILD_QUEUE_CNT    8 UINT "Number of pending commands in queue"
        ByteField("CHILD_QUEUE_CNT", 0),
        # APPEND_ITEM CHILD_CURR_CC      8 UINT "Command code currently executing"
        ByteField("CHILD_CURR_CC", 0),
        # APPEND_ITEM CHILD_PREV_CC      8 UINT "Command code previously executed"
        ByteField("CHILD_PREV_CC", 0),
    ]


bind_layers(CCSDSPacket, FM_HK_TLM_PKT_TlmPkt, pkttype=0, apid=138)


class FM_FILE_INFO_PKT_TlmPkt(Packet):
    """Get File Info telemetry packet

    app = FM
    command = FILE_INFO_PKT
    msg_id = FM_FILE_INFO_TLM_MID = 0x088b = 0x0800 + 0x08b
    """
    name = "FM_FILE_INFO_PKT_TlmPkt"
    fields_desc = [
        # APPEND_ITEM OPEN_STATUS    8 UINT "Status indicating whether the file is open or closed"
        ByteEnumField("OPEN_STATUS", 0, FILENAME_STATUS_ENUM),
        # STATE FALSE   0
        # STATE TRUE    1
        # APPEND_ITEM COMPUTE_CRC    8 UINT "Boolean flag indictaing whether to compute a CRC"
        ByteField("COMPUTE_CRC", 0),
        # STATE FALSE   0
        # STATE TRUE    1
        # APPEND_ARRAY_ITEM SPARE    8 UINT 16 "Structure padding"
        StrFixedLenField("SPARE", b"", 2),  # FIXME: XNBytesField should be better, if supported
        # APPEND_ITEM CRC           32 UINT "CRC value if computed"
        IntField("CRC", 0),
        # APPEND_ITEM SIZE          32 UINT "Size in bytes"
        IntField("SIZE", 0),
        # APPEND_ITEM LAST_MOD_TIME 32 UINT "Last Modification Time of File"
        IntField("LAST_MOD_TIME", 0),
        # APPEND_ITEM MODE          32 UINT "Permissions"
        IntField("MODE", 0),
        # APPEND_ITEM NAME         512 STRING "Name of File"
        StrFixedLenField("NAME", b"", 64),
    ]


bind_layers(CCSDSPacket, FM_FILE_INFO_PKT_TlmPkt, pkttype=0, apid=139)


# TELEMETRY FM DIR_LIST_PKT BIG_ENDIAN "Get Directory Listing telemetry packet"
#   TLMHDR FM_DIR_LIST_TLM_MID
#   APPEND_ITEM DIRNAME 512 STRING "Directory Name"
#   APPEND_ITEM TOTALFILES 32 UINT "Number of files in the directory"
#      LIMITS DEFAULT 3 DISABLED 0 0 40 50
#   APPEND_ITEM PACKETFILES 32 UINT "Number of files in this packet"
#   APPEND_ITEM FIRSTFILE 32 UINT "Index into directory files of first packet file"
#   <%
#     max_entries = FswConfigParam::FM_DIR_LIST_PKT_ENTRIES
#     append_items = ""
#     for i in 0..(max_entries-1)
#       append_items << "APPEND_ITEM FILE#{i}_NAME     512 STRING \"File Name\""        << "\n"
#       append_items << "APPEND_ITEM FILE#{i}_SIZE      32 UINT   \"Size in bytes\""    << "\n"
#       append_items << "APPEND_ITEM FILE#{i}_MOD_TIME  32 UINT   \"Time of last mod\"" << "\n"
#       append_items << "APPEND_ITEM FILE#{i}_MODE      32 UINT   \"Permissions\""      << "\n"
#     end
#   %>
#   <%= append_items %>


# TELEMETRY FM OPEN_FILES_PKT BIG_ENDIAN "Get Open Files telemetry packet"
#   TLMHDR FM_OPEN_FILES_TLM_MID
#   APPEND_ITEM NUM_OPEN_FILES 32 UINT   "Number of files opened via cFE"
#   <%
#     max_entries = FswConfigParam::OS_MAX_NUM_OPEN_FILES
#     append_items = ""
#     for i in 0..(max_entries-1)
#       append_items << "APPEND_ITEM FILE#{i}_NAME     512 STRING \"File Name\""                   << "\n"
#       append_items << "APPEND_ITEM FILE#{i}_APP      160 STRING \"App that opened the file\""    << "\n"
#     end
#   %>
#   <%= append_items %>


# TELEMETRY FM FREE_SPACE_PKT BIG_ENDIAN "Get Free Space telemetry packet"
#   TLMHDR FM_FREE_SPACE_TLM_MID
#   <%
#     max_entries = FswConfigParam::FM_TABLE_ENTRY_COUNT
#     append_items = ""
#     for i in 0..(max_entries-1)
#       append_items << "APPEND_ITEM FREE_SPACE#{i}_SIZE_LO32  32 UINT    \"Low 32-bits of 64 bit integer\""   << "\n"
#       append_items << "APPEND_ITEM FREE_SPACE#{i}_SIZE_HI32  32 UINT    \"High 32-bits of 64 bit integer\""  << "\n"
#       append_items << "APPEND_ITEM FREE_SPACE#{i}_NAME      512 STRING  \"File System Name\""                << "\n"
#     end
#   %>
#   <%= append_items %>
