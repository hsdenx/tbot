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
# start with
# python2.7 src/common/tbot.py -c tbot_shc.cfg -t tc_board_shc_ub_tests.py
# start all U-Boot testcases for the shc board
#
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

#delete old u-boot source tree
tb.eof_call_tc("tc_workfd_rm_uboot_code.py")

#call get u-boot source
tb.statusprint("get u-boot source")
tb.eof_call_tc("tc_lab_get_uboot_source.py")

tb.workfd = tb.c_ctrl

#call set toolchain
tb.statusprint("set toolchain")
tb.eof_call_tc("tc_lab_set_toolchain.py")

#call compile u-boot
tb.statusprint("compile u-boot")
tb.eof_call_tc("tc_lab_compile_uboot.py")

#copy files to tbot dir
tb.statusprint("copy files")
tb.tc_lab_cp_file_a = "u-boot.bin"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "System.map"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "u-boot.img"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "MLO"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "spl/u-boot-spl.bin"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "spl/u-boot-spl.map"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-spl.map"
tb.eof_call_tc("tc_lab_cp_file.py")

# update U-Boot
tb.eof_call_tc("tc_board_shc_upd_ub.py")

tb.workfd = tb.c_con
# activate mmc 0 -> register dump has success
tb.eof_write_cmd(tb.workfd, 'mmc dev 0')

# start U-Boot tests
self.tc_ub_create_reg_file_name = 'src/files/shc_ub_pinmux.reg'
tb.eof_call_tc("tc_ub_check_reg_file.py")
self.tc_ub_create_reg_file_name = 'src/files/shc_ub_pinmux_mmc.reg'
tb.eof_call_tc("tc_ub_check_reg_file.py")
self.tc_ub_create_reg_file_name = 'src/files/shc_ub_pinmux_gpio.reg'
tb.eof_call_tc("tc_ub_check_reg_file.py")
tb.end_tc(True)
