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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_git_get_branch_commit.py
# get current branch, commit from git tree in directory
# tb.config.tc_git_get_branch_commit_tree
#
# save values in
# tb.config.tc_git_get_branch_commit_dirty
# tb.config.tc_git_get_branch_commit_branch
# tb.config.tc_git_get_branch_commit_commit
#
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.workfd, tb.config.tc_git_get_branch_commit_tree)

c = tb.workfd

# get current path
cmd = "pwd"
tb.eof_write_cmd_get_line(c, cmd)
current_path = tb.ret_write_cmd_get_line

tb.write_lx_cmd_check(tb.workfd, 'cd ' + tb.config.tc_git_get_branch_commit_tree)

# is dirty:
tb.event.create_event('main', 'tc_git_get_branch_commit.py', 'SET_DOC_FILENAME', 'get_dirty')
cmd = "git diff --quiet --ignore-submodules HEAD 2>/dev/null; [ $? -eq 1 ] && echo 'dirty'"
tb.eof_write_cmd_get_line(c, cmd)
tb.config.tc_git_get_branch_commit_dirty = tb.ret_write_cmd_get_line

# branch:
tb.event.create_event('main', 'tc_git_get_branch_commit.py', 'SET_DOC_FILENAME', 'get_branch')
cmd ="git branch --no-color 2> /dev/null"
tb.eof_write_cmd_get_line(c, cmd)
tb.config.tc_git_get_branch_commit_branch = tb.ret_write_cmd_get_line

tb.event.create_event('main', 'tc_git_get_branch_commit.py', 'SET_DOC_FILENAME', 'get_commit')
# current commit
cmd = "git rev-parse --short HEAD 2> /dev/null"
tb.eof_write_cmd_get_line(c, cmd)
tb.config.tc_git_get_branch_commit_commit = tb.ret_write_cmd_get_line

# at end, go back to old path
tb.write_lx_cmd_check(tb.workfd, 'cd ' + current_path.strip())

tb.end_tc(True)
