# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple linux "uname -a" command
# End:

from tbotlib import tbot

# here starts the real test
logging.info("args: %s", tb.workfd.name)

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.workfd
tmp = 'uname -a'
tb.eof_write_cmd(c, tmp)

tb.end_tc(True)
