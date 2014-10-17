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
# python2.7 src/common/tbot.py -c tbot_shc.cfg -t tc_board_shc.py
# start all testcases for the shc board
#
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.statusprint("tc_shc u-boot setenv")
#call ubot setenv
tb.eof_call_tc("tc_ub_setenv.py")

tb.statusprint("tc_shc partition check ")
#call linux tc_lx_partition_check.py
#for testing usb memstick
#check if usb stick is authorized
tb.eof_call_tc("tc_lx_check_usb_authorized.py")
tb.eof_call_tc("tc_lx_partition_check.py")
tb.eof_call_tc("tc_lx_bonnie.py")

tb.statusprint("tc_shc eeprom check ")
#gpio 2_5 is eeprom WP
#low = write protect
tb.tc_lx_eeprom_wp_gpio='69'
tb.tc_lx_eeprom_wp_val='0'
#call linux tc_lx_eeprom.py
tb.eof_call_tc("tc_lx_eeprom.py")

#call linux tc_lx_cpufreq.py
tb.statusprint("tc_shc cpu frequenc check")
tb.eof_call_tc("tc_lx_cpufreq.py")

tb.statusprint("tc_shc u-boot setenv")
#call ubot setenv
tb.eof_call_tc("tc_ub_setenv.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
