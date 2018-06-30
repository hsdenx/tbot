# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_trigger_wdt.py
# simple trigger wdt with command tb.config.tc_lx_trigger_wdt_cmd
# End:

from tbotlib import tbot
import re

logging.info("args: %s", tb.config.tc_lx_trigger_wdt_cmd)

# set board state for which the tc is valid
tb.set_board_state("linux")

tb.eof_write_con_lx_cmd(tb.config.tc_lx_trigger_wdt_cmd)

tb.end_tc(True)
