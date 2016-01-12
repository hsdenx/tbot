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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_sudo_cp_file.py
# simple copy  file from a to b with sudo rights
#
from tbotlib import tbot
logging.info("args: workfd %s %s %s", tb.workfd, tb.tc_workfd_cp_file_a, tb.tc_workfd_cp_file_b)

tb.eof_write(tb.workfd, "su")
tb.eof_search_str_in_readline(tb.workfd, "Password", 1)
tb.write_stream_passwd(tb.workfd, "root", "lab")
tmp = "\cp " + tb.tc_workfd_cp_file_a + " " + tb.tc_workfd_cp_file_b
tb.eof_write_lx_cmd_check(tb.workfd, tmp)

tb.eof_write_cmd(tb.workfd, "exit")
tb.end_tc(True)
