# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_cd_to_dir.py
# simple cd into directory tb.config.tc_workfd_cd_name
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd, tb.config.tc_workfd_cd_name)

tb.config.tc_workfd_check_if_dir_exists_name = tb.config.tc_workfd_cd_name
tb.eof_call_tc("tc_workfd_check_if_dir_exist.py")
tmp = "cd " + tb.config.tc_workfd_cd_name
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.end_tc(True)
