# SPDX-License-Identifier: GPL-2.0
#
# Description:
# - load u-boot environment with testcase "tc_ub_load_board_env.py"
# - execute u-boot cmd tb.config.ub_boot_linux_cmd
#
# used variables
#
# - tb.config.tc_ub_boot_linux_cycle
#| count of timeout cycles until testcase ends with failure
#| default: '1'
#
# End:
from tbotlib import tbot

tb.define_variable('tc_ub_boot_linux_cycle', '2')

# here starts the real test
logging.info("args: %s %s %s", tb.config.ub_boot_linux_cmd, tb.config.state_linux_timeout, tb.config.linux_prompt_default)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# load U-Boot environment variables for tbot
tb.eof_call_tc("tc_ub_load_board_env.py")

# run tbot_boot_linux
tb.eof_write_con(tb.config.ub_boot_linux_cmd)

c = tb.c_con
oldt = c.get_timeout()
c.set_prompt(tb.config.linux_prompt_default, 'linux')
c.set_timeout(tb.config.state_linux_timeout)

first = 1
got_login = 0
sl = ['Last login:', 'login:', 'assword', 'Starting kernel', '# L']
try:
    sl = sl + tb.config.state_linux_trigger_list
except:
    pass

loop = 0
while (loop < int(tb.config.tc_ub_boot_linux_cycle)):
    ret = tb.tbot_rup_and_check_strings(c, sl)
    if ret == '0':
        tmp = True
        loop = -1
        continue
    elif ret == '1':
        # login
        tb.write_stream(c, tb.config.linux_user, send_console_start=False)
        got_login = 1
        loop = -1
        continue
    elif ret == '2':
        if got_login:
	    tb.write_stream_passwd(c, tb.config.linux_user, tb.config.boardname)
            loop = -1
        continue
    elif ret == 'prompt':
        # we are in linux
        tb.set_prompt(c, tb.config.linux_prompt, 'linux')
        c.set_timeout(oldt)
        tb.end_tc(True)
    elif ret == 'exception':
        logging.warning('Timeout while trying to boot Linux %s', loop)
        if first == 1:
            # send Ctrl-C
            tb.send_ctrl_c(c)
            first = 0
            loop = -1
    else:
        # if we have trigger strings, we land here
        tb.tbot_trigger_wdt()
        loop = -1

    loop += 1
c.set_timeout(oldt)
tb.end_tc(False)
