# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_rm_file.py
# simple rm directory tb.config.tc_workfd_rm_file_name on the lab
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd, tb.config.tc_workfd_rm_file_name)

tb.config.tc_workfd_check_if_file_exists_name = tb.config.tc_workfd_rm_file_name
ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
if ret == True:
    tmp = "rm " + tb.config.tc_workfd_rm_file_name
    tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
