# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# switch bootmode for the bbb
#
# - power off the board
# - set bootmode
#   2 states:
#   normal: we use emmc
#   recovery: we boot from sd card
#
# End:

from tbotlib import tbot

logging.info("arg: %s", tb.config.tc_board_bootmode)

tb.set_board_state("lab")
savefd = tb.workfd
tb.workfd = tb.c_ctrl

tb.eof_call_tc("tc_lab_poweroff.py")

# low = emmc boot
state = 'high'
if tb.config.tc_board_bootmode == 'normal':
    state = 'low'

tb.eof_call_tc("tc_workfd_set_gpio.py", highlow=state, gpio=tb.config.jumper)

tb.workfd = savefd
tb.end_tc(True)
