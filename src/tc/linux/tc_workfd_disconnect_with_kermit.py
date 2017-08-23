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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_connect_with_kermit.py
# disconnect from a kermit connection
# End:

from tbotlib import tbot

logging.info("args: workdfd: %s", tb.workfd)
logging.info("args: ssh: %s", tb.config.tc_workfd_connect_with_kermit_ssh)
logging.info("args: kermit: %s %s", tb.config.kermit_line, tb.config.kermit_speed)

string = pack('h', 28)
string = string[:1]
tb.workfd.send_raw(string)
tb.workfd.send_raw('C')
tb.workfd.set_prompt('C-Kermit>')
tb.workfd.expect_prompt()

# set lab pc linux prompt
tb.workfd.set_prompt(tb.config.linux_prompt)
tb.eof_write(tb.workfd, 'exit', False)
searchlist = ['OK']
tmp = True
once = 0
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
        if once == 0:
            tb.eof_write(tb.workfd, 'OK', False)
            once = 1
    if ret == 'prompt':
        tmp = False

tb.end_tc(True)
