# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_upd_uboot.py
# update new uboot to board
# steps:
# - load tbot u-boot env vars
# - execute "run tbot_upd_uboot"
# - execute "run tbot_cmp_uboot"
# - reset board
# - get u-boot
# End:

from tbotlib import tbot

try:
    tb.config.tc_ub_upd_uboot_ubvars
except:
    tb.config.tc_ub_upd_uboot_ubvars = ''

logging.info("args: %s %s %s %s", tb.config.ub_load_board_env_addr, tb.config.ub_load_board_env_subdir, tb.config.tc_ub_upd_uboot_latest, tb.config.tc_ub_upd_uboot_ubvars)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

if tb.config.tc_ub_upd_uboot_latest == 'no':
    # call tc tc_ub_load_board_env.py
    tb.eof_call_tc("tc_ub_load_board_env.py")

c = tb.c_con
# start tbot_upd_uboot
# 'OK' must beread, if the board supports
# hush shell, best to run if then else with echoing
# OK ...
tb.event.create_event('main', 'tc_ub_upd_uboot.py', 'SET_DOC_FILENAME', 'print_upd_uboot')
tb.eof_write_cmd(c, "print tbot_upd_uboot " + tb.config.tc_ub_upd_uboot_ubvars)
upd_fail = True
i = 0
retry = 2
while upd_fail == True:
    if i >= retry:
        # board now maybe without u-boot
        # try a save u-boot ?
        tb.end_tc(False)

    tb.event.create_event('main', 'tc_ub_upd_uboot.py', 'SET_DOC_FILENAME', 'upd_uboot')
    tb.eof_write(c, "run tbot_upd_uboot")
    searchlist = ["!= byte at", "error", "Retry count exceeded", "not defined"]
    tmp = True
    upd_fail = False
    while tmp == True:
        ret = tb.tbot_rup_and_check_strings(c, searchlist)
        if ret == '0':
            upd_fail = True
        elif ret == '1':
            upd_fail = True
        elif ret == '2':
            upd_fail = True
        elif ret == '3':
            upd_fail = True
        elif ret == 'prompt':
            i += 1
            tmp = False

# "run tbot_cmp_uboot"
tb.eof_write_cmd(c, "print tbot_cmp_uboot", create_doc_event=True)
tb.event.create_event('main', 'tc_ub_upd_uboot.py', 'SET_DOC_FILENAME', 'cmp_uboot')
tb.eof_write(c, "run tbot_cmp_uboot")

# read "!=" -> error
ret = tb.tbot_expect_string(c, '!=')
if ret != 'prompt':
    tb.end_tc(False)

if tb.config.tc_ub_upd_uboot_latest == 'no':
    # reset the board
    tb.eof_call_tc("tc_ub_reset.py")

tb.end_tc(True)
