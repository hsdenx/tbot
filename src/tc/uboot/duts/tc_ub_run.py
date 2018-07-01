# SPDX-License-Identifier: GPL-2.0
#
# Description:
# convert duts tests from:
#
# http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootRun.tc;h=44f8a0a0de256afdd95b5ec20d1d4570373aeb7d;hb=101ddd5dbd547d5046363358d560149d873b238a
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

cmdlist = [
"help run",
"setenv test echo This is a test\\;printenv ipaddr\\;echo Done.",
"printenv test",
"run test",
"setenv test",
"setenv test echo This is a test\\;printenv ipaddr\\;echo Done.",
"setenv test2 echo This is another Test\\;printenv hostname\\;echo Done.",
"printenv test test2",
"run test test2",
"setenv test test2"
]

tb.eof_write_cmd_list(tb.c_con, cmdlist)
tb.end_tc(True)
