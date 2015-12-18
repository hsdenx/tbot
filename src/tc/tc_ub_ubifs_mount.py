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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubifs_mount.py
# - mounts an ubifs
from tbotlib import tbot

logging.info("args: %s", tb.tc_ub_ubifs_volume_name)

#set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = 'ubifsmount ' + tb.tc_ub_ubifs_volume_name
tb.eof_write_con(tmp)
searchlist = ["Error"]
tmp = True
mounted = True
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
    if tmp == 0:
        mounted = False
        tmp = True
    elif tmp == 'prompt':
        tmp = False

tb.end_tc(mounted)
