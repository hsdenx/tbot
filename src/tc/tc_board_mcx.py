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
# python2.7 src/common/tbot.py -c tbot_mcx.cfg -t tc_board_mcx.py
# start all testcases for the mcx board linux stable and linux-ml
#
from tbotlib import tbot

tb.statusprint("tc_mcx testing linux stable")
tb.eof_call_tc("tc_board_mcx_tests.py")

tb.statusprint("tc_mcx testing linux mainline")
tb.ub_boot_linux_cmd = 'run tbot_boot_linux_ml'
tb.eof_call_tc("tc_board_mcx_tests.py")
tb.end_tc(True)
