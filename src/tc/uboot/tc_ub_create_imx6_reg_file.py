# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# creates U-Boot register dump files for an imx6 based board.
# using testcase tc_ub_create_reg_file.py
#
# dumps:
# - pinmux  20e0000 - 20e0950
#
# into files found in src/files/
# create for your board a subdir in the directory,
# and move the new created files into it, so you have
# them as a base for comparing further use.
#
# End:

import datetime
from tbotlib import tbot

logging.info("args: none")

# set board state for which the tc is valid
tb.set_board_state("u-boot")
tb.workfd = tb.c_con

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_imx6_pinmux.reg'
tb.config.tc_ub_create_reg_file_comment = 'imx6 pinmux'
tb.config.tc_ub_create_reg_file_start = '20e0000'
tb.config.tc_ub_create_reg_file_stop = '20e0950'
tb.config.tc_ub_readreg_mask = '0xffffffff'
tb.config.tc_ub_create_reg_file_mode = 'w+'
tb.config.tc_ub_readreg_type = 'l'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.end_tc(True)
