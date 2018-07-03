# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# install sd card image from
# /boot/ + tb.config.rootfs_sdcard_file into
# of=/dev/mmcblk + devnr
#
# devnr gets detected with 'dmesg | grep mmc | grep SD'
#
# End:

from tbotlib import tbot

tb.config.bbb_check_crng_init = 'no'
tb.set_board_state("linux")

# get sd card device
# dmesg | grep mmc | grep SD
# [    3.339339] mmc0: new high speed SDHC card at address aaaa
cmd = 'dmesg | grep mmc | grep SD'
tb.eof_write_cmd_get_line(tb.c_con, cmd)

dev = tb.ret_write_cmd_get_line.split(':')[0]
if ']' in dev:
    dev = dev.split(']')[1]

dev = dev.replace(' ', '')
devnr = dev.replace('mmc', '')
logging.info("device: %s nr: %s", dev, devnr)

cmd = 'dd if=/boot/' + tb.config.rootfs_sdcard_file + ' of=/dev/mmcblk' + devnr + ' bs=4M'
tb.write_lx_cmd_check(tb.c_con, cmd)
cmd = 'sync'
tb.write_lx_cmd_check(tb.c_con, cmd)
cmd = 'sync'
tb.write_lx_cmd_check(tb.c_con, cmd)

tb.end_tc(True)
