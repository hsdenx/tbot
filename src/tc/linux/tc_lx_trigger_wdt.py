# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple trigger wdt with command tb.config.tc_lx_trigger_wdt_cmd
#
# used variables
#
# - tb.config.tc_lx_trigger_wdt_cmd
#| command with which wdt gets triggered.
#| default: '/home/hs/wdt &'
#
# End:

from tbotlib import tbot
import re

tb.define_variable('tc_lx_trigger_wdt_cmd', '/home/hs/wdt &')

# set board state for which the tc is valid
tb.set_board_state("linux")

tb.eof_write_con_lx_cmd(tb.config.tc_lx_trigger_wdt_cmd)

tb.end_tc(True)
