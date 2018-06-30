# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_poweroff.py
# simple power off the board
# End:

from tbotlib import tbot

ret = tb.set_power_state(self.config.boardname, "off")
if ret != False:
    tb.end_tc(False)

tb.end_tc(True)
