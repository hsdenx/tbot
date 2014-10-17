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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_load_board_env.py
# load U-Boot Environment for the board
#
from tbotlib import tbot

logging.info("args: %s %s %s", tb.boardname, tb.ub_load_board_env_addr, tb.ub_load_board_env_subdir)

#set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = 'mw ' + tb.ub_load_board_env_addr + ' 0 0x4000;tftp ' + tb.ub_load_board_env_addr + ' /tftpboot/' + tb.tftpboardname + '/' + tb.ub_load_board_env_subdir + '/env.txt;env import -t ' + tb.ub_load_board_env_addr
tb.eof_write_con(tmp)
ret = tb.eof_search_str_in_readline_con("Bytes transferred")

# ToDo check if env import has success
tb.eof_read_end_state_con(2)
tb.end_tc(True)
