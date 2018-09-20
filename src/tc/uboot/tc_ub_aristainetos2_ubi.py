# SPDX-License-Identifier: GPL-2.0
#
# Description:
# ubi testcases for the aristainetos2 board
# End:

import time
from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# this board needs some time to settle
time.sleep(10)

# load ub tbot environment
tb.eof_call_tc("tc_ub_load_board_env.py")

# probe spi nor
tb.eof_write_cmd(tb.c_con, "sf probe")

# nand tests
tb.config.tc_ub_ubi_prep_offset = '4096'
tb.config.tc_ub_ubi_prep_partname = 'ubi'
tb.eof_call_tc("tc_ub_ubi_prepare.py")

# check if ubi rootfs volume exists
tb.config.tc_ub_ubi_load_name = 'rootfs'
tb.eof_call_tc("tc_ub_ubi_check_volume.py")

# delete it
# check if rootfs volume exists, must fail
# and create it
# check if rootfs volume exists

# get file
tb.config.tc_ub_tftp_file_addr = tb.config.tc_ub_ubi_write_addr
tb.config.tc_ub_tftp_file_name = '/tftpboot/aristainetos/tbot/rootfs-minimal.ubifs'
tb.eof_call_tc("tc_ub_tftp_file.py")

tb.eof_call_tc("tc_ub_get_filesize.py")
tb.config.tc_ub_ubi_write_len = tb.ub_filesize

# write it in ubi volume
tb.config.tc_ub_ubi_write_len = tb.ub_filesize
tb.eof_call_tc("tc_ub_ubi_write.py")

# read file from ubi volume
tb.config.tc_ub_ubi_read_addr = '11000000'
tb.config.tc_ub_ubi_read_vol_name = tb.config.tc_ub_ubi_write_vol_name
tb.config.tc_ub_ubi_read_len = tb.config.tc_ub_ubi_write_len
tb.eof_call_tc("tc_ub_ubi_read.py")

# cmp if all bytes are the same
tb.config.tc_ub_cmp_addr1 = tb.config.tc_ub_ubi_read_addr
tb.config.tc_ub_cmp_addr2 = tb.config.tc_ub_tftp_file_addr
tb.config.tc_ub_cmp_len = tb.config.tc_ub_ubi_write_len
tb.eof_call_tc("tc_ub_cmp.py")

# mount ubifs
tb.eof_call_tc("tc_ub_ubifs_mount.py")
# ls "/"
tb.config.tc_ub_ubifs_ls_dir = '/'
tb.eof_call_tc("tc_ub_ubifs_ls.py")

# now reset the board
tb.eof_call_tc("tc_ub_reset.py")
# ... and reread the image again

tb.eof_write_cmd(tb.c_con, "sf probe")
tb.config.tc_ub_ubi_prep_offset = '4096'
tb.config.tc_ub_ubi_prep_partname = 'ubi'
tb.eof_call_tc("tc_ub_ubi_prepare.py")

# get file
tb.config.tc_ub_tftp_file_addr = tb.config.tc_ub_ubi_write_addr
tb.config.tc_ub_tftp_file_name = '/tftpboot/aristainetos/tbot/rootfs-minimal.ubifs'
tb.eof_call_tc("tc_ub_tftp_file.py")

tb.eof_call_tc("tc_ub_get_filesize.py")
tb.config.tc_ub_ubi_write_len = tb.ub_filesize

# read file from ubi volume
tb.config.tc_ub_ubi_read_addr = '11000000'
tb.config.tc_ub_ubi_read_vol_name = tb.config.tc_ub_ubi_write_vol_name
tb.config.tc_ub_ubi_read_len = tb.config.tc_ub_ubi_write_len
tb.eof_call_tc("tc_ub_ubi_read.py")

# cmp if all bytes are the same
tb.config.tc_ub_cmp_addr1 = tb.config.tc_ub_ubi_read_addr
tb.config.tc_ub_cmp_addr2 = tb.config.tc_ub_tftp_file_addr
tb.config.tc_ub_cmp_len = tb.config.tc_ub_ubi_write_len
tb.eof_call_tc("tc_ub_cmp.py")


# nor tests
tb.config.tc_ub_ubi_prep_offset = '64'
tb.config.tc_ub_ubi_prep_partname = 'rescue-system'
tb.config.tc_ub_ubi_load_name = 'kernel'
tb.eof_call_tc("tc_ub_ubi_prepare.py")
tb.eof_call_tc("tc_ub_ubi_check_volume.py")

# write file into kernel volume
tb.config.tc_ub_tftp_file_addr = tb.config.tc_ub_ubi_write_addr
tb.config.tc_ub_tftp_file_name = '/tftpboot/aristainetos/tbot/aristainetos2.itb'
tb.eof_call_tc("tc_ub_tftp_file.py")

tb.eof_call_tc("tc_ub_get_filesize.py")
tb.config.tc_ub_ubi_write_len = tb.ub_filesize

tb.config.tc_ub_ubi_write_vol_name = 'kernel'
tb.eof_call_tc("tc_ub_ubi_write.py")

# read file from kernel partition
tb.config.tc_ub_ubi_read_addr = '11000000'
tb.config.tc_ub_ubi_read_vol_name = tb.config.tc_ub_ubi_write_vol_name
tb.config.tc_ub_ubi_read_len = tb.config.tc_ub_ubi_write_len
tb.eof_call_tc("tc_ub_ubi_read.py")

# cmp if all bytes are the same
tb.config.tc_ub_cmp_addr1 = tb.config.tc_ub_ubi_read_addr
tb.config.tc_ub_cmp_addr2 = tb.config.tc_ub_tftp_file_addr
tb.config.tc_ub_cmp_len = tb.config.tc_ub_ubi_write_len
tb.eof_call_tc("tc_ub_cmp.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
