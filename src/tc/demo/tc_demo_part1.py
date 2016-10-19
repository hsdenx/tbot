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
# tbot.py -s lab_denx -c smartweb -t tc_demo_part1.py
# start tc:
# - call tc_demo_get_ub_code.py
# - call tc_demo_compile_install_test.py
# End:

from tbotlib import tbot

# get u-boot code
tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_demo_get_ub_code.py")

# compile, install and do tests
tb.eof_call_tc("tc_demo_compile_install_test.py")
tb.end_tc(True)
