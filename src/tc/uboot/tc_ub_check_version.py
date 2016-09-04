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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_check_version.py
# check if the current running U-Boot vers == tb.uboot_vers
# and SPL vers == tb.spl_vers
# End:

from tbotlib import tbot

logging.info("arg: %s %s", tb.uboot_vers, tb.spl_vers)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# set env var
c = tb.c_con

tmp = 'vers'
tb.eof_write(c, tmp)
searchlist = ['U-Boot 20']
tmp = True
ret = False
while tmp == True:
    retu = tb.tbot_read_line_and_check_strings(c, searchlist)
    if retu == 'prompt':
        tmp = False
    if retu == '0':
        ret = tb.tbot_read_line_and_check_strings(c, '\n')
        if ret == 'prompt':
            tb.enc_tc(False)
        tmp = 'U-Boot 20' + tb.buf.replace('\r','')
        tmp = tmp.replace('\n','')
        if tmp == tb.uboot_vers:
            ret = True
        tmp = True

if ret != True:
    tb.end_tc(False)

if tb.spl_vers == '':
    tb.end_tc(True)

tmp = 'res'
tb.eof_write(c, tmp)
searchlist = ['U-Boot SPL 20']
tmp = True
ret = False
while tmp == True:
    retu = tb.tbot_read_line_and_check_strings(c, searchlist)
    if retu == 'prompt':
        tmp = False
    if retu == '0':
        ret = tb.tbot_read_line_and_check_strings(c, '\n')
        if ret == 'prompt':
            tb.enc_tc(False)
        tmp = 'U-Boot SPL 20' + tb.buf.replace('\r','')
        tmp = tmp.replace('\n','')
        if tmp == tb.spl_vers:
            ret = True
        tmp = True

tb.end_tc(ret)
