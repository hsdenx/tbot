# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get current branch, commit from git tree in directory
# tb.config.tc_git_get_branch_commit_tree
#
# save values in
# tb.config.tc_git_get_branch_commit_dirty
# tb.config.tc_git_get_branch_commit_branch
# tb.config.tc_git_get_branch_commit_commit
#
# used variables
#
# - tb.config.tc_git_get_branch_commit_tree
#|  path to the git tree, for which infos get collected
#|  default: ''
#
# - tb.config.tc_git_get_branch_commit_dirty
#| is tree tb.config.tc_git_get_branch_commit_tree dirty
#| default: no default, get set on runtime of tc_git_get_branch_commit.py
#
# - tb.config.tc_git_get_branch_commit_branch
#| current branch of tree tb.config.tc_git_get_branch_commit_tree
#| default: no default, get set on runtime of tc_git_get_branch_commit.py
#
# - tb.config.tc_git_get_branch_commit_commit
#| current commit of tree tb.config.tc_git_get_branch_commit_tree
#| default: no default, get set on runtime of tc_git_get_branch_commit.py
#
# End:

from tbotlib import tbot

tb.define_variable('tc_git_get_branch_commit_tree', '')
logging.info("args: %s", tb.workfd)

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
