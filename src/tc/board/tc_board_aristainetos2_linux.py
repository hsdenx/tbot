# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c aristainetos2 -t tc_board_aristainetos2_linux.py
# start all linux testcases for the aristainetos2 board
# End:

from tbotlib import tbot

tb.workfd = tb.c_ctrl

#delete old u-boot source tree
tb.eof_call_tc("tc_workfd_rm_linux_code.py")

tb.eof_call_tc("tc_workfd_get_linux_source.py")

tb.eof_call_tc("tc_workfd_goto_linux_code.py")

tb.eof_call_tc("tc_board_aristainetos2_linux_tests.py")

tb.end_tc(True)
