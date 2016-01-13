# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# start with
# python2.7 src/common/tbot.py -c tbot_dxr2.cfg -t tc_board_dxr2_linux.py
# start all linux testcases for the dxr2 board
#
from tbotlib import tbot

tb.workfd = tb.channel_ctrl

#delete old u-boot source tree
tb.tc_lab_rm_dir = tb.tc_lab_source_dir + "/linux-" + tb.boardlabname
tb.eof_call_tc("tc_lab_rm_dir.py")

tb.eof_call_tc("tc_workfd_get_linux_source.py")

tmp = "cd " + tb.tc_lab_source_dir + "/linux-" + tb.boardlabname
tb.eof_write_lx_cmd_check(tb.workfd, tmp)

#compile it
tb.tc_lab_toolchain_rev = '5.4'
tb.tc_lab_toolchain_name = 'armv5te'
tb.tc_workfd_compile_linux_clean = 'no'
tb.tc_workfd_compile_linux_boardname = 'am335x-dxr2'
tb.tc_workfd_compile_linux_load_addr = '0x80008000'
tb.tc_workfd_compile_linux_modules ='yes'
tb.tc_workfd_compile_linux_modules_path ='/opt/eldk-5.5/armv5te/rootfs-qte-sdk/home/hs/dxr2/modules'
tb.tc_workfd_compile_linux_dt_name = 'am335x-draco-ref.dtb'
tb.tc_workfd_compile_linux_fit_its_file = 'no'
tb.tc_workfd_compile_linux_fit_file = 'dxr2.itb'
tb.tc_workfd_compile_linux_append_dt = 'no'
tb.eof_call_tc("tc_workfd_compile_linux.py")

# copy files to tftpdir
tb.statusprint("copy files")
tb.tc_lab_cp_file_a = "/work/hs/tbot/linux-dxr2/arch/arm/boot/uImage"
tb.tc_lab_cp_file_b = "/tftpboot/dxr2/tbot/uImage-hs-cur"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "/work/hs/tbot/linux-dxr2/arch/arm/boot/dts/" + tb.tc_workfd_compile_linux_dt_name
tb.tc_lab_cp_file_b = "/tftpboot/dxr2/tbot/dxr2.dtb"
tb.eof_call_tc("tc_lab_cp_file.py")

#call ubot setenv
tb.set_board_state("u-boot")
tb.eof_write_cmd(tb.channel_con, "version")

tb.workfd = tb.channel_con
# start triggering wdt immediately
tb.eof_call_tc("tc_lx_trigger_wdt.py")

tb.statusprint("tc_shc linux dmesg checks")
checks = ['Siemens',
'Linux version',
'Kernel command line',
'Manufacturer ID: 0x2c',
'9 cmdlinepart partitions found on MTD device omap2-nand_concat',
'at24 0-0050: 16384 byte',
'input: gpio-keys as /devices/gpio-keys/input/input0'
]

for tb.tc_lx_dmesg_grep_name in checks:
    tb.eof_call_tc("tc_lx_dmesg_grep.py")

tb.statusprint("tc_mcx pinmux check")
files = ['src/files/dxr2_etamin_pinmux.reg']
for tb.tc_lx_create_reg_file_name in files:
    tb.eof_call_tc("tc_lx_check_reg_file.py")

tb.statusprint("ubi checks")
tb.eof_call_tc("tc_lx_ubi_tests.py")
tb.eof_call_tc("tc_board_dxr2_lx_ubi_tests.py")

# power off board at the end
#tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
