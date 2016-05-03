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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_connect_with_kermit.py
from tbotlib import tbot

logging.info("args: workdfd: %s", tb.workfd)
logging.info("args: ssh: %s", tb.tc_workfd_connect_with_kermit_ssh)
logging.info("args: kermit: %s %s", tb.kermit_line, tb.kermit_speed)

if tb.tc_workfd_connect_with_kermit_ssh != 'none':
    tb.workfd_ssh_cmd = tb.tc_workfd_connect_with_kermit_ssh
    tb.workfd_ssh_cmd_prompt = '$'
    tb.eof_call_tc("tc_workfd_ssh.py")

tb.eof_write(tb.workfd, 'kermit')
oldprompt = tb.workfd.get_prompt()
tb.workfd.set_prompt('C-Kermit>')
tb.workfd.expect_prompt()

if tb.tc_workfd_connect_with_kermit_rlogin == 'none':
    # check for "no effect", "Sorry, write access"
    tb.eof_write(tb.workfd, "set line " + tb.kermit_line)
    searchlist = ["no effect", "Sorry, write access"]
    tmp = True
    retu = False
    while tmp == True:
        ret = tb.tbot_read_line_and_check_strings(tb.workfd, searchlist)
        if ret == '0':
            retu = True
        if ret == '1':
            retu = True
        elif ret == 'prompt':
            tmp = False

    if retu == True:
        tb.workfd.set_prompt(oldprompt)
        tb.end_tc(False)

    tb.eof_write_cmd(tb.workfd, "set speed " + tb.kermit_speed)
    tb.eof_write_cmd(tb.workfd, "set flow-control none")
    tb.eof_write_cmd(tb.workfd, "set carrier-watch off")
    tb.eof_write(tb.workfd, "connect")
    searchlist = ["Connecting"]
    tmp = True
    ret = tb.tbot_read_line_and_check_strings(tb.workfd, searchlist)
    if ret != '0':
        tb.end_tc(False)
else:
    tb.eof_write(tb.workfd, tb.tc_workfd_connect_with_kermit_rlogin)

searchlist = ['----------------------------------------------------']
ret = tb.tbot_read_line_and_check_strings(tb.workfd, searchlist)
if ret != '0':
    tb.end_tc(False)

if tb.tc_workfd_connect_with_kermit_rlogin != 'none':
    searchlist = ['----------------------------------------------------']
    oldt = tb.workfd.get_timeout()
    tb.workfd.set_timeout(5)
    tmp = True
    while tmp == True:
        ret = tb.tbot_read_line_and_check_strings(tb.workfd, searchlist)
        if ret == '0':
            # some Error with connect, leave kermit
            tb.workfd.set_timeout(oldt)
            tb.workfd.set_prompt(oldprompt)
            tb.eof_write_cmd(tb.workfd, 'exit')
            tb.end_tc(False)
        else:
            tmp = False

tb.workfd.set_timeout(oldt)
# set now U-Boot prompt ?
tb.workfd.set_prompt(tb.uboot_prompt)
tb.end_tc(True)
