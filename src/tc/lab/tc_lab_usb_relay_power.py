# SPDX-License-Identifier: GPL-2.0
#
# Description:
# power on / off the board tb.config.boardlabpowername
# with testcase tc_linux_relay_simple_set.py
#
# simple util must be installed, source see
# src/files/relay/simple.c
#
# adapt dependend on tb.config.boardlabpowername
# which port you use..
#
# If you have more than one USB relay from sainsmart
# adapt simple.c to work with the serial ID, and adapt
# also tb.config.tc_linux_relay_simple_set_cmd
#
# End:

from tbotlib import tbot

logging.info("args: %s %s %s", tb.config.boardname, tb.config.boardlabpowername, tb.power_state)

#set board state for which the tc is valid
tb.set_board_state("lab")

if tb.config.boardlabpowername == 'pi':
    port = "1"
else:
    logging.error("define port for board %s on USB relay" % (tb.config.boardlabpowername))
    tb.end_tc(False)

if tb.power_state == 'on':
    state = "1"
else:
    state = "0"

tb.config.tc_linux_relay_simple_set_cmd = "simple " + state + " " + port
tb.eof_call_tc("tc_linux_relay_simple_set.py")

tb.end_tc(True)
