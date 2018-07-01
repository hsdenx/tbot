# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# switch into yocto source directory $TBOT_BASEDIR_REPO
# created with repo tool.
#
# Which is tb.config.tc_lab_source_dir + "/repo-" + tb.config.boardlabname
#
# set tb.config.repo_name to "repo-" + tb.config.boardlabname
# and tb.config.repo_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.repo_name
# and set $TBOT_BASEDIR_REPO to tb.config.repo_fulldir_name
#
# used variables
#
# - tb.config.tc_workfd_goto_repo_code_dirext
#| if != 'none' add this string to tb.config.repo_name
#| default: 'none'
#
# - tb.config.tc_workfd_goto_repo_code_checked
#| variable at runtime set, do not set it from a config file
#| marker, if setup for this testcase is already done.
#
# - tb.config.repo_name
#| set to to "repo-" + tb.config.boardlabname
#
# - tb.config.repo_fulldir_name
#| set to tb.config.tc_lab_source_dir + "/" + tb.config.repo_name
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_goto_repo_code_dirext', 'none')

try:
    tb.config.tc_workfd_goto_repo_code_checked
except:
    tb.config.tc_workfd_goto_repo_code_checked = False

logging.info("args: %s %s", tb.workfd, tb.config.tc_workfd_goto_repo_code_checked)

if tb.config.tc_workfd_goto_repo_code_checked == False:
    # set some global config variables
    try:
        tb.config.repo_name
    except:
        tb.config.repo_name = "repo-" + tb.config.boardlabname
        if tb.config.tc_workfd_goto_repo_code_dirext != 'none':
            tb.config.repo_name = tb.config.repo_name + tb.config.tc_workfd_goto_repo_code_dirext

    # first check, that we are in our base dir
    tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")
    tb.config.repo_fulldir_name = "$TBOT_BASEDIR/" + tb.config.repo_name

    tb.event.create_event('main', 'tc_workfd_goto_repo_code.py', 'SET_DOC_FILENAME', 'set_repo_env_var')
    tmp = 'export TBOT_BASEDIR_REPO=' + tb.config.repo_fulldir_name
    tb.write_lx_cmd_check(tb.workfd, tmp)

    tb.event.create_event('main', 'tc_workfd_goto_repo_code.py', 'SET_DOC_FILENAME', 'check_repo_dir_exist')
    tb.config.tc_workfd_check_if_dir_exists_name = '$TBOT_BASEDIR_REPO'
    ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
    if ret == False:
        tb.config.tc_workfd_goto_repo_code_checked = True
        tb.end_tc(False)
 
# cd into repo code
tmp = "cd $TBOT_BASEDIR_REPO"
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
