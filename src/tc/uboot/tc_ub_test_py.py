# SPDX-License-Identifier: GPL-2.0
#
# Description:
# call test/py from u-boot source
# - power off the board
# - disconnect console
# - goto u-boot code with testcase tc_workfd_goto_uboot_code.py
# - call test/py
# - power off the board
# - connect back to console
# test/py hookscript directory:
# tb.config.tc_ub_test_py_hook_script_path
#
# you can disable this testcase with tb.config.tc_ub_test_py_start = 'no'
#
# may a configure file is needed, so create it with
# tb.config.tc_ub_test_py_configfile. This variable contains
# the config file, which gets created.
#
# at the end create event with ID UBOOT_TEST_PY
#
# used variables
#
# - tb.config.tc_ub_test_py_hook_script_path
#| full path to hook scripts for test/py
#| default: '$HOME/testframework/hook-scripts'
#
# - tb.config.tc_ub_test_py_configfile
#| list of strings with configsettings for test/py
#| default: '[]'
#
# - tb.config.tc_ub_test_py_start
#| if 'no' do not start test/py
#| default: 'yes'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_test_py_hook_script_path', '$HOME/testframework/hook-scripts')
tb.define_variable('tc_ub_test_py_configfile', '[]')
tb.define_variable('tc_ub_test_py_start', 'yes')

logging.info("args: %s %s", tb.config.boardname, tb.config.boardlabname)
logging.info("args: %s", tb.config.tc_lab_compile_uboot_boardname)
logging.info("args: %s", tb.config.tc_lab_source_dir)

if tb.config.tc_ub_test_py_start == 'no':
    tb.end_tc(True)

# power off the board. test.py should start from scratch
tb.eof_call_tc("tc_lab_poweroff.py")

tb.disconnect_from_board(tb.config.boardlabname)

c = tb.c_con
savefd = tb.workfd
tb.workfd = c

tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

tb.event.create_event('main', 'tc_ub_test_py.py', 'SET_DOC_FILENAME', 'test_py_start')
tc_ub_test_py_uboot_dir = tb.config.tc_lab_source_dir + "/u-boot-" + tb.config.boardlabname

# create config file if needed
if tb.config.tc_ub_test_py_configfile != []:
    cfgname = tb.config.tc_lab_compile_uboot_boardname.replace('-', '_')
    fn = tc_ub_test_py_uboot_dir + '/test/py/u_boot_boardenv_' + cfgname + '.py'
    opp = ' > '
    for line in tb.config.tc_ub_test_py_configfile:
        cmd = 'echo ' + line + opp + fn
        tb.eof_write(c, cmd)
        opp = ' >> '
    cmd = 'cat ' + fn
    tb.write_lx_cmd_check(c, cmd)

cmd = 'PATH=' + tb.config.tc_ub_test_py_hook_script_path + ':$PATH;PYTHONPATH=' + tc_ub_test_py_uboot_dir + ';./test/py/test.py --bd ' + tb.config.tc_lab_compile_uboot_boardname + ' -s --build-dir .'
tb.eof_write(c, cmd)
c.set_check_error(False)
searchlist = ['INTERNALERROR']
tmp = True
cmdsuccess = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
        cmdsuccess = False
    if ret == 'prompt':
        tmp = False

c.set_check_error(True)
cmdsuccess = tb.call_tc("tc_workfd_check_cmd_success.py")
logging.info("test/py: %s", cmdsuccess)

# power off board at end
tb.eof_call_tc("tc_lab_poweroff.py")
import time
time.sleep(2)

ret = tb.connect_to_board(tb.config.boardlabname)
if ret == False:
    tb.workfd = savefd
    tb.end_tc(ret)

tb.workfd = savefd

tb.event.create_event('main', tb.config.boardname, "UBOOT_TEST_PY", tc_ub_test_py_uboot_dir)
tb.end_tc(cmdsuccess)
