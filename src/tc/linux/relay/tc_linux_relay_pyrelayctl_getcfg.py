# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# set tb.config.tc_linux_relay_pyrelayctl_device and
# tb.config.tc_linux_relay_pyrelayctl_port dependend
# on tb.config.boardlabpowername
#
# for usage with testcase
# tc_linux_relay_pyrelayctl_set_power.py and
# tc_linux_relay_pyrelayctl_get_power.py 
#
# used variables:
#
# - tb.config.boardlabpowername
#   boards name in the lab.
#
# returns:
#
# - tb.config.tc_linux_relay_pyrelayctl_device
#   device used with pyrelayctl command.
#
# - tb.config.tc_linux_relay_pyrelayctl_port
#   port used with pyrealyctl command.
#
# End:

from tbotlib import tbot

logging.info("args: %s", tb.config.boardlabpowername)

if tb.config.boardlabpowername == 'bbb':
    tb.config.tc_linux_relay_pyrelayctl_device = 'A907PJK8'
    tb.config.tc_linux_relay_pyrelayctl_port = '2'

logging.info("result: device %s port %s", tb.config.tc_linux_relay_pyrelayctl_device, tb.config.tc_linux_relay_pyrelayctl_port)

tb.end_tc(True)
