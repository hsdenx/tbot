# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple set default values for U-Boot testcases
#
# used variables
#
# End:

from tbotlib import tbot

tb.call_tc('tc_def_tbot.py')

tb.gotprompt = True
tb.end_tc(True)
