# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get the linux version and create event LINUX_VERSION
# save the linux version in tb.config.tc_return
# End:

from tbotlib import tbot

logging.info("args: %s", tb.workfd.name)

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.workfd
tmp = 'cat /proc/version'
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'Linux version')
if ret == 'prompt':
    tb.end_tc(False)
ret = tb.tbot_expect_string(c, '\n')
if ret == 'prompt':
    tb.end_tc(False)
tb.config.tc_return = tb.buf.rstrip()
tb.event.create_event('main', tb.config.boardname, "LINUX_VERSION", tb.config.tc_return)
tb.tbot_expect_prompt(c)

tb.end_tc(True)
