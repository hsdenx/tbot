# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get in linux bootcount value
# through file tb.config.tc_workfd_lx_get_bc_file
# if not found testcases end with failure
# value returned in var tb.lx_bc
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd.name, tb.config.tc_workfd_lx_get_bc_file)

tb.set_board_state("linux")
c = tb.workfd
tb.eof_write_cmd_get_line(c, "cat " + tb.config.tc_workfd_lx_get_bc_file)

tb.lx_bc = tb.ret_write_cmd_get_line
tb.lx_bc = tb.lx_bc.replace('\r\n', '')

logging.info("args: linux bc value: %s", tb.lx_bc)
tb.end_tc(True)
