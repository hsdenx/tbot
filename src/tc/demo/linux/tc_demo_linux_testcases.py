# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# - if tb.config.tc_board_bootmode_tc is set, call
#   tb.config.tc_board_bootmode_tc
# - boot a linux kernel if tb.config.tc_demo_linux_tc_boot_lx
#   is set to 'yes' 
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
# used variables
#
# - tb.config.tc_demo_linux_tc_boot_lx
#| if == 'yes' boot a linux kernel
#| default: 'yes'
#
# - tb.config.tc_demo_linux_test_dmesg
#| list of strings, which must be in dmesg
#| default: 'none'
#
# - tb.config.tc_demo_linux_test_reg_files
#| list of register filenames, which get
#| checked with testcase tc_lx_check_reg_file.py
#| default: 'none'
#
# - tb.config.tc_demo_linux_test_basic_cmd
#| list of dictionary with key = 'cmd' and value = 'val'
#| command in 'cmd gets executed and checked if string in 'val'
#| is found. if 'val' == 'undef', no check, only command is
#| executed.
#| default: 'none'
#
# - tb.config.tc_demo_linux_tc_list
#| list of testcasenames, which get called
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_demo_linux_tc_boot_lx', 'yes')
tb.define_variable('tc_demo_linux_test_dmesg', 'none')
tb.define_variable('tc_demo_linux_test_reg_files', 'none')
tb.define_variable('tc_demo_linux_test_basic_cmd', 'none')
tb.define_variable('tc_demo_linux_tc_list', 'none')

try:
    tb.config.tc_board_bootmode_tc
except:
    tb.config.tc_board_bootmode_tc = ''

logging.info("args: %s", tb.config.tc_board_bootmode_tc)

if tb.config.tc_demo_linux_tc_boot_lx == 'yes':
    if tb.config.tc_board_bootmode_tc != '':
        tb.config.tc_board_bootmode = 'normal'
        tb.eof_call_tc(tb.config.tc_board_bootmode_tc)

    # call ubot setenv
    tb.set_board_state("u-boot")
    tb.eof_write_cmd(tb.c_con, "version")

save = tb.workfd
tb.workfd = tb.c_con

tb.eof_call_tc("tc_lx_get_version.py")

tb.statusprint("Linux vers: %s" % (tb.config.tc_return))

lx_vers = tb.config.tc_return.split()[0]
tb.statusprint("Linux Version %s" % (lx_vers))

# you can use now the lx_vers for differ between linux versions

tb.set_board_state("linux")

# dmesg checks
if tb.config.tc_demo_linux_test_dmesg != 'none':
    check = tb.config.tc_demo_linux_test_dmesg
    tb.statusprint("linux dmesg checks")
    for tb.config.tc_lx_dmesg_grep_name in check:
        tb.eof_call_tc("tc_lx_dmesg_grep.py")

# register checks
if tb.config.tc_demo_linux_test_reg_files != 'none':
    files = tb.config.tc_demo_linux_test_reg_files
    for tb.config.tc_lx_create_reg_file_name in files:
        tb.eof_call_tc("tc_lx_check_reg_file.py")

# do some basic tests
if tb.config.tc_demo_linux_test_basic_cmd != 'none':
    bcmd = tb.config.tc_demo_linux_test_basic_cmd
    tb.statusprint("start basic checks")
    for bl in bcmd:
        if bl["val"] == 'undef':
            tb.eof_write_cmd(tb.c_con, bl["cmd"])
        else:
            tb.eof_write_cmd_check(tb.c_con, bl["cmd"], bl["val"])

if tb.config.tc_demo_linux_tc_list != 'none':
    tc = tb.config.tc_demo_linux_tc_list
    tb.statusprint("Call board specific testcases")
    for tcname in tc:
        tb.eof_call_tc(tcname)

tb.workfd = save
tb.end_tc(True)
