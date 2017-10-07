# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
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
