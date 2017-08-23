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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_bdi_disconnect.py
# disconnect from the BDI
# - send bdi command "quit"
# - set tb.config.linux_prompt
# End:

from tbotlib import tbot

logging.info("args: %s %s %s", tb.config.board_has_debugger, tb.workfd.name,
             tb.config.lab_bdi_upd_uboot_bdi_prompt)

c = tb.workfd

# check if we are in the BDI
if c.get_prompt() != tb.config.lab_bdi_upd_uboot_bdi_prompt:
    tb.end_tc(False)

tb.write_stream(c, 'quit')
c.set_prompt(tb.config.linux_prompt)
tb.tbot_expect_prompt(c)
c.lineend = '\n'

tb.end_tc(True)
