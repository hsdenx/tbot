# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# execute U-Boots "version" cmd, and create event
# - DUTS_UBOOT_VERSION
# - DUTS_SPL_VERSION
# - DUTS_BOARDNAME = tb.config.boardlabpowername
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

tb.c_con.set_check_error(False)
tb.write_stream(c, 'res')
searchlist = ['U-Boot SPL 20', 'autoboot']
tmp = True
splvers = 'undef'
while tmp == True:
    retu = tb.tbot_rup_and_check_strings(c, searchlist)
    if retu == 'prompt':
        tmp = False
    if retu == '1':
        tmp = False
    if retu == '0':
        tb.tbot_rup_and_check_strings(c, '\n')
        tmp2 = 'U-Boot SPL 20' + tb.buf.replace('\r','')
        splvers = tmp2.replace('\n','')
        tmp = False

tb.set_board_state("u-boot")
tb.c_con.set_check_error(True)

if uvers != 'undef':
    tb.event.create_event('main', tb.config.boardname, "DUTS_UBOOT_VERSION", uvers)
if splvers != 'undef':
    tb.event.create_event('main', tb.config.boardname, "DUTS_SPL_VERSION", splvers)

tb.end_tc(True)
