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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_connect_with_kermit.py
# connect with kermit to serials board console
# - if tb.config.tc_workfd_connect_with_kermit_ssh != 'none'
#   connect first with ssh to another PC (where kermit is started)
# - start kermit
# - if tb.config.tc_workfd_connect_with_kermit_rlogin == 'none'
#     set line tb.config.kermit_line and speed tb.config.kermit_speed and
#     kermit parameter list tb.config.tc_workfd_connect_with_kermit_settings
#     than connect to serial line.
#   else
#     connect with command in tb.config.tc_workfd_connect_with_kermit_rlogin
# - if you need sudo rights set tb.config.tc_workfd_connect_with_kermit_sudo = 'yes'
#   and a sudo is preceded to kermit.
#   the sudo password is searched with
#   user:  tb.config.user + '_kermit'
#   board: tb.config.boardname
#
# End:

from tbotlib import tbot

logging.info("args: workdfd: %s", tb.workfd)
logging.info("args: ssh: %s", tb.config.tc_workfd_connect_with_kermit_ssh)
logging.info("args: sudo: %s", tb.config.tc_workfd_connect_with_kermit_sudo)
logging.info("args: kermit: %s %s", tb.config.kermit_line, tb.config.kermit_speed)

try:
    tb.config.tc_workfd_connect_with_kermit_settings
except:
    tb.config.tc_workfd_connect_with_kermit_settings = [
        "set carrier-watch off",
        "set handshake none",
        "set flow-control none",
        "robust",
        "set file type bin",
        "set file name lit",
        "set rec pack 1000",
        "set send pack 1000",
        "set window 5",
    ]

if tb.config.tc_workfd_connect_with_kermit_ssh != 'none':
    tb.workfd_ssh_cmd = tb.config.tc_workfd_connect_with_kermit_ssh
    tb.config.workfd_ssh_cmd_prompt = '$'
    tb.eof_call_tc("tc_workfd_ssh.py")

if tb.config.tc_workfd_connect_with_kermit_sudo != 'none':
    pre = 'sudo '
else:
    pre = ''

tb.eof_write(tb.workfd, pre + 'kermit', start=False)
oldprompt = tb.workfd.get_prompt()
tb.workfd.set_prompt('C-Kermit>')

searchlist = ["assword"]
tmp = True
retu = False
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
       tb.write_stream_passwd(tb.workfd, tb.config.user + '_kermit', tb.config.boardname)
    elif ret == 'prompt':
       tmp = False

if tb.config.tc_workfd_connect_with_kermit_rlogin == 'none':
    # check for "no effect", "Sorry, write access"
    tb.eof_write(tb.workfd, "set line " + tb.config.kermit_line, start=False)
    searchlist = ["no effect", "Sorry, write access", "Sorry, device is in use", "Device or resource busy"]
    tmp = True
    retu = False
    while tmp == True:
        ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
        if ret == '0':
            retu = True
        if ret == '1':
            retu = True
        if ret == '2':
            retu = True
        if ret == '3':
            retu = True
        elif ret == 'prompt':
            tmp = False

    if retu == True:
        tb.workfd.set_prompt(oldprompt)
        tb.gotprompt = True
        tb.end_tc(False)

    tb.eof_write_cmd(tb.workfd, "set speed " + tb.config.kermit_speed, start=False)
    for cmd in tb.config.tc_workfd_connect_with_kermit_settings:
        tb.eof_write_cmd(tb.workfd, cmd, start=False)

    tb.eof_write(tb.workfd, "connect")
    searchlist = ["Connecting"]
    tmp = True
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret != '0':
        tb.gotprompt = True
        tb.end_tc(False)
else:
    tb.eof_write(tb.workfd, tb.config.tc_workfd_connect_with_kermit_rlogin, start=False)

searchlist = ['----------------------------------------------------']
ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
if ret != '0':
    tb.gotprompt = True
    tb.end_tc(False)

if tb.config.tc_workfd_connect_with_kermit_rlogin != 'none':
    searchlist = ['----------------------------------------------------']
    oldt = tb.workfd.get_timeout()
    tb.workfd.set_timeout(5)
    tmp = True
    while tmp == True:
        ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
        if ret == '0':
            # some Error with connect, leave kermit
            tb.workfd.set_timeout(oldt)
            tb.workfd.set_prompt(oldprompt)
            tb.eof_write_cmd(tb.workfd, 'exit', start=False)
            tb.gotprompt = True
            tb.end_tc(False)
        else:
            tmp = False
    tb.workfd.set_timeout(oldt)

tb.gotprompt = True
# set now U-Boot prompt ?
tb.workfd.set_prompt(tb.config.uboot_prompt)
tb.end_tc(True)
