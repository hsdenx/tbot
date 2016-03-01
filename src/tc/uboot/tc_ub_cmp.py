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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_cmp.py
# - compare 2 the contents of tb.tc_ub_cmp_addr1 with tb.tc_ub_cmp_addr2
# bytes tb.tc_ub_cmp_len length
from tbotlib import tbot

logging.info("args: %s %s %s", tb.tc_ub_cmp_addr1, tb.tc_ub_cmp_addr2,
             tb.tc_ub_cmp_len)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = "cmp.b " + tb.tc_ub_cmp_addr1 + " " + tb.tc_ub_cmp_addr2 + " " + tb.tc_ub_cmp_len
c = tb.c_con
tb.eof_write(c, tmp)

searchlist = ["!= byte"]
tmp = True
same = True
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(c, searchlist)
    if ret == '0':
        same = False
    elif ret == 'prompt':
        tmp = False

tb.end_tc(same)