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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_upd_spl.py
# update new spl to board
# steps:
# - load tbot u-boot env vars
# - execute "run upd_spl"
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
tb.eof_write_con("print tbot_upd_spl")
tb.eof_read_end_state_con(1)
upd_fail = True
i = 0
retry = 2
while upd_fail == True:
    if i >= retry:
        # board now maybe without u-boot
        # try a save u-boot ?
        tb.end_tc(False)

    tb.eof_write_con("run tbot_upd_spl")
    searchlist = ["!= byte at", "error", "Retry count exceeded", "not defined"]
    tmp = True
    upd_fail = False
    while tmp == True:
        tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
        if tmp == 0:
            upd_fail = True
            tmp = True
        elif tmp == 1:
            upd_fail = True
            tmp = True
        elif tmp == 2:
            upd_fail = True
            tmp = True
        elif tmp == 3:
            upd_fail = True
            tmp = True
        elif tmp == None:
            tmp = True
        elif tmp == 'prompt':
            i += 1
            tmp = False

# "run tbot_cmp_uboot"
tb.eof_write_con("print tbot_cmp_spl")
tb.eof_read_end_state_con(1)
tb.eof_write_con("run tbot_cmp_spl")

# read "!=" -> error
tb.eof_search_str_in_readline_end_con("!=")

# reset the board
tb.eof_write_con("res")

# get u-boot login
tb.set_board_state("u-boot")

tb.end_tc(True)
