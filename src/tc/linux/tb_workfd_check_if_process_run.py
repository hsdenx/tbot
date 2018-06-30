# SPDX-License-Identifier: GPL-2.0
#
# Description:
# check if process with name
# tb.config.tc_workfd_check_if_process_run_name
# runs
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_check_if_process_run_name
except:
    tb.config.tc_workfd_check_if_process_run_name = 'none'


logging.info("args: workfd %s %s", tb.workfd.name, tb.config.tc_workfd_check_if_process_run_name)

tb.eof_write_cmd_get_line(tb.workfd, "ps | grep " + tb.config.tc_workfd_check_if_process_run_name + " | wc -l")

line = tb.ret_write_cmd_get_line.replace('\r\n', '')

if line == '1':
    tb.end_tc(False)

tb.end_tc(True)
