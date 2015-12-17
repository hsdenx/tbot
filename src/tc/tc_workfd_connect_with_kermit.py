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
    tb.eof_write(tb.workfd, tb.tc_workfd_connect_with_kermit_ssh)
    ret = tb.wait_answer(tb.workfd, 'password:', 2)
    if ret == False:
        logging.error("No ssh to %s", tb.tc_workfd_connect_with_kermit_ssh)
        tb.end_tc(False)
    string = tb.lab.get_password(tb.tc_workfd_connect_with_kermit_ssh, 'lab')
    tb.lab.write(tb.workfd, string)
    searchlist = ["login:"]
    tmp = True
    ret = False
    while tmp == True:
        tmp = tb.readline_and_search_strings(tb.workfd, searchlist)
        if tmp == 0:
            ret = True
            tmp = True
        elif tmp == 'prompt':
            tmp = False

    if ret != True:
        logging.error("No login to %s", tb.tc_workfd_connect_with_kermit_ssh)
        tb.end_tc(False)

    # set prompt
    tb.set_prompt(tb.workfd, tb.labprompt, 'export PS1="\u@\h [\$(date +%k:%M:%S)] ', ' >"')
    tb.eof_read_end_state(tb.workfd, 1)

tb.set_term_length(tb.workfd)
tb.eof_write(tb.workfd, 'kermit')
tb.prompt = 'C-Kermit>'

searchlist = ["Kermit"]
tmp = True
ret = False
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.workfd, searchlist)
    if tmp == 0:
        ret = True
        tmp = True
    elif tmp == 'prompt':
        tmp = False

# check for "no effect", "Sorry, write access"
tb.eof_write(tb.workfd, "set line " + tb.kermit_line)
searchlist = ["no effect", "Sorry, write access"]
tmp = True
ret = False
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.workfd, searchlist)
    if tmp == 0:
        ret = True
        tmp = True
    if tmp == 1:
        ret = True
        tmp = True
    elif tmp == 'prompt':
        tmp = False

if ret == True:
    tb.end_tc(False)

tb.eof_write(tb.workfd, "set speed " + tb.kermit_speed)

# check for "you must SET LINE"

tb.eof_read_end_state(tb.workfd, 1)
tb.eof_write(tb.workfd, "set flow-control none")
tb.eof_read_end_state(tb.workfd, 1)
tb.eof_write(tb.workfd, "set carrier-watch off")
tb.eof_read_end_state(tb.workfd, 1)
tb.lab.write(tb.workfd, "connect")

# set back U-Boot prompt
tb.prompt = tb.uboot_prompt
tb.end_tc(True)
