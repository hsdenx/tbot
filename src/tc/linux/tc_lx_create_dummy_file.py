# SPDX-License-Identifier: GPL-2.0
#
# Description:
# create a random dummy file tb.tc_lx_dummy_file_tempfile in tb.config.lab_tmp_dir
# on tb.c_con with bs = tb.tc_lx_dummy_file_bs and
# count = tb.tc_lx_dummy_file_count
#
# used variables
#
# - tb.config.tc_lx_dummy_file_tempfile
#| name of the created dummy file
#| testcase tc_lx_create_dummy_file.py adds fullpath
#| default: ''
#
# - tb.config.tc_lx_dummy_file_bs
#| dd bs paramter
#| default: ''
#
# - tb.config.tc_lx_dummy_file_count
#| dd count paramter
#| default: ''
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lx_dummy_file_tempfile', '')
tb.define_variable('tc_lx_dummy_file_count', '')
tb.define_variable('tc_lx_dummy_file_bs', '')

# set board state for which the tc is valid
tb.set_board_state("linux")

f = tb.config.lab_tmp_dir + tb.config.tc_lx_dummy_file_tempfile
tb.config.tc_lx_dummy_file_tempfile = f
tmp = "dd if=/dev/urandom of=" + f + " bs=" + tb.config.tc_lx_dummy_file_bs + " count=" + tb.config.tc_lx_dummy_file_count
tb.eof_write(tb.c_con, tmp)

ret = tb.tbot_expect_string(tb.c_con, 'copied')
if ret == 'prompt':
    tb.end_tc(False)

tb.tbot_expect_prompt(tb.c_con)
tb.end_tc(True)
