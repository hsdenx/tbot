# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start all U-Boot testcases for the fipad board
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.workfd = tb.c_ctrl
# delete old u-boot source tree
tb.eof_call_tc("tc_workfd_rm_uboot_code.py")

# call get u-boot source
tb.statusprint("get u-boot source")
tb.eof_call_tc("tc_lab_get_uboot_source.py")

tb.eof_call_tc("tc_workfd_goto_uboot_code.py")
if tb.config.tc_lab_get_uboot_source_git_repo == '/home/git/u-boot.git':
    tb.config.tc_workfd_apply_local_patches_dir = "/work/hs/tbot/patches/fipad_uboot_patches"
    tb.config.tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"
    tb.config.tc_workfd_apply_local_patches_checkpatch_cmd = 'scripts/checkpatch.pl'
    tb.eof_call_tc("tc_workfd_apply_local_patches.py")

# call set toolchain
tb.statusprint("set toolchain")
tb.eof_call_tc("tc_workfd_set_toolchain.py")

# call compile u-boot
tb.statusprint("compile u-boot")
tb.eof_call_tc("tc_lab_compile_uboot.py")

# copy files to tbot dir
tb.statusprint("copy files")
c = tb.workfd
so = "u-boot.bin"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = ".config"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "System.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "u-boot.img"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "SPL"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "spl/u-boot-spl.bin"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "spl/u-boot-spl.map"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-spl.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# check U-Boot version
tb.workfd = tb.c_ctrl
tb.config.tc_ub_get_version_file = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/u-boot.bin'
tb.config.tc_ub_get_version_string = 'U-Boot 20'
tb.eof_call_tc("tc_ub_get_version.py")
tb.uboot_vers = tb.config.tc_return

# update U-Boot
tb.config.tc_board_fipad_upd_ub_typ = 'MMC0'
tb.eof_call_tc("tc_board_fipad_upd_ub.py")

tb.workfd = tb.c_con
# activate mmc 0 -> register dump has success
tb.eof_write_cmd(tb.workfd, 'mmc dev 0')

# start U-Boot tests
self.tc_ub_create_reg_file_name = 'src/files/fipad_ub_pinmux.reg'
tb.eof_call_tc("tc_ub_check_reg_file.py")

tb.workfd = tb.c_ctrl
tb.statusprint("start all DUTS testcases")
tb.eof_call_tc("uboot/duts/tc_ub_start_all_duts.py")

"""
#call test/py
tb.statusprint("u-boot test/py test")
tb.eof_call_tc("tc_ub_test_py.py")
"""

# start usb tests
tb.eof_call_tc("tc_board_fipad_ub_usb.py")

# save working u-boot bin
c = tb.workfd
so = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot.bin"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-latestworking.bin"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/System.map"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-latestworking.System.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot.img"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-latestworking-u-boot.img"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/SPL"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-latestworking-SPL"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-spl.bin"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-latestworking-spl.bin"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-spl.map"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-latestworking-spl.System.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
