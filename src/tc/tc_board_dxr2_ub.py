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
# python2.7 src/common/tbot.py -c tbot_dxr2.cfg -t tc_board_dxr2_ub.py
# start all u-boot testcases for the dxr2 board
#
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

#delete old u-boot source tree
tb.tc_lab_rm_dir = tb.tc_lab_source_dir + '/u-boot-' + tb.boardlabname
tb.eof_call_tc("tc_lab_rm_dir.py")

#call get u-boot source
tb.statusprint("get u-boot source")
tb.eof_call_tc("tc_lab_get_uboot_source.py")

#get current list of patches in ToDo list
tb.statusprint("get patchwork patches")
tb.eof_call_tc("tc_workfd_get_patchwork_number_list.py")

tb.tc_workfd_apply_patchwork_patches_list_hand += tb.tc_workfd_apply_patchwork_patches_list
tb.tc_workfd_apply_patchwork_patches_list = tb.tc_workfd_apply_patchwork_patches_list_hand

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

#call update spl
tb.statusprint("update spl")
tb.eof_call_tc("tc_ub_upd_spl.py")

#call update u-boot
tb.statusprint("update u-boot")
tb.eof_call_tc("tc_ub_upd_uboot.py")

#call dxr2 u-boot ubi tests
tb.statusprint("u-boot ubi test")
tb.eof_call_tc("tc_board_dxr2_ub_ubi.py")

#save working u-boot bin
tb.tc_lab_cp_file_a = "u-boot.bin"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-latestworking.bin"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "System.map"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-latestworking.System.map"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "u-boot.img"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-latestworking-u-boot.img"
tb.tc_lab_cp_file_a = "MLO"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-latestworking-MLO"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "spl/u-boot-spl.bin"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-latestworking-spl.bin"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "spl/u-boot-spl.map"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir + "/u-boot-latestworking-spl.System.map"
tb.eof_call_tc("tc_lab_cp_file.py")

# power off board at the end
#tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
