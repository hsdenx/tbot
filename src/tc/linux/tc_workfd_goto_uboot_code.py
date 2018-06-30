# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_goto_uboot_code.py
# switch into U-Boot source tb.config.tc_lab_source_dir + "/u-boot-" + tb.config.boardlabname
# set tb.config.uboot_name to "u-boot-" + tb.config.boardlabname
# and tb.config.uboot_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.uboot_name
# and set $TBOT_BASEDIR_UBOOT to tb.config.uboot_fulldir_name
#
# End:

from tbotlib import tbot

logging.info("args: %s", tb.workfd.name)

tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")

try:
    tb.workfd.tc_workfd_goto_uboot_code_checked
except:
    tb.workfd.tc_workfd_goto_uboot_code_checked = False

if tb.workfd.tc_workfd_goto_uboot_code_checked == False:
    # set some global config variables
    tb.config.uboot_name = "u-boot-" + tb.config.boardlabname
    tb.config.uboot_fulldir_name = "$TBOT_BASEDIR/" + tb.config.uboot_name

    tmp = 'export TBOT_BASEDIR_UBOOT=' + tb.config.uboot_fulldir_name
    tb.write_lx_cmd_check(tb.workfd, tmp)

    tb.config.tc_workfd_check_if_dir_exists_name = '$TBOT_BASEDIR_UBOOT'
    ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
    if ret == False:
        tb.workfd.tc_workfd_goto_uboot_code_checked = True
        tb.end_tc(False)

tmp = "cd $TBOT_BASEDIR_UBOOT"
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
