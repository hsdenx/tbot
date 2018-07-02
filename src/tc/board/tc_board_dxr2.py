# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start all testcases for the dxr2 board
# End:

from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

# start all u-boot tests
tb.statusprint("start all u-boot testcases")
tb.eof_call_tc("tc_board_dxr2_ub.py")

# start all linux tests
tb.statusprint("start all linux testcases")
tb.eof_call_tc("tc_board_dxr2_linux.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
