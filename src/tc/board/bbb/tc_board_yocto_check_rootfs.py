# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# check if in booted rootfs, the rootfs version is the
# same as in tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version
#
# End:

from tbotlib import tbot

tb.config.bbb_check_crng_init = 'no'

tb.set_board_state("linux")

try:
    tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version
except:
    tb.config.tc_yocto_get_rootfs_from_tarball = tb.config.yocto_results_dir_lab + tb.config.rootfs_tar_file
    tb.workfd = tb.c_ctrl
    tb.eof_call_tc("tc_yocto_get_rootfs_from_tarball.py")

logging.info("args: %s", tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version)

tb.eof_call_tc("tc_workfd_yocto_check_rootfs_version.py")

tb.end_tc(True)
