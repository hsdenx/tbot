# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# get rootfs version from rootfs tar ball filepath and name stored in
# tb.config.tc_yocto_get_rootfs_from_tarball
# and store versionstring in variable:
# tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version
#
# creates event ID DUTS_YOCTO_VERSION
#
# used variables:
#
# - tb.config.tc_yocto_get_rootfs_from_tarball
#| filename of tar.gz or tar.bz2 rootfsfile
#| default: ''
#
# - tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version
#| created while running tc_yocto_get_rootfs_from_tarball.py
#| contains the content of '/etc/version' of a yocto builded rootfs
#
# End:

from tbotlib import tbot

logging.info("args: workfd %s", tb.workfd.name)

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
