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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_goto_tbot_workdir.py
# go into the tbot work dir
# if not exist, create it
from tbotlib import tbot

logging.info("args: workfd: %s %s", tb.workfd, tb.tc_workfd_work_dir)

tmp = '[ ! -d "' + tb.tc_workfd_work_dir + '" ] && echo "Does not exist"'
tb.eof_write(tb.workfd, tmp)
ret = tb.eof_search_str_in_readline(tb.workfd, "Does not exist", 0)
if ret == True:
    # directory does not exist, create it
    cd_cmd_error_txt = "could not"
    tmp = "mkdir -p " + tb.tc_workfd_work_dir
    tb.eof_write(tb.workfd, tmp)
    tb.eof_search_str_in_readline_end(tb.workfd, cd_cmd_error_txt)
if ret == None:
    tb.end_tc(False)

cd_cmd_error_txt = "No such"
tmp = "cd " + tb.tc_workfd_work_dir
tb.eof_write_cmd(tb.workfd, tmp)
tb.end_tc(True)
