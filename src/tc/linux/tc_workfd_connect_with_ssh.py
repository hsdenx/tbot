# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# connect wit ssh to board, and use it as console
#
# End:

from tbotlib import tbot

try:
    tb.config.connect_with_ssh_user
except:
    tb.config.connect_with_ssh_user = 'root'

try:
    tb.config.connect_with_ssh_ip
except:
    tb.config.connect_with_ssh_ip = '192.168.3.23'

logging.info("args: workdfd: %s", tb.workfd)
logging.info("args: %s %s %s", tb.config.connect_with_ssh_user, tb.config.connect_with_ssh_ip, tb.config.linux_prompt_default)

save = tb.workfd
tb.workfd = tb.c_con
tb.config.workfd_ssh_cmd = tb.config.connect_with_ssh_user + '@' + tb.config.connect_with_ssh_ip
tb.config.tc_workfd_ssh_opt = ''
tb.config.workfd_ssh_cmd_prompt = tb.config.linux_prompt_default
tb.config.workfd_ssh_do_first = 'no'
tb.eof_call_tc("tc_workfd_ssh.py")

tb.set_prompt(tb.workfd, tb.config.linux_prompt, 'linux')
tb.set_term_length(tb.workfd)

tb.workfd = save
tb.end_tc(True)
