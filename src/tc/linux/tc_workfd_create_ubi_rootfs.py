# SPDX-License-Identifier: GPL-2.0
#
# Description:
# create a ubifs rootfs
# ubi rootfs path: tb.config.tc_workfd_create_ubi_rootfs_path
# ubi parameters:
# tb.config.tc_ubi_min_io_size tb.config.tc_ubi_leb_size tb.config.tc_ubi_max_leb_cnt
# output path: tb.config.tc_workfd_create_ubi_rootfs_target
#
# used variables
#
# - tb.config.tc_workfd_create_ubi_rootfs_path
#| path into which the ubifs image with name
#| tb.config.tc_workfd_create_ubi_rootfs_target get created
#| default: '/opt/eldk-5.4/armv7a-hf/rootfs-minimal-mtdutils'
#
# - tb.config.tc_workfd_create_ubi_rootfs_target
#| name of the ubi image which get created
#| default: '/tftpboot/dxr2/tbot/rootfs-minimal.ubifs'
#
# End:
from tbotlib import tbot

tb.define_variable('tc_workfd_create_ubi_rootfs_path', '/opt/eldk-5.4/armv7a-hf/rootfs-minimal-mtdutils')
tb.define_variable('tc_workfd_create_ubi_rootfs_target', '/tftpboot/dxr2/tbot/rootfs-minimal.ubifs')
logging.info("args: workdfd: %s", tb.workfd.name)
logging.info("args: %s %s %s", tb.config.tc_ubi_min_io_size, tb.config.tc_ubi_leb_size, tb.config.tc_ubi_max_leb_cnt)
tb.eof_call_tc("tc_workfd_switch_su.py")

tmp = "date > " + tb.config.tc_workfd_create_ubi_rootfs_path + "/creation_time"
tb.write_lx_cmd_check(tb.workfd, tmp)
tmp = "cat " + tb.config.tc_workfd_create_ubi_rootfs_path + "/creation_time"
tb.write_lx_cmd_check(tb.workfd, tmp)

tmp = "mkfs.ubifs --root=" + tb.config.tc_workfd_create_ubi_rootfs_path + " -m " + tb.config.tc_ubi_min_io_size + " -e " + tb.config.tc_ubi_leb_size + " -c " + tb.config.tc_ubi_max_leb_cnt + " -F --output=" + tb.config.tc_workfd_create_ubi_rootfs_target
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.eof_write_cmd(tb.workfd, "exit")
tb.end_tc(True)
