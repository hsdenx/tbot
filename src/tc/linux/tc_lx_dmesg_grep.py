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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_dmesg_grep.py
# check if string tb.tc_lx_dmesg_grep_name is in dmesg output.
# End:

from tbotlib import tbot

# here starts the real test
logging.info("args: %s", tb.tc_lx_dmesg_grep_name)

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.c_con
tmp = 'dmesg | grep \'' + tb.tc_lx_dmesg_grep_name + '\''
tb.eof_write(c, tmp)
tb.eof_expect_string(c, tb.tc_lx_dmesg_grep_name)

tb.end_tc(True)
