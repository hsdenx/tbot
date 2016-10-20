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
# tbot.py -s lab_denx -c dxr2 -t tc_board_dxr2_ub.py
# start all u-boot testcases for the dxr2 board
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# delete old u-boot source tree
tb.eof_call_tc("tc_workfd_rm_uboot_code.py")

# call get u-boot source
tb.statusprint("get u-boot source")
tb.eof_call_tc("tc_lab_get_uboot_source.py")

# call set toolchain
tb.statusprint("set toolchain")
tb.eof_call_tc("tc_lab_set_toolchain.py")

# get current list of patches in ToDo list
# tb.statusprint("get patchwork patches")
# tb.eof_call_tc("tc_workfd_get_patchwork_number_list.py")

# tb.config.tc_workfd_apply_patchwork_patches_list_hand += tb.config.tc_workfd_apply_patchwork_patches_list
# tb.config.tc_workfd_apply_patchwork_patches_list = tb.config.tc_workfd_apply_patchwork_patches_list_hand

# apply local patches
tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# save linux settings
tmp = tb.config.tc_workfd_apply_local_patches_dir
tb.config.tc_workfd_apply_local_patches_dir = "/work/hs/tbot/patches/dxr2_uboot_patches"
tb.eof_call_tc("tc_workfd_apply_local_patches.py")
tb.config.tc_workfd_apply_local_patches_dir = tmp

# add patchwork patches
# tb.statusprint("apply patchwork patches")
# tb.config.tc_workfd_apply_patchwork_patches_checkpatch_cmd = 'scripts/checkpatch.pl'
# tb.eof_call_tc("tc_workfd_apply_patchwork_patches.py")

# call compile u-boot
tb.statusprint("compile u-boot")
tb.eof_call_tc("tc_lab_compile_uboot.py")

# copy files to tbot dir
tb.statusprint("copy files")
c = tb.workfd
so = "u-boot.bin"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "System.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "u-boot.img"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "MLO"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "spl/u-boot-spl.bin"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "spl/u-boot-spl.map"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-spl.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

# check U-Boot version
tb.workfd = tb.c_ctrl
tb.tc_ub_get_version_file = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/u-boot.bin'
tb.tc_ub_get_version_string = 'U-Boot 20'
tb.eof_call_tc("tc_ub_get_version.py")
tb.uboot_vers = tb.config.tc_return
tb.tc_ub_get_version_file = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/u-boot-spl.bin'
tb.tc_ub_get_version_string = 'U-Boot SPL'
tb.eof_call_tc("tc_ub_get_version.py")
tb.spl_vers = tb.config.tc_return

# call update spl
tb.statusprint("update spl")
tb.eof_call_tc("tc_ub_upd_spl.py")

# call update u-boot
tb.statusprint("update u-boot")
tb.eof_call_tc("tc_ub_upd_uboot.py")

# call dxr2 u-boot ubi tests
tb.statusprint("u-boot ubi test")
tb.eof_call_tc("tc_board_dxr2_ub_ubi.py")

tb.workfd = tb.c_ctrl
tb.statusprint("start all DUTS testcases")
tb.eof_call_tc("uboot/duts/tc_ub_start_all_duts.py")

# call test/py
tb.statusprint("u-boot test/py test")
tb.eof_call_tc("tc_ub_test_py.py")

tb.eof_call_tc("tc_ub_dfu_random.py")
tb.config.tc_ub_dfu_dfu_util_alt_setting = 'uboot_def_test'
tb.eof_call_tc("tc_ub_dfu_random_default.py")

# save working u-boot bin
c = tb.workfd
so = "u-boot.bin"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-latestworking.bin"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "System.map"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-latestworking.System.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "MLO"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-latestworking-MLO"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "spl/u-boot-spl.bin"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-latestworking-spl.bin"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "spl/u-boot-spl.map"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-latestworking-spl.System.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

# power off board at the end
# tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
