from scapy.all import *
from ccsds_base import CCSDSPacket


class FM_NOOP_CmdPkt(Packet):
    """Generate an info event message with app version

    app = FM
    command = NOOP
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 0
    data_len = 0 bytes
    """
    name = "FM_NOOP_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, FM_NOOP_CmdPkt, pkttype=1, apid=140, cmd_func_code=0)


class FM_RESET_CTRS_CmdPkt(Packet):
    """Resets HK TLM parent and child task counters

    app = FM
    command = RESET_CTRS
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 1
    data_len = 0 bytes
    """
    name = "FM_RESET_CTRS_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, FM_RESET_CTRS_CmdPkt, pkttype=1, apid=140, cmd_func_code=1)


class FM_COPY_FILE_CmdPkt(Packet):
    """Copy the source file to the target file.

    app = FM
    command = COPY_FILE
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 2
    data_len = 130 bytes
    """
    name = "FM_COPY_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER OVERWRITE 16 UINT MIN_UINT16 MAX_UINT16 0 "1 = Allow overwriting an existing target file"
        ShortField("OVERWRITE", 0),
        # APPEND_PARAMETER SOURCE   512 STRING "osk_tmp_bin.dat"  "Complete source /path/filename"
        StrFixedLenField("SOURCE", b"osk_tmp_bin.dat", 64),
        # APPEND_PARAMETER TARGET   512 STRING "osk_tmp_bin.dat"  "Complete target /path/filename"
        StrFixedLenField("TARGET", b"osk_tmp_bin.dat", 64),
    ]


bind_layers(CCSDSPacket, FM_COPY_FILE_CmdPkt, pkttype=1, apid=140, cmd_func_code=2)


class FM_MOVE_FILE_CmdPkt(Packet):
    """Move the source file to the target file.

    app = FM
    command = MOVE_FILE
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 3
    data_len = 130 bytes
    """
    name = "FM_MOVE_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER OVERWRITE 16 UINT MIN_UINT16 MAX_UINT16 0 "1 = Allow overwriting an existing target file"
        ShortField("OVERWRITE", 0),
        # APPEND_PARAMETER SOURCE   512 STRING "osk_tmp_bin.dat"  "Complete source /path/filename"
        StrFixedLenField("SOURCE", b"osk_tmp_bin.dat", 64),
        # APPEND_PARAMETER TARGET   512 STRING "osk_tmp_bin.dat"  "Complete source /path/filename"
        StrFixedLenField("TARGET", b"osk_tmp_bin.dat", 64),
    ]


bind_layers(CCSDSPacket, FM_MOVE_FILE_CmdPkt, pkttype=1, apid=140, cmd_func_code=3)


class FM_RENAME_FILE_CmdPkt(Packet):
    """Rename the source file to the target file. Source must be an existing file and target must not exist. Source and target must both be on the same file system. The rename command does not actually move any file data. The command modifies the file system directory structure to create a different file entry for the same file data. If the user wishes to rename a file across file systems, he must first copy the file and then delete the original.

    app = FM
    command = RENAME_FILE
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 4
    data_len = 128 bytes
    """
    name = "FM_RENAME_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SOURCE 512 STRING "osk_tmp_bin.dat" "Source filename"
        StrFixedLenField("SOURCE", b"osk_tmp_bin.dat", 64),
        # APPEND_PARAMETER TARGET 512 STRING "osk_tmp_bin.dat" "Target filename"
        StrFixedLenField("TARGET", b"osk_tmp_bin.dat", 64),
    ]


bind_layers(CCSDSPacket, FM_RENAME_FILE_CmdPkt, pkttype=1, apid=140, cmd_func_code=4)


class FM_DELETE_FILE_CmdPkt(Packet):
    """Delete the source file. Source must be an existing file that is not open.

    app = FM
    command = DELETE_FILE
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 5
    data_len = 64 bytes
    """
    name = "FM_DELETE_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "osk_tmp_bin.dat" "Delete filename"
        StrFixedLenField("FILENAME", b"osk_tmp_bin.dat", 64),
    ]


bind_layers(CCSDSPacket, FM_DELETE_FILE_CmdPkt, pkttype=1, apid=140, cmd_func_code=5)


class FM_DELETE_ALL_FILES_CmdPkt(Packet):
    """Delete all files in the source directory. Source must be an existing directory. Open files and sub-directories are not deleted. Because of the possibility that this command might take a very long time to complete, command argument validation will be done immediately but reading the directory and deleting each file will be performed by a lower priority child task. As such, the return value for this function only refers to the result of command argument verification and being able to place the command on the child task interface queue.

    app = FM
    command = DELETE_ALL_FILES
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 7
    data_len = 64 bytes
    """
    name = "FM_DELETE_ALL_FILES_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER DIRECTORY 512 STRING "/cf" "Directory name"
        StrFixedLenField("DIRECTORY", b"/cf", 64),
    ]


bind_layers(CCSDSPacket, FM_DELETE_ALL_FILES_CmdPkt, pkttype=1, apid=140, cmd_func_code=7)


class FM_DECOMPRESS_FILE_CmdPkt(Packet):
    """Decompress the source file into the target file. Source must be an existing file and target must not exist. Source and target may be on different file systems. Because of the possibility that this command might take a very long time to complete, command argument validation will be done immediately but decompressing the source file into the target file will be performed by a lower priority child task. As such, the return value for this function only refers to the result of command argument verification and being able to place the command on the child task interface queue.

    app = FM
    command = DECOMPRESS_FILE
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 8
    data_len = 128 bytes
    """
    name = "FM_DECOMPRESS_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SOURCE 512 STRING "osk_tmp_bin.dat" "Source filename"
        StrFixedLenField("SOURCE", b"osk_tmp_bin.dat", 64),
        # APPEND_PARAMETER TARGET 512 STRING "osk_tmp_bin.dat" "Target filename"
        StrFixedLenField("TARGET", b"osk_tmp_bin.dat", 64),
    ]


bind_layers(CCSDSPacket, FM_DECOMPRESS_FILE_CmdPkt, pkttype=1, apid=140, cmd_func_code=8)


class FM_CONCAT_FILES_CmdPkt(Packet):
    """Concatenate two source files into the target file. Sources must both be existing files and target must not exist. Sources and target may be on different file systems. Because of the possibility that this command might take a very long time to complete, command argument validation will be done immediately but copying the first source file to the target file and then appending the second source file to the target file will be performed by a lower priority child task. As such, the return value for this function only refers to the result of command argument verification and being able to place the command on the child task interface queue.

    app = FM
    command = CONCAT_FILES
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 9
    data_len = 192 bytes
    """
    name = "FM_CONCAT_FILES_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER SOURCE1 512 STRING "osk_tmp_bin.dat" "Source 1 filename"
        StrFixedLenField("SOURCE1", b"osk_tmp_bin.dat", 64),
        # APPEND_PARAMETER SOURCE2 512 STRING "osk_tmp_bin.dat" "Source 2 filename"
        StrFixedLenField("SOURCE2", b"osk_tmp_bin.dat", 64),
        # APPEND_PARAMETER TARGET  512 STRING "osk_tmp_bin.dat" "Target filename"
        StrFixedLenField("TARGET", b"osk_tmp_bin.dat", 64),
    ]


bind_layers(CCSDSPacket, FM_CONCAT_FILES_CmdPkt, pkttype=1, apid=140, cmd_func_code=9)


class FM_SEND_FILE_INFO_CmdPkt(Packet):
    """Create a file information telemetry packet for the specified file

    app = FM
    command = SEND_FILE_INFO
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 10
    data_len = 68 bytes
    """
    name = "FM_SEND_FILE_INFO_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "osk_tmp_bin.dat"  "Filename"
        StrFixedLenField("FILENAME", b"osk_tmp_bin.dat", 64),
        # APPEND_PARAMETER CRC       32 UINT MIN_UINT32 MAX_UINT32 2         "CRC method"
        IntField("CRC", 2),
    ]


bind_layers(CCSDSPacket, FM_SEND_FILE_INFO_CmdPkt, pkttype=1, apid=140, cmd_func_code=10)


class FM_GET_OPEN_FILES_CmdPkt(Packet):
    """Creates an 'open files' telemetry packet. The open files packet includes the number of open files and for each open file, the name of the file and the name of the application that has the file opened.

    app = FM
    command = GET_OPEN_FILES
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 11
    data_len = 0 bytes
    """
    name = "FM_GET_OPEN_FILES_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, FM_GET_OPEN_FILES_CmdPkt, pkttype=1, apid=140, cmd_func_code=11)


class FM_CREATE_DIR_CmdPkt(Packet):
    """Create the source directory. Source must be a valid directory name that does not exist

    app = FM
    command = CREATE_DIR
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 12
    data_len = 64 bytes
    """
    name = "FM_CREATE_DIR_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER DIRECTORY 512 STRING "osk_tmp_bin.dat" "Directory to be created"
        StrFixedLenField("DIRECTORY", b"osk_tmp_bin.dat", 64),
    ]


bind_layers(CCSDSPacket, FM_CREATE_DIR_CmdPkt, pkttype=1, apid=140, cmd_func_code=12)


class FM_DELETE_DIR_CmdPkt(Packet):
    """Delete the source directory, it does not delete the contents of the directory. Source must be a valid directory name that exists.

    app = FM
    command = DELETE_DIR
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 13
    data_len = 64 bytes
    """
    name = "FM_DELETE_DIR_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER DIRECTORY 512 STRING "osk_tmp_bin.dat" "Directory to be deleted"
        StrFixedLenField("DIRECTORY", b"osk_tmp_bin.dat", 64),
    ]


bind_layers(CCSDSPacket, FM_DELETE_DIR_CmdPkt, pkttype=1, apid=140, cmd_func_code=13)


class FM_WRITE_DIR_TO_FILE_CmdPkt(Packet):
    """Write a listing of the contents of the source directory to the target file. If the target filename buffer is empty, then the default target filename FM_DIR_LIST_FILE_DEFNAME is used. The command will overwrite a previous copy of the target file, if one exists. Because of the possibility that this command might take a very long time to complete, command argument validation will be done immediately but reading the directory will be performed by a lower priority child task. As such, the return value for this function only refers to the result of command argument verification and being able to place the command on the child task interface queue.

    app = FM
    command = WRITE_DIR_TO_FILE
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 14
    data_len = 132 bytes
    """
    name = "FM_WRITE_DIR_TO_FILE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER DIRECTORY     512 STRING "/cf" "Directory to be listed"
        StrFixedLenField("DIRECTORY", b"/cf", 64),
        # APPEND_PARAMETER FILENAME      512 STRING "/cf/fm_dirlist.out" "Filename"
        StrFixedLenField("FILENAME", b"/cf/fm_dirlist.out", 64),
        # APPEND_PARAMETER SIZE_TIME_MODE  8 UINT MIN_UINT8  MAX_UINT8  0 "Option to query size, time, and mode of files (CPU intensive)"
        ByteField("SIZE_TIME_MODE", 0),
        # APPEND_PARAMETER SPARE           8 UINT MIN_UINT8  MAX_UINT8  0 "Pad to 16 bit boundary"
        ByteField("SPARE", 0),
        # APPEND_PARAMETER SPARE          16 UINT MIN_UINT8  MAX_UINT8  0 "Pad to 32 bit boundary"
        ShortField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, FM_WRITE_DIR_TO_FILE_CmdPkt, pkttype=1, apid=140, cmd_func_code=14)


class FM_SEND_DIR_PKT_CmdPkt(Packet):
    """Creates a telemetry packet that contains a listing of the entries in the specified directory. Since the packet will likely hold fewer entries than will be possible in a directory, the command also provides an index argument to define which entry in the directory is the first entry reported in the telemetry packet. After reading the directory list and skipping entries until reaching the index of the first entry reported, the remaining entries in the packet are filled sequentially until either the packet is full or until there are no more entries in the directory. The first entry index is zero based - thus, when the first entry index is zero the first directory entry will be the first packet entry. The number of entries per packet FM_DIR_LIST_PKT_ENTRIES is a platform configuration definition. Because of the possibility that this command might take a very long time to complete, command argument validation will be done immediately but reading the directory will be performed by a lower priority child task. As such, the return value for this function only refers to the result of command argument verification and being able to place the command on the child task interface queue.

    app = FM
    command = SEND_DIR_PKT
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 15
    data_len = 72 bytes
    """
    name = "FM_SEND_DIR_PKT_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER DIRECTORY       512 STRING "/cf"  "Directory to bee listed"
        StrFixedLenField("DIRECTORY", b"/cf", 64),
        # APPEND_PARAMETER DIR_LIST_OFFSET  32 UINT MIN_UINT32 MAX_UINT32 0 "Index of 1st dir entry to put in packet"
        IntField("DIR_LIST_OFFSET", 0),
        # APPEND_PARAMETER SIZE_TIME_MODE    8 UINT MIN_UINT8  MAX_UINT8  0 "Option to query size, time, and mode of files (CPU intensive)"
        ByteField("SIZE_TIME_MODE", 0),
        # APPEND_PARAMETER SPARE             8 UINT MIN_UINT8  MAX_UINT8  0 "Pad to 16 bit boundary"
        ByteField("SPARE", 0),
        # APPEND_PARAMETER SPARE            16 UINT MIN_UINT8  MAX_UINT8  0 "Pad to 32 bit boundary"
        ShortField("SPARE", 0),
    ]


bind_layers(CCSDSPacket, FM_SEND_DIR_PKT_CmdPkt, pkttype=1, apid=140, cmd_func_code=15)


class FM_SEND_FREE_SPACE_PKT_CmdPkt(Packet):
    """Queries the amount of free space for each of the enabled entries in the file system free space table. The data is then placed in a telemetry packet and sent to ground.

    app = FM
    command = SEND_FREE_SPACE_PKT
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 16
    data_len = 0 bytes
    """
    name = "FM_SEND_FREE_SPACE_PKT_CmdPkt"
    fields_desc = [
    ]


bind_layers(CCSDSPacket, FM_SEND_FREE_SPACE_PKT_CmdPkt, pkttype=1, apid=140, cmd_func_code=16)


class FM_SET_TABLE_STATE_CmdPkt(Packet):
    """Enable/disable a single entry in the FM file system free space table. Unused table entries cannot be modified.

    app = FM
    command = SET_TABLE_STATE
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 17
    data_len = 8 bytes
    """
    name = "FM_SET_TABLE_STATE_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER TABLEENTRYINDEX 32 UINT MIN_UINT32 MAX_UINT32 0 "Table entry index"
        IntField("TABLEENTRYINDEX", 0),
        # APPEND_PARAMETER TABLEENTRYSTATE 32 UINT MIN_UINT32 MAX_UINT32 0 "New table entry state"
        IntField("TABLEENTRYSTATE", 0),
    ]


bind_layers(CCSDSPacket, FM_SET_TABLE_STATE_CmdPkt, pkttype=1, apid=140, cmd_func_code=17)


class FM_SET_FILE_PERMISSIONS_CmdPkt(Packet):
    """Sets the permissions for a file. This is a direct interface to OS_chmod() in the OSAL.

    app = FM
    command = SET_FILE_PERMISSIONS
    msg_id = FM_CMD_MID = 0x188c = 0x1800 + 0x08c
    cmd_func_code = 15
    data_len = 68 bytes
    """
    name = "FM_SET_FILE_PERMISSIONS_CmdPkt"
    fields_desc = [
        # APPEND_PARAMETER FILENAME 512 STRING "/cf"  "Filename"
        StrFixedLenField("FILENAME", b"/cf", 64),
        # APPEND_PARAMETER MODE      32 UINT MIN_UINT32 MAX_UINT32 0 "Permissions, passed directly to OS_chmod()"
        IntField("MODE", 0),
    ]


bind_layers(CCSDSPacket, FM_SET_FILE_PERMISSIONS_CmdPkt, pkttype=1, apid=140, cmd_func_code=15)
