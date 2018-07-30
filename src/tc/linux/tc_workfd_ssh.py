# SPDX-License-Identifier: GPL-2.0
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
#
# used variables
#
# - tb.config.workfd_ssh_cmd
#| ssh command string
#| default:
#
# - tb.config.workfd_ssh_cmd_prompt
#| prompt after successful ssh
#| default: '$'
#
# - tb.config.workfd_ssh_opt
#| option string for ssh
#| default: 'none'
#
# - tb.config.workfd_ssh_do_first
#| if == 'yes', call
#|     tb.do_first_settings_after_login(c)
#| after successful login.
#| default: 'yes'
#
# End:

from tbotlib import tbot

tb.define_variable('workfd_ssh_cmd', '')
tb.define_variable('workfd_ssh_cmd_prompt', '$')
tb.define_variable('workfd_ssh_opt', 'none')
tb.define_variable('workfd_ssh_do_first', 'yes')

logging.info("args: workfd %s", tb.workfd.name)

c = tb.workfd

if tb.config.tc_workfd_ssh_opt == 'none':
    opt = ''
else:
    opt = tb.config.tc_workfd_ssh_opt

cmd = 'ssh ' + opt + ' ' + tb.config.workfd_ssh_cmd
tb.eof_write(c, cmd)
loop = True
s = ['Are you sure', 'assword', tb.config.workfd_ssh_cmd_prompt]
while loop:
    tmp = tb.tbot_rup_and_check_strings(c, s)
    if tmp == '0':
        tb.eof_write(c, 'yes', start=False)
    elif tmp == '1':
        buf = tb.buf.split('\n')[-1]
        # get the user name (before @) from scp output
        tmp = buf.split('@')
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

tb.gotprompt = True
tb.end_tc(True)
