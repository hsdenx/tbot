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
# python2.7 src/common/tbot.py -c tbot_tqm5200s.cfg -t tc_board_git_bisect.py
# get a source code with tc tb.board_git_bisect_get_source_tc
# and start a "git bisect" session
# current commit is bad
# good commit id is defined through board_git_bisect_good_commit
# tc for testing good or bad is board_git_bisect_call_tc
from tbotlib import tbot

logging.info("args: %s %s %s", tb.board_git_bisect_get_source_tc, tb.board_git_bisect_call_tc, tb.board_git_bisect_good_commit)

def send_cmd(tb, cmd):
    tb.eof_write_ctrl(cmd)
    tb.eof_read_end_state_ctrl(1)

#call get u-boot source
tb.statusprint("get source tree")
tb.eof_call_tc(tb.board_git_bisect_get_source_tc)

#git bisect start
send_cmd(tb, 'git bisect start')

#current version is bad
send_cmd(tb, 'git bisect bad')

#git bisect good commit
tmp = 'git bisect good ' + tb.board_git_bisect_good_commit
tb.eof_write_ctrl(tmp)
ret = tb.read_end(tb.channel_ctrl, 4, "Bisecting")
if ret != True:
    tb.end_tc(False)
#read commit id
tb.read_line(tb.channel_ctrl, 1)
commit = self.buf[0][1:8]
tb.eof_read_end_state_ctrl(1)

#do the steps
i = 0
inwhile = True
while inwhile:
    i += 1
    tb.statusprint("cycle %s" % (i))
    logging.info("cycle %s", i)
    ret = tb.call_tc(tb.board_git_bisect_call_tc)
    if ret == True:
        tmp = 'git bisect good'
    else:
        tmp = 'git bisect bad'
    tb.eof_write_ctrl(tmp)
    ret = tb.eof_search_str_in_readline(tb.channel_ctrl, "the first bad commit", 0)
    if ret == True:
        inwhile = False
        tb.eof_read_end_state_ctrl(1)

# print some statistic
send_cmd(tb, 'git bisect visualize')
send_cmd(tb, 'git bisect log')

# reset source tree
send_cmd(tb, 'git bisect reset')

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
