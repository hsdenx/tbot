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
# python2.7 src/common/tbot.py -c tbot_mcx.cfg -t tc_board_mcx_tests.py
# start all testcases for the mcx board
#
from tbotlib import tbot

#set board state for which the tc is valid
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

for tb.tc_lx_dmesg_grep_name in checks:
    tb.eof_call_tc("tc_lx_dmesg_grep.py")

tb.statusprint("tc_mcx pinmux part 1 check")
files = ['src/files/mcx_pinmux_part1.reg',
'src/files/mcx_pinmux_part2.reg',
'src/files/mcx_pinmux_part3.reg',
'src/files/mcx_pinmux_part4.reg',
'src/files/mcx_pinmux_part5.reg',
'src/files/mcx_pinmux_part6.reg']
for tb.tc_lx_create_reg_file_name in files:
    tb.eof_call_tc("tc_lx_check_reg_file.py")

tb.statusprint("tc_mcx regulator check")
tb.eof_call_tc("tc_lx_regulator.py")

#call linux tc_lx_partition_check.py
tb.eof_call_tc("tc_lx_partition_check.py")
tb.eof_call_tc("tc_lx_bonnie.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
