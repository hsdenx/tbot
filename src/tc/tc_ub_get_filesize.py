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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_get_filesize.py
# simple get the content of U-Boot env variable filesize
# and store it in tb.ub_filesize
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.eof_write_con('printenv filesize')
searchlist = ["filesize"]
tmp = True
found = False
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
    if tmp == 0:
        tmp=self.buf[tb.channel_con].split("=")[1]
        tb.ub_filesize = tmp.rstrip()
        logging.info("set tb.ub_filesize to %s", tb.ub_filesize)
        tmp = True
        found = True
    elif tmp == 'prompt':
        tmp = False

tb.end_tc(found)
