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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_dmesg_grep.py
from tbotlib import tbot

#here starts the real test
logging.info("args: %s", tb.tc_lx_dmesg_grep_name)

#set board state for which the tc is valid
tb.set_board_state("linux")

tmp='dmesg | grep "' + tb.tc_lx_dmesg_grep_name + '"'
tb.eof_write_con(tmp)
tb.eof_search_str_in_readline_con(tb.tc_lx_dmesg_grep_name)
tb.eof_read_end_state_con(1)

tb.end_tc(True)
