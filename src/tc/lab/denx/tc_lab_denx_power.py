# SPDX-License-Identifier: GPL-2.0
#
# Description:
# power on/off the board tb.config.boardlabpowername
# End:

from tbotlib import tbot

logging.info("args: %s %s %s", tb.config.boardname, tb.config.boardlabpowername, tb.power_state)

#set board state for which the tc is valid
tb.set_board_state("lab")

c = tb.c_ctrl
oldt = c.get_timeout()
c.set_timeout(None)
tmp = "remote_power " + tb.config.boardlabpowername + " " + tb.power_state
tb.eof_write(c, tmp)

searchlist = ["error"]
tmp = True
power_set = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        power_set = False
    elif ret == 'prompt':
        tmp = False

c.set_timeout(oldt)
tb.end_tc(power_set)
