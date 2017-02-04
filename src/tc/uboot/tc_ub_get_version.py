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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_get_version.py
# get the U-Boot and/or SPL version from a binary
# and save it in tb.uboot_vers or tb.spl_vers
# End:

from tbotlib import tbot

logging.info("arg: %s %s %s", tb.workfd.name, tb.tc_ub_get_version_file, tb.tc_ub_get_version_string)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# set env var
c = tb.workfd

sf = tb.tc_ub_get_version_file
se = tb.tc_ub_get_version_string

tmp = 'strings -a ' + sf + ' | grep "' + se + '"'
tb.eof_write(c, tmp)

searchlist = [se]
tmp = True
ret = False
while tmp == True:
    retu = tb.tbot_rup_and_check_strings(c, searchlist)
    if retu == 'prompt':
        tmp = False
    if retu == '0':
        ret = tb.tbot_rup_and_check_strings(c, '\n')
        if ret == 'prompt':
            tb.enc_tc(False)
        tmp = tb.buf.split('\x1b')
        tmp = tmp[2][2:]
        tmp = se + tmp.replace('\r','')
        tmp = tmp.replace('\n','')
        tb.config.tc_return = tmp
        tmp = True
        ret = True

tb.event.create_event('main', tb.config.boardname, "UBOOT_VERSION", tb.config.tc_return)

tb.end_tc(ret)
