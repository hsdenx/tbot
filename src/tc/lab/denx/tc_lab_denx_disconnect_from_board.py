# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_denx_disconnect_from_board.py
# disconnect from board in denx vlab
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.workfd.name, tb.config.boardlabname)

# what do we need to send ???
tmp = ''
tb.eof_write(tb.workfd, tmp)

# set lab pc linux prompt
tb.workfd.set_prompt(tb.config.linux_prompt, 'linux')
# check if we get linux prompt
tb.tbot_expect_prompt(tb.workfd)
tb.end_tc(True)
