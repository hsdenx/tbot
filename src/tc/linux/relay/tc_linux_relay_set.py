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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_linux_relay_set.py
# set relay port tb.config.tc_linux_relay_set_port to state
# tb.config.tc_linux_relay_set_state.
#
# you need to adapt tc_linux_relay_get_config.py, which does
# the mapping from port/state to your specific lab settings.
#
# End:

from tbotlib import tbot
from tbotlib import tb_call_tc

@tb_call_tc
def linux_relay_set_port(tb, c, port, state):
    import tc_linux_relay_get_config

    ret = tc_linux_relay_get_config.tc_linux_relay_get_config(tb, port, state)
    if ret == False:
        return False
    tb.eof_call_tc(tb.config.tc_linux_relay_set_tc)

    return True

if __name__ == "tbotlib":
    from tbotlib import tbot
    if tb.arguments and (tb.starttestcase == tb.calltestcase):
        port = tb.arguments.split()[0]
        state = tb.arguments.split()[1]
    else:
        port = tb.config.tc_linux_relay_set_port
        state = tb.config.tc_linux_relay_set_state

    ret = linux_relay_set_port(tb, tb.c_ctrl, port, state)
    tb.end_tc(ret)
