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
# check if process with name
# tb.config.tc_workfd_check_if_process_run_name
# runs
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_check_if_process_run_name
except:
    tb.config.tc_workfd_check_if_process_run_name = 'none'


logging.info("args: workfd %s %s", tb.workfd.name, tb.config.tc_workfd_check_if_process_run_name)

tb.eof_write_cmd_get_line(tb.workfd, "ps | grep " + tb.config.tc_workfd_check_if_process_run_name + " | wc -l")

line = tb.ret_write_cmd_get_line.replace('\r\n', '')

if line == '1':
    tb.end_tc(False)

tb.end_tc(True)
