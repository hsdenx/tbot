# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# This testcase creates a third connection handle to the lab and uses
# ssh to create a connection to a compile pc.
# The third connection can then be used with tb.workfd and tb.c_cpc
# to outsource resource hungry tasks like compiling.
#
# ! workfd is set after calling this testcase to the new connection !
#
# The vars tb.config.compile_pc_ip, tb.config.compile_pc_user
# tb.config.connect_to_compilepc_ssh_opt, tb.config.connect_to_compilepc_ssh_cmd_prompt
# could also be a list of strings.
#
# used variables
#
# - tb.config.compile_pc_ip
#| ip address to the compile PC
#| default: ''
#
# - tb.config.compile_pc_user
#| login user name of compile PC
#| default:
#
# - tb.config.connect_to_compilepc_ssh_opt
#| ssh options for the ssh command for logging into compile PC
#| default:
#
# - tb.config.connect_to_compilepc_ssh_cmd_prompt
#| prompt of the compile PC, after login
#| default:
#
# End:

from tbotlib import tbot

tb.define_variable('compile_pc_ip', '')
tb.define_variable('compile_pc_user', '')
tb.define_variable('connect_to_compilepc_ssh_opt', '')
tb.define_variable('connect_to_compilepc_ssh_cmd_prompt', '')
logging.info("args: workfd %s", tb.workfd.name)

tb.set_board_state('lab')

# We want to have an own connection to out compile PC, so
# create the new connection
try:
    tb.c_cpc
except:
    tb.c_cpc = Connection(tb, "tb_cpc")
    tb.check_open_fd(tb.c_cpc)

tb.workfd = tb.c_cpc

if type(tb.config.compile_pc_ip) != list:
    ips = []
    ips.append(tb.config.compile_pc_ip)
else:
    ips = tb.config.compile_pc_ip

if type(tb.config.compile_pc_user) != list:
    users = []
    users.append(tb.config.compile_pc_user)
else:
    users = tb.config.compile_pc_user

if type(tb.config.connect_to_compilepc_ssh_opt) != list:
    opts = []
    opts.append(tb.config.connect_to_compilepc_ssh_opt)
else:
    opts = tb.config.connect_to_compilepc_ssh_opt

if type(tb.config.connect_to_compilepc_ssh_cmd_prompt) != list:
    prompts = []
    prompts.append(tb.config.connect_to_compilepc_ssh_cmd_prompt)
else:
    prompts = tb.config.connect_to_compilepc_ssh_cmd_prompt

cons = zip(ips, users, opts, prompts)

for con in cons:
    cur_p = tb.workfd.get_prompt()

    if cur_p != tb.config.compile_pc_prompt:
        # we are not @ compile PC
        # go to compile PC
        tb.config.workfd_ssh_cmd = con[1] + '@' + con[0]
        tb.config.tc_workfd_ssh_opt = con[2]
        tb.config.workfd_ssh_cmd_prompt = con[3]
        tb.eof_call_tc("tc_workfd_ssh.py")
        # we should set in tc_workfd_ssh.py the new prompt !
        # and check in tc_workfd_ssh.py if we have the correct prompt!
        # TODO
        tb.set_prompt(tb.c_cpc, tb.config.compile_pc_prompt, 'linux')

tb.end_tc(True)
