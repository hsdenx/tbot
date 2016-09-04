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
# python2.7 src/common/tbot.py -c tbot_tqm5200s.cfg -t tc_board_git_bisect.py
# get a source code with tc tb.board_git_bisect_get_source_tc
# and start a "git bisect" session
# current commit is bad
# good commit id is defined through tb.board_git_bisect_good_commit
# tc for testing good or bad is tb.board_git_bisect_call_tc
# if you have some local patches, which needs to be applied
# each git bisect step, set tb.board_git_bisect_patches
# End:
from tbotlib import tbot

logging.info("args: %s %s %s %s", tb.board_git_bisect_get_source_tc, tb.board_git_bisect_call_tc, tb.board_git_bisect_good_commit, tb.board_git_bisect_patches)

#call get u-boot source
tb.statusprint("get source tree")
tb.eof_call_tc(tb.board_git_bisect_get_source_tc)

c = tb.c_ctrl
#git bisect start
tb.eof_write_cmd(c, 'git bisect start')

#current version is bad
tb.eof_write_cmd(c, 'git bisect bad')

#git bisect good commit
tmp = 'git bisect good ' + tb.board_git_bisect_good_commit
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'Bisecting')
if ret == 'prompt':
    tb.end_tc(False)
tb.tbot_expect_prompt(c)

#do the steps
i = 0
inwhile = True
error = False
while inwhile:
    i += 1
    tb.statusprint("cycle %s" % (i))
    logging.info("cycle %s", i)

    if tb.board_git_bisect_patches != 'none':
        tmp = tb.tc_lab_apply_patches_dir
        tb.eof_call_tc("tc_lab_apply_patches.py")
        tb.tc_lab_apply_patches_dir = tb.board_git_bisect_patches

    ret = tb.call_tc(tb.board_git_bisect_call_tc)
    if ret == True:
        tmp = 'git bisect good'
    else:
        tmp = 'git bisect bad'
    tb.eof_write(c, tmp)
    tmp2 = True
    se = ['the first bad commit', 'Aborting']
    while tmp2 == True:
        ret = tb.tbot_read_line_and_check_strings(c, se)
        if ret == '0':
            inwhile = False
        if ret == '1':
            inwhile = False
            error = True
        if ret == 'prompt':
            tmp2 = False

    if tb.board_git_bisect_patches != 'none':
        tb.eof_write_cmd(c, 'git reset --hard HEAD')
        tb.eof_write_cmd(c, 'git clean -f')

tb.tc_lab_apply_patches_dir = tmp

if error:
    tb.end_tc(False)

# print some statistic
tb.eof_write_cmd(c, 'git bisect visualize')
tb.eof_write_cmd(c, 'git bisect log')

# reset source tree
tb.eof_write_cmd(c, 'git bisect reset')

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
