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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_denx_connect_to_board.py
# connect to board with connect
from tbotlib import tbot

logging.info("args: %s %s", tb.workfd, tb.boardlabname)

tmp = "connect " + tb.boardlabname
ret = tb.write_stream(tb.workfd, tmp)
if not ret:
    tb.end_tc(False)

searchlist = ["Unknown target", "Connect"]
tmp = True
connected = True
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
    if tmp == 0:
        connected = False
    elif tmp == None:
        # ! endless loop ...
        tmp = True
    elif tmp == 1:
        tmp = False

if not connected:
    tb.end_tc(False)

tb.end_tc(True)
