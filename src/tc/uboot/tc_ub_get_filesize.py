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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_get_filesize.py
# simple get the content of U-Boot env variable filesize
# and store it in tb.ub_filesize
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

c = tb.c_con
tb.eof_write(c, 'printenv filesize')
searchlist = ["filesize"]
tmp = True
found = False
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        ret = tb.read_line(c)
        if ret == True:
            tmp = self.buf.replace('=','')
            tmp = tmp.replace('\r','')
            tmp = tmp.replace('\n','')
            tb.ub_filesize = tmp
            logging.info("set tb.ub_filesize to %s", tb.ub_filesize)
            found = True
            tmp = True
    elif ret == 'prompt':
        tmp = False

tb.end_tc(found)
