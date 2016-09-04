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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_goto_tbot_workdir.py
# go into the tbot work dir tb.tc_workfd_work_dir
# if not exist, create it
# End:

from tbotlib import tbot

logging.info("args: workfd: %s %s", tb.workfd, tb.tc_workfd_work_dir)

tmp = '[ ! -d "' + tb.tc_workfd_work_dir + '" ] && echo "Does not exist"'
tb.eof_write(tb.workfd, tmp)
ret = tb.tbot_expect_string(tb.workfd, 'Does not exist')
if ret != 'prompt':
    # directory does not exist, create it
    tmp = "mkdir -p " + tb.tc_workfd_work_dir
    tb.eof_write_lx_cmd_check(c, tmp)

tmp = "cd " + tb.tc_workfd_work_dir
tb.eof_write_lx_cmd_check(tb.workfd, tmp)
tb.end_tc(True)
