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
# python2.7 src/common/tbot.py -c tbot_shc.cfg -t tc_board_shc_ub_create_regdump.py
# create a uboot regdump for all interesting registers
# on the shc board
#
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.workfd = tb.c_con

tb.tc_ub_create_reg_file_name = 'src/files/shc_ub_pinmux_new.reg'
tb.tc_ub_create_reg_file_comment = 'pinmux'
tb.tc_ub_create_reg_file_start = '44e10800'
tb.tc_ub_create_reg_file_stop = '44e10a34'
tb.tc_ub_readreg_mask = '0xffffffff'
tb.tc_ub_create_reg_file_mode = 'w+'
tb.tc_ub_readreg_type = 'l'

# dump now pinmux registers
tb.eof_call_tc("tc_ub_create_reg_file.py")

# now append all further register dumps
tb.tc_ub_create_reg_file_mode = 'a'

tb.tc_ub_create_reg_file_comment = 'CM_PER'
tb.tc_ub_create_reg_file_start = '44e00000'
tb.tc_ub_create_reg_file_stop = '44e00154'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.tc_ub_create_reg_file_comment = 'CM_WKUP'
tb.tc_ub_create_reg_file_start = '44e00400'
tb.tc_ub_create_reg_file_stop = '44e004dc'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.tc_ub_create_reg_file_comment = 'CM_DPLL'
tb.tc_ub_create_reg_file_start = '44e00500'
tb.tc_ub_create_reg_file_stop = '44e00540'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.tc_ub_create_reg_file_comment = 'CM_MPU'
tb.tc_ub_create_reg_file_start = '44e00600'
tb.tc_ub_create_reg_file_stop = '44e00608'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.tc_ub_create_reg_file_comment = 'CM_RTC'
tb.tc_ub_create_reg_file_start = '44e00800'
tb.tc_ub_create_reg_file_stop = '44e00808'
tb.eof_call_tc("tc_ub_create_reg_file.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
