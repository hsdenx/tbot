# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_info.py
# - simple print ubi info
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = "ubi info"
tb.eof_write_cmd(tb.c_con, tmp)

tmp = "ubi info l"
tb.eof_write_cmd(tb.c_con, tmp)

tb.end_tc(True)
