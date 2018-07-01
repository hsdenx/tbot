# SPDX-License-Identifier: GPL-2.0
#
# Description:
# ls ubifs tb.config.tc_ub_ubifs_ls_dir
#
# used variables
#
# - tb.config.tc_ub_ubifs_ls_dir
#| directory path which gets listed with 'ubifsls'
#| default: '/'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_ubifs_ls_dir', '/')

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
