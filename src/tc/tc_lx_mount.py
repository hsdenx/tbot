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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_mount.py
from tbotlib import tbot

#here starts the real test
logging.info("dev: %s fs_type: %s dir: %s", tb.tc_lx_mount_dev, tb.tc_lx_mount_fs_type, tb.tc_lx_mount_dir)

#set board state for which the tc is valid
tb.set_board_state("linux")

tb.eof_write_con("mount")
ret = tb.search_str_in_readline_con(tb.tc_lx_mount_dev)
if ret != True:
    #mount device
    tmp = "mount -t " + tb.tc_lx_mount_fs_type + " " + tb.tc_lx_mount_dev + " " + tb.tc_lx_mount_dir
    tb.eof_write_con(tmp)
    tb.eof_search_str_in_readline_con("mounted filesystem")

tb.eof_read_end_state_con(2)
tb.end_tc(True)
