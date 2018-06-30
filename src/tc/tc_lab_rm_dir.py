# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_rm_dir.py
# simple rm a directory on the lab
# End:

from tbotlib import tbot

tb.set_board_state("lab")

tmp = "rm -rf " + self.config.tc_lab_rm_dir
tb.write_lx_cmd_check(tb.c_ctrl, tmp)
tb.end_tc(True)
