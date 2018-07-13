# SPDX-License-Identifier: GPL-2.0
#
# Description:
# run a bonnie test, if timer tc_workfd_check_tc_time.py timed out
# - if bonnie is not installed, try to install bonnie with
#|  tc_lx_bonnie_install.py
# - start bonnie on device tb.config.tc_lx_bonnie_dev with
#|   size tb.config.tc_lx_bonnie_sz
#
# used variables
#
# - tb.config.tc_lx_bonnie_dev
#| device used for bonnie
#| default: '/dev/sda1'
#
# - tb.config.tc_lx_bonnie_sz
#| bonnie size
#| default: '968'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lx_bonnie_dev', '/dev/sda1')
tb.define_variable('tc_lx_bonnie_sz', '968')

# set board state for which the tc is valid
tb.set_board_state("linux")

tb.config.tc_workfd_check_tc_time_tcname = 'bonnie'
savefd = tb.workfd
tb.workfd = tb.c_ctrl
ret = tb.call_tc("tc_workfd_check_tc_time.py")
if ret == False:
    # do not start bonnie, timer is not expired
    tb.workfd = savefd
    tb.end_tc(True)

tb.workfd = savefd
# check if bonnie exist
# if not download it, and try to install
tb.eof_call_tc("tc_lx_bonnie_install.py")

# start test
# detect tc_lx_bonnie_sz ... should be 2*RAM size
tmp = "bonnie++ -d " + tb.config.tc_lx_bonnie_dev + " -s " + tb.config.tc_lx_bonnie_sz + " -f -b -u root -m " + tb.config.boardname

tb.eof_write(tb.c_con, tmp)
# bonnie takes loooong
tb.tbot_expect_prompt(tb.c_con)
tb.end_tc(True)
