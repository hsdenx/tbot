# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
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
