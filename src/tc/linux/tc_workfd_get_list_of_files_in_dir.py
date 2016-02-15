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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_get_list_of_files_in_dir.py
# get a list of files in a directory
from tbotlib import tbot

logging.info("args: workfd: %s %s %s", tb.workfd, tb.tc_workfd_get_list_of_files_dir,
             tb.tc_workfd_get_list_of_files_mask)

c = tb.c_con
tb.buf = c.get_log()

tb.list_of_files = []

tb.eof_write(tb.workfd, 'find ' + tb.tc_workfd_get_list_of_files_dir +
             ' -name  "' + tb.tc_workfd_get_list_of_files_mask + '"' +
             ' | sort')

tb.tbot_expect_prompt(tb.workfd)

tmp = tb.buf.lstrip('\r\n')
tmp = tmp.split('\r\n')
for line in tmp:
    tb.list_of_files.append(line)

tb.list_of_files.pop()
tb.end_tc(True)
