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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_erase.py
# - erase an ubi device
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.eof_write_con("print tbot_ubi_erase")
tb.eof_read_end_state_con(1)

tb.eof_write_con("run tbot_ubi_erase")
searchlist = ["!= byte at", "error", "Retry count exceeded", "not defined"]
tmp = True
cmd_nok = False
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
    if tmp == 0:
        cmd_nok = True
        tmp = True
    elif tmp == 1:
        cmd_nok = True
        tmp = True
    elif tmp == 2:
        cmd_nok = True
        tmp = True
    elif tmp == 3:
        cmd_nok = True
        tmp = True
    elif tmp == 'prompt':
        tmp = False

if cmd_nok == True:
    tb.end_tc(False)

#reset the board ... as a ubi dettach writes
#into the mtd partition, which now is empty
tb.eof_write_con("res")

tb.set_board_state("u-boot")
tb.end_tc(True)
