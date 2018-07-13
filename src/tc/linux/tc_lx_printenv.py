# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple printenv linux command
# End:

import re
from tbotlib import tbot

# here starts the real test
logging.info("linux printenv testcase")

# set board state for which the tc is valid
tb.set_board_state("linux")

tb.eof_write_con_lx_cmd('printenv')
tb.end_tc(True)
