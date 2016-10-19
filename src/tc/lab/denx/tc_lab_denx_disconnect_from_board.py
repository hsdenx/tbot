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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_denx_disconnect_from_board.py
# disconnect from board in denx vlab
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.workfd.name, tb.config.boardlabname)

# what do we need to send ???
tmp = ''
tb.eof_write(tb.workfd, tmp)

# set lab pc linux prompt
tb.workfd.set_prompt(tb.config.linux_prompt)
# check if we get linux prompt
tb.tbot_expect_prompt(tb.workfd)
tb.end_tc(True)
