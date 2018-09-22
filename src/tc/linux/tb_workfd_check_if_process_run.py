# SPDX-License-Identifier: GPL-2.0
#
# Description:
# check if proces with name
# tb.config.tc_workfd_check_if_process_run_name
# runs
#
# used variables
#
# - tb.config.tc_workfd_check_if_process_run_name
#| check if process with name tb.config.tc_workfd_check_if_process_run_name
#| runs.
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_check_if_process_run_name', 'none')

tb.eof_write_cmd_get_line(tb.workfd, "ps | grep " + tb.config.tc_workfd_check_if_process_run_name + " | wc -l")

line = tb.ret_write_cmd_get_line.replace('\r\n', '')

if line == '1':
    tb.end_tc(False)

tb.end_tc(True)
