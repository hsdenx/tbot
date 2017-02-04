# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Description:
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_denx_get_power_state.py
# get the power state of the board, and save it in
# tb.power_state
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
