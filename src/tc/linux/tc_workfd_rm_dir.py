# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# remove the path tb.config.tc_lab_rm_dir
#
# End:

from tbotlib import tbot

logging.info("arg: %s %s", tb.workfd.name, tb.config.tc_lab_rm_dir)

tb.set_board_state("lab")
if tb.workfd.name == "tb_con":
    tb.set_board_state("linux")

tmp = "rm -rf " + self.config.tc_lab_rm_dir
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
