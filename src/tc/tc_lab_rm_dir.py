# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple rm a directory tb.config.tc_lab_rm_dir
# in the lab.
# End:

from tbotlib import tbot

tb.set_board_state("lab")

tmp = "rm -rf " + tb.config.tc_lab_rm_dir
tb.write_lx_cmd_check(tb.c_ctrl, tmp)
tb.end_tc(True)
