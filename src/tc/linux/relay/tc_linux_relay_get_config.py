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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_linux_relay_get_config.py
# get relay tbot configuration
#
# input:
# tb.config.tc_linux_relay_set_port
# tb.config.tc_linux_relay_set_state
#
# output:
# tb.config.tc_linux_relay_set_tc
#   testcase which gets called for setting relay port  with state state
# also set the config variables for tb.config.tc_linux_relay_set_tc
# accordingly.
# End:

from tbotlib import tbot
from tbotlib import tb_call_tc

@tb_call_tc
def tc_linux_relay_get_config(tb, port, state):
    tb.log.info("setup port %s state %s." % (port, state))
    if port == 'bbb_bootmode':
        tb.config.tc_linux_relay_set_tc = 'tc_linux_relay_simple_set.py'
        tb.config.tc_linux_relay_simple_set_sudo = 'yes'
        tb.config.tc_linux_relay_simple_set_cmd = '/home/hs/Software/usbrelais/src/simple '
        if state == 'sd':
            tb.config.tc_linux_relay_simple_set_cmd += '1 1'
        else:
            tb.config.tc_linux_relay_simple_set_cmd += '0 1'
        return True

    tb.log.warn("port %s not known." % port)
    tb.event.create_event_log(tb.workfd, 're', "port %s not known." % port)
    return False
