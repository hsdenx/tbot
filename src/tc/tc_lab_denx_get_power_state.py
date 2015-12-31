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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_denx_get_power_state.py
# get the power state of the board, and save it in
# tb.power_state
from tbotlib import tbot

logging.info("args: %s %s", tb.boardname, tb.boardlabpowername)

#set board state for which the tc is valid
tb.set_board_state("lab")

tmp = "remote_power " + tb.boardlabpowername + " -l"
tb.eof_write_ctrl(tmp)

searchlist = ["error", "ON", "off"]
tmp = True
power_get = True
tb.power_state = 'undef'
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_ctrl, searchlist)
    if tmp == 0:
        power_get = False
        tmp = True
    elif tmp == 1:
        tb.power_state = 'on'
        tmp = True
    elif tmp == 2:
        tb.power_state = 'off'
        tmp = True
    elif tmp == None:
        #endless loop
        tmp = True
    elif tmp == 'prompt':
        tmp = False

tb.end_tc(power_get)
