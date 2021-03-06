# SPDX-License-Identifier: GPL-2.0
#
# Description:
# check if a device tb.config.tc_workfd_check_if_device_exists_name exist
# this tc returns always true, but sets
# tb.config.tc_return True or False, because we may not
# want to end testcase failed, if device not exists.
#
# used variables
#
# - tb.config.tc_workfd_check_if_device_exists_name
#| device name
#| default: ''
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_check_if_device_exists_name', '')
logging.info("args: workfd %s", tb.workfd)

tmp = 'test -c ' + tb.config.tc_workfd_check_if_device_exists_name
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.end_tc(True)
