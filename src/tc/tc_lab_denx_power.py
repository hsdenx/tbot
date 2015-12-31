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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_denx_power.py
# power on/off the board 
from tbotlib import tbot

logging.info("args: %s %s %s", tb.boardname, tb.boardlabpowername, tb.power_state)

#set board state for which the tc is valid
tb.set_board_state("lab")

tmp = "remote_power " + tb.boardlabpowername + " " + tb.power_state
tb.eof_write_ctrl(tmp)

searchlist = ["error"]
tmp = True
power_set = True
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_ctrl, searchlist)
    if tmp == 0:
        power_set = False
        tmp = True
    elif tmp == None:
        #endless loop
        tmp = True
    elif tmp == 'prompt':
        tmp = False

tb.end_tc(power_set)
