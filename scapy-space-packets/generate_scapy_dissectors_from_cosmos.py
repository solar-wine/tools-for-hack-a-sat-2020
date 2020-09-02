#!/usr/bin/env python3
"""Generate Scapy dissector for CCSDS Space Packet Protocol payload used by Hack-A-Sat final
"""
import argparse
from pathlib import Path
import re
from typing import Dict, FrozenSet, Generator, Iterable, List, Mapping, Optional, Set

from apids import APID_NAMES


# Find APID from literal msg_id
COMMANDS_APID: Dict[str, int] = {msg_id: apid for apid, msg_id in APID_NAMES[1].items()}
TELEMETRY_APID: Dict[str, int] = {msg_id: apid for apid, msg_id in APID_NAMES[0].items()}
TELEMETRY_APID['CFE_EVS_EVENT_MSG'] = TELEMETRY_APID['CFE_EVS_LONG_EVENT_MSG']  # Renaming
assert TELEMETRY_APID['CFE_EVS_EVENT_MSG'] == 0x008


RUBY_GLOBAL_VARIABLES: Dict[str, str] = {
    # cosmos/llib/fsw_config_param.rb
    'FswConfigParam::BOOT_PATH': '"/cf"',
    'FswConfigParam::CFE_ES_DEFAULT_APP_LOG_FILE': 'cfe_es_app_info.log"',
    'FswConfigParam::CFE_ES_DEFAULT_CDS_REG_DUMP_FILE': '"cfe_cds_reg.log"',
    'FswConfigParam::CFE_ES_DEFAULT_ER_LOG_FILE': '"cfe_erlog.log"',
    'FswConfigParam::CFE_ES_DEFAULT_SYSLOG_FILE': '"cfe_es_syslog.log"',
    'FswConfigParam::CFE_ES_DEFAULT_TASK_LOG_FILE': '"cfe_es_task_info.log"',
    'FswConfigParam::CFE_EVS_DEFAULT_APP_DATA_FILE': '"cfe_evs_app.dat"',
    'FswConfigParam::CFE_EVS_DEFAULT_LOG_FILE': '"cfe_evs.log"',
    'FswConfigParam::CFE_SB_DEFAULT_MAP_FILENAME': '"cfe_sb_msgmap.dat"',
    'FswConfigParam::CFE_SB_DEFAULT_PIPE_FILENAME': '"cfe_sb_pipe.dat"',
    'FswConfigParam::CFE_SB_DEFAULT_ROUTING_FILENAME': '"cfe_sb_route.dat"',
    'FswConfigParam::CFE_TBL_DEFAULT_REG_DUMP_FILE': '"cfe_tbl_reg.log"',
    'FswConfigParam::FM_DIR_LIST_FILE_DEFNAME': '"fm_dirlist.out"',

    # Shared definitions from cosmos/lib/osk_config.rb
    'Osk::Cfg.processor_endian': 'BIG_ENDIAN',

    # Shared definitions from cosmos/lib/osk_global.rb
    'Osk::PASSWORD': '"osk"',
    'Osk::JSON_APP_TYPE_CFS': '"cfs"',
    'Osk::JSON_APP_TYPE_OSK': '"osk"',
    'Osk::NULL_IP_ADDR': '"0.0.0.0"',
    'Osk::COSMOS_IP_ADDR': '"127.0.0.1"',
    'Osk::COSMOS_CFS_INT': '"LOCAL_CFS_INT"',
    'Osk::PISAT_IP_ADDR': '"192.168.0.1"',
    'Osk::PISAT_CFS_INT': '"PISAT_CFS_INT"',
    'Osk::PISAT_CONTROL': '"PISAT_CONTROL"',
    'Osk::HOST_IP_ADDR': '"192.168.0.6"',
    'Osk::CFS_CMD_PORT': '"1234"',
    'Osk::CFS_TLM_PORT': '"1235"',
    'Osk::GET_FILE_TIMEOUT': '15',
    'Osk::PUT_FILE_TIMEOUT': '15',
    'Osk::CFDP_APP_ENTITY_ID': '"23"',
    'Osk::CFDP_GND_ENTITY_ID': '"0.21"',
    'Osk::CFDP_GET_TIMEOUT': '15',
    'Osk::CFDP_PUT_TIMEOUT': '15',
    'Osk::TFTP_GET_TIMEOUT': '15',
    'Osk::TFTP_PUT_TIMEOUT': '15',
    'Osk::MSG_BUTTON_YES': '"Yes"',
    'Osk::MSG_BUTTON_NO': '"No"',
    'Osk::MSG_BUTTON_CONT': '"OK"',
    'Osk::MSG_BUTTON_CANCEL': '"Cancel"',
    'Osk::MSG_UNDEFSTR': '"Undefined"',
    'Osk::MSG_TBD_FEATURE': '"Feature coming soon..."',
    'Osk::DOCS_QUICK_START_FILE': '"OSK-Quick-Start-Guide.pdf"',
    'Osk::DOCS_USERS_GUIDE_FILE': '"OSK-Users-Guide.pdf"',
    'Osk::TRAIN_OSK_INTRO_FILE': '"OSK-Training-Intro.pdf"',
    'Osk::TRAIN_OSK_CFE_SERVICE_FILE': '"OSK-Ex-cFE_02A-cFE-Services.pdf"',
    'Osk::TRAIN_OSK_CFE_APP_DEV_FILE': '"OSK-Ex-cFE_02B-cFE-App-Dev.pdf"',
    'Osk::TRAIN_CFS_INTRO_FILE': '"cFS_Training_01-Intro.pdf"',
    'Osk::TRAIN_CFE_SERVICE_FILE': '"cFS_Training_02A-cFE-Overview.pdf"',
    'Osk::TRAIN_CFE_APP_DEV_FILE': '"cFS_Training_02B-cFE-App-Dev.pdf"',
    'Osk::ABOUT_SCR_FILE': '"about_scr.txt"',
    'Osk::TUTORIAL_DEF_FILE': '"osk_tutorials.json"',
    'Osk::TUTORIAL_SCR_FILE': '"tutorial_scr.txt"',
    'Osk::CREATE_APP_JSON_FILE': '"create-app.json"',
    'Osk::CREATE_APP_TEMPLATE_FILE': '"app-template.json"',
    'Osk::CREATE_APP_SCR_FILE': '"create_app_scr.txt"',
    'Osk::TEMPLATE_INFO_SCR_FILE': '"template_info_scr.txt"',
    'Osk::SIMSAT_OVERVIEW_FILE': '"OSK-Simple-Sat.pdf"',
    'Osk::TUTORIAL_HTML': '"HTML"',
    'Osk::TUTORIAL_PDF': '"PDF"',
    'Osk::TUTORIAL_SCRIPT': '"SCRIPT"',
    'Osk::CFE_UG_FILE': '"index.html"',
    'Osk::CFE_APP_DEV_FILE': '"cFE_Application_Developers_Guide.pdf"',
    'Osk::CFE_TRAINING_SLIDES_FILE': '"cFS_Training-cFE_Services.pdf"',
    'Osk::CFE_EXERCISE_SLIDES_FILE': '"OSK_Training-cFE_Exercises.pdf"',
    'Osk::CFE_STARTUP_FILE': '"cfe_es_startup.scr"',
    'Osk::CPU1_TARGET_FILE': '"targets.cmake"',
    'Osk::CPU1_PLT_CFG_FILE': '"cpu1_platform_cfg.h"',
    'Osk::CPU1_MSG_ID_FILE': '"cpu1_msgids.h"',
    'Osk::CPU1_OS_CFG_FILE': '"cpu1_osconfig.h"',
    'Osk::CPU1_STARTUP_FILE': '"cpu1_cfe_es_startup.scr"',
    'Osk::JSON_TBL_MGMT_SCR_FILE': '"json_table_mgmt_scr.txt"',
    'Osk::TMP_BIN_FILE': '"osk_tmp_bin.dat"',
    'Osk::TMP_TBL_FILE': '"osk_tmp_tbl.dat"',
    'Osk::TMP_JSON_FILE': '"osk_tmp.json"',
    'Osk::TMP_TXT_FILE': '"osk_tmp.txt"',
    'Osk::TMP_FLT_CMD_SCR_FILE': '"osk_tmp_flt_cmd_scr.txt"',
    'Osk::TMP_FLT_CMD_SCR_STR': '"OSK_TMP_FLT_CMD_SCR"',
    'Osk::TMP_TBL_MGR_SCR_FILE': '"osk_tmp_tbl_mgr_scr.txt"',
    'Osk::TMP_TBL_MGR_SCR_STR': '"OSK_TMP_TBL_MGR_SCR"',
    'Osk::TMP_GET_BIN_FILE_SCR_FILE': '"osk_tmp_get_bin_file_scr.txt"',
    'Osk::TMP_GET_BIN_FILE_SCR_STR': '"OSK_TMP_GET_BIN_FILE_SCR"',
    'Osk::DMP_FILE_TAG': '"~"',
    'Osk::TBL_MGR_DEF_CFE_ES_APP_INFO': '"cfe_es_app_info.txt"',
    'Osk::TBL_MGR_DEF_CFE_ES_CDS_REG': '"cfe_es_cds_reg.txt"',
    'Osk::TBL_MGR_DEF_CFE_ES_ERLOG': '"cfe_es_erlog.txt"',
    'Osk::TBL_MGR_DEF_CFE_ES_SYSLOG': '"cfe_es_syslog.txt"',
    'Osk::TBL_MGR_DEF_CFE_ES_TASK_INFO': '"cfe_es_task_info.txt"',
    'Osk::TBL_MGR_DEF_CFE_EVS_LOG': '"cfe_evs_log.txt"',
    'Osk::TBL_MGR_DEF_CFE_EVS_APP_INFO': '"cfe_evs_app_info.txt"',
    'Osk::TBL_MGR_DEF_CFE_SB_PIPE': '"cfe_sb_pipe_info.txt"',
    'Osk::TBL_MGR_DEF_CFE_SB_ROUTES': '"cfe_sb_routes.txt"',
    'Osk::TBL_MGR_DEF_CFE_SB_MSG_MAP': '"cfe_sb_msg_map.txt"',
    'Osk::TBL_MGR_DEF_CFE_TBL_REG': '"cfe_tbl_reg.txt"',
    'Osk::TBL_MGR_DEF_DS_FILE_TBL': '"ds_file_tbl.txt"',
    'Osk::TBL_MGR_DEF_DS_FILTER_TBL': '"ds_filter_tbl.txt"',
    'Osk::TBL_MGR_DEF_DS_EVENT_LOG': '"ds_event_log.txt"',
    'Osk::TBL_MGR_DEF_FM_DIR': '"fm_dir_list.txt"',
    'Osk::TBL_MGR_DEF_FM_FREESPACE': '"fm_freespace_tbl.txt"',
    'Osk::TBL_MGR_DEF_HK_COPY': '"hk_copy_tbl.txt"',
    'Osk::TBL_MGR_DEF_MD_TBL': '"md_tbl.txt"',
    'Osk::TBL_MGR_DEF_MM_DMP': '"mm_dump.txt"',
    'Osk::REL_DIR_CFS': '"../cfs"',
    'Osk::REL_DIR_42': '"../42"',
    'Osk::REL_DIR_DOCS': '"../docs"',
    'Osk::OSK_42_DIR': '"../42/cosmos"',
    'Osk::OSK_CFS_DIR': '"../cfs/cosmos"',
    'Osk::OSK_DOCS_DIR': '"../docs/cosmos"',
    'Osk::CFS_EXE_DIR': '"../cfs/cosmos/build/exe/cpu1"',
    'Osk::CFS_EXE_CF_DIR': '"../cfs/cosmos/build/exe/cpu1/cf"',
    'Osk::CFS_CMAKE_DIR': '"../cfs/cosmos/osk_defs"',
    'Osk::REL_SRV_DIR': '"cfs_kit/file_server"',
    'Osk::REL_SRV_TBL_DIR': '"cfs_kit/file_server/tables"',
    'Osk::GND_SRV_DIR': '"cosmos/cfs_kit/file_server"',
    'Osk::GND_SRV_TBL_DIR': '"cosmos/cfs_kit/file_server/tables"',
    'Osk::FLT_SRV_DIR': '"/cf"',
    'Osk::LIB_DIR': '"cosmos/config/targets/CFS_KIT/lib"',
    'Osk::SCR_DIR': '"cosmos/config/targets/CFS_KIT/screens"',
    'Osk::CFE_DOCS_DIR': '"cosmos/cfs_kit/docs"',
    'Osk::CFE_UG_DIR': '"cosmos/cfs_kit/docs/cfe_users_guide"',
    'Osk::REL_TUTORIAL_DIR': '"cfs_kit/tutorials"',
    'Osk::TUTORIAL_DIR': '"cosmos/cfs_kit/tutorials"',
    'Osk::CFE_TRAINING_DIR': '"cosmos/cfs_kit/tutorials/cfe/training"',
    'Osk::TOOLS_DIR': '"cosmos/cfs_kit/tools"',
    'Osk::PERF_MON_DIR': '"cosmos/cfs_kit/tools/perf-monitor"',
    'Osk::CREATE_APP_DIR': '"cosmos/cfs_kit/tools/create-app',
    'Osk::PROC_DIR': '"cosmos/procedures"',
    'Osk::COSMOS_CFG_EDITOR': '"cosmos/tools/ConfigEditor"',
    'Osk::COSMOS_PKT_VIEWER': '"cosmos/tools/PacketViewer"',
    'Osk::COSMOS_SCR_RUNNER': '"cosmos/tools/ScriptRunner"',
    'Osk::COSMOS_TBL_MANAGER': '"cosmos/tools/TableManager"',
    'Osk::COSMOS_TLM_GRAPHER': '"cosmos/tools/TlmGrapher"',
    'Osk::COSMOS_CMD_TLM_SRV': '"cosmos/tools/CmdTlmServer"',
    'Osk::COSMOS_TST_RUNNER': '"cosmos/tools/TestRunner"',
    'Osk::TMP_FLT_BIN_PATH_FILE': '"/cf/osk_tmp_bin.dat"',
    'Osk::TMP_GND_BIN_PATH_FILE': '"cosmos/cfs_kit/file_server/osk_tmp_bin.dat"',
    'Osk::TMP_FLT_TXT_PATH_FILE': '"/cf/osk_tmp.txt"',
    'Osk::TMP_GND_TXT_PATH_FILE': '"cosmos/cfs_kit/file_server/osk_tmp.txt"',
    'Osk::DEMO_STEP_NO_INFO': '"\n\nNo additional information for this demo step."',
    'Osk::WIDGET_GND_WORK_DIR': '"gnd_work_dir"',
    'Osk::WIDGET_FLT_WORK_DIR': '"flt_work_dir"',
    'Osk::CMD_STR_NOOP': 'NOOP',
    'Osk::CMD_STR_RESET': 'RESET_CTRS',
    'Osk::CMD_STR_LOAD_TBL': 'LOAD_TBL',
    'Osk::CMD_STR_DUMP_TBL': 'DUMP_TBL',
    'Osk::CMD_DEF_FILENAME': '"osk_tmp_bin.dat"',
    'Osk::CMD_DEF_DIR_NAME': '"/cf"',
    'Osk::TLM_STR_HK_PKT': 'HK_TLM_PKT',
    'Osk::TLM_STR_CMD_VLD': 'CMD_VALID_COUNT',
    'Osk::TLM_STR_CMD_ERR': 'CMD_ERROR_COUNT',

    # "Dynamic" variables
    'Osk::Cfg.get_fsw_cfg_str_param(@APP_PREFIX_STR, @DS_TOTAL_FNAME_BUFSIZE)*8': str(64 * 8),
    'Osk::Cfg.get_fsw_cfg_str_param(@APP_PREFIX_STR, @DS_PATHNAME_BUFSIZE)*8': str(64 * 8),
    'Osk::Cfg.get_fsw_cfg_str_param(@APP_PREFIX_STR, @DS_BASENAME_BUFSIZE)*8': str(64 * 8),
    'Osk::Cfg.get_fsw_cfg_str_param(@APP_PREFIX_STR, @DS_EXTENSION_BUFSIZE)*8': str(8 * 8),
}


# Record all targets and packets (cmd and telemetry)
# Add values that are not parsed in Cosmos files
cosmos_target_packets = {
    'FM': {
        'DIR_LIST_PKT': 'FM_DIR_LIST_PKT_TlmPkt',
    },
    'PDU': {
        'CF_SPACE_TO_GND_PDU': 'CFDP_TlmPkt',
    },
}


def resolve_ruby_variables(current_variables: Mapping[str, str], block_lines: Iterable[str]
                           ) -> Generator[str, None, None]:
    for line in block_lines:
        # Find Ruby code in the line and replace it using the variables
        while True:
            matches = re.match(r'^(.+?)<%= ([^%>]+) %>(.*)$', line)
            if not matches:
                break
            prefix, ruby, suffix = matches.groups()

            if ruby.startswith('Osk::Cfg.cmd_hdr'):
                # Parse <%= Osk::Cfg.cmd_hdr(@APP_PREFIX_STR, @CMD_MID_STR, 0, 0) %>
                matches = re.match(r'^Osk::Cfg\.cmd_hdr\(@APP_PREFIX_STR, @CMD_MID_STR, ([0-9]+), ([0-9]+)\)$', ruby)
                if not matches:
                    raise ValueError(f'Unexpected Ruby call {ruby!r}')
                msg_id = current_variables['@CMD_MID_STR']
                func_code = int(matches.group(1))
                data_len = int(matches.group(2))
                line = f'{prefix}CMDHDR {msg_id} {func_code} {data_len}{suffix}'
                continue

            if ruby.startswith('Osk::Cfg.tlm_hdr'):
                # Parse <%= Osk::Cfg.tlm_hdr(@APP_PREFIX_STR, @HK_TLM_MID_STR) %>
                matches = re.match(r'^Osk::Cfg\.tlm_hdr\(@APP_PREFIX_STR, (@[0-9A-Z_]+)\)$', ruby)
                if not matches:
                    raise ValueError(f'Unexpected Ruby call {ruby!r}')
                msg_id = current_variables[matches.group(1)]
                line = f'{prefix}TLMHDR {msg_id}{suffix}'
                continue

            # Embedded Ruby variables
            matches = re.match(r'^"([0-9A-Z_]+)#\{(Osk::[0-9A-Z_]+)\}"$', ruby)
            if matches:
                ruby_prefix, var_name = matches.groups()
                line = prefix + ruby_prefix + current_variables[var_name] + suffix
                continue

            matches = re.match(r'^(FswConfigParam::BOOT_PATH)\+"/"\+(FswConfigParam::[0-9A-Z_]+)$', ruby)
            if matches:
                var1, var2 = matches.groups()
                value1 = current_variables[var1].strip('"')
                value2 = current_variables[var2].strip('"')
                line = f'{prefix}"{value1}/{value2}"{suffix}'
                continue

            # Special case for Telemetry packets
            if line == '  <%= append_items %>':
                break

            try:
                line = prefix + current_variables[ruby] + suffix
            except KeyError:
                print(f'Warning: unknown Ruby variable {ruby!r}')
                break
        yield line


def parse_command_block(output_lines: List[str], current_variables: Mapping[str, str], block_lines: Iterable[str]):
    # Resolve Ruby code
    block_lines = list(resolve_ruby_variables(current_variables, block_lines))
    if len(block_lines) < 2:
        raise ValueError("Not enough lines in command block")

    # Parse COMMAND CF NOOP BIG_ENDIAN "Generate an info event message with app version"
    matches = re.match(r'COMMAND ([A-Z_]+) ([0-9A-Z_]+) BIG_ENDIAN "([^"]+)"$', block_lines[0])
    if not matches:
        raise ValueError(f"Unexpected first COMMAND line: {block_lines[0]!r}")
    app_name, cmd_name, description = matches.groups()

    # Parse CMDHDR CF_CMD_MID 0 0
    matches = re.match(r'  CMDHDR ([0-9A-Z_]+) ([0-9]+) ([0-9]+)$', block_lines[1])
    if not matches:
        raise ValueError(f"Unexpected second COMMAND line: {block_lines[1]!r}")
    msg_id_str = matches.group(1)
    func_code = int(matches.group(2))
    data_len = int(matches.group(3))

    assert msg_id_str.endswith('_MID'), f'unexpected message ID name {msg_id_str!r}'
    apid = COMMANDS_APID[msg_id_str[:-4]]

    python_class_name = f'{app_name}_{cmd_name}_CmdPkt'

    output_lines.append('')
    output_lines.append('')
    output_lines.append(f'class {python_class_name}(Packet):')
    output_lines.append(f'    """{description}')
    output_lines.append('')
    output_lines.append(f'    app = {app_name}')
    output_lines.append(f'    command = {cmd_name}')
    output_lines.append(f'    msg_id = {msg_id_str} = {0x1800 + apid:#06x} = 0x1800 + {apid:#05x}')
    output_lines.append(f'    cmd_func_code = {func_code}')
    output_lines.append(f'    data_len = {data_len} bytes')
    output_lines.append('    """')
    output_lines.append(f'    name = "{python_class_name}"')
    output_lines.append('    fields_desc = [')
    fields_size = 0
    for line in block_lines[2:]:
        line = line.strip()
        output_lines.append('        # ' + line)

        matches = re.match(r'^APPEND_PARAMETER +([0-9A-Za-z_]+) +8 +UINT +(MIN_UINT8|[0-9]+) +(MAX_UINT8|[0-9]+) +([0-9]+|0x[0-9A-Fa-f]+) +"([^"]*)"$', line)  # noqa
        if matches:
            name, minval, maxval, default, comment = matches.groups()
            output_lines.append(f'        ByteField("{name}", {default}),')
            fields_size += 1
            continue

        matches = re.match(r'^APPEND_PARAMETER +([0-9A-Za-z_]+) +16 +UINT +(MIN_UINT16|MIN_UINT8|0|1) +(MAX_UINT16|MAX_UINT8|MIN_UINT8|1|2|4|32767) +([0-9]+) +"([^"]*)"$', line)  # noqa
        if matches:
            name, minval, maxval, default, comment = matches.groups()
            output_lines.append(f'        ShortField("{name}", {default}),')
            fields_size += 2
            continue

        matches = re.match(r'^APPEND_PARAMETER +([0-9A-Za-z_]+) +16 +INT +(MIN_INT16|0|1) +(MAX_INT16|2|7|250|32767) +([0-9]+) +"([^"]*)"$', line)  # noqa
        if matches:
            name, minval, maxval, default, comment = matches.groups()
            output_lines.append(f'        SignedShortField("{name}", {default}),')
            fields_size += 2
            continue

        matches = re.match(r'^APPEND_PARAMETER +([0-9A-Za-z_]+) +32 +UINT +(MIN_UINT32) +(MAX_UINT32) +([0-9]+) +"([^"]*)"$', line)  # noqa
        if matches:
            name, minval, maxval, default, comment = matches.groups()
            output_lines.append(f'        IntField("{name}", {default}),')
            fields_size += 4
            continue

        matches = re.match(r'^APPEND_PARAMETER +([0-9A-Za-z_]+) +32 +FLOAT +(MIN|[-0-9.]+) +(MAX|[0-9.]+) +([0-9.]+) +"([^"]*)"$', line)  # noqa
        if matches:
            name, minval, maxval, default, comment = matches.groups()
            output_lines.append(f'        IEEEFloatField("{name}", {default}),')
            fields_size += 4
            continue

        matches = re.match(r'^APPEND_PARAMETER +([0-9A-Za-z_]+) +([0-9]+) +STRING +"([^"]*)" +"([^"]*)"$', line)  # noqa
        if not matches:
            matches = re.match(r'^APPEND_PARAMETER +([0-9A-Za-z_]+) +([0-9]+) +STRING +([^" ]+) +"([^"]*)"$', line)  # noqa
        if matches:
            name, string_size, default, comment = matches.groups()
            string_size_bits = int(string_size)
            assert (string_size_bits % 8) == 0
            string_size_bytes = string_size_bits // 8
            output_lines.append(f'        StrFixedLenField("{name}", b"{default}", {string_size_bytes}),')
            fields_size += string_size_bytes
            continue

        matches = re.match(r'^APPEND_ARRAY_PARAMETER +([0-9A-Za-z_]+) +8 +UINT +([0-9]+) +"([^"]*)"$', line)  # noqa
        if matches:
            name, byte_array_size, comment = matches.groups()
            byte_array_size_bits = int(byte_array_size)
            assert (byte_array_size_bits % 8) == 0
            byte_array_size_bytes = byte_array_size_bits // 8
            output_lines.append(f'        StrFixedLenField("{name}", b"", {byte_array_size_bytes}),')
            fields_size += byte_array_size_bytes
            continue

        if line.startswith(('STATE ', 'UNITS ')):
            # Ignore such lines
            continue
        print(f"Warning: unknown command statement {line!r}")
        output_lines.append('        # WARNING: UNKNOWN FIELD')
    output_lines.append('    ]')
    if data_len != 0 and fields_size != data_len:
        output_lines.append(f'    # WARNING: mismatched size, expected {data_len} != cumulated {fields_size}')
    output_lines.append('')
    output_lines.append('')
    output_lines.append(
        f'bind_layers(CCSDSPacket, {python_class_name}, pkttype=1, apid={apid}, cmd_func_code={func_code})')

    if app_name not in cosmos_target_packets:
        cosmos_target_packets[app_name] = {}
    assert cmd_name not in cosmos_target_packets[app_name], f"Duplicate packet definition {app_name}/{cmd_name}"
    cosmos_target_packets[app_name][cmd_name] = python_class_name


def parse_telemetry_block(output_lines: List[str], current_variables: Mapping[str, str], block_lines: Iterable[str]):
    # Resolve Ruby code
    block_lines = list(resolve_ruby_variables(current_variables, block_lines))
    if len(block_lines) < 2:
        raise ValueError("Not enough lines in telemetry block")

    # Parse TELEMETRY CFE_ES HK_TLM_PKT BIG_ENDIAN "Housekeeping data (general status) autonomously sent"
    matches = re.match(r'TELEMETRY ([A-Z_]+) ([0-9A-Z_]+) BIG_ENDIAN "([^"]+)"$', block_lines[0])
    if not matches:
        raise ValueError(f"Unexpected first TELEMETRY line: {block_lines[0]!r}")
    app_name, cmd_name, description = matches.groups()

    # Parse TLMHDR CFE_ES_HK_TLM_MID
    matches = re.match(r'  TLMHDR ([0-9A-Z_]+)$', block_lines[1])
    if not matches:
        raise ValueError(f"Unexpected second TELEMETRY line: {block_lines[1]!r}")
    msg_id_str = matches.group(1)

    apid = TELEMETRY_APID[msg_id_str.replace('_MID', '')]

    if '  <%= append_items %>' in block_lines:
        # TODO: resolve Ruby magic. For now, comment-out the packet
        output_lines.append('')
        output_lines.append('')
        for line in block_lines:
            output_lines.append(f'#{(" " + line).rstrip()}')
        return

    python_class_name = f'{app_name}_{cmd_name}_TlmPkt'

    output_lines.append('')
    output_lines.append('')
    output_lines.append(f'class {python_class_name}(Packet):')
    output_lines.append(f'    """{description}')
    output_lines.append('')
    output_lines.append(f'    app = {app_name}')
    output_lines.append(f'    command = {cmd_name}')
    output_lines.append(f'    msg_id = {msg_id_str} = {0x0800 + apid:#06x} = 0x0800 + {apid:#05x}')
    output_lines.append('    """')
    output_lines.append(f'    name = "{python_class_name}"')
    output_lines.append('    fields_desc = [')
    for line in block_lines[2:]:
        line = line.strip()
        output_lines.append('        # ' + line)

        matches = re.match(r'^APPEND_ITEM +([0-9A-Za-z_]+) +8 +UINT +"([^"]*)"$', line)
        if matches:
            name, comment = matches.groups()
            output_lines.append(f'        ByteField("{name}", 0),')
            continue

        matches = re.match(r'^APPEND_ITEM +([0-9A-Za-z_]+) +8 +INT +"([^"]*)"$', line)
        if matches:
            name, comment = matches.groups()
            output_lines.append(f'        SignedByteField("{name}", 0),')
            continue

        matches = re.match(r'^APPEND_ITEM +([0-9A-Za-z_]+) +16 +UINT +"([^"]*)"$', line)
        if matches:
            name, comment = matches.groups()
            output_lines.append(f'        ShortField("{name}", 0),')
            continue

        matches = re.match(r'^APPEND_ITEM +([0-9A-Za-z_]+) +16 +INT +"([^"]*)"$', line)
        if matches:
            name, comment = matches.groups()
            output_lines.append(f'        SignedShortField("{name}", 0),')
            continue

        matches = re.match(r'^APPEND_ITEM +([0-9A-Za-z_]+) +24 +UINT +"([^"]*)"$', line)
        if matches:
            name, comment = matches.groups()
            output_lines.append(f'        X3BytesField("{name}", 0),')
            continue

        matches = re.match(r'^APPEND_ITEM +([0-9A-Za-z_]+) +32 +UINT +"([^"]*)"$', line)
        if matches:
            name, comment = matches.groups()
            output_lines.append(f'        IntField("{name}", 0),')
            continue

        matches = re.match(r'^APPEND_ITEM +([0-9A-Za-z_]+) +32 +INT +"([^"]*)"$', line)
        if matches:
            name, comment = matches.groups()
            output_lines.append(f'        SignedIntField("{name}", 0),')
            continue

        matches = re.match(r'^APPEND_ITEM +([0-9A-Za-z_]+) +32 +FLOAT +"([^"]*)"$', line)
        if matches:
            name, comment = matches.groups()
            output_lines.append(f'        IEEEFloatField("{name}", 0.0),')
            continue

        matches = re.match(r'^APPEND_ITEM +([0-9A-Za-z_]+) +64 +FLOAT +"([^"]*)"$', line)
        if matches:
            name, comment = matches.groups()
            output_lines.append(f'        IEEEDoubleField("{name}", 0.0),')
            continue

        matches = re.match(r'^APPEND_ITEM +([0-9A-Za-z_]+) +([0-9]+) +STRING +"([^"]*)"$', line)
        if matches:
            name, string_size, comment = matches.groups()
            string_size_bits = int(string_size)
            assert (string_size_bits % 8) == 0
            string_size_bytes = string_size_bits // 8
            output_lines.append(f'        StrFixedLenField("{name}", b"", {string_size_bytes}),')
            continue

        matches = re.match(r'^APPEND_ARRAY_ITEM +([0-9A-Za-z_]+) +([0-9]+) +UINT +([0-9]+) +"([^"]*)"$', line)
        if matches:
            name, item_size_str, total_size_str, comment = matches.groups()
            item_size_bits = int(item_size_str)
            assert (item_size_bits % 8) == 0
            item_size_bytes = item_size_bits // 8
            total_size_bits = int(total_size_str)
            assert (total_size_bits % item_size_bits) == 0
            count_items = total_size_bits // item_size_bits
            assert count_items > 0
            if item_size_bytes == 1:
                output_lines.append(f'        StrFixedLenField("{name}", b"", {count_items}),  # FIXME: XNBytesField should be better, if supported')  # noqa
                continue
            if item_size_bytes == 2:
                for idx in range(count_items):
                    output_lines.append(f'        ShortField("{name}__{idx}", 0),')
                continue

            for idx in range(count_items):
                output_lines.append(f'        StrFixedLenField("{name}__{idx}", b"", {item_size_bytes}),  # FIXME: XNBytesField should be better, if supported')  # noqa
            continue

        if line.startswith(('FORMAT_STRING ', 'ITEM ', 'LIMITS ', 'READ_CONVERSION ', 'STATE ', 'UNITS ')):
            # Ignore such lines
            continue

        print(f"Warning: unknown command statement {line!r}")
        output_lines.append('        # WARNING: UNKNOWN FIELD')
    output_lines.append('    ]')
    output_lines.append('')
    output_lines.append('')
    output_lines.append(
        f'bind_layers(CCSDSPacket, {python_class_name}, pkttype=0, apid={apid})')

    if app_name not in cosmos_target_packets:
        cosmos_target_packets[app_name] = {}
    assert cmd_name not in cosmos_target_packets[app_name], f"Duplicate packet definition {app_name}/{cmd_name}"
    cosmos_target_packets[app_name][cmd_name] = python_class_name


def parse_cosmos_file(text_file: Path) -> List[str]:
    print(f"Parsing {text_file}")
    current_variables: Dict[str, str] = RUBY_GLOBAL_VARIABLES.copy()
    line_state = ''
    block_lines: Optional[List[str]] = None
    output_lines: List[str] = []
    with text_file.open('r') as stream:
        for lineno, line in enumerate(stream, start=1):
            line = line.rstrip()
            stripped_line = line.lstrip()
            # Always ignore empty lines
            if line == '':
                continue

            # Ignore "#~~define " and comments
            if stripped_line.startswith('#'):
                continue

            if line_state == 'in-Ruby-code':
                if stripped_line == '%>':
                    line_state = ''
                    continue
                # Accept known require lines
                if re.match(r"^ *require '(fsw_config_param|osk_config|osk_global)'$", line):
                    continue
                # Local variables
                matches = re.match(r'^ *(@[0-9A-Za-z_]+) *= *"([^"]+)"(?: *#.*)?$', line)
                if matches:
                    name, value = matches.groups()
                    assert name not in current_variables
                    current_variables[name] = value
                    continue

            if line_state == 'command-block':
                assert block_lines is not None
                # Save indented lines
                if line.startswith(' '):
                    block_lines.append(line)
                    continue
                if line.startswith('COMMAND '):
                    # End the last command block and start a new one
                    parse_command_block(output_lines, current_variables, block_lines)
                    block_lines = [line]
                    continue

            if line_state == 'telemetry-block':
                assert block_lines is not None
                if line.startswith(' '):
                    block_lines.append(line)
                    continue
                if line.startswith('TELEMETRY '):
                    parse_telemetry_block(output_lines, current_variables, block_lines)
                    block_lines = [line]
                    continue

            if line_state == '':
                assert block_lines is None
                if line == '':
                    continue
                if stripped_line == '<%':
                    line_state = 'in-Ruby-code'
                    continue
                if line.startswith('COMMAND '):
                    line_state = 'command-block'
                    block_lines = [line]
                    continue
                if line.startswith('TELEMETRY '):
                    line_state = 'telemetry-block'
                    block_lines = [line]
                    continue

            raise ValueError(f"Error: unexpected line {lineno} in state {line_state!r}: {line!r}")

    # End of file
    if line_state == 'command-block':
        assert block_lines is not None
        parse_command_block(output_lines, current_variables, block_lines)
    elif line_state == 'telemetry-block':
        assert block_lines is not None
        parse_telemetry_block(output_lines, current_variables, block_lines)
    return output_lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cosmos', type=Path, help='Path to cosmos/ directory')
    args = parser.parse_args()

    base_dir = Path(__file__).parent

    # Ignore some files that define pseudo-packets that are managed directly by COSMOS
    IGNORED_FILES: FrozenSet[str] = frozenset((
        'cfdp_cmd',
        'cfdp_tlm',
        'cfs_kit_psuedo_demo_tlm',
        'cosmos_server_cmds',
        'cosmos_server_tlm',
        'meta_tlm',
        'pdu_cmd',
        'pdu_tlm',
        'radio_cmd',
        'system_cmds',
        'system_tlm',
    ))

    # Find all command & telemetry directories
    found_file_names: Set[str] = set()
    for cmd_tlm_directory in sorted(args.cosmos.glob('config/targets/**/cmd_tlm')):
        for text_file in sorted(cmd_tlm_directory.glob('*')):
            assert text_file.suffix == '.txt'

            if text_file.stem in IGNORED_FILES:
                continue

            # Check for duplicate file names
            if text_file.stem in found_file_names:
                raise RuntimeError(f"Duplicate file {text_file}")
            found_file_names.add(text_file.stem)

            output_lines = parse_cosmos_file(text_file)
            output_file_name = f'packets_{text_file.stem}.py'
            with (base_dir / output_file_name).open('w') as stream:
                stream.write('from scapy.all import *\n')
                stream.write('from ccsds_base import CCSDSPacket\n')
                for line in output_lines:
                    stream.write(f'{line}\n')

    # Generate all_packets.py
    with (base_dir / 'all_packets.py').open('w') as stream:
        stream.write('from cosmos_soft_packets import *\n')
        stream.write('from noncosmos_packets import *\n')
        for file_name in sorted(found_file_names):
            stream.write(f'from packets_{file_name} import *\n')

        # Allow finding the Packet class from (target app, command)
        stream.write('\n\nCOSMOS_TARGET_PACKETS = {\n')
        for app_name, cmd_packets in sorted(cosmos_target_packets.items()):
            stream.write(f'    {app_name!r}: {{\n')
            for cmd_name, pkt_cls in sorted(cmd_packets.items()):
                stream.write(f'        {cmd_name!r}: {pkt_cls},\n')
            stream.write('    },\n')
        stream.write('}\n')

        # Reverse the table
        stream.write('\n')
        stream.write('COSMOS_TARGET_PACKETS_REV = {}\n')
        stream.write('for target, cmds in COSMOS_TARGET_PACKETS.items():\n')
        stream.write('    for cmd, pktclass in cmds.items():\n')
        stream.write('        COSMOS_TARGET_PACKETS_REV[pktclass] = (target, cmd)\n')
