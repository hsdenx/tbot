# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# - set recovery mode
# - boot with linux from tftp
# - boot sd card image
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_board_bootmode_tc
except:
    tb.end_tc(False)

tb.config.tc_board_bootmode = 'recovery'
tb.eof_call_tc(tb.config.tc_board_bootmode_tc)

tb.config.uboot_prompt = '=> '
time.sleep(2)
tb.eof_call_tc("tc_lab_poweron.py")
tb.set_board_state("u-boot")

tb.config.linux_user = tb.config.linux_user_yoctorootfs
tb.config.ub_boot_linux_cmd = 'run netmmcboot'
tb.config.bbb_check_crng_init = 'no'
tb.set_board_state("linux")
tb.end_tc(True)
