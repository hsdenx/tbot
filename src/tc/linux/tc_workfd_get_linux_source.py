# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get Linux source tb.config.tc_lab_get_linux_source_git_repo with "git clone"
# and go into the source tree.
# check out branch tc_lab_get_linux_source_git_branch if tc_lab_get_linux_source_git_commit_id == 'none'
# else checkout commit tc_lab_get_linux_source_git_commit_id
# Apply patches if needed with:
# tc_lab_apply_patches.py and tc_workfd_apply_local_patches.py
#
# used variables
#
# - tb.config.tc_lab_get_linux_source_git_repo
#| git repo to checkout
#| default: '/home/git/linux.git'
#
# - tb.config.tc_lab_get_linux_source_git_branch
#| branch which get checkout
#| default: 'master'
#
# - tb.config.tc_lab_get_linux_source_git_reference
#| if != 'none' add --reference option to git clone
#| default: 'none'
#
# - tb.config.tc_lab_get_linux_source_git_commit_id
#| if != 'none' checkout commit id instead branch
#| default: 'none'
#
# - tb.config.tc_lab_get_linux_source_git_repo_user
#| if a username is needed for cloning
#| password comes from password.py
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lab_get_linux_source_git_repo', '/home/git/linux.git')
tb.define_variable('tc_lab_get_linux_source_git_branch', 'master')
tb.define_variable('tc_lab_get_linux_source_git_reference', 'none')
tb.define_variable('tc_lab_get_linux_source_git_repo_user', 'anonymous')
tb.define_variable('tc_lab_get_linux_source_git_commit_id', 'none')

logging.info("args: workdfd: %s %s", tb.workfd.name, tb.config.tc_lab_apply_patches_dir)

ret = tb.call_tc("tc_workfd_goto_linux_code.py")
if ret == False:
    linux_name = "linux-" + tb.config.boardlabname
    tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")
    # clone linux git
    if tb.config.tc_lab_get_linux_source_git_reference != 'none':
        opt = '--reference=' + tb.config.tc_lab_get_linux_source_git_reference + ' '
    else:
        opt = ''
    tmp = "git clone " + opt + tb.config.tc_lab_get_linux_source_git_repo + " " + linux_name
    tb.eof_write(tb.workfd, tmp)
    searchlist = ["Username", "Password", "Authentication failed", "Receiving"] # add here error cases
    tmp = True
    clone_ok = True
    while tmp == True:
        ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
        if ret == '0':
            tb.write_stream(tb.workfd, tb.config.tc_lab_get_linux_source_git_repo_user)
        if ret == '1':
            tb.write_stream_passwd(tb.workfd, tb.config.tc_lab_get_linux_source_git_repo_user,
                                   tb.config.tc_lab_get_linux_source_git_repo)
        if ret == '2':
            clone_ok = False
        if ret == '3':
            tb.tbot_trigger_wdt()
        elif ret == 'prompt':
            tmp = False

    if clone_ok != True:
        tb.end_tc(False)

    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

    tmp = "cd " + linux_name
    tb.write_lx_cmd_check(tb.workfd, tmp)

    if tb.config.tc_lab_get_linux_source_git_commit_id == 'none':
        # check out a specific branch
        tmp = "git checkout " + tb.config.tc_lab_get_linux_source_git_branch
        tb.write_lx_cmd_check(tb.workfd, tmp)
    else:
        # check out commit id
        tmp = "git reset --hard " + tb.config.tc_lab_get_linux_source_git_commit_id
        tb.write_lx_cmd_check(tb.workfd, tmp)

# check if there are patches to apply
tb.eof_call_tc("tc_lab_apply_patches.py")

# check if there are local "git am" patches to apply
tb.eof_call_tc("tc_workfd_apply_local_patches.py")

tb.end_tc(True)
