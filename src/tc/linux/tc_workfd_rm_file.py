# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple rm file tb.config.tc_workfd_rm_file_name on the lab
#
# used variables tc_workfd_rm_file_name
#
# - tb.config.tc_workfd_rm_file_name
#| filenam which get removed (call rm tb.config.tc_workfd_rm_file_name)
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_rm_file_name', 'none')
logging.info("args: workfd %s", tb.workfd)

tb.config.tc_workfd_check_if_file_exists_name = tb.config.tc_workfd_rm_file_name
ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
if ret == True:
    tmp = "rm " + tb.config.tc_workfd_rm_file_name
    tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
