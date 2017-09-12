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
# tbot.py -s lab_denx -c smartweb -t tc_demo_uboot_tests.py
# start all "standard" u-boot testcases
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# call tc tc_ub_load_board_env.py
tb.eof_call_tc("tc_ub_load_board_env.py")

tb.workfd = tb.c_ctrl
tb.statusprint("start all DUTS testcases")
tb.eof_call_tc("uboot/duts/tc_ub_start_all_duts.py")

# call test/py
tb.statusprint("u-boot test/py test")
tb.eof_call_tc("tc_ub_test_py.py")

tb.end_tc(True)
