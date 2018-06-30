# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c smartweb -t tc_demo_part3.py
# start tc:
# End:

from tbotlib import tbot

# set wordkfd to the connection we want to work on
tb.workfd = tb.c_ctrl

# set specific parameters for this demo
tb.config.board_git_bisect_get_source_tc = "tc_workfd_goto_uboot_code.py"
tb.config.board_git_bisect_call_tc = "tc_demo_compile_install_test.py"
tb.config.board_git_bisect_good_commit = "035ebf85b09cf11c820ae9eec414097420741abd"
tb.config.board_git_bisect_patches = 'none'

# start bisecting now
tb.eof_call_tc("tc_board_git_bisect.py")

tb.end_tc(True)
