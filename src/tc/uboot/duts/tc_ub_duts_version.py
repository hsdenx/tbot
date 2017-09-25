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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_duts_version.py
#
# execute U-Boots "version" cmd, and create event
# DUTS_UBOOT_VERSION
# DUTS_SPL_VERSION
# DUTS_BOARDNAME = tb.config.boardlabpowername
#
# End:

from tbotlib import tbot

logging.info("args: %s", tb.workfd.name)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

c = tb.c_con

tb.eof_write(c, 'vers')
searchlist = ['U-Boot 20']
tmp = True
uvers = 'undef'
while tmp == True:
    retu = tb.tbot_rup_and_check_strings(c, searchlist)
    if retu == 'prompt':
        tmp = False
    if retu == '0':
        ret = tb.tbot_rup_and_check_strings(c, '\n')
        if ret == 'prompt':
            tb.enc_tc(False)
        tmp = 'U-Boot 20' + tb.buf.replace('\r','')
        uvers = tmp.replace('\n','')
        tmp = True

tb.eof_write(c, 'res')
searchlist = ['U-Boot SPL 20']
tmp = True
splvers = 'undef'
while tmp == True:
    retu = tb.tbot_rup_and_check_strings(c, searchlist)
    if retu == 'prompt':
        tmp = False
    if retu == '0':
        tb.tbot_rup_and_check_strings(c, '\n')
        tmp2 = 'U-Boot SPL 20' + tb.buf.replace('\r','')
        splvers = tmp2.replace('\n','')
        tmp = False

tb.set_board_state("u-boot")

if uvers != 'undef':
    tb.event.create_event('main', tb.config.boardname, "DUTS_UBOOT_VERSION", uvers)
if splvers != 'undef':
    tb.event.create_event('main', tb.config.boardname, "DUTS_SPL_VERSION", splvers)

tb.end_tc(True)
