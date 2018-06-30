# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# call testcases
# tc_connect_to_compilepc.py
# tc_demo_compile_install_test.py
#
# End:

from tbotlib import tbot

tb.eof_call_tc("tc_connect_to_compilepc.py")

tb.eof_call_tc("tc_demo_compile_install_test.py")

tb.end_tc(True)
