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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_upd_uboot.py
# update new uboot to board
# steps:
# - load tbot u-boot env vars
# - execute "run upd_uboot"
# - reset board
# - get u-boot
from tbotlib import tbot

logging.info("args: %s %s %s", tb.boardname, tb.ub_load_board_env_addr, tb.ub_load_board_env_subdir)

#set board state for which the tc is valid
tb.set_board_state("u-boot")

#call tc tc_ub_load_board_env.py
tb.eof_call_tc("tc_ub_load_board_env.py")

#start tbot_upd_uboot
# 'OK' must beread, if the board supports
# hush shell, best to run if then else with echoing
# OK ...
tb.eof_write_con("print tbot_upd_uboot")
tb.eof_read_end_state_con(1)
tb.eof_write_con("run tbot_upd_uboot")
tb.eof_search_str_in_readline_con("OK")

# "run tbot_cmp_uboot"
tb.eof_write_con("print tbot_cmp_uboot")
tb.eof_read_end_state_con(1)
tb.eof_write_con("run tbot_cmp_uboot")

# read "!=" -> error
tb.eof_search_str_in_readline_end_con("!=")

# reset the board
tb.eof_write_con("res")

# get u-boot login
tb.set_board_state("u-boot")

tb.end_tc(True)
