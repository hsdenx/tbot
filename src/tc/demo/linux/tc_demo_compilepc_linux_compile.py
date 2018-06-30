# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# - switch to compile PC (call tc_connect_to_compilepc.py)
# - call tc_demo_linux_compile.py
#
# !! changes tb.workfd !!
#
# End:

from tbotlib import tbot

tb.eof_call_tc("tc_connect_to_compilepc.py")

tb.eof_call_tc("tc_demo_linux_compile.py")

tb.end_tc(True)
