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
# python2.7 src/common/tbot.py -s lab_denx -c exceet -t tc_workfd_scp.py
#
# start an scp transfer
# tb.config.tc_workfd_scp_opt: scp options
# tb.config.tc_workfd_scp_from: from where
# tb.config.tc_workfd_scp_to: to where
#
# If the scp command asks for  "password" the testcase extracts
# the user and ip from scp output "user@ip's password:"
# and writes the password it find in password.py with
#
# tb.write_stream_passwd(tb.workfd, user, ip)
#
# to the scp command ... if no user and or ip
# is found ... scp command fails and so the testcase.
#
# An errorneous scp command exits with an error code.
# check this error code when scp command finished,
# and return True, if no error, else False.
#
# End:

from tbotlib import tbot

logging.info("args: workfd %s", tb.workfd.name)
logging.info("args: %s %s %s", tb.config.tc_workfd_scp_opt, tb.config.tc_workfd_scp_from, tb.config.tc_workfd_scp_to)

c = tb.workfd

cmd = 'scp ' + tb.config.tc_workfd_scp_opt + ' ' + tb.config.tc_workfd_scp_from + ' ' + tb.config.tc_workfd_scp_to
tb.eof_write(c, cmd, split=c.line_length / 2)
loop = True
s = ['Are you sure', 'Do you want to', 'password', 'ETA', '\n']
while loop:
    tmp = tb.tbot_rup_and_check_strings(c, s)
    if tmp == '0':
        tb.eof_write(c, 'yes', start=False)
    if tmp == '1':
        tb.eof_write(c, 'y', start=False)
    elif tmp == '2':
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
    elif tmp == '3':
        tb.tbot_trigger_wdt()
    elif tmp == '4':
        tb.tbot_trigger_wdt()
    elif tmp == 'prompt':
        loop = False

ret = self.call_tc("tc_workfd_check_cmd_success.py")
tb.end_tc(ret)
