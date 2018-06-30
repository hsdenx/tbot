# SPDX-License-Identifier: GPL-2.0
#
# Description:
# create ubi volume tb.config.tc_ub_ubi_create_vol_name with size
# tb.config.tc_ub_ubi_create_vol_sz
#
# used variables
#
# - tb.config.tc_ub_ubi_create_vol_name
#| volume name, which get created
#| default: tb.config.tc_ub_ubi_load_name
#
# - tb.config.tc_ub_ubi_create_vol_sz
#| size of volume which get created
#| default: '600000'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_ubi_create_vol_name', tb.config.tc_ub_ubi_load_name)
tb.define_variable('tc_ub_ubi_create_vol_sz', '600000')

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = 'ubi create ' + tb.config.tc_ub_ubi_create_vol_name + ' ' + tb.config.tc_ub_ubi_create_vol_sz
tb.eof_write(tb.c_con, tmp)
ret = tb.tbot_expect_string(tb.c_con, 'exit not allowed')
if ret == 'prompt':
    tb.end_tc(True)

tb.tbot_expect_prompt(tb.c_con)
tb.end_tc(True)
