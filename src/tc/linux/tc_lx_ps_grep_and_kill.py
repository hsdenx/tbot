# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# kills all process which contain tb.config.tc_lx_ps_grep_and_kill_name
#
# End:

from tbotlib import tbot

tb.config.tc_lx_ps_grep_and_kill_name = 'hackbench'
try:
    tb.config.tc_lx_ps_grep_and_kill_name
except:
    tb.config.tc_lx_ps_grep_and_kill_name = 'none'

logging.info("args: workfd: %s %s", tb.workfd.name, tb.config.tc_lx_ps_grep_and_kill_name)

if tb.config.tc_lx_ps_grep_and_kill_name == 'none':
   tb.end_tc(True)

c = tb.workfd

# set board state for which the tc is valid
tb.set_board_state("linux")

cmd = 'ps | grep ' + tb.config.tc_lx_ps_grep_and_kill_name
tb.eof_write(c, cmd)

pid_list = []
loop = True
while loop == True:
    ret = tb.tbot_get_line(c)
    if ret != '':
        pid = ret.strip()
        pid = pid.split(' ')
        pid = pid[0]
        pid_list.append(pid)
    else:
        # got prompt -> end
        loop = False

for pid in pid_list:
    cmd = 'kill ' + pid
    tb.eof_write(c, cmd)
    tb.tbot_expect_prompt(c)
    tb.tbot_trigger_wdt()

tb.end_tc(True)
