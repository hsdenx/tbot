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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_ubi_attach.py
from tbotlib import tbot
import re

#here starts the real test
logging.info("args: %s %s %s", tb.tc_ubi_cmd_path, tb.tc_ubi_mtd_dev, tb.tc_ubi_vid_hdr_offset)

mtd_dev_nr = re.sub("[^0-9]", "", tb.tc_ubi_mtd_dev)
logging.info("mtd_dev_nr: %s", mtd_dev_nr)

#set board state for which the tc is valid
tb.set_board_state("linux")

def create_ubi_cmd(tb, cmd):
    tmp = tb.tc_ubi_cmd_path + '/' + cmd
    return tmp

tmp = create_ubi_cmd(tb, 'ubi-utils/ubiattach /dev/ubi_ctrl -m ' + mtd_dev_nr)
if tb.tc_ubi_vid_hdr_offset != 'default':
    tmp += ' -O ' + tb.tc_ubi_vid_hdr_offset

ret = True
i = 0
while ret == True:
    tb.eof_write_con(tmp)
    ret = tb.search_str_in_readline_con('error')
    if ret == True:
        if i == 0:
            i += 1
            ret = tb.call_tc("tc_lx_ubi_detach.py")
            if ret != True:
                tb.end_tc(False)
        else:
            tb.end_tc(False)
           
tb.flush_con()
tb.end_tc(True)
