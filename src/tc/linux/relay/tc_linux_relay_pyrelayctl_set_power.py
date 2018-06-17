# SPDX-License-Identifier: GPL-2.0
#
# Description:
# set relay port with the pyrelayctl cmd to state
# tb.power_state with testcase
# tc_linux_relay_pyrelayctl_set.py
#
# relay info set from testcase
# tb.config.tc_linux_relay_pyrelayctl_getconfig
#
# used variables:
#
# - tb.config.tc_linux_relay_pyrelayctl_getconfig
#   used testcase name for getting pyrelayctl configuration
#
# - tb.config.tc_linux_relay_pyrelayctl_state
#   current state for the relay on device and port
#
# End:

from tbotlib import tbot

savefd = tb.workfd
tb.workfd = tb.c_ctrl

try:
    tb.config.tc_linux_relay_pyrelayctl_getconfig
except:
    tb.config.tc_linux_relay_pyrelayctl_getconfig = 'tc_linux_relay_pyrelayctl_getcfg.py'

logging.info("args: %s %s %s", tb.workfd.name, tb.power_state, tb.config.tc_linux_relay_pyrelayctl_getconfig)

tb.eof_call_tc(tb.config.tc_linux_relay_pyrelayctl_getconfig)

tb.config.tc_linux_relay_pyrelayctl_state = tb.power_state
tb.eof_call_tc("tc_linux_relay_pyrelayctl_set.py")

tb.workfd = savefd
tb.end_tc(True)
