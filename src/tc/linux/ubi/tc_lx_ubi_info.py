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

# here starts the real test
logging.info("args: %s %s", tb.tc_ubi_cmd_path, tb.tc_ubi_ubi_dev)

# set board state for which the tc is valid
tb.set_board_state("linux")

def create_ubi_cmd(tb, cmd):
    tmp = tb.tc_ubi_cmd_path + '/' + cmd
    return tmp

tmp = create_ubi_cmd(tb, 'ubi-utils/ubinfo ' + tb.tc_ubi_ubi_dev)
c = tb.c_con
tb.eof_write(c, tmp)

searchlist = ["Present volumes", "error"]
tmp = True
volume_list = ""
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(c, searchlist)
    if ret == '0':
        ret = tb.tbot_expect_string(c, '\n')
        if ret == 'prompt':
            tb.end_tc(False)
        tmp2 = tb.buf.split(":")[1]
        tmp2 = tmp2[1:]
        tmp2 = tmp2.strip()
        volume_list = tmp2.split(",")
    elif ret == '1':
        tb.tbot_expect_prompt(c)
        tb.end_tc(False)
    elif ret == 'prompt':
        tmp = False

if volume_list != "":
    for vol in volume_list:
        vol = vol.lstrip()
        tmp = create_ubi_cmd(tb, 'ubi-utils/ubinfo ' + tb.tc_ubi_ubi_dev + '_' + vol)
        tb.eof_write(c, tmp)
        tb.tbot_expect_prompt(c)

tb.end_tc(True)
