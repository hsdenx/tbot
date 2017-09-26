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
# tbot.py -c -s lab_denx -c demo -t tc_demo_compile_install_test.py
# start tc:
# - if tb.config.tc_board_bootmode_tc is defined
#   call tc tb.config.tc_board_bootmode_tc
#   (set bootmode for the board)
# - go to uboot code with tc_workfd_goto_uboot_code.py
# - set toolchain with tc_workfd_set_toolchain.py
# - compile source tree with tc_workfd_compile_uboot.py
# - if tb.config.tc_demo_uboot_test_deploy != ''
#     call tb.config.tc_demo_uboot_test_deploy
#   else
#     copy files in list tb.config.tc_demo_compile_install_test_files
#     tb.config.tc_demo_compile_install_test_files contains a list of files,
#     which are copied to tftp directory
#     tb.config.tftpdir + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir
# - get u-boot version from binary with tc_ub_get_version.py
# - if tb.config.tc_demo_uboot_test_update != '':
#     call tb.config.tc_demo_uboot_test_update
#   else:
#     call tc_ub_upd_uboot.py
#     call tc_ub_upd_spl.py
# - if tb.config.tc_demo_compile_install_test_spl_vers_file and/or
#   tc_tb.config.demo_compile_install_test_ub_vers_file != ''
#   check if the new installed version is the same
#   as in the binary files, defined in
#   tb.config.tc_demo_compile_install_test_ub_vers_file or
#   tb.config.tc_demo_compile_install_test_spl_vers_file
# - call tb.config.tc_demo_compile_install_test_name
#     which should contain a testcase, which tests the new
#     installed u-boot
# End:

from tbotlib import tbot

try:
    tc_demo_compile_install_test_ub_vers_file
except:
    tc_demo_compile_install_test_ub_vers_file = ''

try:
    tc_demo_compile_install_test_spl_vers_file
except:
    tc_demo_compile_install_test_spl_vers_file = ''

try:
    tb.config.tc_demo_uboot_test_deploy
except:
    tb.config.tc_demo_uboot_test_deploy = ''

try:
    tb.config.tc_demo_uboot_test_update
except:
    tb.config.tc_demo_uboot_test_update = ''

try:
    tb.config.tc_board_bootmode_tc
except:
    tb.config.tc_board_bootmode_tc = ''

logging.info("args: %s %s %s %s", tb.workfd.name, tb.config.tc_demo_uboot_test_deploy,
             tb.config.tc_demo_uboot_test_update, tb.config.tc_board_bootmode_tc)

if tb.config.tc_board_bootmode_tc != '':
    tb.config.tc_board_bootmode = 'normal'
    tb.eof_call_tc(tb.config.tc_board_bootmode_tc)

# go into u-boot code
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# call set toolchain
tb.statusprint("set toolchain")
tb.eof_call_tc("tc_workfd_set_toolchain.py")

# call compile u-boot
tb.statusprint("compile u-boot")
tb.eof_call_tc("tc_workfd_compile_uboot.py")

r = tb.config.tftpdir + '/'
if tb.config.tc_demo_uboot_test_deploy != '':
    tb.eof_call_tc(tb.config.tc_demo_uboot_test_deploy)
else:
    # copy files to tbot dir
    tb.statusprint("copy files")
    c = tb.workfd

    for f in tb.config.tc_demo_compile_install_test_files:
        ta = r + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir
        tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=f, t=ta)

tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# check U-Boot version
if tb.config.tc_demo_compile_install_test_ub_vers_file != '':
    tb.tc_ub_get_version_file = tb.config.tc_demo_compile_install_test_ub_vers_file
    tb.tc_ub_get_version_string = 'U-Boot 20'
    tb.eof_call_tc("tc_ub_get_version.py")
    tb.uboot_vers = tb.config.tc_return
else:
    tb.uboot_vers = ''

if tb.config.tc_demo_compile_install_test_spl_vers_file != '':
    tb.tc_ub_get_version_file = tb.config.tc_demo_compile_install_test_spl_vers_file
    tb.tc_ub_get_version_string = 'U-Boot SPL'
    tb.eof_call_tc("tc_ub_get_version.py")
    tb.spl_vers = tb.config.tc_return
else:
    tb.spl_vers = ''

if tb.config.tc_demo_uboot_test_update != '':
    tb.eof_call_tc(tb.config.tc_demo_uboot_test_update)
else:
    # call upd_uboot
    tb.eof_call_tc("tc_ub_upd_uboot.py")

    # call upd_spl
    tb.eof_call_tc("tc_ub_upd_spl.py")

# check if correct u-boot version is installed
tb.eof_call_tc("tc_ub_check_version.py")

# call tc_help
tb.statusprint("start u-boot tests")
tb.eof_call_tc(tb.config.tc_demo_compile_install_test_name)

if tb.config.tc_demo_uboot_test_deploy != '':
    # save working u-boot bin
    c = tb.c_ctrl
    p = tb.config.tftpdir + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/"
    for f in tb.config.tc_demo_compile_install_test_files:
        tmp = f.replace('/', "_")
        sa = p + os.path.basename(f)
        ta = p + "/latestworking-" + tmp
        tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=sa, t=ta)

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
