# SPDX-License-Identifier: GPL-2.0
#
# Description:
# write image @ tb.config.tc_ub_ubi_write_addr to ubi volume
# tb.config.tc_ub_ubi_write_vol_name with len tb.config.tc_ub_ubi_write_len
#
# used variables
#
# - tb.config.tc_ub_ubi_write_addr
#| RAM address of image, which gets written into ubi volume
#| default: '14000000'
#
# - tb.config.tc_ub_ubi_write_vol_name
#| ubi volume name in which the image gets written
#| default: tb.config.tc_ub_ubi_create_vol_name
#
# - tb.config.tc_ub_ubi_write_len
#| length in bytes which gets written into ubi volume
#| default: '0xc00000'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_ubi_write_addr', '14000000')
tb.define_variable('tc_ub_ubi_write_vol_name', tb.config.tc_ub_ubi_create_vol_name)
tb.define_variable('tc_ub_ubi_write_len', '0xc00000')

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
