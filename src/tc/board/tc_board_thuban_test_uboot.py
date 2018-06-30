# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# boot linux
# install the nand dump, which leads in u-boot crash
# when ubi is not fixed.

tb.eof_call_tc("tc_ub_boot_linux.py")
tb.eof_call_tc("tc_lx_trigger_wdt.py")

c = tb.c_con

cmd = 'flash_erase /dev/mtd8 0 0'
tb.write_lx_cmd_check(c, cmd, triggerlist=['Erasing'])

cmd = 'nandwrite -q -n -o /dev/mtd8 /home/hs/thuban/mtd8_ft2_1_on.dump'
tb.write_lx_cmd_check(c, cmd, triggerlist=['Writing'])

# now go into u-boot
tb.set_board_state("u-boot")

# try_uboot, which has the bug
# ubi part -> crash
cmd = 'dca off;ica off;tftp 0x80100000 /tftpboot/dxr2/20171213/u-boot-dump-noheader.bin;go 0x80100000'
tb.eof_write_cmd(c, cmd)

cmd = 'run nand_args'
tb.eof_write_cmd(c, cmd)
tb.c_con.set_check_error(False)
cmd = 'ubi part rootfs 2048'
tb.write_cmd_check(c, cmd, 'Resetting CPU')
tb.c_con.set_check_error(True)

# after crash, we are now in the new installed U-Boot

cmd = 'run nand_args'
tb.eof_write_cmd(c, cmd)
# ubi part -> kein crash with new u-boot allowed
cmd = 'ubi part rootfs 2048'
tb.eof_write_cmd(c, cmd)

# after reset load u-boot env we need
tb.eof_call_tc("tc_ub_load_board_env.py")
# try_uboot
# ubi part -> kein crash
cmd = 'dca off;ica off;tftp 0x80100000 /tftpboot/dxr2/20171213/u-boot-dump-noheader.bin;go 0x80100000'
tb.eof_write_cmd(c, cmd)

cmd = 'run nand_args'
tb.eof_write_cmd(c, cmd)
cmd = 'ubi part rootfs 2048'
tb.eof_write_cmd(c, cmd)

tb.config.tc_uboot_load_bin_with_kermit_possible = 'no'
tb.config.tc_ub_test_py_start = 'no'
# now we can test standard U-Boot things
tb.eof_call_tc("tc_demo_uboot_tests.py")

tb.end_tc(True)
