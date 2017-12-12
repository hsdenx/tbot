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
# - install tb.config.rootfs_tar_file in path tb.config.tc_yocto_install_rootfs_as_nfs_path
#   into tb.config.nfs_subdir
#
# End:

from tbotlib import tbot

logging.info("args: %s %s %s %s", tb.workfd.name, tb.config.rootfs_tar_file, tb.config.tc_yocto_install_rootfs_as_nfs_path, tb.config.nfs_subdir)

# remove all files from nfs dir
cmd = 'sudo rm -rf ' + tb.config.nfs_subdir + '/*'
tb.write_lx_sudo_cmd_check(tb.c_ctrl, cmd, tb.config.user, tb.config.ip)

tb.config.tc_workfd_check_if_dir_exists_name = tb.config.nfs_subdir
tb.config.tc_workfd_check_if_dir_exists_create = 'yes'
tb.eof_call_tc("tc_workfd_check_if_dir_exist.py")
cmd = 'cd ' + tb.config.nfs_subdir
tb.write_lx_cmd_check(tb.c_ctrl, cmd)

if 'tar.bz2' in tb.config.rootfs_tar_file:
    opt = 'xfj '
else:
    opt = 'zxf '

cmd = 'sudo tar ' + opt + tb.config.tc_yocto_install_rootfs_as_nfs_path + tb.config.rootfs_tar_file
tb.write_lx_sudo_cmd_check(tb.c_ctrl, cmd, tb.config.user, tb.config.ip, triggerlist=['tar'])

tb.end_tc(True)
