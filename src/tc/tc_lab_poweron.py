# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_poweron.py
# simple power on the board
# End:

from tbotlib import tbot

ret = tb.set_power_state(self.config.boardname, "on")
if ret != True:
    tb.end_tc(False)

tb.end_tc(True)
