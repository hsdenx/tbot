# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get the power state of the board through user input,
# and save it in tb.power_state
#
# Currently nothing done.
#
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.config.boardname, tb.config.boardlabpowername)

#set board state for which the tc is valid
tb.set_board_state("lab")

print("Power State (on/off)\n")

# read this info from user ?
# tb.power_state = 'off'
# variable is set when calling tc_lab_interactive_power.py
# so in the first step, we do not read it from user
tb.end_tc(True)
