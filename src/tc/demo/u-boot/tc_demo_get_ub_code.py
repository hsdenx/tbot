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
# python2.7 src/common/tbot.py -c tbot_board.cfg -t tc_demo_get_ub_code.py
# start tc:
# - rm old u-boot tree (if there is one)
# - tc_lab_get_uboot_source.py
# - 
# End:

from tbotlib import tbot

# delete old u-boot source tree
tb.eof_call_tc("tc_workfd_rm_uboot_code.py")

# call get u-boot source
tb.statusprint("get u-boot source")
tb.eof_call_tc("tc_lab_get_uboot_source.py")
tb.end_tc(True)
