# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_sispmctl_get_power_state.py
# get the power state of the board through sispmctl
# and save it in tb.power_state
# find more information for the Gembird Silver Shield PM power controller:
# http://sispmctl.sourceforge.net/
#
# use testcase "tc_lab_sispmctl_get_variables.py" for setting
# the serial and the index you need for the specific board.
#
# This file is an example for a setup, you need to adapt
# this to your needs.
#
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.config.boardname, tb.config.boardlabpowername)

#set board state for which the tc is valid
tb.set_board_state("lab")

tb.eof_call_tc("tc_lab_sispmctl_get_variables.py")

c = tb.c_ctrl
oldt = c.get_timeout()
c.set_timeout(None)

idx = tb.config.gembird_index
serial = tb.config.gembird_serial
tmp = "sispmctl -D "+ serial + " -g " + idx
tb.eof_write(c, tmp)

searchlist = ["Check USB connections", "Status"]
tmp = True
power_get = True
tb.power_state = 'undef'
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        power_get = False
    elif ret == '1':
        tmp = False
    elif ret == 'prompt':
        power_get = False
        tmp = False

if power_get == False:
    c.set_timeout(oldt)
    tb.end_tc(power_get)

searchlist = ["error", "on", "off", "Invalid"]
tmp = True
power_get = True
tb.power_state = 'undef'
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        power_get = False
    elif ret == '1':
        tb.power_state = 'on'
    elif ret == '2':
        tb.power_state = 'off'
    if ret == '3':
        power_get = False
    elif ret == 'prompt':
        tmp = False

c.set_timeout(oldt)
tb.end_tc(power_get)
