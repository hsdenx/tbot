# SPDX-License-Identifier: GPL-2.0
#
# Description:
# read ubi volume tb.config.tc_ub_ubi_prep_offset to tb.config.tc_ub_ubi_read_addr
# with len tb.config.tc_ub_ubi_read_len
#
# used variables
#
# - tb.config.tc_ub_ubi_read_addr
#| ram address for 'ubi read'
#| default: ''
#
# - tb.config.tc_ub_ubi_read_vol_name
#| ubi volume name, which get read into ram
#| default: ''
#
# - tb.config.tc_ub_ubi_read_len
#| length in bytes for 'ubi read'
#| default: ''
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_ubi_read_addr', '')
tb.define_variable('tc_ub_ubi_read_vol_name', '')
tb.define_variable('tc_ub_ubi_read_len', '')

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = "ubi read " + tb.config.tc_ub_ubi_read_addr + " " + tb.config.tc_ub_ubi_read_vol_name
if tb.config.tc_ub_ubi_read_len != 'none':
    tmp += ' ' + tb.config.tc_ub_ubi_read_len

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
