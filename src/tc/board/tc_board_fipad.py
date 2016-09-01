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
# python2.7 src/common/tbot.py -c tbot_fipad.cfg -t tc_board_fipad.py
# start all U-Boot/linux testcases for the fipad board
#
from tbotlib import tbot

tb.eof_call_tc("tc_board_fipad_ub_tests.py")
tb.eof_call_tc("tc_board_fipad_linux.py")

# power off board at the end
#tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
