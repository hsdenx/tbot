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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_set_toolchain.py
# set the toolchain
from tbotlib import tbot

tmp = "eldk-switch -m -r " + tb.tc_lab_toolchain_rev + " " + tb.tc_lab_toolchain_name
tb.eof_write_ctrl(tmp)
tb.eof_search_str_in_readline_ctrl("using ELDK")

tb.eof_read_end_state_ctrl(1)
tb.end_tc(True)
