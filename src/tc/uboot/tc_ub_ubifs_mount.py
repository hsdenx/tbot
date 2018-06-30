# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubifs_mount.py
# - mount ubifs tb.config.tc_ub_ubifs_volume_name
# End:

from tbotlib import tbot

logging.info("args: %s", tb.config.tc_ub_ubifs_volume_name)

#set board state for which the tc is valid
tb.set_board_state("u-boot")

c = tb.c_con
tmp = 'ubifsmount ' + tb.config.tc_ub_ubifs_volume_name
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'Error')
if ret == 'prompt':
    tb.end_tc(True)

tb.tbot_expect_prompt(c)
tb.end_tc(False)
