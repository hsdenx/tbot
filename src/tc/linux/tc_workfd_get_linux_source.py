# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_linux_source.py
# get Linux source tb.config.tc_lab_get_linux_source_git_repo with "git clone"
# and go into the source tree.
# check out branch tc_lab_get_linux_source_git_branch if tc_lab_get_linux_source_git_commit_id == 'none'
# else checkout commit tc_lab_get_linux_source_git_commit_id
# Apply patches if needed with:
# tc_lab_apply_patches.py and tc_workfd_apply_local_patches.py
# End:

from tbotlib import tbot

try:
    tb.config.tc_lab_get_linux_source_git_commit_id
except:
    tb.config.tc_lab_get_linux_source_git_commit_id = 'none'

logging.info("args: workdfd: %s %s %s %s", tb.workfd.name, tb.config.tc_lab_get_linux_source_git_repo,
             tb.config.tc_lab_get_linux_source_git_branch, tb.config.tc_lab_apply_patches_dir)
logging.info("args: %s %s ", tb.config.tc_lab_get_linux_source_git_reference,
             tb.config.tc_lab_get_linux_source_git_repo_user)
logging.info("args: %s", tb.config.tc_lab_get_linux_source_git_commit_id)

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
