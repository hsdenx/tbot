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
# tbot.py -s lab_denx -c smartweb -t tc_demo_uboot_tests.py
#
# start all "standard" u-boot testcases
#
# - if tb.config.tc_demo_uboot_test_reg_files contains
#   a list of files, check for each file with testcase
#   tc_ub_check_reg_file.py if the registersettings are
#   correct.
#
# - start cmd defined in tb.config.tc_demo_uboot_test_basic_cmd
#   and check the returning strings.
#
# - tb.eof_call_tc("uboot/duts/tc_ub_start_all_duts.py")
#
# - tb.eof_call_tc("tc_ub_test_py.py")
#
# - call a list of testcases defined in
#   tb.config.tc_demo_uboot_tc_list
#
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# call tc tc_ub_load_board_env.py
tb.eof_call_tc("tc_ub_load_board_env.py")

# register checks
try:
    files = tb.config.tc_demo_uboot_test_reg_files
except:
    files = ''

if (files != ''):
    tb.statusprint("start register check")
    for tb.config.tc_ub_create_reg_file_name in files:
        tb.eof_call_tc('tc_ub_check_reg_file.py')

# call basic cmd list
try:
    bcmd = tb.config.tc_demo_uboot_test_basic_cmd
except:
    bcmd = ''

if bcmd != '':
    tb.statusprint("start basic U-Boot checks")
    for bl in bcmd:
        if bl["val"] == 'undef':
            tb.eof_write_cmd(tb.c_con, bl["cmd"])
        else:
            tb.eof_call_tc('tc_workfd_write_cmd_check.py', cmd=bl["cmd"], string=bl["val"])

tb.workfd = tb.c_ctrl
tb.statusprint("start all DUTS testcases")
tb.eof_call_tc("uboot/duts/tc_ub_start_all_duts.py")

# call test/py
tb.statusprint("u-boot test/py test")
tb.eof_call_tc("tc_ub_test_py.py")

try:
    tc = tb.config.tc_demo_uboot_tc_list
except:
    tc = ''

if tc != '':
    tb.statusprint("Call board specific testcases")
    for tcname in tc:
        tb.eof_call_tc(tcname)

tb.end_tc(True)
