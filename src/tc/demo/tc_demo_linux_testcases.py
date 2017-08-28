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
# tbot.py -s lab_denx -c beagleboneblack -t tc_demo_linux_testcases.py
#
# - boot a linux kernel
# - get booted linux version
# - grep through dmesg and check if strings in
#   tb.config.tc_demo_linux_test_dmesg exist
# - check with devmem2 if the register values defined
#   in the register files tb.config.tc_demo_linux_test_reg_files
#   are identical with the values defined in the files
# - start cmd defined in tb.config.tc_demo_linux_test_basic_cmd
#   and check the returning strings.
# - call testcase names defined in list tb.config.tc_demo_linux_tc_list
#
# End:

from tbotlib import tbot

# call ubot setenv
tb.set_board_state("u-boot")
tb.eof_write_cmd(tb.c_con, "version")

tb.workfd = tb.c_con

ret = tb.eof_call_tc("tc_lx_get_version.py")
if ret == False:
    tb.end_tc(False)

tb.statusprint("Linux vers: %s" % (tb.config.tc_return))

lx_vers = tb.config.tc_return.split()[0]
tb.statusprint("linux checking Linux Version %s" % (lx_vers))

# you can use now the lx_vers for differ between linux versions

tb.set_board_state("linux")

# dmesg checks
try:
    check = tb.config.tc_demo_linux_test_dmesg
except:
    check = ''

if check != '':
    tb.statusprint("linux dmesg checks")
    for tb.config.tc_lx_dmesg_grep_name in check:
        tb.eof_call_tc("tc_lx_dmesg_grep.py")

# register checks
try:
    files = tb.config.tc_demo_linux_test_reg_files
except:
    files = ''
if (files != ''):
    tb.statusprint("start register check")
    for tb.config.tc_lx_create_reg_file_name in files:
        tb.eof_call_tc("tc_lx_check_reg_file.py")

# do some basic tests
try:
    bcmd = tb.config.tc_demo_linux_test_basic_cmd
except:
    bcmd = ''

if bcmd != '':
    tb.statusprint("start basic checks")
    for bl in bcmd:
        if bl["val"] == 'undef':
            tb.eof_write_cmd(tb.c_con, bl["cmd"])
        else:
            tb.eof_write_cmd_check(tb.c_con, bl["cmd"], bl["val"])

try:
    tc = tb.config.tc_demo_linux_tc_list
except:
    tc = ''

if tc != '':
    tb.statusprint("Call board specific testcases")
    for tcname in tc:
        tb.eof_call_tc(tcname)

tb.end_tc(True)
