# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_cmp.py
# - compare 2 the contents of tb.tc_ub_cmp_addr1 with tb.tc_ub_cmp_addr2
# bytes tb.tc_ub_cmp_len length
# End:

from tbotlib import tbot

logging.info("args: %s %s %s", tb.tc_ub_cmp_addr1, tb.tc_ub_cmp_addr2,
             tb.tc_ub_cmp_len)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = "cmp.b " + tb.tc_ub_cmp_addr1 + " " + tb.tc_ub_cmp_addr2 + " " + tb.tc_ub_cmp_len
c = tb.c_con
tb.eof_write(c, tmp)

searchlist = ["!= byte"]
tb.tbot_rup_error_on_strings(c, searchlist, endtc=True)
