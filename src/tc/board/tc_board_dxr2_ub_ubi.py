# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c dxr2 -t tc_board_dxr2_ub_ubi.py
# start all ubi testcases for the dxr2 board
# End:

import time
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

#load ub tbot environment
tb.eof_call_tc("tc_ub_load_board_env.py")

tb.eof_write_cmd(tb.c_con, "mtdparts")
# all 30 days, erase the nand
savefd = tb.workfd
tb.workfd = tb.c_ctrl
tb.tc_workfd_check_tc_time_timeout = 60 * 60 * 24 * 30
tb.tc_workfd_check_tc_time_tcname = 'dxr2_ub_ubi'
ret = tb.call_tc("tc_workfd_check_tc_time.py")
if ret == True:
    tb.eof_call_tc("tc_ub_ubi_erase.py")

tb.workfd = savefd

#nand tests
tb.eof_call_tc("tc_ub_ubi_prepare.py")

tb.eof_call_tc("tc_ub_ubi_info.py")

#check if volume exist
ret = tb.call_tc("tc_ub_ubi_check_volume.py")
if ret == False:
    # if not create it
    tb.config.tc_ub_ubi_create_vol_name = tb.config.tc_ub_ubi_load_name
    tb.eof_call_tc("tc_ub_ubi_create_volume.py")
    tb.eof_call_tc("tc_ub_ubi_check_volume.py")

tb.eof_call_tc("tc_ub_ubi_info.py")

#create rootfs (needed for ubifs tests, also for linux tests)
tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_generate_random_file.py")
tb.tc_workfd_cp_file_a = tb.tc_workfd_generate_random_file_name
tb.tc_workfd_cp_file_b = tb.config.tc_workfd_create_ubi_rootfs_path + '/boot/ubi_random'
tb.eof_call_tc("tc_workfd_sudo_cp_file.py")
tb.tc_workfd_cp_file_a = tb.tc_workfd_generate_random_file_name
tb.tc_workfd_cp_file_b = tb.tc_board_dxr2_ub_ubi_rootfs_randomfile_path
tb.eof_call_tc("tc_workfd_sudo_cp_file.py")
tb.eof_call_tc("tc_workfd_create_ubi_rootfs.py")

#write new rootfs into it
tb.config.tc_ub_ubi_write_vol_name = tb.config.tc_ub_ubi_load_name
tb.config.tc_ub_tftp_file_addr = tb.config.tc_ub_ubi_write_addr
tb.config.tc_ub_tftp_file_name = tb.config.tc_workfd_create_ubi_rootfs_target
tb.eof_call_tc("tc_ub_tftp_file.py")

tb.eof_call_tc("tc_ub_get_filesize.py")
tb.config.tc_ub_ubi_write_len = tb.ub_filesize

tb.eof_call_tc("tc_ub_ubi_write.py")

#compare rootfs
tb.tc_ub_ubi_read_vol_name = tb.config.tc_ub_ubi_write_vol_name
tb.tc_ub_ubi_read_len = tb.config.tc_ub_ubi_write_len
tb.eof_call_tc("tc_ub_ubi_read.py")

tb.config.tc_ub_tftp_file_addr = '80000000'
tb.config.tc_ub_tftp_file_name = tb.config.tc_workfd_create_ubi_rootfs_target
tb.eof_call_tc("tc_ub_tftp_file.py")

if tb.ub_filesize != tb.tc_ub_ubi_read_len:
    logging.info("Buggy filesize %s %s", tb.ub_filesize, tb.tc_ub_ubi_read_len)
    tb.end_tc(False)

#compare the both files ...
tb.tc_ub_cmp_addr1 = tb.config.tc_ub_tftp_file_addr
tb.tc_ub_cmp_addr2 = tb.tc_ub_ubi_read_addr
tb.tc_ub_cmp_len = tb.ub_filesize
tb.eof_call_tc("tc_ub_cmp.py")

#now do some ubifs tests
tb.workfd = tb.c_con
def tbot_ub_write_cmd_check(tb, cmd):
    tmp = "if " + cmd + "; then; echo OK; else; echo FAIL; fi"
    tb.eof_write_cmd_check(tb.workfd, tmp, "OK")

tmp = "ubifsmount ubi:" + tb.config.tc_ub_ubi_write_vol_name
tbot_ub_write_cmd_check(tb, tmp)

tmp = "ubifsls /"
tbot_ub_write_cmd_check(tb, tmp)

tmp = "ubifsls /boot"
tbot_ub_write_cmd_check(tb, tmp)

tmp = "ubifsload " + tb.tc_ub_ubi_read_addr + " /creation_time"
tbot_ub_write_cmd_check(tb, tmp)
tmp = "md " + tb.tc_ub_ubi_read_addr
tbot_ub_write_cmd_check(tb, tmp)

tb.config.tc_ub_tftp_file_name = '/tftpboot/dxr2/tbot/ubi_random'
tb.eof_call_tc("tc_ub_tftp_file.py")
tb.eof_call_tc("tc_ub_get_filesize.py")

tmp = "ubifsload " + tb.tc_ub_ubi_read_addr + " /boot/ubi_random"
tbot_ub_write_cmd_check(tb, tmp)

tb.tc_ub_cmp_addr1 = tb.config.tc_ub_tftp_file_addr
tb.tc_ub_cmp_addr2 = tb.tc_ub_ubi_read_addr
tb.tc_ub_cmp_len = tb.ub_filesize
tb.eof_call_tc("tc_ub_cmp.py")

tb.end_tc(True)
