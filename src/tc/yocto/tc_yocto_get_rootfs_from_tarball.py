# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c boardname -t tc_yocto_get_rootfs_from_tarball.py
#
# get rootfs version from rootfs tar ball filepath and name stored in
# tb.config.tc_yocto_get_rootfs_from_tarball
# and store versionstring in variable:
# tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd.name, tb.config.tc_yocto_get_rootfs_from_tarball)

if 'tar.bz2' in tb.config.tc_yocto_get_rootfs_from_tarball:
    opt = 'xfvj '
else:
    opt = 'zxvf '

cmd = 'tar ' + opt + tb.config.tc_yocto_get_rootfs_from_tarball + ' ./etc/version'
tb.write_lx_cmd_check(tb.workfd, cmd)
cmd = 'cat etc/version'
tb.eof_write_cmd_get_line(tb.workfd, cmd)
tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version = tb.ret_write_cmd_get_line.strip()
tb.event.create_event('main', tb.config.boardname, "DUTS_YOCTO_VERSION", tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version)
cmd = 'rm -rf etc/'
tb.write_lx_cmd_check(tb.workfd, cmd)

tb.end_tc(True)
