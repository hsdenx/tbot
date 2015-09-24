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
# python2.7 src/common/tbot.py -c tbot_mcx.cfg -t tc_board_mcx.py
# start all testcases for the mcx board
#
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.statusprint("u-boot setenv")
#call ubot setenv
tb.eof_call_tc("tc_ub_setenv.py")

tb.statusprint("tc_shc linux dmesg checks")
tb.tc_lx_dmesg_grep_name = "htkw mcx"
tb.eof_call_tc("tc_lx_dmesg_grep.py")

tb.tc_lx_dmesg_grep_name = "Manufacturer ID: 0x2c"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.tc_lx_dmesg_grep_name = "ti_hecc 5c050000.hecc: device registered"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.tc_lx_dmesg_grep_name = "ehci-omap 48064800.ehci"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.tc_lx_dmesg_grep_name = "usb usb1: New USB device"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.tc_lx_dmesg_grep_name = "usb usb2: New USB device found"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.tc_lx_dmesg_grep_name = "rtc-ds1307 0-0068: setting system"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.tc_lx_dmesg_grep_name = "input: EP0700M06"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.tc_lx_dmesg_grep_name = "Initialized drm"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.tc_lx_dmesg_grep_name = "Initialized omapdrm"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.tc_lx_dmesg_grep_name = "asix 2-1.3:1.0 eth1: register"
tb.eof_call_tc("tc_lx_dmesg_grep.py")

#call linux tc_lx_partition_check.py
tb.eof_call_tc("tc_lx_partition_check.py")
tb.eof_call_tc("tc_lx_bonnie.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
