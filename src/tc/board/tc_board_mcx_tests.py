# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c mcx -t tc_board_mcx_tests.py
# start all testcases for the mcx board
# End:

from tbotlib import tbot

tb.workfd = tb.c_ctrl

tb.config.tc_workfd_apply_local_patches_checkpatch_cmd = 'scripts/checkpatch.pl'
tb.config.tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"

tb.eof_call_tc("tc_workfd_rm_linux_code.py")

#get linux code
tb.eof_call_tc("tc_workfd_get_linux_source.py")

tb.eof_call_tc("tc_workfd_goto_linux_code.py")

#compile it
tb.config.tc_lab_toolchain_rev = '5.4'
tb.config.tc_lab_toolchain_name = 'armv5te'
tb.config.tc_workfd_compile_linux_clean = 'no'
tb.config.tc_workfd_compile_linux_load_addr = '0x80008000'
tb.config.tc_workfd_compile_linux_modules ='yes'
tb.config.tc_workfd_compile_linux_modules_path ='/opt/eldk-5.5/armv5te/rootfs-qte-sdk/home/hs/mcx/modules'
tb.config.tc_workfd_compile_linux_dt_name = 'am3517-mcx.dtb'
tb.config.tc_workfd_compile_linux_fit_its_file = '/work/hs/tbot/files/kernel_fdt_mcx.its'
tb.config.tc_workfd_compile_linux_fit_file = 'mcx.itb'
tb.config.tc_workfd_compile_linux_append_dt = 'Image-self-mcx'
tb.eof_call_tc("tc_workfd_compile_linux.py")

# copy files to tftpdir
tb.statusprint("copy files")
c = tb.workfd
so = "/work/hs/tbot/linux-mcx/arch/arm/boot/uImage"
ta = "/tftpboot/mcx/tbot/uImage-hs-cur"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "/work/hs/tbot/linux-mcx/arch/arm/boot/dts/am3517-mcx.dtb"
ta = "/tftpboot/mcx/tbot/mcx.dtb"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

tb.set_board_state("u-boot")

tb.statusprint("u-boot setenv")
#call ubot setenv
tb.eof_call_tc("tc_ub_setenv.py")

tb.statusprint("tc_shc linux dmesg checks")
checks = ['htkw mcx',
'Linux version',
'Kernel command line',
'Manufacturer ID: 0x2c',
'5 cmdlinepart partitions found on MTD device omap2-nand.0',
'ti_hecc 5c050000.hecc: device registered',
'ehci-omap 48064800.ehci',
'usb usb1: New USB device',
'usb usb2: New USB device found',
'rtc-ds1307 0-0068: setting system',
'input: EP0700M06',
'Initialized drm',
'Initialized omapdrm']

for tb.config.tc_lx_dmesg_grep_name in checks:
    tb.eof_call_tc("tc_lx_dmesg_grep.py")

tb.statusprint("tc_mcx pinmux part 1 check")
files = ['src/files/mcx_pinmux_part1.reg',
'src/files/mcx_pinmux_part2.reg',
'src/files/mcx_pinmux_part3.reg',
'src/files/mcx_pinmux_part4.reg',
'src/files/mcx_pinmux_part5.reg',
'src/files/mcx_pinmux_part6.reg']
for tb.config.tc_lx_create_reg_file_name in files:
    tb.eof_call_tc("tc_lx_check_reg_file.py")

tb.statusprint("tc_mcx regulator check")
tb.eof_call_tc("tc_lx_regulator.py")

tb.workfd = tb.c_con
#call linux tc_lx_partition_check.py
tb.eof_call_tc("tc_lx_partition_check.py")
# only all 60 days
tb.tc_workfd_check_tc_time_timeout = 60 * 24 * 60 * 60
tb.eof_call_tc("tc_lx_bonnie.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
