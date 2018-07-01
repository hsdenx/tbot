# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# check if repo cmd exists, if not try to set
# PATH variable stored in tb.config.tc_workfd_repo_path
#
# used variable:
#
# - tb.config.tc_workfd_repo_path
#| PATH to repo command. If 'repo' command is not found
#| add this path to PATH Environment variable.
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_repo_path', 'none')
try:
    tb.config.tc_workfd_repo_cmd_checked
except:
    tb.config.tc_workfd_repo_cmd_checked = False

logging.info("args: %s %s", tb.workfd, tb.config.tc_workfd_repo_cmd_checked)

if tb.config.tc_workfd_repo_cmd_checked == False:
    tb.config.tc_workfd_check_if_cmd_exist_cmdname = 'repo'
    ret = tb.call_tc("tc_workfd_check_if_cmd_exist.py")
    if ret == True:
        tb.config.tc_workfd_repo_cmd_checked = True
        tb.end_tc(True)

    # repo not found
    if tb.config.tc_workfd_repo_path == 'none':
        tb.end_tc(False)
    else:
        # set path stored in tb.config.tc_workfd_repo_path
        cmd = 'export PATH=' + tb.config.tc_workfd_repo_path + ':$PATH'
        tb.write_lx_cmd_check(tb.workfd, cmd)
        tb.eof_call_tc("tc_workfd_check_if_cmd_exist.py")
        tb.config.tc_workfd_repo_cmd_checked = True

tb.end_tc(True)
