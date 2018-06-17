# SPDX-License-Identifier: GPL-2.0
#
# Description:
# set relay port with the pyrelayctl cmd to state
# find the c source code for the pyrelayctl cmd here:
# 
# git clone https://github.com/xypron/pyrelayctl.git
#
# install python3-usb
# apt-get install python3-usb
#
# python3 setup.py build
# sudo python3 setup.py install
#
# add file /lib/udev/rules.d/60-relayctl.rules
# SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6001", GROUP="relayctl", MODE="660", ENV{MODALIAS}="ignore"
#
# (execute udevadm control --reload-rules)
#
# used variables:
#
# - tb.config.tc_linux_relay_pyrelayctl_state
#   state which get set
#
# - tb.config.tc_linux_relay_pyrelayctl_device
#   device on which state get set
#
# - tb.config.tc_linux_relay_pyrelayctl_port
#   port on the device for which the state get set
#
# End:

from tbotlib import tbot

logging.info("args: %s state %s", tb.workfd.name, tb.config.tc_linux_relay_pyrelayctl_state)
logging.info("args: device %s port %s", tb.config.tc_linux_relay_pyrelayctl_device, tb.config.tc_linux_relay_pyrelayctl_port)

path = '/work/tbot2go/tbot/src/pyrelayctl/examples/'
relcmd = 'relctl.py'
device = tb.config.tc_linux_relay_pyrelayctl_device
port = tb.config.tc_linux_relay_pyrelayctl_port

cmd = 'sudo ' + path + relcmd + ' -D ' + device
if (tb.config.tc_linux_relay_pyrelayctl_state == 'on'):
    cmd = cmd + ' -o ' + port
else:
    cmd = cmd + ' -f ' + port

tb.write_lx_sudo_cmd_check(tb.workfd, cmd, tb.config.user, tb.config.ip)

tb.end_tc(True)
