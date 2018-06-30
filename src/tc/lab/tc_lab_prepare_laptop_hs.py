# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_prepare_laptop_hs.py
#
# do setup needed for the laptop from hs, when used as
# lapPC
#
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd, tb.config.tc_workfd_check_if_dir_exists_name)

# setup ip addr for p2p1 interface
cmd = 'sudo ifconfig p2p1 192.168.2.1 up'
tb.write_lx_sudo_cmd_check(tb.workfd, cmd, tb.config.user, tb.config.ip)

# check if ftdi module is loaded, rmmod it if yes
cmd = 'sudo lsmod | grep ftdi'
ret = tb.write_lx_sudo_cmd_check(tb.workfd, cmd, tb.config.user, tb.config.ip, endTC = False)
if ret == True:
    cmd = 'sudo rmmod ftdi_sio'
    tb.write_lx_sudo_cmd_check(tb.workfd, cmd, tb.config.user, tb.config.ip)

tb.end_tc(True)
