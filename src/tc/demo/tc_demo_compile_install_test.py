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
# - compile source tree
# - install bin on board
# - call board uboot testcase
# tb.config.tc_demo_compile_install_test_files contains a list of files,
# which are copied to
# tb.config.tftprootdir + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir
# End:

from tbotlib import tbot

# set workfd to the connection we want to work on
tb.workfd = tb.c_ctrl

# go into u-boot code
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# call set toolchain
tb.statusprint("set toolchain")
tb.eof_call_tc("tc_workfd_set_toolchain.py")

# call compile u-boot
tb.statusprint("compile u-boot")
tb.eof_call_tc("tc_lab_compile_uboot.py")

# copy files to tbot dir
tb.statusprint("copy files")
c = tb.workfd

r = tb.config.tftprootdir
for f in tb.config.tc_demo_compile_install_test_files:
    ta = r + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir
    tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=f, t=ta)

# set workfd to the connection we want to work on
tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# check U-Boot version
tb.tc_ub_get_version_file = r + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/u-boot.bin'
tb.tc_ub_get_version_string = 'U-Boot 20'
tb.eof_call_tc("tc_ub_get_version.py")
tb.uboot_vers = tb.config.tc_return

# call upd_uboot
tb.eof_call_tc("tc_ub_upd_uboot.py")

# call tc_help
tb.statusprint("u-boot help test")
tb.eof_call_tc("tc_ub_help.py")

# save working u-boot bin
c = tb.workfd
for f in tb.config.tc_demo_compile_install_test_files:
    tmp = f.replace('/', "_")
    ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/latestworking-" + tmp
    tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=f, t=ta)

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
