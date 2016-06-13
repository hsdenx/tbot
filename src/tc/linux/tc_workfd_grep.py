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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_grep.py
# search string in file
from tbotlib import tbot

logging.info("args: workfd: %s %s %s", tb.workfd.name, tb.tc_workfd_grep_file, tb.tc_workfd_grep_string)

c = tb.workfd
result = False

tmp = 'cat ' + tb.tc_workfd_grep_file + ' | grep --color=never ' + tb.tc_workfd_grep_string
tb.eof_write(c, tmp)

searchlist = [tb.tc_workfd_grep_string]
tmp = True
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(c, searchlist)
    if ret == 'prompt':
        tmp = False
    if ret == '0':
        result = True

tb.end_tc(result)
