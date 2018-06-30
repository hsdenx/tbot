# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c shc -t tc_board_shc_ub_create_regdump.py
# create a uboot regdump for all interesting registers
# on the shc board
# End:

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
