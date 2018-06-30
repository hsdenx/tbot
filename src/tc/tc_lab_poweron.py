# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple power on the board
# with name tb.config.boardname
# End:

from tbotlib import tbot

ret = tb.set_power_state(tb.config.boardname, "on")
if ret != True:
    tb.end_tc(False)

tb.end_tc(True)
