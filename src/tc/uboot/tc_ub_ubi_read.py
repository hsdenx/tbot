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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_read.py
# - read ubi volume tb.config.tc_ub_ubi_prep_offset to tb.tc_ub_ubi_read_addr
# with len tb.tc_ub_ubi_read_len
# End:

from tbotlib import tbot

logging.info("args: %s %s %s", tb.tc_ub_ubi_read_addr, tb.tc_ub_ubi_read_vol_name, tb.tc_ub_ubi_read_len)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = "ubi read " + tb.tc_ub_ubi_read_addr + " " + tb.tc_ub_ubi_read_vol_name
if tb.tc_ub_ubi_read_len != 'none':
    tmp += ' ' + tb.tc_ub_ubi_read_len

c = tb.c_con
tb.eof_write(c, tmp)

searchlist = ["bytes from volume"]
tmp = True
found = False
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        found = True
    elif ret == 'prompt':
        tmp = False

# clear ubi part from uboot cmd buffer
tb.eof_write(c, "ubi info")
tb.tbot_expect_prompt(c)

if found == False:
    tb.end_tc(False)

tb.end_tc(True)
