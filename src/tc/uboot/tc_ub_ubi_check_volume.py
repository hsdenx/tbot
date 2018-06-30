# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_check_volume.py
# - checks if ubi volume tb.config.tc_ub_ubi_load_name exists
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.config.tc_ub_ubi_load_addr, tb.config.tc_ub_ubi_load_name)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = "if ubi check  " + tb.config.tc_ub_ubi_load_name + "; then; echo OK; else; echo FAIL; fi"
tb.eof_write(tb.c_con, tmp)
ret = tb.tbot_expect_string(tb.c_con, 'FAIL')
if ret == 'prompt':
    tb.end_tc(True)

tb.tbot_expect_prompt(tb.c_con)
tb.end_tc(False)
