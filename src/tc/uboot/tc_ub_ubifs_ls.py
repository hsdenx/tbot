# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubifs_ls.py
# - ls ubifs tb.config.tc_ub_ubifs_ls_dir
# End:

from tbotlib import tbot

logging.info("args: %s", tb.config.tc_ub_ubifs_ls_dir)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

c = tb.c_con
tmp = 'ubifsls ' + tb.config.tc_ub_ubifs_ls_dir
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'File not')
if ret == 'prompt':
    tb.end_tc(True)

tb.tbot_expect_prompt(c)
tb.end_tc(False)
