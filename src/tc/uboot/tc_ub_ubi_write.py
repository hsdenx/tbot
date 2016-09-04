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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_write.py
# - write image @ tb.tc_ub_ubi_write_addr to ubi volume
#   tb.tc_ub_ubi_write_vol_name with len tb.tc_ub_ubi_write_len
# End:

from tbotlib import tbot

logging.info("args: %s %s %s", tb.tc_ub_ubi_write_addr, tb.tc_ub_ubi_write_vol_name, tb.tc_ub_ubi_write_len)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

c = tb.c_con
# tmp = "ubi write " + tb.tc_ub_ubi_write_addr + " " + tb.tc_ub_ubi_write_vol_name + " ${filesize}"
# does not work, beause console hangs when getting $ ... :-( ToDo
# or make a ub env command for this
# or get the filesize from the tftp...
tmp = "ubi write " + tb.tc_ub_ubi_write_addr + " " + tb.tc_ub_ubi_write_vol_name + ' ' + tb.tc_ub_ubi_write_len
tb.eof_write(c, tmp)

searchlist = ["written to volume"]
tmp = True
found = False
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(c, searchlist)
    if ret == '0':
        found = True
    elif ret == 'prompt':
        tmp = False

# clear ubi part from uboot cmd buffer
tb.eof_write(c, "ubi info")
tb.tbot_expect_prompt(c)

tb.end_tc(found)
