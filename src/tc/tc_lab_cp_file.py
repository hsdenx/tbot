# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple copy  file from arg.get('s')
# to arg.get('t') on the channel arg.get('ch')
# End:

from tbotlib import tbot

args = ['ch', 's', 't']
arg = tb.check_args(args)

tmp = "cp " + arg.get('s') + " " + arg.get('t')
tb.write_lx_cmd_check(arg.get('ch'), tmp)
tb.end_tc(True)
