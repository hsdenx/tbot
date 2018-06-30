# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c smartweb -t tc_demo_part1.py
# start tc:
#
# - set workfd to c_ctrl
# - call tc_demo_uboot_test.py
#
# End:

from tbotlib import tbot

tb.workfd = tb.c_ctrl

tb.eof_call_tc("tc_demo_uboot_test.py")

tb.end_tc(True)
