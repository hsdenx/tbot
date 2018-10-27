# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# simply call ptest-runner and create
# some events:
#
# SET_PTEST_START
# created when ptest-runner send "START:"
#
# SET_PTEST_BEGIN
# created when ptest-runner send "BEGIN:"
#
# SET_PTEST_PASS
# created when ptest-runner send "PASS:"
#
# SET_PTEST_SKIP
# created when ptest-runner send "SKIP:"
#
# SET_PTEST_FAIL
# created when ptest-runner send "FAIL:"
#
# SET_PTEST_ERROR
# created when ptest-runner send "ERROR:"
#
# SET_PTEST_SUM_PASS
# count of 'PASS:' a test created
#
# SET_PTEST_SUM_SKIP
# count of 'SKIP:' a test created
#
# SET_PTEST_SUM_FAIL
# count of 'FAIL:' a test created
#
# SET_PTEST_SUM
# created when ptest-runner send 'END:'
# created before 'SET_PTEST_END' is created.
# contains a statistic of all pass, skip and fails a
# test created.
#
# SET_PTEST_END
# created when ptest-runner send 'END:'
#
# SET_PTEST_SUM_PASS_A
# count of all 'PASS:' all tests created
#
# SET_PTEST_SUM_SKIP_A
# count of all 'SKIP:' all tests created
#
# SET_PTEST_SUM_FAIL_A
# count of all 'FAIL:' all tests created
#
# SET_PTEST_SUM_ALL
# created when ptest-runner send 'STOP:'
# created before 'SET_PTEST_STOP' is created.
# contains a statistic of all pass, skip and fails all
# tests created.
#
# SET_PTEST_STOP
# created when ptest-runner send 'STOP:'
#
# End:

from tbotlib import tbot


tb.set_board_state("linux")
c = tb.c_con

tb.config.tc_workfd_check_if_cmd_exist_cmdname = 'ptest-runner'
ret = tb.call_tc("tc_workfd_check_if_cmd_exist.py")
# if ptest-runner does not exist, simply return True
if ret == False:
    tb.end_tc(True)

# collect pass, skip and fail infos for each subtest
# and create events for it, so we can later parse
# them in a backend
tb.eof_write(c, 'ptest-runner')
loop = True
skip_a = 0
fail_a = 0
pas_a = 0
skip = 0
fail = 0
pas = 0
name = 'unknown'
fname = 'tc_board_k30rf_ptest_runner.py'
strings = ['START:', 'BEGIN:', 'PASS:', 'SKIP:', 'FAIL:', 'ERROR', 'END:', 'STOP:', '======================', '\n']
while loop:
    ret = tb.tbot_rup_and_check_strings(c, strings)
    if ret == '0':
        ret = tb.tbot_get_line(c)
        name = tb.buf.replace(' ', '_').strip()
        tb.event.create_event('main', fname, 'SET_PTEST_START', name)
    elif ret == '1':
        ret = tb.tbot_get_line(c)
        name = tb.buf.replace(' ', '_').strip()
        tb.event.create_event('main', fname, 'SET_PTEST_BEGIN', name)
    elif ret == '2':
        pas += 1
        ret = tb.tbot_get_line(c)
        value = tb.buf.replace(' ', '_').strip()
        tb.event.create_event('main', fname, 'SET_PTEST_PASS', value)
    elif ret == '3':
        skip += 1
        ret = tb.tbot_get_line(c)
        value = tb.buf.replace(' ', '_').strip()
        tb.event.create_event('main', fname, 'SET_PTEST_SKIP', value)
    elif ret == '4':
        fail += 1
        ret = tb.tbot_get_line(c)
        value = tb.buf.replace(' ', '_').strip()
        tb.event.create_event('main', fname, 'SET_PTEST_FAIL', value)
    elif ret == '5':
        fail += 1
        ret = tb.tbot_get_line(c)
        value = tb.buf.replace(' ', '_').strip()
        tb.event.create_event('main', fname, 'SET_PTEST_ERROR', value)
    elif ret == '6':
        ret = tb.tbot_get_line(c)
        value = tb.buf.replace(' ', '_').strip()
        tb.event.create_event('main', fname, 'SET_PTEST_SUM_PASS', str(pas))
        tb.event.create_event('main', fname, 'SET_PTEST_SUM_SKIP', str(skip))
        tb.event.create_event('main', fname, 'SET_PTEST_SUM_FAIL', str(fail))
        string = ("%s stats: pass: %d skip: %d fail: %d" %(value, pas, skip, fail))
        logging.info(string)
        tb.event.create_event('main', fname, 'SET_PTEST_SUM', string)
        tb.event.create_event('main', fname, 'SET_PTEST_END', value)
        skip_a += skip
        fail_a += fail
        pas_a += pas
        skip = 0
        fail = 0
        pas = 0
    elif ret == '7':
        ret = tb.tbot_get_line(c)
        value = tb.buf.replace(' ', '_').strip()
        tb.event.create_event('main', fname, 'SET_PTEST_SUM_PASS_A', str(pas_a))
        tb.event.create_event('main', fname, 'SET_PTEST_SUM_SKIP_A', str(skip_a))
        tb.event.create_event('main', fname, 'SET_PTEST_SUM_FAIL_A', str(fail_a))
        string = ("%s all stats: pass: %d skip: %d fail: %d" %(value, pas_a, skip_a, fail_a))
        logging.info(string)
        tb.event.create_event('main', fname, 'SET_PTEST_SUM_ALL', string)
        tb.event.create_event('main', fname, 'SET_PTEST_STOP', value)
    elif ret == '8':
        ret = tb.tbot_get_line(c)
        value = tb.buf.replace(' ', '_').strip()
        tb.event.create_event('main', 'tc_board_k30rf_ptest_runner.py', 'SET_PTEST_SUBSTART', value)
    elif ret == 'prompt':
        loop = False

ret = tb.call_tc("tc_workfd_check_cmd_success.py")
# check if name != value -> means something gone wrong
value = 'False'
if ret == True:
    value = 'True'
tb.end_tc(ret)
