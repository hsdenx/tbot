# SPDX-License-Identifier: GPL-2.0
#
# Description:
# set in linux bootcount value tb.lx_bc
# through file tb.config.tc_workfd_lx_get_bc_file
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s %s", tb.workfd.name, tb.config.tc_workfd_lx_get_bc_file, tb.lx_bc)

tb.set_board_state("linux")
c = tb.workfd
tb.write_lx_cmd_check(c, "echo " + tb.lx_bc + " > " + tb.config.tc_workfd_lx_get_bc_file)

tb.end_tc(True)
