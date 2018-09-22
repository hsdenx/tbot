# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple linux "uname -a" command
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.workfd
tmp = 'uname -a'
tb.eof_write_cmd(c, tmp)

tb.end_tc(True)
