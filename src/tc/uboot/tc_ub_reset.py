# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# simply call U-Boots reset command
# This testcase works only on the console connection c_con
#
# End:

from tbotlib import tbot

# do not check error strings, as we want to reboot U-Boot
tb.c_con.set_check_error(False)

# reset the board
tb.write_stream(tb.c_con, "res")
tb.gotprompt = True

# get u-boot login
tb.set_board_state("u-boot")

# enable error strng checking now again
tb.c_con.set_check_error(True)

tb.end_tc(True)
