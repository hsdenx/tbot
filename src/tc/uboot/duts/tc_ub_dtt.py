# SPDX-License-Identifier: GPL-2.0
#
# Description:
# convert duts tests from:
#
# http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootDtt.tc;h=e420c7b45cd73b00465d69f969039222868f4cc7;hb=101ddd5dbd547d5046363358d560149d873b238a
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

ret = tb.write_cmd_check(tb.c_con, "help dtt", "Unknown command")
if ret == True:
    tb.end_tc(True)

tb.eof_write_cmd_check(tb.c_con, "dtt", "DTT")
tb.end_tc(True)
