# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_write.py
# - write image @ tb.config.tc_ub_ubi_write_addr to ubi volume
#   tb.config.tc_ub_ubi_write_vol_name with len tb.config.tc_ub_ubi_write_len
# End:

from tbotlib import tbot

logging.info("args: %s %s %s", tb.config.tc_ub_ubi_write_addr, tb.config.tc_ub_ubi_write_vol_name, tb.config.tc_ub_ubi_write_len)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

c = tb.c_con
# tmp = "ubi write " + tb.config.tc_ub_ubi_write_addr + " " + tb.config.tc_ub_ubi_write_vol_name + " ${filesize}"
# does not work, beause console hangs when getting $ ... :-( ToDo
# or make a ub env command for this
# or get the filesize from the tftp...
tmp = "ubi write " + tb.config.tc_ub_ubi_write_addr + " " + tb.config.tc_ub_ubi_write_vol_name + ' ' + tb.config.tc_ub_ubi_write_len
tb.eof_write(c, tmp)

searchlist = ["written to volume"]
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

tb.end_tc(found)
