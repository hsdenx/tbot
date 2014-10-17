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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_check_if_cmd_exist.py
# check if a command exists
# this tc returns always true, but sets
# tb.tc_return True or False, because we may not
# want to end testcase failed, if command not exists.
from tbotlib import tbot

logging.info("args: %s", tb.tc_lx_check_if_cmd_exist_cmdname)
#command -v foo >/dev/null 2>&1 || { echo >&2 "I require foo but it's not installed.  Aborting."; exit 1; }
tmp = 'command -v ' + tb.tc_lx_check_if_cmd_exist_cmdname + ' >/dev/null 2>&1 || { echo >&2 "not installed.";}'
tb.eof_write_con(tmp)
ret = tb.search_str_in_readline_con("not installed")
if ret == True:
    tb.tc_return = False
if ret == None:
    tb.tc_return = False
if ret == False:
    tb.tc_return = True

tb.eof_read_end_state_con(0)
tb.end_tc(True)
