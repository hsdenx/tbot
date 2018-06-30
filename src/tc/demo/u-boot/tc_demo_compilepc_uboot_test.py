# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# - switch to compile PC (call tc_connect_to_compilepc.py)
# - call tc_demo_uboot_test.py
#
# !! changes tb.workfd !!
#
# End:

from tbotlib import tbot

tb.eof_call_tc("tc_connect_to_compilepc.py")

tb.eof_call_tc("tc_demo_uboot_test.py")

tb.config.create_documentation_auto = 'uboot'

tb.end_tc(True)
