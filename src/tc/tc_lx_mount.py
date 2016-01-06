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
searchlist = [tb.tc_lx_mount_dev]
tmp = True
found = False
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
    if tmp == 0:
        found = True
        tmp = True
    elif tmp == None:
        #endless loop ...
        tmp = True
    elif tmp == 'prompt':
        tmp = False

if found == True:
    tb.end_tc(True)

#mount device
tmp = "mount -t " + tb.tc_lx_mount_fs_type + " " + tb.tc_lx_mount_dev + " " + tb.tc_lx_mount_dir
tb.eof_write_con(tmp)
searchlist = ["mounted filesystem"]
tmp = True
cmd_ok = False
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
    if tmp == 0:
        cmd_ok = True
        tmp = True
    elif tmp == None:
        #endless loop ...
        tmp = True
    elif tmp == 'prompt':
        tmp = False

if cmd_ok == True:
    tb.end_tc(True)

tb.workfd = tb.channel_con
tb.eof_call_tc("tc_workfd_check_cmd_success.py")
