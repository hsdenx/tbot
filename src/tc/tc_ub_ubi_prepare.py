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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_prepare.py
# - ubi prepare
from tbotlib import tbot

logging.info("args: %s %s", tb.tc_ub_ubi_prep_partname, tb.tc_ub_ubi_prep_offset)

#set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = "ubi part " + tb.tc_ub_ubi_prep_partname
if tb.tc_ub_ubi_prep_offset != 'none':
    tmp += " " + tb.tc_ub_ubi_prep_offset

tb.eof_write_con(tmp)
tb.eof_search_str_in_readline_con("available PEBs")

tb.end_tc(True)
