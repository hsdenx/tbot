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
#
# login with ssh to tb.config.workfd_ssh_cmd and ssh options
# tb.config.tc_workfd_ssh_opt.
# This testcases expects
# tb.config.workfd_ssh_cmd_prompt
# as the prompt it get, after a succefull log in.
# When logged in call
# if tb.config.workfd_ssh_do_first == 'yes':
#      tb.do_first_settings_after_login(c)
#
# End:

from tbotlib import tbot

try:
    tb.config.workfd_ssh_do_first
except:
    tb.config.workfd_ssh_do_first = 'yes'

logging.info("args: workfd %s %s %s %s %s", tb.workfd.name, tb.config.workfd_ssh_cmd,
             tb.config.tc_workfd_ssh_opt,
             tb.config.workfd_ssh_cmd_prompt, tb.config.workfd_ssh_do_first)

c = tb.workfd

cmd = 'ssh ' + tb.config.tc_workfd_ssh_opt + ' ' + tb.config.workfd_ssh_cmd
tb.eof_write(c, cmd)
loop = True
s = ['Are you sure', 'assword', tb.config.workfd_ssh_cmd_prompt]
while loop:
    tmp = tb.tbot_rup_and_check_strings(c, s)
    if tmp == '0':
        tb.eof_write(c, 'yes', start=False)
    elif tmp == '1':
        # get the user name (before @) from scp output
        tmp = tb.buf.split('@')
        try:
            tmp[1]
            # OK, there is a @
            user = tmp[0].replace('\r', '')
            user = user.replace('\n', '')
        except:
            # Hmm.. no user name found ... what to do?
            # currently tbot searches now for user ''
            # which it not found -> wrng password send,
            # which leads in failure of the scp cmd ...
            user = ''

        if user != '':
            tmp = tmp[1].split("'s ")
            try:
                tmp[1]
                # Ok "'s " found
                ip = tmp[0]
            except:
                # no ip, same as no user ...
                ip = ''
        tb.write_stream_passwd(tb.workfd, user, ip)
    elif tmp == '2':
        loop = False
    elif tmp == 'prompt':
        tb.end_tc(False)

if tb.config.workfd_ssh_do_first == 'yes':
    tb.do_first_settings_after_login(c)

tb.end_tc(True)
