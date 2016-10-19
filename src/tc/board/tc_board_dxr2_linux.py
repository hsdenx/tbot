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
# Description:
# start with
# tbot.py -s lab_denx -c dxr2 -t tc_board_dxr2_linux.py
# start all linux testcases for the dxr2 board
# End:

from tbotlib import tbot

tb.workfd = tb.c_ctrl

#delete old u-boot source tree
tb.eof_call_tc("tc_workfd_rm_linux_code.py")

tb.eof_call_tc("tc_workfd_get_linux_source.py")

tb.eof_call_tc("tc_workfd_goto_linux_code.py")

#compile it
tb.config.tc_lab_toolchain_rev = '5.4'
tb.config.tc_lab_toolchain_name = 'armv5te'
tb.config.tc_workfd_compile_linux_clean = 'no'
tb.config.tc_workfd_compile_linux_boardname = 'am335x-dxr2'
tb.config.tc_workfd_compile_linux_load_addr = '0x80008000'
tb.config.tc_workfd_compile_linux_modules ='yes'
tb.config.tc_workfd_compile_linux_modules_path ='/opt/eldk-5.5/armv5te/rootfs-qte-sdk/home/hs/dxr2/modules'
tb.config.tc_workfd_compile_linux_dt_name = 'am335x-draco-ref-ddp.dtb'
tb.config.tc_workfd_compile_linux_fit_its_file = 'no'
tb.config.tc_workfd_compile_linux_fit_file = 'dxr2.itb'
tb.config.tc_workfd_compile_linux_append_dt = 'no'
tb.eof_call_tc("tc_workfd_compile_linux.py")

# copy files to tftpdir
tb.statusprint("copy files")
tb.config.tc_lab_cp_file_a = "/work/hs/tbot/linux-dxr2/arch/arm/boot/uImage"
tb.config.tc_lab_cp_file_b = "/tftpboot/dxr2/tbot/uImage-hs-cur"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.config.tc_lab_cp_file_a = "/work/hs/tbot/linux-dxr2/arch/arm/boot/dts/" + tb.config.tc_workfd_compile_linux_dt_name
tb.config.tc_lab_cp_file_b = "/tftpboot/dxr2/tbot/dxr2.dtb"
tb.eof_call_tc("tc_lab_cp_file.py")

#call ubot setenv
tb.set_board_state("u-boot")
tb.eof_write_cmd(tb.c_con, "version")

tb.workfd = tb.c_con
# start triggering wdt immediately
tb.eof_call_tc("tc_lx_trigger_wdt.py")

tb.statusprint("tc_shc linux dmesg checks")
checks = ['Siemens',
'Linux version',
'Kernel command line',
'Manufacturer ID: 0x2c',
'cmdlinepart partitions found on MTD device omap2-nand_concat',
'at24 0-0050: 16384 byte',
'input: gpio-keys'
]

for tb.config.tc_lx_dmesg_grep_name in checks:
    tb.eof_call_tc("tc_lx_dmesg_grep.py")

tb.statusprint("tc_mcx pinmux check")
files = ['src/files/dxr2_etamin_pinmux.reg']
for tb.config.tc_lx_create_reg_file_name in files:
    tb.eof_call_tc("tc_lx_check_reg_file.py")

tb.statusprint("ubi checks")
tb.eof_call_tc("tc_lx_ubi_tests.py")
tb.eof_call_tc("tc_board_dxr2_lx_ubi_tests.py")

# power off board at the end
#tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
