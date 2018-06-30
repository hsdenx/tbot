# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# search string tb.tc_workfd_grep_string in file tb.tc_workfd_grep_file
# grep options configurable through tb.config.tc_workfd_grep_option
# default '--color=never'
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_grep_option
except:
    tb.config.tc_workfd_grep_option = '--color=never'

logging.info("args: workfd: %s %s %s", tb.workfd.name, tb.tc_workfd_grep_file, tb.tc_workfd_grep_string)

c = tb.workfd

cmd = 'cat ' + tb.tc_workfd_grep_file + ' | grep ' + tb.config.tc_workfd_grep_option + ' ' + tb.tc_workfd_grep_string
tb.write_lx_cmd_check(c, cmd, split=100)

tb.end_tc(True)
