# SPDX-License-Identifier: GPL-2.0
#
# Description:
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
