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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_mount.py
# mount device tb.config.tc_lx_mount_dev with fs type tb.config.tc_lx_mount_fs_type
# to tb.config.tc_lx_mount_dir
# End:

from tbotlib import tbot

# here starts the real test
logging.info("dev: %s fs_type: %s dir: %s", tb.config.tc_lx_mount_dev, tb.config.tc_lx_mount_fs_type, tb.config.tc_lx_mount_dir)

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.c_con
tb.eof_write(c, "mount")
searchlist = [tb.config.tc_lx_mount_dev]
tmp = True
found = False
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(c, searchlist)
    if ret == '0':
        found = True
    elif ret == 'prompt':
        tmp = False

if found == True:
    tb.end_tc(True)

# mount device
tmp = "mount -t " + tb.config.tc_lx_mount_fs_type + " " + tb.config.tc_lx_mount_dev + " " + tb.config.tc_lx_mount_dir
tb.eof_write(c, tmp)
searchlist = ["mounted filesystem"]
tmp = True
cmd_ok = False
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(c, searchlist)
    if ret == '0':
        cmd_ok = True
    elif ret == 'prompt':
        tmp = False

if cmd_ok == True:
    tb.end_tc(True)

tb.workfd = tb.c_con
tb.eof_call_tc("tc_workfd_check_cmd_success.py")
tb.end_tc(True)
