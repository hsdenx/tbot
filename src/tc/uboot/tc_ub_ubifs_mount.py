# SPDX-License-Identifier: GPL-2.0
#
# Description:
# mount ubifs tb.config.tc_ub_ubifs_volume_name
#
# used variables
#
# - tb.config.tc_ub_ubifs_volume_name
#| ubifs volume name which gets mounted with 'ubifsmount'
#| default: 'ubi:rootfs'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_ubifs_volume_name', 'ubi:rootfs')

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
