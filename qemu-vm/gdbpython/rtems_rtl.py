# Solar Wine addition
"""Support RTEMS 5 Runtime Linker (RTL)"""
import gdb

from rtems_chains import RtemsChainControl


class RtemsRtlObjects(gdb.Command):
    """Display RTEMS RTL objects"""
    def __init__(self):
        super(RtemsRtlObjects, self).__init__(
            'rtems rtlobj', gdb.COMMAND_DATA, gdb.COMPLETE_NONE)

    def invoke(self, arg, from_tty):
        rtl_objects = RtemsChainControl(gdb.parse_and_eval('rtl.objects'))
        print('    .text                  .rodata                .data                  .bss                   name')
        for idx, rtl_obj in enumerate(rtl_objects.cast_nodes('rtems_rtl_obj')):
            if int(rtl_obj['aname']):
                rtl_obj_name = rtl_obj['aname'].string('ascii', 'ignore')
            else:
                rtl_obj_name = rtl_obj['oname'].string('ascii', 'ignore')
            text_base = int(rtl_obj['text_base'])
            text_size = int(rtl_obj['text_size'])
            const_base = int(rtl_obj['const_base'])
            const_size = int(rtl_obj['const_size'])
            data_base = int(rtl_obj['data_base'])
            data_size = int(rtl_obj['data_size'])
            bss_base = int(rtl_obj['bss_base'])
            bss_size = int(rtl_obj['bss_size'])
            print('%2d: %#010x..%#010x %#010x..%#010x %#010x..%#010x %#010x..%#010x %s' % (
                idx,
                text_base, text_base + text_size,
                const_base, const_base + const_size,
                data_base, data_base + data_size,
                bss_base, bss_base + bss_size,
                rtl_obj_name))


class RtemsLoadSymbols(gdb.Command):
    """Display commands to add symbols to the current environment

    Use 'rtems loadsymbols run' to run the command too
    """
    def __init__(self):
        super(RtemsLoadSymbols, self).__init__(
            'rtems loadsymbols', gdb.COMMAND_DATA, gdb.COMPLETE_NONE)

    def invoke(self, arg, from_tty):
        do_run = (arg == 'run')
        cmd = 'add-symbol-file "core-cpu3.prom"'
        print(cmd)
        if do_run:
            gdb.execute(cmd)
        rtl_objects = RtemsChainControl(gdb.parse_and_eval('rtl.objects'))
        for rtl_obj in rtl_objects.cast_nodes('rtems_rtl_obj'):
            if rtl_obj['aname']:
                continue
            rtl_obj_name = rtl_obj['oname'].string('ascii', 'ignore')
            if not rtl_obj_name.startswith('/eeprom'):
                continue
            text_base = int(rtl_obj['text_base'])
            const_base = int(rtl_obj['const_base'])
            data_base = int(rtl_obj['data_base'])
            bss_base = int(rtl_obj['bss_base'])
            cmd = 'add-symbol-file "{}"'.format(rtl_obj_name[1:])
            if text_base:
                cmd += ' -s .text {:#x}'.format(text_base)
            if const_base:
                cmd += ' -s .rodata {:#x}'.format(const_base)
            if text_base:
                cmd += ' -s .data {:#x}'.format(data_base)
            if text_base:
                cmd += ' -s .bss {:#x}'.format(bss_base)
            print(cmd)
            if do_run:
                gdb.execute(cmd)
        cmd = 'add-symbol-file "core-cpu3.exe"'
        print(cmd)
        if do_run:
            gdb.execute(cmd)
