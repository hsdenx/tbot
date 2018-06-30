# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_demo_get_ub_code.py")
tb.config.tc_demo_compile_install_test_poweroff = 'no'

tb.eof_call_tc("tc_demo_compile_install_test.py")

tb.end_tc(True)
