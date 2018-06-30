# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# - set jumper to normal
# - boot sd card image
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_board_bootmode_tc
except:
    tb.end_tc(False)

tb.config.tc_board_bootmode = 'normal'
tb.eof_call_tc(tb.config.tc_board_bootmode_tc)

tb.config.uboot_prompt = '=> '
time.sleep(2)
tb.eof_call_tc("tc_lab_poweron.py")
tb.set_board_state("u-boot")

tb.config.linux_user = tb.config.linux_user_yoctorootfs
tb.config.ub_boot_linux_cmd = 'run sd_sd'
tb.config.bbb_check_crng_init = 'no'
tb.set_board_state("linux")

tb.eof_call_tc("tc_board_yocto_check_rootfs.py")
tb.end_tc(True)
