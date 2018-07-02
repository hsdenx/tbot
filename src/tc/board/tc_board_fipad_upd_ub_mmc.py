# SPDX-License-Identifier: GPL-2.0
#
# Description:
# update SPL and u-boot.img on the MMC0
# End:

from tbotlib import tbot

logging.info("typ: %s", tb.config.tc_board_fipad_upd_ub_typ)

# set board state for which the tc is valid
tb.set_board_state("linux")

tb.workfd = tb.c_con

# get rootfspath from cmdline ToDo
rootfspath = '/opt/eldk-5.5/armv7a-hf/rootfs-sato-sdk'
rootfsworkdir = '/home/hs/fipad'

tb.workfd = tb.c_ctrl
# copy files to rootfs dir
tb.statusprint("copy files")
c = tb.workfd
so = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/u-boot.img'
ta = rootfspath + rootfsworkdir + '/u-boot.img'
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

so = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/SPL'
ta = rootfspath + rootfsworkdir + '/SPL'
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

tb.workfd = tb.c_con
dev = '/dev/mmcblk0'
tmp = 'dd if=' + rootfsworkdir + '/SPL of=' + dev + ' bs=1K seek=1 oflag=sync status=none && sync'
tb.write_lx_cmd_check(tb.workfd, tmp)
tmp = 'dd if=' + rootfsworkdir + '/u-boot.img of=' + dev + ' bs=1K seek=69 oflag=sync status=none && sync'
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
