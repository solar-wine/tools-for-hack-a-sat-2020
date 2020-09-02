# Python script for GDB

Original source: <https://git.rtems.org/rtems-tools/tree/tools/gdb/python>

Adapted for RTEMS 5, which was not yet released as of 2020-08-09 but used in Hack-A-Sat final event.

# RTEMS GDB

GDB extensions to help accelarting RTEMS debugging.

## Usage

In parent directory (so in the root directory of this `git` project):
```console
# Copy here the firmware PROM (core-cpu3.prom) and ELF (core-cpu3.exe)
$ sha256sum core-cpu3.prom core-cpu3.exe
53d87829ca8d2a6354fda4604fd5e47f0937df82a757be8667cadd7a53328c06  core-cpu3.prom
f35c3b874745d2cabc3b127efce4f9ecedb74872f07dfde8a4b00cf704b3a1f8  core-cpu3.exe

# Extract the eeprom tar archive from the firmware (at ELF symbol eeprom_tar)
# This allows loading symbols from the .obj files (cFS modules)
$ dd if=core-cpu3.exe bs=1 skip=$((0x12dea0)) count=$((0x3a2000)) |tar x

# Launch QEMU-SPARC-RTEMS with gdb
$ ./launch-qemu.sh core-cpu3.prom -gdb tcp::1234

# In another terminal
$ gdb-multiarch -q \
    -ex 'target remote 127.0.0.1:1234' \
    -ex 'file core-cpu3.exe' \
    -ex 'source gdbpython/__init__.py' \
    -ex 'rtems rtlobj' \
    -ex 'rtems loadsymbols run'

Reading symbols from core-cpu3.exe...
RTEMS GDB Support
    .text                  .rodata                .data                  .bss                   name
 0: 0x00000000..0x00000000 0x00000000..0x00000000 0x00000000..0x00000000 0x00000000..0x00000000 rtems-kernel
 1: 0x40f2b438..0x40f2bdf0 0x40f2bdf8..0x40f2be22 0x40f2be30..0x40f2be38 0x40f2be40..0x40f2bf08 /eeprom/cfs_lib.obj
 2: 0x40f2ce20..0x40f3085c 0x40f30868..0x40f3121f 0x40f31238..0x40f31298 0x40f312a0..0x40f312a4 /eeprom/osk_app_lib.obj
 3: 0x40f34b30..0x40f63dac 0x40f63db8..0x40f659c8 0x00000000..0x00000000 0x00000000..0x00000000 /eeprom/expat_lib.obj
 4: 0x40f659d0..0x40f6bbe4 0x40f32cb8..0x40f33965 0x40f33970..0x40f33978 0x40f33980..0x40f33bf0 /eeprom/io_lib.obj
 5: 0x40f6c278..0x40f71b04 0x40f71b10..0x40f72baf 0x40f33e40..0x40f33e44 0x40f72bb8..0x40fc914a /eeprom/kit_sch.obj
 6: 0x40fc9bd0..0x40fcd944 0x40fcd950..0x40fce79c 0x40fce7b8..0x40fce7c2 0x40fce7d0..0x40ff6de4 /eeprom/uart_to_ci.obj
 7: 0x40ff7ba8..0x40ffcf90 0x40ffcf98..0x40ffde47 0x40ffde50..0x40ffde54 0x40ffde60..0x410117f8 /eeprom/eyassat_if.obj
 8: 0x41013cf8..0x4102c87c 0x4102c888..0x4102dfa0 0x4102dfb8..0x4102dfc0 0x4102dfc8..0x410541a4 /eeprom/ephem.obj
 9: 0x410550d8..0x4105bddc 0x4105bde8..0x4105d8f2 0x4105d900..0x4105d904 0x4105d910..0x4105eb04 /eeprom/ds.obj
10: 0x4105fae0..0x41066644 0x41066650..0x41067aa2 0x41067ab0..0x41067ab4 0x41067ac0..0x41069f58 /eeprom/fm.obj
11: 0x4106ab08..0x4106f678 0x4106f680..0x410705f9 0x41070608..0x4107060c 0x41070618..0x41070994 /eeprom/hs.obj
12: 0x41071198..0x41072e74 0x41072e80..0x4107355f 0x41073568..0x4107356c 0x41073578..0x41074db0 /eeprom/hk.obj
13: 0x41075800..0x410795a0 0x410795a8..0x4107a282 0x4107a290..0x4107a294 0x4107a2a0..0x4107a98c /eeprom/md.obj
14: 0x4107b620..0x41082ff4 0x41083000..0x4108470c 0x41084718..0x41084720 0x41084728..0x41084ac8 /eeprom/mm.obj
15: 0x41085920..0x4108e528 0x4108e530..0x4108fa82 0x4108fa90..0x4108fa94 0x4108faa0..0x41096a9c /eeprom/sc.obj
16: 0x41097e78..0x410a2aa0 0x410a2aa8..0x410a4f31 0x410a4f40..0x410a4f44 0x410a4f50..0x410a58a4 /eeprom/cs.obj
17: 0x410aa5e8..0x410d0eb0 0x410d0eb8..0x410d7ef0 0x410d7f08..0x410d8074 0x410d8080..0x41102b10 /eeprom/cf.obj
18: 0x41102b18..0x4110a824 0x4110a830..0x4110b775 0x410a6b10..0x410a6b14 0x4110b780..0x4110dcf8 /eeprom/lc.obj
19: 0x00000000..0x00000000 0x00000800..0x00000800 0xffffffff..0xffffffff 0x00000000..0x00000000 /etc/libdl.conf

...

(gdb) p EyasSatObj
$1 = (EYASSATOBJ_Class *) 0x40ffe0b8        // in eyassat_if.obj's .bss
(gdb) p PktMgr
$2 = (PKTMGR_Class *) 0x40fe1058            // in uart_to_ci.obj's .bss
(gdb) p &PktMgr
$3 = (PKTMGR_Class **) 0x40fce7d0 <PktMgr>  // in uart_to_ci.obj's .data
```

## GDB Commands Implemented

* `help rtems`: show available commands specific to RTEMS
* `rtems loadsymbols`: display commands to add symbols to the current environment
* `rtems rtlobj`: display RTEMS RTL objects
