# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# check if the current running U-Boot vers == tb.uboot_vers
# and SPL vers == tb.spl_vers
#
# End:

from tbotlib import tbot

logging.info("arg: %s %s", tb.uboot_vers, tb.spl_vers)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# set env var
c = tb.c_con

if tb.uboot_vers != '':
    tmp = 'vers'
    tb.eof_write(c, tmp)
    searchlist = ['U-Boot 20']
    tmp = True
    ret = False
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
            if uvers == tb.uboot_vers:
                ret = True
            tmp = True

    if ret != True:
        logging.warn("UB Vers differ %s != %s", uvers, tb.uboot_vers)
        tb.end_tc(False)

if tb.spl_vers == '':
    tb.end_tc(True)

tmp = 'res'
tb.c_con.set_check_error(False)
tb.eof_write(c, tmp)
searchlist = ['U-Boot SPL 20']
tmp = True
ret = False
splvers = 'undef'
while tmp == True:
    retu = tb.tbot_rup_and_check_strings(c, searchlist)
    if retu == 'prompt':
        tmp = False
    if retu == '0':
        ret = tb.tbot_rup_and_check_strings(c, '\n')
        if ret == 'prompt':
            tb.enc_tc(False)
        tmp = 'U-Boot SPL 20' + tb.buf.replace('\r','')
        splvers = tmp.replace('\n','')
        ret == False
        if splvers == tb.spl_vers:
            ret = True
        tmp = False

tb.set_board_state("u-boot")
tb.c_con.set_check_error(True)

if ret == False:
    logging.warn("UB SPL Vers differ %s != %s", splvers, tb.spl_vers)


tb.gotprompt = True
tb.end_tc(ret)
