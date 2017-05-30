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
# tbot.py -s lab_denx -c cuby -t tc_workfd_yocto_basic_check.py
#
# do basic yocto checks
#
# - check rootfs version
# - check dmesg output
#   check if strings defined in tb.config.tc_demo_yocto_test_checks
#   are found in dmesg output
# - check if devmem2 tool is in rootfs, if so, do register checks
#
# End:

from tbotlib import tbot

# boot into linux
tb.set_board_state("linux")

tb.eof_call_tc("tc_workfd_yocto_check_rootfs_version.py")

tb.statusprint("linux dmesg checks")
for tb.config.tc_lx_dmesg_grep_name in tb.config.tc_demo_yocto_test_checks:
    tb.eof_call_tc("tc_lx_dmesg_grep.py")

# devmem2 checks
tb.config.tc_workfd_check_if_cmd_exist_cmdname = 'devmem2'
ret = tb.call_tc("tc_workfd_check_if_cmd_exist.py")
if ret == True:
    tb.statusprint("linux register checks")
    for tb.config.tc_lx_create_reg_file_name in tb.config.tc_workfd_yocto_basic_check_regfiles:
        tb.eof_call_tc("tc_lx_check_reg_file.py")

tb.end_tc(True)
