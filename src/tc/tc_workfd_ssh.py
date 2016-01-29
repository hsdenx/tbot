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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_ssh.py
# login with ssh
#
from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd, tb.workfd_ssh_cmd)

#switch to root
tb.eof_write(tb.workfd, "ssh " + tb.workfd_ssh_cmd)
ret = tb.wait_answer(tb.workfd, 'password:', 2)
if ret == False:
    logging.error("No ssh to %s", tb.workfd_ssh_cmd)
    tb.end_tc(False)

string = tb.lab.get_password(tb.workfd_ssh_cmd, 'lab')
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
    logging.error("No login to %s", tb.workfd_ssh_cmd)
    tb.end_tc(False)

# set prompt
tb.set_prompt(tb.workfd, tb.labprompt, 'export PS1="\u@\h [\$(date +%k:%M:%S)] ', ' >"')
tb.eof_read_end_state(tb.workfd)

tb.set_term_length(tb.workfd)
tb.end_tc(True)
