# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c boardname -t tc_workfd_yocto_basic_check.py
#
# do basic yocto checks
#
# - check rootfs version
#   only if tb.config.tc_workfd_yocto_basic_check_rootfsversion == 'yes'
#   which is the default.
# - check dmesg output
#   check if strings defined in tb.config.tc_demo_yocto_test_checks
#   are found in dmesg output
# - check if devmem2 tool is in rootfs, if so, do register checks
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_yocto_basic_check_rootfsversion
except:
    tb.config.tc_workfd_yocto_basic_check_rootfsversion = 'yes'

try:
    tb.config.tc_workfd_yocto_basic_check_board_specific
except:
    tb.config.tc_workfd_yocto_basic_check_board_specific = ''

# boot into linux
tb.set_board_state("linux")

if tb.config.tc_workfd_yocto_basic_check_rootfsversion == 'yes':
    tb.statusprint("checks yocto rootfs version")
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

# call board specific checks
if tb.config.tc_workfd_yocto_basic_check_board_specific != '':
    tb.eof_call_tc(tb.config.tc_workfd_yocto_basic_check_board_specific)

tb.end_tc(True)
