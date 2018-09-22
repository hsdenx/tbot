# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# basic xenomai tests
#
# - simply call "cat /proc/xenomai/*"
#
# ToDo: call xeno-test
#
# End:

from tbotlib import tbot

tb.set_board_state("linux")
save = tb.workfd
tb.workfd = tb.c_con
c = tb.workfd
result = True

tb.config.tc_workfd_check_if_dir_exists_name = '/proc/xenomai'
tb.eof_call_tc("tc_workfd_check_if_dir_exist.py")

cmd = 'cat ' + tb.config.tc_workfd_check_if_dir_exists_name + '/*'
tb.eof_write_cmd(c, cmd)

#cmd ='xeno-test'
#tb.eof_write(c, cmd)
#ret = tb.tbot_expect_string(c, 'Testing built-in CLOCK_HOST_REALTIME')
#if ret == 'prompt':
#    tb.end_tc(False)
#ret = tb.tbot_expect_string(c, '\n')
#if ret == 'prompt':
#    tb.end_tc(False)

#== Testing built-in CLOCK_HOST_REALTIME (32)
#CPU      ToD offset [us] ToD drift [us/s]      warps max delta [us]
#--- -------------------- ---------------- ---------- --------------
#  0                  1.6           -0.004          5         9966.3

#loop = True
#clk_res = []
#once = 0
#while loop == True:
#    ret = tb.tbot_get_line(c)
#    if 'switchtest' in ret:
#        if once == 0:
#            tb.send_ctrl_c(c)
#            once = 1
#            continue
#    elif ret == 'prompt':
#        loop = False

tb.workfd = save
tb.end_tc(True)
