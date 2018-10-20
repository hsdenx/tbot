# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# do basic yocto checks
#
# - check rootfs version
#|   only if tb.config.tc_workfd_yocto_basic_check_rootfsversion == 'yes'
#|   which is the default.
# - check dmesg output
#|   check if strings defined in tb.config.tc_demo_yocto_test_checks
#|   are found in dmesg output
# - check if devmem2 tool is in rootfs, if so, do register checks
#
# used variables
#
# - tb.config.tc_workfd_yocto_basic_check_rootfsversion
#| if 'yes' check rootfs version with testcase
#| tc_workfd_yocto_check_rootfs_version.py
#| default: 'yes'
#
# - tb.config.tc_workfd_yocto_basic_check_board_specific
#| if != 'none, contains a list of testcasenames
#| which get called.
#| default: '[]'
#
# - tb.config.tc_demo_yocto_test_checks
#| list of strings, which must be in 'dmesg' output
#| default: '[]'
#
# - tb.config.tc_workfd_yocto_basic_check_basic_cmd
#| contains a list of dictionaries from format:
#| {"cmd":"commandstring", "val":"expected value"}
#| comand(s) get executed and "val" must come back.
#| end command must have exit code 0.
#| if "val" = "undef", only returncode get checked.
#| default: '[]'
#
# - tb.config.tc_workfd_yocto_basic_check_regfiles
#| list of filenames, which contain register dumps.
#| This registerdumps are checked with testcase
#| tc_lx_check_reg_file.py if devmem2 command exists.
#| default: '[]'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_yocto_basic_check_rootfsversion', 'yes')
tb.define_variable('tc_workfd_yocto_basic_check_board_specific', '[]')
tb.define_variable('tc_demo_yocto_test_checks', '[]')
tb.define_variable('tc_workfd_yocto_basic_check_regfiles', '[]')
tb.define_variable('tc_workfd_yocto_basic_check_basic_cmd', '[]')

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

if tb.config.tc_workfd_yocto_basic_check_basic_cmd != '[]':
    bcmd = tb.config.tc_workfd_yocto_basic_check_basic_cmd
    tb.statusprint("start basic checks")
    for bl in bcmd:
        if bl["val"] == 'undef':
            tb.eof_write_cmd(tb.c_con, bl["cmd"])
        else:
            tb.eof_write_cmd_check(tb.c_con, bl["cmd"], bl["val"])

# call board specific checks
if tb.config.tc_workfd_yocto_basic_check_board_specific != '[]':
    tc = tb.config.tc_workfd_yocto_basic_check_board_specific
    tb.statusprint("Call board specific testcases")
    for tcname in tc:
        tb.eof_call_tc(tcname)

tb.end_tc(True)
