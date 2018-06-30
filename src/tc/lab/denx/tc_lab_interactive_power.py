# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_denx_power.py
# power on/off the board from hand
# End:

from tbotlib import tbot
import time

logging.info("args: %s %s %s", tb.config.boardname, tb.config.boardlabpowername, tb.power_state)

#set board state for which the tc is valid
tb.set_board_state("lab")

print("Please switch power %s" % tb.power_state)
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")

tb.end_tc(True)
