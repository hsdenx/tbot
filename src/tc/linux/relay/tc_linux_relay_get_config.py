# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get relay tbot configuration
#
# used variables
#
# - tb.config.tc_linux_relay_simple_set_cmd
#| command string for simple command
#| default: '/home/hs/Software/usbrelais/src/simple '
#
# - tb.config.tc_linux_relay_simple_set_sudo
#| if 'yes' preceed tb.config.tc_linux_relay_simple_set_cmd
#| with sudo
#| default: 'yes'
#
# - tb.config.tc_linux_relay_set_tc
#| testcase which get called for setting the relay
#| default: 'tc_linux_relay_simple_set.py'
#
# End:

from tbotlib import tbot
from tbotlib import tb_call_tc

tb.define_variable('tc_linux_relay_set_tc', 'tc_linux_relay_simple_set.py')
tb.define_variable('tc_linux_relay_simple_set_sudo', 'yes')
tb.define_variable('tc_linux_relay_simple_set_cmd', '/home/hs/Software/usbrelais/src/simple ')

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
