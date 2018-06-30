# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_linux_mkdir.py
# check if the directory tb.config.tc_workfd_linux_mkdir_dir exists.
# if not, create it
# End:

from tbotlib import tbot

logging.info("args: workfd: %s %s", tb.workfd, tb.config.tc_workfd_linux_mkdir_dir)

tb.config.tc_workfd_check_if_dir_exists_name = tb.config.tc_workfd_linux_mkdir_dir
ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
if ret == False:
    cmd = 'mkdir -p ' + tb.config.tc_workfd_linux_mkdir_dir
    tb.write_lx_cmd_check(tb.workfd, cmd)

tb.end_tc(True)
