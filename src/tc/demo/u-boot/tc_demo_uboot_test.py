# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# call testcases
# tc_demo_get_ub_code.py
# tc_demo_compile_install_test.py
#
# End:

from tbotlib import tbot

tb.eof_call_tc("tc_demo_get_ub_code.py")

tb.eof_call_tc("tc_demo_compile_install_test.py")

tb.end_tc(True)
