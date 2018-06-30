# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_create_ubi_rootfs.py
# create a ubifs rootfs
# ubi rootfs path: tb.config.tc_workfd_create_ubi_rootfs_path
# ubi parameters:
# tb.config.tc_ubi_min_io_size tb.config.tc_ubi_leb_size tb.config.tc_ubi_max_leb_cnt
# output path: tb.config.tc_workfd_create_ubi_rootfs_target
# End:
from tbotlib import tbot

logging.info("args: workdfd: %s %s", tb.workfd.name, tb.config.tc_workfd_create_ubi_rootfs_path)
logging.info("%s", tb.config.tc_workfd_create_ubi_rootfs_target)

tb.eof_call_tc("tc_workfd_switch_su.py")

tmp = "date > " + tb.config.tc_workfd_create_ubi_rootfs_path + "/creation_time"
tb.write_lx_cmd_check(tb.workfd, tmp)
tmp = "cat " + tb.config.tc_workfd_create_ubi_rootfs_path + "/creation_time"
tb.write_lx_cmd_check(tb.workfd, tmp)

tmp = "mkfs.ubifs --root=" + tb.config.tc_workfd_create_ubi_rootfs_path + " -m " + tb.config.tc_ubi_min_io_size + " -e " + tb.config.tc_ubi_leb_size + " -c " + tb.config.tc_ubi_max_leb_cnt + " -F --output=" + tb.config.tc_workfd_create_ubi_rootfs_target
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.eof_write_cmd(tb.workfd, "exit")
tb.end_tc(True)
