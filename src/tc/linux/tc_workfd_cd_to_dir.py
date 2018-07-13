# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple cd into directory tb.config.tc_workfd_cd_name
#
# used variables
#
# - tb.config.tc_workfd_cd_name
#| name of path
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_cd_name', 'none')
logging.info("args: workfd %s", tb.workfd)

tb.config.tc_workfd_check_if_dir_exists_name = tb.config.tc_workfd_cd_name
tb.eof_call_tc("tc_workfd_check_if_dir_exist.py")
tmp = "cd " + tb.config.tc_workfd_cd_name
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.end_tc(True)
