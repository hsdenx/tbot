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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_partition_check.py
# cp a dummy file into a partiton umount/mount it and
# diff it
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("linux")

#call tc mount partition
tb.eof_call_tc("tc_lx_mount.py")

#create tempfile
tb.tc_lx_dummy_file_bs = "1024"
tb.tc_lx_dummy_file_count = "1024"
tb.tc_lx_dummy_file_tempfile = "/tmp/gnlmpf_partition"
ret = tb.eof_call_tc("tc_lx_create_dummy_file.py")

#copy dummy file into partition
tmp = "cp " + tb.tc_lx_dummy_file_tempfile + " " + tb.tc_lx_mount_dir
tb.eof_write_con(tmp)
tb.eof_wait_prompt(5)

#umount the partition
tmp = "umount " + tb.tc_lx_mount_dev
tb.eof_write_con(tmp)
tb.eof_wait_prompt(5)

#mount it again
tb.eof_call_tc("tc_lx_mount.py")

#compare the dummy file with the file in the partition
tmp = "cmp " + tb.tc_lx_dummy_file_tempfile + " " + tb.tc_lx_mount_dir + "/gnlmpf_partition"
tb.eof_write_con(tmp)
searchlist = ["diff"]
tmp = True
cmd_ok = True
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
    if tmp == 0:
        cmd_ok = False
        tmp = True
    elif tmp == None:
        #endless loop...
        tmp = True
    elif tmp == 'prompt':
        tmp = False

tb.end_tc(cmd_ok)
