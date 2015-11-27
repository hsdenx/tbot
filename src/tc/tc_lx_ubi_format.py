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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_ubi_format.py
from tbotlib import tbot
import re

#here starts the real test
logging.info("args: %s %s %s", tb.tc_ubi_cmd_path, tb.tc_ubi_mtd_dev, tb.tc_lx_ubi_format_filename)

#set board state for which the tc is valid
tb.set_board_state("linux")

def create_ubi_cmd(tb, cmd):
    tmp = tb.tc_ubi_cmd_path + '/' + cmd
    return tmp

tmp = create_ubi_cmd(tb, 'ubi-utils/ubiformat ' + tb.tc_ubi_mtd_dev + ' -y -f ' + tb.tc_lx_ubi_format_filename)
tb.eof_write_con(tmp)
ret = tb.search_str_in_readline_con('error')
if ret == True:
    tb.eof_read_end_state_con(1)

tb.flush_con()
tb.end_tc(True)
