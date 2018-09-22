# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# install tb.config.rootfs_tar_file from path tb.config.tc_yocto_install_rootfs_as_nfs_path
# into tb.config.nfs_subdir
#
# used variables
#
# - tb.config.rootfs_tar_file
#| tar file with rootfs content
#| default: ''
#
# - tb.config.tc_yocto_install_rootfs_as_nfs_path
#| path to testcase finds file tb.config.rootfs_tar_file
#| default: ''
#
# - tb.config.nfs_subdir
#| nfs path
#| default: ''
#
# End:

from tbotlib import tbot

tb.define_variable('rootfs_tar_file', '')
tb.define_variable('tc_yocto_install_rootfs_as_nfs_path', '')
tb.define_variable('nfs_subdir', '')

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
