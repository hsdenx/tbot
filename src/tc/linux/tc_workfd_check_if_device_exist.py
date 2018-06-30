# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_if_device_exist.py
# check if a device tb.config.tc_workfd_check_if_device_exists_name exist
# this tc returns always true, but sets
# tb.config.tc_return True or False, because we may not
# want to end testcase failed, if device not exists.
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd, tb.config.tc_workfd_check_if_device_exists_name)

tmp = 'test -c ' + tb.config.tc_workfd_check_if_device_exists_name
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.end_tc(True)
