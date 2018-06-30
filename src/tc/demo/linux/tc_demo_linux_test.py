# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# - if tb.config.tc_board_bootmode_tc is defined
#   call tc tb.config.tc_board_bootmode_tc
#   (set bootmode for the board)
# - call tc_workfd_rm_linux_code.py
# - call tc_workfd_get_linux_source.py
# - call tc_workfd_goto_linux_code.py
# - call tc_demo_linux_compile.py
# - tc_demo_linux_testcases.py
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_board_bootmode_tc
except:
    tb.config.tc_board_bootmode_tc = ''

logging.info("args: %s %s", tb.workfd.name, tb.config.tc_board_bootmode_tc)

if tb.config.tc_board_bootmode_tc != '':
    tb.config.tc_board_bootmode = 'normal'
    tb.eof_call_tc(tb.config.tc_board_bootmode_tc)

# delete old linux source tree
tb.eof_call_tc("tc_workfd_rm_linux_code.py")

tb.eof_call_tc("tc_workfd_get_linux_source.py")

tb.eof_call_tc("tc_workfd_goto_linux_code.py")

# compile it
tb.eof_call_tc("tc_demo_linux_compile.py")

tb.eof_call_tc("tc_demo_linux_testcases.py")

tb.end_tc(True)
