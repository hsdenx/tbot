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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_check_if_cmd_exist.py
# check if a command exists
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd,
             tb.config.tc_workfd_check_if_cmd_exist_cmdname)

tmp = 'command -v ' + tb.config.tc_workfd_check_if_cmd_exist_cmdname + ' >/dev/null 2>&1 || { echo >&2 "not installed.";}'
tb.eof_write(tb.workfd, tmp)
searchlist = ["not installed"]
tmp = True
cmd_installed = True
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
        cmd_installed = False
    elif ret == 'prompt':
        tmp = False

tb.end_tc(cmd_installed)
