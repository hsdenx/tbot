# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# - switch to compile PC
# - call tc_demo_linux_test.py
#
# End:

from tbotlib import tbot

tb.eof_call_tc('tc_connect_to_compilepc.py')

tb.eof_call_tc("tc_demo_linux_test.py")

tb.end_tc(True)
