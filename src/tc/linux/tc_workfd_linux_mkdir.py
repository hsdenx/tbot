# SPDX-License-Identifier: GPL-2.0
#
# Description:
# check if the directory tb.config.tc_workfd_linux_mkdir_dir exists.
# if not, create it
#
# used variables
#
# - tb.config.tc_workfd_linux_mkdir_dir
#| directory which get created
#| default:
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_linux_mkdir_dir', '')
logging.info("args: workfd: %s", tb.workfd)

tb.config.tc_workfd_check_if_dir_exists_name = tb.config.tc_workfd_linux_mkdir_dir
ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
if ret == False:
    cmd = 'mkdir -p ' + tb.config.tc_workfd_linux_mkdir_dir
    tb.write_lx_cmd_check(tb.workfd, cmd)

tb.end_tc(True)
