# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get in uboot bootcount value
# if not found testcases end with failure
# value returned in var tb.ub_bc
# End:

from tbotlib import tbot

tb.set_board_state("u-boot")
c = tb.workfd
tb.eof_write_cmd_get_line(c, "printenv bootcount")

tb.ub_bc = 'not found'
if 'bootcount' in tb.ret_write_cmd_get_line:
    tmp = tb.ret_write_cmd_get_line.split('=')
    tb.ub_bc = tmp[1]
    tb.ub_bc = tb.ub_bc.replace('\r\n', '')

logging.info("args: u-boot bc value: %s", tb.ub_bc)
tb.end_tc(True)
