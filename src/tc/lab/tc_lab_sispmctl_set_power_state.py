# SPDX-License-Identifier: GPL-2.0
#
# Description:
# power on/off the board with Gembird Silver Shiels
#
# get the power state of the board through sispmctl tool
# and save it in tb.power_state
# find more information for the Gembird Silver Shield PM power controller:
# http://sispmctl.sourceforge.net/
#
# use testcase tc_lab_sispmctl_get_variables.py for setting
# the tb.config.gembird_serial and tb.config.gembird_index
# you need for the specific board.
#
# End:

from tbotlib import tbot

logging.info("args: %s %s %s", tb.config.boardname, tb.config.boardlabpowername, tb.power_state)

#set board state for which the tc is valid
tb.set_board_state("lab")

tb.eof_call_tc("tc_lab_sispmctl_get_variables.py")

c = tb.c_ctrl
oldt = c.get_timeout()
c.set_timeout(None)

if tb.power_state == 'on':
    opt = ' -o '
else:
    opt = ' -f '

idx = tb.config.gembird_index
serial = tb.config.gembird_serial
tmp = "sispmctl -D "+ serial + opt + idx
tb.eof_write(c, tmp)

searchlist = ["Check USB connections", "Switched"]
tmp = True
power_set = True
tb.power_state = 'undef'
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        power_set = False
    elif ret == '1':
        tmp = False
    elif ret == 'prompt':
        power_set = False
        tmp = False

if power_set == False:
    c.set_timeout(oldt)
    tb.end_tc(power_set)

searchlist = ["error", "on", "off", "Invalid"]
tmp = True
power_set = True
tb.power_state = 'undef'
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        power_set = False
    elif ret == '1':
        tb.power_state = 'on'
    elif ret == '2':
        tb.power_state = 'off'
    if ret == '3':
        power_set = False
    elif ret == 'prompt':
        tmp = False

c.set_timeout(oldt)
tb.end_tc(power_set)
