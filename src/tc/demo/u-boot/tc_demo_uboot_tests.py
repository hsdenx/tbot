# SPDX-License-Identifier: GPL-2.0
#
# Description:
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
# used variables:
#
# - tb.config.tc_demo_uboot_test_reg_files
#| list of register files, which contain registerdumps
#| used for testcase
#| tc_ub_check_reg_file.py
#| default: 'none'
#
# - tb.config.tc_demo_uboot_test_basic_cmd
#| list of dictionary, which contains key = 'cmd' and
#| value = 'val' entries
#| default: 'none'
#| example: [
#|              {"cmd":"help", "val":"i2c"},
#|              {"cmd":"md", "val":"undef"},
#|          ]
#|
#| If "val" = 'undef' only command gets executed, no check
#
# - tb.config.tc_demo_uboot_tc_list
#| list of testcasesnames, which get called
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_demo_uboot_test_reg_files', 'none')
tb.define_variable('tc_demo_uboot_test_basic_cmd', 'none')
tb.define_variable('tc_demo_uboot_tc_list', 'none')

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# call tc tc_ub_load_board_env.py
tb.eof_call_tc("tc_ub_load_board_env.py")

# register checks
if tb.config.tc_demo_uboot_test_reg_files != 'none':
    tb.statusprint("start register check")
    for tb.config.tc_ub_create_reg_file_name in tb.config.tc_demo_uboot_test_reg_files:
        tb.eof_call_tc('tc_ub_check_reg_file.py')

# call basic cmd list
if tb.config.tc_demo_uboot_test_basic_cmd != 'none':
    bcmd = tb.config.tc_demo_uboot_test_basic_cmd
    tb.statusprint("start basic U-Boot checks")
    for bl in bcmd:
        if bl["val"] == 'undef':
            tb.eof_write_cmd(tb.c_con, bl["cmd"])
        else:
            tb.eof_call_tc('tc_workfd_write_cmd_check.py', cmd=bl["cmd"], string=bl["val"])

save = tb.workfd
try:
    tb.c_cpc
    tb.workfd = tb.c_cpc
except:
    tb.workfd = tb.c_ctrl

tb.statusprint("start all DUTS testcases")
tb.eof_call_tc("uboot/duts/tc_ub_start_all_duts.py")

# call test/py
tb.statusprint("u-boot test/py test")
tb.eof_call_tc("tc_ub_test_py.py")

if tb.config.tc_demo_uboot_tc_list != 'none':
    tb.statusprint("Call board specific testcases")
    for tcname in tb.config.tc_demo_uboot_tc_list:
        tb.eof_call_tc(tcname)

tb.workfd = save
tb.end_tc(True)
