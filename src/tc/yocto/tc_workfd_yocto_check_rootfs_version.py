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
# tbot.py -s lab_denx -c cuby -t tc_workfd_yocto_check_rootfs_version.py
#
# check if the current /etc/version on the target rootfs is the
# same as in tb.onfig.tc_yocto_get_rootfs_from_tarball
#
# End:

from tbotlib import tbot

# boot into linux
tb.set_board_state("linux")

try:
    tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version
except:
    tb.workfd = tb.c_ctrl
    tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")
    tb.eof_call_tc("tc_workfd_goto_yocto_code.py")
    tb.eof_call_tc("tc_yocto_get_rootfs_from_tarball.py")

# check if we booted the new rootfs version
cmd = 'cat /etc/version'
tb.eof_write_cmd_get_line(tb.c_con, cmd)
rootfsvers = tb.ret_write_cmd_get_line.strip()
if tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version != rootfsvers:
    logging.error("Wrong rootfs vers found: %s != %s" % (rootfsvers, tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version))
    tb.end_tc(False)

tb.end_tc(True)
