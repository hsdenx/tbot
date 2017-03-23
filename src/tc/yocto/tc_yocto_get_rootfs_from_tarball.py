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
# start with
# tbot.py -s lab_denx -c cuby -t tc_yocto_get_rootfs_from_tarball.py
#
# get rootfs version from rootfs tar ball filepath and name stored in
# tb.config.tc_yocto_get_rootfs_from_tarball
# and store versionstring in variable:
# tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version
# End:

from tbotlib import tbot

tb.workfd = tb.c_ctrl

cmd = 'tar zxvf ' + tb.config.tc_yocto_get_rootfs_from_tarball + ' ./etc/version'
tb.write_lx_cmd_check(tb.c_ctrl, cmd)
cmd = 'cat etc/version'
tb.eof_write_cmd_get_line(tb.c_ctrl, cmd)
tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version = tb.ret_write_cmd_get_line.strip()
cmd = 'rm -rf etc/'
tb.write_lx_cmd_check(tb.c_ctrl, cmd)

tb.end_tc(True)
