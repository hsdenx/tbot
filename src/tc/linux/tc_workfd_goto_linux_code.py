# SPDX-License-Identifier: GPL-2.0
#
# Description:
# switch into linux source tb.config.tc_lab_source_dir + "/linux-" + tb.config.boardlabname
# set tb.config.linux_name to "linux-" + tb.config.boardlabname
# and tb.config.linux_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.linux_name
# and set $TBOT_BASEDIR_LINUX to tb.config.linux_fulldir_name
#
# used variables
#
# - tb.config.linux_name
#| "linux-" + tb.config.boardlabname
#| directory in lab source dir
#| default: get set from tc_workfd_goto_linux_code.py
#
# End:

from tbotlib import tbot

logging.info("args: %s", tb.workfd)

tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")

try:
    tb.workfd.tc_workfd_goto_linux_code_checked
except:
    tb.workfd.tc_workfd_goto_linux_code_checked = False

if tb.workfd.tc_workfd_goto_linux_code_checked == False:
    # set some global config variables
    tb.config.linux_name = "linux-" + tb.config.boardlabname
    tb.config.linux_fulldir_name = "$TBOT_BASEDIR/" + tb.config.linux_name

    tmp = 'export TBOT_BASEDIR_LINUX=' + tb.config.linux_fulldir_name
    tb.write_lx_cmd_check(tb.workfd, tmp)

    tb.config.tc_workfd_check_if_dir_exists_name = '$TBOT_BASEDIR_LINUX'
    ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
    if ret == False:
        tb.workfd.tc_workfd_goto_linux_code_checked = True
        tb.end_tc(False)

tmp = "cd $TBOT_BASEDIR_LINUX"
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
