# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c shc -t tc_board_shc.py
# start all testcases for the shc board linux and linux-stable
# End:

from tbotlib import tbot

"""
tb.statusprint("tc_shc testing linux stable")
tb.eof_call_tc("tc_board_shc_tests.py")
"""
tb.statusprint("tc_shc testing linux mainline")
tb.eof_call_tc("tc_board_shc_compile_ml.py")

tb.config.ub_boot_linux_cmd = 'run tbot_boot_linux_ml'
tb.eof_call_tc("tc_board_shc_tests.py")
tb.end_tc(True)
