# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_create_dummy_file.py
# create a random dummy file tb.tc_lx_dummy_file_tempfile in linux
# on tb.c_con with bs = tb.tc_lx_dummy_file_bs and
# count = tb.tc_lx_dummy_file_count
# End:

from tbotlib import tbot

# here starts the real test
logging.info("linux create dummy file")

# set board state for which the tc is valid
tb.set_board_state("linux")

tmp = "dd if=/dev/urandom of=" + tb.tc_lx_dummy_file_tempfile + " bs=" + tb.tc_lx_dummy_file_bs + " count=" + tb.tc_lx_dummy_file_count
tb.eof_write(tb.c_con, tmp)

ret = tb.tbot_expect_string(tb.c_con, 'copied')
if ret == 'prompt':
    tb.end_tc(False)

tb.tbot_expect_prompt(tb.c_con)
tb.end_tc(True)
