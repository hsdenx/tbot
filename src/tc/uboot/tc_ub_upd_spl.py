# SPDX-License-Identifier: GPL-2.0
#
# Description:
# update new spl to board if tb.config.tc_ub_upd_spl_withspl == 'yes'
#
# steps:
# - load tbot u-boot env vars if tb.config.tc_ub_upd_spl_latest != 'no'
#|  with testcase tc_ub_load_board_env.py
# - execute "run tbot_upd_spl"
# - execute "run tbot_cmp_spl"
# - reset board
# - get u-boot
#
# used variables
#
# - tb.config.tc_ub_upd_spl_ubvars
#| additionaly printed U-Boot Environmnet variables, if != 'none'
#| default: 'none'
#
# - tb.config.tc_ub_upd_spl_withspl
#| if != 'yes' do nothing, return True
#| default: 'yes'
#
# - tb.config.tc_ub_upd_spl_latest
#| if == 'no' load U-Boot Environment with testcase
#| tc_ub_load_board_env.py
#| default: 'no'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_upd_spl_ubvars', 'none')
tb.define_variable('tc_ub_upd_spl_withspl', 'yes')
tb.define_variable('tc_ub_upd_spl_latest', 'no')

logging.info("args: %s %s", tb.config.ub_load_board_env_addr, tb.config.ub_load_board_env_subdir)

if tb.config.tc_ub_upd_spl_withspl != 'yes':
    tb.end_tc(True)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

if tb.config.tc_ub_upd_spl_latest == 'no':
    # call tc tc_ub_load_board_env.py
    tb.eof_call_tc("tc_ub_load_board_env.py")

c = tb.c_con
# start tbot_upd_uboot
# 'OK' must beread, if the board supports
# hush shell, best to run if then else with echoing
# OK ...
tb.event.create_event('main', 'tc_ub_upd_spl.py', 'SET_DOC_FILENAME', 'print_upd_spl')
cmd = "print tbot_upd_spl"
if tb.config.tc_ub_upd_spl_ubvars != 'none':
    cmd = cmd + ' ' + tb.config.tc_ub_upd_spl_ubvars
tb.eof_write_cmd(c, cmd)
upd_fail = True
i = 0
retry = 2
while upd_fail == True:
    if i >= retry:
        # board now maybe without u-boot
        # try a save u-boot ?
        tb.end_tc(False)

    tb.event.create_event('main', 'tc_ub_upd_spl.py', 'SET_DOC_FILENAME', 'upd_spl')
    tb.eof_write(c, "run tbot_upd_spl")
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
tb.eof_write_cmd(c, "print tbot_cmp_spl", create_doc_event=True)
tb.event.create_event('main', 'tc_ub_upd_spl.py', 'SET_DOC_FILENAME', 'cmp_spl')
tb.eof_write(c, "run tbot_cmp_spl")

# read "!=" -> error
ret = tb.tbot_expect_string(c, '!=')
if ret != 'prompt':
    tb.end_tc(False)

if tb.config.tc_ub_upd_spl_latest == 'no':
    # reset the board
    tb.eof_call_tc("tc_ub_reset.py")

tb.end_tc(True)
