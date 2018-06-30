# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c boardname -t tc_workfd_linux_get_ifconfig.py
# read from tb.config.linux_get_ifconfig_dev the current
# ip addr and save it in tb.config.linux_get_ifconfig_ip
# broadcast and save it in tb.config.linux_get_ifconfig_broadcast
# mask and save it in tb.config.linux_get_ifconfig_mask
# End:

from tbotlib import tbot

tb.config.linux_get_ifconfig_dev = 'eth0'
tb.workfd = tb.c_con
tb.set_board_state("linux")

logging.info("args: workfd %s %s", tb.workfd.name, tb.config.linux_get_ifconfig_dev)

c = tb.workfd
dev = tb.config.linux_get_ifconfig_dev

cmd = 'ifconfig ' + dev + ' | grep "inet addr"'
tb.eof_write(c, cmd)
ret = True
suc = False
while ret:
    tmp = tb.tbot_rup_and_check_strings(c, '\n')
    if tmp == '0':
        # analyse string
        # inet addr:192.168.20.102  Bcast:192.168.255.255  Mask:255.255.0.0
        tmp = tb.buf.lstrip('\r\n')
        tmp = tmp.split('\r\n')
        tmp = tmp[0].split()
        if len(tmp) == 4:
            addr = tmp[1]
            bcas = tmp[2]
            mask = tmp[3]
            tmp = addr.split(':')
            tb.config.linux_get_ifconfig_ip = tmp[1]
            tmp = bcas.split(':')
            tb.config.linux_get_ifconfig_broadcast = tmp[1]
            tmp = mask.split(':')
            tb.config.linux_get_ifconfig_mask = tmp[1]
            suc = True
    if tmp == 'prompt':
        ret = False

tb.end_tc(suc)
