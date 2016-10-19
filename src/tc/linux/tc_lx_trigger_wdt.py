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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_trigger_wdt.py
# simple trigger wdt with command tb.config.tc_lx_trigger_wdt_cmd
# End:

from tbotlib import tbot
import re

logging.info("args: %s", tb.config.tc_lx_trigger_wdt_cmd)

# set board state for which the tc is valid
tb.set_board_state("linux")

tb.eof_write_con_lx_cmd(tb.config.tc_lx_trigger_wdt_cmd)

tb.end_tc(True)
