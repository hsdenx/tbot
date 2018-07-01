# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# check if the current /etc/version on the target rootfs is the
# same as in tb.config.tc_yocto_get_rootfs_from_tarball
#
# End:

from tbotlib import tbot

# boot into linux
tb.set_board_state("linux")

try:
    tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version
except:
    save = tb.workfd
    tb.workfd = tb.c_ctrl
    tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")
    tb.eof_call_tc("tc_workfd_goto_yocto_code.py")
    tb.eof_call_tc("tc_yocto_get_rootfs_from_tarball.py")
    tb.workfd = save

# check if we booted the new rootfs version
cmd = 'cat /etc/version'
tb.eof_write_cmd_get_line(tb.c_con, cmd)
rootfsvers = tb.ret_write_cmd_get_line.strip()
if tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version != rootfsvers:
    logging.error("Wrong rootfs vers found: %s != %s" % (rootfsvers, tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version))
    tb.end_tc(False)

tb.end_tc(True)
