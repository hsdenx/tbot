# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple power off the board with name
# tb.config.boardname
# End:

from tbotlib import tbot

ret = tb.set_power_state(tb.config.boardname, "off")
if ret != False:
    tb.end_tc(False)

tb.end_tc(True)
