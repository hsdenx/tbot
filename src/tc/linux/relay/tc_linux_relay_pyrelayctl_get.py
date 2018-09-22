# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get state of relay port
# tb.config.tc_linux_relay_pyrelayctl_device
# tb.config.tc_linux_relay_pyrelayctl_port
#
# with the pyrelayctl cmd
# and set state in
# tb.config.tc_linux_relay_pyrelayctl_get_state
# "on", "off" or "undef"
# 
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
# End:

from tbotlib import tbot

logging.info("args: device %s port %s", tb.config.tc_linux_relay_pyrelayctl_device, tb.config.tc_linux_relay_pyrelayctl_port)

path = '/work/tbot2go/tbot/src/pyrelayctl/examples/'
relcmd = 'relctl.py'
device = tb.config.tc_linux_relay_pyrelayctl_device
port = tb.config.tc_linux_relay_pyrelayctl_port

cmd = 'sudo ' + path + relcmd + ' -D ' + device + ' -g ' + port

tb.eof_write(tb.workfd, cmd)
lineport = 'status[' + port + ']'
searchlist = ['sudo', lineport, '\n']
tmp = True
found = False
tb.config.tc_linux_relay_pyrelayctl_get_state = 'undef'
while tmp == True:
    ret = self.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
        tb.write_stream_passwd(tb.workfd, tb.config.user + '_sudo', tb.config.ip)
    elif ret == '1':
        found = True
    elif ret == '2':
        if found == True and tb.config.tc_linux_relay_pyrelayctl_get_state == 'undef':
            if '0' in tb.buf.strip():
                tb.config.tc_linux_relay_pyrelayctl_get_state = 'off'
            else:
                tb.config.tc_linux_relay_pyrelayctl_get_state = 'on'
    elif ret == 'prompt':
        tmp = False
    else:
        self.tbot_trigger_wdt()

ret = self.call_tc("tc_workfd_check_cmd_success.py")

logging.info("result: %s", tb.config.tc_linux_relay_pyrelayctl_get_state)
tb.end_tc(ret)
