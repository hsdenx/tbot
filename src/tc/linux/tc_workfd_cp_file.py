# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_cp_file.py
# simple copy file from tb.tc_workfd_cp_file_a to tb.tc_workfd_cp_file_b
# End:
from tbotlib import tbot

logging.info("args: workfd %s %s %s", tb.workfd, tb.tc_workfd_cp_file_a, tb.tc_workfd_cp_file_b)

tmp = "cp " + tb.tc_workfd_cp_file_a + " " + tb.tc_workfd_cp_file_b
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.end_tc(True)
