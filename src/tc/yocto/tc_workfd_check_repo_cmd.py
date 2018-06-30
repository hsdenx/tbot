# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_repo_cmd.py
#
# check if repo cmd exists, if not try to set
# PATH variable stored in tb.config.tc_workfd_repo_path
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_repo_cmd_checked
except:
    tb.config.tc_workfd_repo_cmd_checked = False

try:
    tb.config.tc_workfd_repo_path
except:
    tb.config.tc_workfd_repo_path = ''

logging.info("args: %s %s", tb.workfd, tb.config.tc_workfd_repo_cmd_checked)
logging.info("args: %s", tb.config.tc_workfd_repo_path)

if tb.config.tc_workfd_repo_cmd_checked == False:
    tb.config.tc_workfd_check_if_cmd_exist_cmdname = 'repo'
    ret = tb.call_tc("tc_workfd_check_if_cmd_exist.py")
    if ret == True:
        tb.config.tc_workfd_repo_cmd_checked = True
        tb.end_tc(True)

    # repo not found
    if tb.config.tc_workfd_repo_path == '':
        tb.end_tc(False)
    else:
        # set path stored in tb.config.tc_workfd_repo_path
        cmd = 'export PATH=' + tb.config.tc_workfd_repo_path + ':$PATH'
        tb.write_lx_cmd_check(tb.workfd, cmd)
        tb.eof_call_tc("tc_workfd_check_if_cmd_exist.py")
        tb.config.tc_workfd_repo_cmd_checked = True

tb.end_tc(True)
