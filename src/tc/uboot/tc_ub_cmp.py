# SPDX-License-Identifier: GPL-2.0
#
# Description:
# compare the contents of tb.config.tc_ub_cmp_addr1 with
# tb.config.tc_ub_cmp_addr2 of tb.config.tc_ub_cmp_len
# bytes length
#
# used variables
#
# - tb.config.tc_ub_cmp_addr1
#| address one
#| default: ''
#
# - tb.config.tc_ub_cmp_addr2
#| address one
#| default: ''
#
# - tb.config.tc_ub_cmp_len
#| length of bytes which get compared
#| default: ''
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_cmp_addr1', '')
tb.define_variable('tc_ub_cmp_addr2', '')
tb.define_variable('tc_ub_cmp_len', '')

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = "cmp.b " + tb.config.tc_ub_cmp_addr1 + " " + tb.config.tc_ub_cmp_addr2 + " " + tb.config.tc_ub_cmp_len
c = tb.c_con
tb.eof_write(c, tmp)

searchlist = ["!= byte"]
tb.tbot_rup_error_on_strings(c, searchlist, endtc=True)
