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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_set_toolchain.py
# set the toolchain
# End:

from tbotlib import tbot

c = tb.c_ctrl
tmp = "eldk-switch -m -r " + tb.tc_lab_toolchain_rev + " " + tb.tc_lab_toolchain_name
tb.event.create_event('main', tb.boardname, "Toolchain", tmp)
tb.eof_write(c, tmp)
tb.eof_expect_string(c, 'using ELDK')
tb.end_tc(True)
