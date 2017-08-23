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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_get_version.py
# get the linux version and create event LINUX_VERSION
# save the linux version in tb.config.tc_return
# End:

from tbotlib import tbot

logging.info("args: %s", tb.workfd.name)

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.workfd
tmp = 'cat /proc/version'
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'Linux version')
if ret == 'prompt':
    tb.end_tc(False)
ret = tb.tbot_expect_string(c, '\n')
if ret == 'prompt':
    tb.end_tc(False)
tb.config.tc_return = tb.buf.rstrip()
tb.event.create_event('main', tb.config.boardname, "LINUX_VERSION", tb.config.tc_return)
tb.tbot_expect_prompt(c)

tb.end_tc(True)
