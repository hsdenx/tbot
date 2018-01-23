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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_test_py.py
# call test/py from u-boot source
# - disconnect console
# - call test/py
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
# End:

from tbotlib import tbot

try:
    tb.config.tc_lab_compile_uboot_boardname
except:
    tb.config.tc_lab_compile_uboot_boardname = tb.config.boardname

try:
    tb.config.tc_ub_test_py_configfile
except:
    tb.config.tc_ub_test_py_configfile = []

logging.info("args: %s %s %s", tb.config.boardname, tb.config.boardlabname, tb.config.tc_ub_test_py_hook_script_path)
logging.info("args: %s", tb.config.tc_lab_compile_uboot_boardname)

if tb.config.tc_ub_test_py_start == 'no':
    tb.end_tc(True)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

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
ret = tb.connect_to_board(tb.config.boardlabname)
if ret == False:
    tb.workfd = savefd
    tb.end_tc(ret)

tb.set_board_state("u-boot")
tb.workfd = savefd

tb.event.create_event('main', tb.config.boardname, "UBOOT_TEST_PY", tc_ub_test_py_uboot_dir)
tb.end_tc(cmdsuccess)
