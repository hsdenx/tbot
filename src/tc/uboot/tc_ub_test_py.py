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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_test_py.py
# call test/py from u-boot source
# - disconnect console
# - call test/py
# - connect back to console
#
from tbotlib import tbot

logging.info("args: %s %s %s", tb.boardname, tb.boardlabname, tb.tc_ub_test_py_hook_script_path)

tb.disconnect_from_board(tb.boardlabname)

c = tb.c_con
savefd = tb.workfd
tb.workfd = c

tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

tc_ub_test_py_uboot_dir = tb.tc_lab_source_dir + "/u-boot-" + tb.boardlabname

cmd = 'PATH=' + tb.tc_ub_test_py_hook_script_path + ':$PATH;PYTHONPATH=' + tc_ub_test_py_uboot_dir + ';./test/py/test.py --bd ' + tb.boardname + ' -s --build-dir .'
tb.eof_write(c, cmd)
searchlist = ['INTERNALERROR', '====', 'failed', 'error']
tmp = True
cmdsuccess = True
track = 0
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
        cmdsuccess = False
    if ret == '1':
        track = 1
    if ret == '2':
        if track == 1:
            cmdsuccess = False
    if ret == '3':
        if track == 1:
            cmdsuccess = False
    if ret == 'prompt':
        tmp = False

ret = tb.connect_to_board(tb.boardlabname)
if ret == False:
    tb.workfd = savefd
    tb.end_tc(ret)

tb.set_board_state("u-boot")
tb.workfd = savefd
tb.end_tc(cmdsuccess)
