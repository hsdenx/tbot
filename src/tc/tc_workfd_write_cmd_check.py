# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# Wrap a testcase around tb.write_cmd_check.
#
# This testcase can be called via
# tb.call_tc('tc_workfd_write_cmd_check.py', cmd='foo', string='bar').
#
# End:

from tbotlib import tbot

args = ['cmd', 'string']
arg = tb.check_args(args)

command = arg.get('cmd')
string = arg.get('string')

logging.info("args: workfd %s %s %s", tb.workfd.name, command, string)

tb.eof_write_cmd_check(tb.workfd, command, string)

tb.end_tc(True)
