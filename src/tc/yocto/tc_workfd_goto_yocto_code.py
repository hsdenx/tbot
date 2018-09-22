# SPDX-License-Identifier: GPL-2.0
#
# Description:
# switch into yocto source tb.config.tc_lab_source_dir + "/yocto-" + tb.config.boardlabname
# set tb.config.yocto_name to "yocto-" + tb.config.boardlabname
# and tb.config.yocto_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.yocto_name
# and set $TBOT_BASEDIR_YOCTO to tb.config.yocto_fulldir_name
#
# used variables
#
# - tb.config.tc_workfd_goto_yocto_code_dirext
#| if != 'none' add this string to tb.config.yocto_name
#| default: 'none'
#
# - tb.workfd.tc_workfd_goto_yocto_code_path
#| if != 'none' tb.config.yocto_name = os.path.basename(tb.workfd.tc_workfd_goto_yocto_code_path)
#| default: 'none'
#
# - tb.workfd.tc_workfd_goto_yocto_code_checked
#| marker, if setup for this testcase is already done.
#| variable at runtime set, do not set it from a config file.
#
# - tb.config.yocto_fulldir_name
#| set at runtime, full path to yocto source code
#
# - tb.config.yocto_name
#| set at runtime, name of yocto source code directory
#| "yocto-" + tb.config.boardlabname
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_goto_yocto_code_dirext', 'none')
try:
    tb.workfd.tc_workfd_goto_yocto_code_checked
except:
    tb.workfd.tc_workfd_goto_yocto_code_checked = False

try:
    tb.workfd.tc_workfd_goto_yocto_code_path
except:
    tb.workfd.tc_workfd_goto_yocto_code_path = ''

logging.info("args: %s", tb.workfd.tc_workfd_goto_yocto_code_checked)
logging.info("args path: %s", tb.workfd.tc_workfd_goto_yocto_code_path)

if tb.workfd.tc_workfd_goto_yocto_code_checked == False:
    # set some global config variables
    try:
        tb.config.yocto_name
        logging.info("args yocto_name: %s", tb.config.yocto_name)
    except:
        if tb.workfd.tc_workfd_goto_yocto_code_path == '':
            tb.config.yocto_name = "yocto-" + tb.config.boardlabname
            if tb.config.tc_workfd_goto_yocto_code_dirext != 'none':
                tb.config.yocto_name = tb.config.yocto_name + tb.config.tc_workfd_goto_yocto_code_dirext
        else:
            tb.config.yocto_name = os.path.basename(tb.workfd.tc_workfd_goto_yocto_code_path)
        logging.info("args define yocto_name: %s", tb.config.yocto_name)

    # first check, that we are in our base dir
    tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")
    if tb.workfd.tc_workfd_goto_yocto_code_path == '':
        tb.config.yocto_fulldir_name = "$TBOT_BASEDIR/" + tb.config.yocto_name
    else:
        tb.config.yocto_fulldir_name = tb.workfd.tc_workfd_goto_yocto_code_path

    tb.event.create_event('main', 'tc_workfd_goto_yocto_code.py', 'SET_DOC_FILENAME', 'set_yocto_env_var')
    tmp = 'export TBOT_BASEDIR_YOCTO=' + tb.config.yocto_fulldir_name
    tb.write_lx_cmd_check(tb.workfd, tmp)

    tb.event.create_event('main', 'tc_workfd_goto_yocto_code.py', 'SET_DOC_FILENAME', 'check_yocto_dir_exist')
    tb.config.tc_workfd_check_if_dir_exists_name = '$TBOT_BASEDIR_YOCTO'
    ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
    if ret == False:
        tb.workfd.tc_workfd_goto_yocto_code_checked = True
        tb.end_tc(False)
 
# cd into yocto code
tmp = "cd $TBOT_BASEDIR_YOCTO"
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
