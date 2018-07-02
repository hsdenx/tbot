# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get the power state of the board tb.config.boardlabpowername,
# and save it in tb.power_state
#
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.config.boardname, tb.config.boardlabpowername)

#set board state for which the tc is valid
tb.set_board_state("lab")

c = tb.c_ctrl
oldt = c.get_timeout()
c.set_timeout(None)
tmp = "remote_power " + tb.config.boardlabpowername + " -l"
tb.eof_write(c, tmp)

searchlist = ["error", "ON", "off"]
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
    elif ret == 'prompt':
        tmp = False

c.set_timeout(oldt)
tb.end_tc(power_get)
