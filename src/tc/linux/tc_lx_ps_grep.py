# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# check, if all strings in tb.config.tc_lx_ps_grep are
# in ps output.
#
#
# used variables
#
# - tb.config.tc_lx_ps_grep
#| list of strings, which must be in ps output
#| default: '[]'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lx_ps_grep', '[]')

c = tb.workfd

# set board state for which the tc is valid
tb.set_board_state("linux")

tb.config.tc_workfd_grep_file = 'gnlmpf'
cmd = 'ps > ' + tb.config.tc_workfd_grep_file
tb.write_lx_cmd_check(c, cmd)

for t in tb.config.tc_lx_ps_grep:
    tb.config.tc_workfd_grep_string = '"' + t + '"'
    tb.eof_call_tc("tc_workfd_grep.py")

tb.write_lx_cmd_check(c, 'rm ' + tb.config.tc_workfd_grep_file)
tb.end_tc(True)
