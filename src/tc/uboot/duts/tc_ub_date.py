# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_date.py
# convert duts tests from:
# http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootDate.tc;h=03b7d53fd93bd61381db4095a4bff58b1d1efff7;hb=101ddd5dbd547d5046363358d560149d873b238a
# End:

from tbotlib import tbot
from time import gmtime, strftime

# set board state for which the tc is valid
tb.set_board_state("u-boot")

ret = tb.write_cmd_check(tb.c_con, "help date", "Unknown command")
if ret == True:
    tb.end_tc(True)

tb.eof_write_cmd(tb.c_con, "date reset")
time=strftime("%m%d%H%M%Y.%S", gmtime())
tb.eof_write_cmd(tb.c_con, "date " + time)
tb.eof_write_cmd_check(tb.c_con, "date", "Date:")

tb.end_tc(True)
