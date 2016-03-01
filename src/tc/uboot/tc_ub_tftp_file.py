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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_tftp_file.py
# load file tc_ub_tftp_file_name to tc_ub_tftp_file_addr
# with tftp command in uboot
from tbotlib import tbot

logging.info("args: %s %s %s", tb.boardname, tb.tc_ub_tftp_file_addr, tb.tc_ub_tftp_file_name)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

c = tb.c_con
tmp = 'tftp ' + tb.tc_ub_tftp_file_addr + ' ' + tb.tc_ub_tftp_file_name
tb.eof_write(c, tmp)
searchlist = ["Bytes transferred", "error", "Retry count exceeded"]
tmp = True
load_fail = True
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(c, searchlist)
    if ret == '0':
        load_fail = False
    elif ret == '1':
        load_fail = True
    elif ret == '2':
        load_fail = True
    elif ret == 'prompt':
        tmp = False

if load_fail == True:
    tb.end_tc(False)

tb.end_tc(True)