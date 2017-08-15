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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_linux_relay_set.py
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
