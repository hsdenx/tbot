# SPDX-License-Identifier: GPL-2.0
#
# Description:
# cp a dummy file into a partiton umount/mount it and
# compare it.
# - Mount tb.config.tc_lx_mount_dir with tc_lx_mount.py
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("linux")

# call tc mount partition
tb.eof_call_tc("tc_lx_mount.py")

# create tempfile
tb.config.tc_lx_dummy_file_bs = "1024"
tb.config.tc_lx_dummy_file_count = "1024"
tb.config.tc_lx_dummy_file_tempfile = "gnlmpf_partition"
tb.eof_call_tc("tc_lx_create_dummy_file.py")

# copy dummy file into partition
tmp = "cp " + tb.config.tc_lx_dummy_file_tempfile + " " + tb.config.tc_lx_mount_dir
tb.write_lx_cmd_check(tb.workfd, tmp)

# umount the partition
tmp = "umount " + tb.config.tc_lx_mount_dev
tb.write_lx_cmd_check(tb.workfd, tmp)

# mount it again
tb.eof_call_tc("tc_lx_mount.py")

# compare the dummy file with the file in the partition
tmp = "cmp " + tb.config.tc_lx_dummy_file_tempfile + " " + tb.config.tc_lx_mount_dir + "/gnlmpf_partition"
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.end_tc(True)
