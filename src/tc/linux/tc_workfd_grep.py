# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# search string tb.config.tc_workfd_grep_string in file tb.config.tc_workfd_grep_file
# grep options configurable through tb.config.tc_workfd_grep_option
# default '--color=never'
#
# used variables
#
# - tb.config.tc_workfd_grep_file
#| file in which we grep
#| default: ''
#
# - tb.config.tc_workfd_grep_string
#| string we search in file
#| default: ''
#
# - tb.config.tc_workfd_grep_option
#| grep options
#| default: '--color=never'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_grep_file', '')
tb.define_variable('tc_workfd_grep_string', '')
tb.define_variable('tc_workfd_grep_option', '--color=never')

c = tb.workfd

cmd = 'cat ' + tb.config.tc_workfd_grep_file + ' | grep ' + tb.config.tc_workfd_grep_option + ' ' + tb.config.tc_workfd_grep_string
tb.write_lx_cmd_check(c, cmd, split=100)

tb.end_tc(True)
