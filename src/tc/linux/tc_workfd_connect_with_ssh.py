# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# connect wit ssh to board, and use it as console
#
# used variables
#
# - tb.config.connect_with_ssh_user
#| username for connecting to boards "console"
#| default: 'root'
#
# - tb.config.connect_with_ssh_ip
#| ip to connect with
#| default: '192.168.3.23'
#
# End:

from tbotlib import tbot

tb.define_variable('connect_with_ssh_user', 'root')
tb.define_variable('connect_with_ssh_ip', '192.168.3.23')
logging.info("args: workdfd: %s", tb.workfd)
logging.info("args: %s", tb.config.linux_prompt_default)

save = tb.workfd
tb.workfd = tb.c_con
tb.config.workfd_ssh_cmd = tb.config.connect_with_ssh_user + '@' + tb.config.connect_with_ssh_ip
tb.config.tc_workfd_ssh_opt = 'none'
tb.config.workfd_ssh_cmd_prompt = tb.config.linux_prompt_default
tb.config.workfd_ssh_do_first = 'no'
tb.eof_call_tc("tc_workfd_ssh.py")

tb.set_prompt(tb.workfd, tb.config.linux_prompt, 'linux')
tb.set_term_length(tb.workfd)

tb.workfd = save
tb.end_tc(True)
