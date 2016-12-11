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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_ssh.py
# login with ssh to tb.workfd_ssh_cmd and set new ssh prompt
# tb.config.workfd_ssh_cmd_prompt
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s %s", tb.workfd.name, tb.workfd_ssh_cmd,
             tb.config.workfd_ssh_cmd_prompt)

# switch to root
tb.eof_write(tb.workfd, "ssh " + tb.workfd_ssh_cmd)
ret = tb.tbot_expect_string(tb.workfd, 'password')
if ret == 'prompt':
    logging.error("No ssh to %s", tb.workfd_ssh_cmd)
    tb.end_tc(False)

tb.write_stream_passwd(tb.workfd, tb.workfd_ssh_cmd, 'lab')
ret = tb.tbot_expect_string(tb.workfd, tb.config.workfd_ssh_cmd_prompt)
if ret == 'prompt':
    logging.error("No login to %s", tb.workfd_ssh_cmd)
    tb.end_tc(False)

# set prompt
tb.set_prompt(tb.workfd, tb.config.labprompt, 'linux')

tb.set_term_length(tb.workfd)
tb.end_tc(True)
