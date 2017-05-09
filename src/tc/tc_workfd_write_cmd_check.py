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
# Wrap a testcase around tb.write_cmd_check.
#
# This testcase can be called via
# tb.call_tc('tc_workfd_write_cmd_check.py', cmd='foo', string='bar').
#
# End:

from tbotlib import tbot

args = ['cmd', 'string']
arg = tb.check_args(args)

command = arg.get('cmd')
string = arg.get('string')

logging.info("args: workfd %s %s %s", tb.workfd.name, command, string)

tb.eof_write_cmd_check(tb.workfd, command, string)

tb.end_tc(True)
