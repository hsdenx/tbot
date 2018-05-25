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
# check, if all strings in tb.config.tc_lx_ps_partitions are
# in "cat /proc/partitions" output.
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_lx_ps_partitions
except:
    tb.config.tc_lx_ps_partitions = []

logging.info("args: workfd: %s %s", tb.workfd.name, tb.config.tc_lx_ps_partitions)

c = tb.workfd

# set board state for which the tc is valid
tb.set_board_state("linux")

tb.tc_workfd_grep_file = 'gnlmpf'
cmd = 'cat /proc/partitions > ' + tb.tc_workfd_grep_file
tb.write_lx_cmd_check(c, cmd)

for t in tb.config.tc_lx_ps_partitions:
    tb.tc_workfd_grep_string = '"' + t + '"'
    tb.eof_call_tc("tc_workfd_grep.py")

tb.write_lx_cmd_check(c, 'rm ' + tb.tc_workfd_grep_file)
tb.end_tc(True)
