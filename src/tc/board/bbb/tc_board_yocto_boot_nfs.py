# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# - set boot mode normal
# - go into u-boot
# - boot linux with "run net_nfs"
# - call tc_board_yocto_install_sdcard.py
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_board_bootmode_tc
except:
    tb.end_tc(False)

logging.info("args: %s %s", tb.workfd.name, tb.config.tc_board_bootmode_tc)

tb.config.tc_board_bootmode = 'normal'
tb.eof_call_tc(tb.config.tc_board_bootmode_tc)

tb.config.uboot_prompt = '=> '
time.sleep(2)
tb.eof_call_tc("tc_lab_poweron.py")
tb.set_board_state("u-boot")

# go into linux, rootfs nfs
tb.config.ub_boot_linux_cmd = 'run net_nfs'
tb.config.linux_user = tb.config.linux_user_nfsrootfs
tb.config.linux_prompt_default = tb.config.linux_prompt_default_nfsrootfs
tb.config.bbb_check_crng_init = 'no'
tb.set_board_state("linux")

tb.eof_call_tc("tc_board_yocto_install_sdcard.py")

tb.end_tc(True)
