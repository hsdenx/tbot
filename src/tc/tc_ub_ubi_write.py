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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_write.py
# - write image into ubi volume
from tbotlib import tbot

logging.info("args: %s %s %s", tb.tc_ub_ubi_write_addr, tb.tc_ub_ubi_write_vol_name, tb.tc_ub_ubi_write_len)

#set board state for which the tc is valid
tb.set_board_state("u-boot")

#tmp = "ubi write " + tb.tc_ub_ubi_write_addr + " " + tb.tc_ub_ubi_write_vol_name + " ${filesize}"
#does not work, beause console hangs when getting $ ... :-( ToDo
#or make a ub env command for this
#or get the filesize from the tftp...
tmp = "ubi write " + tb.tc_ub_ubi_write_addr + " " + tb.tc_ub_ubi_write_vol_name + ' ' + tb.tc_ub_ubi_write_len
tb.eof_write_con(tmp)
tb.eof_search_str_in_readline_con("written to volume")
tb.eof_read_end_state_con(0)

tmp = "ubi info l"
tb.eof_write_con(tmp)
tb.eof_read_end_state_con(1)

tb.end_tc(True)
