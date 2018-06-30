# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_linux_relay_set.py
# set relay port with the simple cmd to state
# find the c source code for the simple cmd in src/files/relay/simple.c
#
# tb.config.tc_linux_relay_simple_set_sudo if 'yes' "sudo" is perpended to
# tb.config.tc_linux_relay_simple_set_cmd and if password is needed, password
# is searched in password.py with board = tb.config.ip and user = tb.config.user + '_sudo'
#
# End:

from tbotlib import tbot

tb.workfd = tb.c_ctrl

logging.info("args: %s %s %s", tb.workfd.name, tb.config.tc_linux_relay_simple_set_sudo, tb.config.tc_linux_relay_simple_set_cmd)

if tb.config.tc_linux_relay_simple_set_sudo != 'none':
    pre = 'sudo '
else:
    pre = ''

tb.eof_write(tb.workfd, pre + tb.config.tc_linux_relay_simple_set_cmd, start=False)

searchlist = ['sudo', 'RES']
tmp = True
retu = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
       tb.write_stream_passwd(tb.workfd, tb.config.user + '_sudo', tb.config.ip)
    if ret == '1':
       retu = False
    elif ret == 'prompt':
       tmp = False

if retu == False:
        tb.end_tc(False)

tb.end_tc(True)
