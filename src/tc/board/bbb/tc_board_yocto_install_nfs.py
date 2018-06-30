# SPDX-License-Identifier: GPL-2.0
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
