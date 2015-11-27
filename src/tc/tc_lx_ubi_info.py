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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_ubi_info.py
from tbotlib import tbot
import re

#here starts the real test
logging.info("args: %s %s", tb.tc_ubi_cmd_path, tb.tc_ubi_ubi_dev)

#set board state for which the tc is valid
tb.set_board_state("linux")

def create_ubi_cmd(tb, cmd):
    tmp = tb.tc_ubi_cmd_path + '/' + cmd
    return tmp

tmp = create_ubi_cmd(tb, 'ubi-utils/ubinfo ' + tb.tc_ubi_ubi_dev)
tb.eof_write_con(tmp)

searchlist = ["Present volumes", "error"]
tmp = True
volume_list = ""
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
    if tmp == 0:
        tmp=self.buf[tb.channel_con].split(":")[1]
        tmp=tmp.lstrip()
        volume_list = tmp.split(",")
        tmp = True
    elif tmp == 1:
        tb.eof_read_end_state_con(1)
        tb.end_tc(False)
    elif tmp == 'prompt':
        tmp = False

if volume_list != "":
    for vol in volume_list:
        vol = vol.lstrip()
        tmp = create_ubi_cmd(tb, 'ubi-utils/ubinfo ' + tb.tc_ubi_ubi_dev + '_' + vol)
        tb.eof_write_con(tmp)
        tb.eof_read_end_state_con(1)

tb.flush_con()
tb.end_tc(True)
