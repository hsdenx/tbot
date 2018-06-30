# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c fipad -t tc_board_fipad.py
# start all U-Boot/linux testcases for the fipad board
# End:

from tbotlib import tbot

tb.eof_call_tc("tc_board_fipad_ub_tests.py")
tb.eof_call_tc("tc_board_fipad_linux.py")

# power off board at the end
#tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
