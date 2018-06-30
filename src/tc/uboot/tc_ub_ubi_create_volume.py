# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_create_volume.py
# - create ubi volume tb.config.tc_ub_ubi_create_vol_name with size
# tb.config.tc_ub_ubi_create_vol_sz
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.config.tc_ub_ubi_create_vol_name, tb.config.tc_ub_ubi_create_vol_sz)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = 'ubi create ' + tb.config.tc_ub_ubi_create_vol_name + ' ' + tb.config.tc_ub_ubi_create_vol_sz
tb.eof_write(tb.c_con, tmp)
ret = tb.tbot_expect_string(tb.c_con, 'exit not allowed')
if ret == 'prompt':
    tb.end_tc(True)

tb.tbot_expect_prompt(tb.c_con)
tb.end_tc(True)
