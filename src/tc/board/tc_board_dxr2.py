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
# tbot.py -s lab_denx -c dxr2 -t tc_board_dxr2.py
# start all testcases for the dxr2 board
# End:

from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

# start all u-boot tests
tb.statusprint("start all u-boot testcases")
tb.eof_call_tc("tc_board_dxr2_ub.py")

# start all linux tests
tb.statusprint("start all linux testcases")
tb.eof_call_tc("tc_board_dxr2_linux.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
