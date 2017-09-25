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
# - set workfd to c_ctrl
# - call tc_yocto_install_rootfs_as_nfs.py
# - if tb.config.rootfs_sdcard_file != ''
#     copy sd card image into nfs
# - restore old workfd
#
# End:

from tbotlib import tbot

try:
    tb.config.rootfs_sdcard_file
except:
    tb.config.rootfs_sdcard_file = ''

logging.info("args: %s %s %s %s", tb.workfd.name, tb.config.yocto_results_dir_lab, tb.config.nfs_subdir, tb.config.rootfs_sdcard_file)

save = tb.workfd
tb.workfd = tb.c_ctrl

tb.config.tc_yocto_install_rootfs_as_nfs_path = tb.config.yocto_results_dir_lab
tb.eof_call_tc("tc_yocto_install_rootfs_as_nfs.py")

if tb.config.rootfs_sdcard_file != '':
    # copy sd card image into nfs
    cmd = 'sudo cp ' + tb.config.yocto_results_dir_lab + tb.config.rootfs_sdcard_file + ' '  + tb.config.nfs_subdir + '/boot'
    tb.write_lx_sudo_cmd_check(tb.c_ctrl, cmd, tb.config.user, tb.config.ip)

tb.workfd = save
tb.end_tc(True)
