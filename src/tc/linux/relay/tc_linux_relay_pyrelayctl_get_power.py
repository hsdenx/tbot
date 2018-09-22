# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get tb.power_state of the relay port with the testcases
# tc_linux_relay_pyrelayctl_get.py
#
# used variables:
# 
# - tb.config.tc_linux_relay_pyrelayctl_getconfig
#   testcase name which gets called for getting pyrelayctl
#   configuration
#
# - tb.config.tc_linux_relay_pyrelayctl_get_state
#   contains current state of the relay
#
# End:

from tbotlib import tbot

savefd = tb.workfd
tb.workfd = tb.c_ctrl

try:
    tb.config.tc_linux_relay_pyrelayctl_getconfig
except:
    tb.config.tc_linux_relay_pyrelayctl_getconfig = 'tc_linux_relay_pyrelayctl_getcfg.py'

logging.info("args: %s", tb.config.tc_linux_relay_pyrelayctl_getconfig)

tb.eof_call_tc(tb.config.tc_linux_relay_pyrelayctl_getconfig)

ret = tb.call_tc("tc_linux_relay_pyrelayctl_get.py")
tb.power_state = tb.config.tc_linux_relay_pyrelayctl_get_state

tb.workfd = savefd
tb.end_tc(ret)
