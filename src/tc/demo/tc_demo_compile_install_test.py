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
# python2.7 src/common/tbot.py -c tbot_demo.cfg -t tc_demo_compile_install_test.py
# start tc:
# - compile source tree
# - install bin on board
# - call board uboot testcase
# End:

from tbotlib import tbot

# set workfd to the connection we want to work on
tb.workfd = tb.c_ctrl

# go into u-boot code
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# call set toolchain
tb.statusprint("set toolchain")
tb.eof_call_tc("tc_lab_set_toolchain.py")

# call compile u-boot
tb.statusprint("compile u-boot")
tb.eof_call_tc("tc_lab_compile_uboot.py")

# copy files to tbot dir
tb.statusprint("copy files")
tb.tc_lab_cp_file_a = "u-boot.bin"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "System.map"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "boot.bin"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "spl/u-boot-spl.bin"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "spl/u-boot-spl.map"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-spl.map"
tb.eof_call_tc("tc_lab_cp_file.py")

# set workfd to the connection we want to work on
tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# check U-Boot version
tb.tc_ub_get_version_file = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + '/u-boot.bin'
tb.tc_ub_get_version_string = 'U-Boot 20'
tb.eof_call_tc("tc_ub_get_version.py")
tb.uboot_vers = tb.tc_return

# call upd_uboot
tb.eof_call_tc("tc_ub_upd_uboot.py")

# call tc_help
tb.statusprint("u-boot help test")
tb.eof_call_tc("tc_ub_help.py")

# save working u-boot bin
tb.tc_lab_cp_file_a = "u-boot.bin"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-latestworking.bin"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "System.map"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-latestworking.System.map"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "boot.bin"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-latestworking-boot.bin"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "spl/u-boot-spl.bin"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-latestworking-spl.bin"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "spl/u-boot-spl.map"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-latestworking-spl.System.map"
tb.eof_call_tc("tc_lab_cp_file.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
