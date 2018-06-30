# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# switch bootmode for the bbb
#
# - power off the board
# - set bootmode
#   2 states:
#   normal: we use sd card
#   recovery: we boot from emmc
#
# End:

from tbotlib import tbot

logging.info("arg: %s", tb.config.tc_board_bootmode)

tb.set_board_state("lab")
savefd = tb.workfd
tb.workfd = tb.c_ctrl

tb.eof_call_tc("tc_lab_poweroff.py")

# low = sd card boot
if tb.config.tc_board_bootmode == 'normal':
    tb.write_lx_cmd_check(tb.c_ctrl, 'relais   relsrv-02-02  1  off')
else:
    tb.write_lx_cmd_check(tb.c_ctrl, 'relais   relsrv-02-02  1  on')

tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
