# SPDX-License-Identifier: GPL-2.0
#
# Description:
# checks if ubi volume tb.config.tc_ub_ubi_load_name exists
#
# used variables
#
# - tb.config.tc_ub_ubi_load_name
#| volume name
#| default: 'kernel'
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_ubi_load_name', 'kernel')

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = "if ubi check  " + tb.config.tc_ub_ubi_load_name + "; then; echo OK; else; echo FAIL; fi"
tb.eof_write(tb.c_con, tmp)
ret = tb.tbot_expect_string(tb.c_con, 'FAIL')
if ret == 'prompt':
    tb.end_tc(True)

tb.tbot_expect_prompt(tb.c_con)
tb.end_tc(False)
