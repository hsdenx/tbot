# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_read.py
# - read ubi volume tb.config.tc_ub_ubi_prep_offset to tb.tc_ub_ubi_read_addr
# with len tb.tc_ub_ubi_read_len
# End:

from tbotlib import tbot

logging.info("args: %s %s %s", tb.tc_ub_ubi_read_addr, tb.tc_ub_ubi_read_vol_name, tb.tc_ub_ubi_read_len)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = "ubi read " + tb.tc_ub_ubi_read_addr + " " + tb.tc_ub_ubi_read_vol_name
if tb.tc_ub_ubi_read_len != 'none':
    tmp += ' ' + tb.tc_ub_ubi_read_len

c = tb.c_con
tb.eof_write(c, tmp)

searchlist = ["bytes from volume"]
tmp = True
found = False
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        found = True
    elif ret == 'prompt':
        tmp = False

# clear ubi part from uboot cmd buffer
tb.eof_write(c, "ubi info")
tb.tbot_expect_prompt(c)

if found == False:
    tb.end_tc(False)

tb.end_tc(True)
