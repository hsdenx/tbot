# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# go into git source tree tb.config.tc_workfd_git_rebase_git_src_path
# checkout branch tb.config.tc_workfd_git_rebase_git_base_branch
# call "git fetch" and "git pull"
# checkout branch tb.config.tc_workfd_git_rebase_git_work_branch
# and rebase tb.config.tc_workfd_git_rebase_git_work_branch with
# tb.config.tc_workfd_git_rebase_git_base_branch
#
# used variables
#
# - tb.config.tc_workfd_git_rebase_git_src_path
#| path to source tree
#| default: ''
#
# - tb.config.tc_workfd_git_rebase_git_base_branch
#| branch name, which get rebased against tb.config.tc_workfd_git_rebase_git_work_branch
#| default: ''
#
# - tb.config.tc_workfd_git_rebase_git_work_branch
#| branch name with which tb.config.tc_workfd_git_rebase_git_base_branch gets rebased
#| default: ''
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_git_rebase_git_src_path', '')
tb.define_variable('tc_workfd_git_rebase_git_base_branch', '')
tb.define_variable('tc_workfd_git_rebase_git_work_branch', '')

logging.info("arg: %s", tb.workfd.name)

# save current pwd ?

base = os.path.basename(tb.config.tc_workfd_git_rebase_git_src_path)
tb.event.create_event('main', 'tc_workfd_git_rebase.py', 'SET_DOC_FILENAME_NOIRQ', 'git_rebase_' + base)
tb.write_lx_cmd_check(tb.workfd, 'cd ' + tb.config.tc_workfd_git_rebase_git_src_path)
tb.write_lx_cmd_check(tb.workfd, 'git checkout ' + tb.config.tc_workfd_git_rebase_git_base_branch)
tb.write_lx_cmd_check(tb.workfd, 'git fetch')
tb.write_lx_cmd_check(tb.workfd, 'git pull')
tb.write_lx_cmd_check(tb.workfd, 'git checkout ' + tb.config.tc_workfd_git_rebase_git_work_branch)
tb.write_lx_cmd_check(tb.workfd, 'git rebase ' + tb.config.tc_workfd_git_rebase_git_base_branch)
tb.event.create_event('main', 'tc_workfd_git_rebase.py', 'SET_DOC_FILENAME_NOIRQ_END', 'git_rebase_' + base)

# go back to old path ?
tb.end_tc(True)
