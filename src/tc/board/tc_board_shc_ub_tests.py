# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c shc -t tc_board_shc_ub_tests.py
# start all U-Boot testcases for the shc board
# End:

from tbotlib import tbot

tb.workfd = tb.c_ctrl

tb.eof_call_tc("tc_lab_poweroff.py")

# set board state for which the tc is valid
# tb.set_board_state("u-boot")

# delete old u-boot source tree
tb.eof_call_tc("tc_workfd_rm_uboot_code.py")

# call get u-boot source
tb.statusprint("get u-boot source")
tb.eof_call_tc("tc_lab_get_uboot_source.py")

# call set toolchain
tb.statusprint("set toolchain")
tb.eof_call_tc("tc_lab_set_toolchain.py")

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
so = ".config"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/.config"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# check U-Boot version
tb.workfd = tb.c_ctrl
tb.tc_ub_get_version_file = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/u-boot.bin'
tb.tc_ub_get_version_string = 'U-Boot 20'
tb.eof_call_tc("tc_ub_get_version.py")
tb.uboot_vers = tb.config.tc_return

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

tb.workfd = tb.c_ctrl
tb.statusprint("start all DUTS testcases")
tb.eof_call_tc("uboot/duts/tc_ub_start_all_duts.py")

# call test/py
tb.statusprint("u-boot test/py test")
tb.eof_call_tc("tc_ub_test_py.py")

# save working u-boot bin
c = tb.workfd
p = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/"
so = p + "u-boot.bin"
ta = p + "u-boot-latestworking.bin"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = p + "System.map"
ta = p + "u-boot-latestworking.System.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = p + "MLO"
ta = p + "u-boot-latestworking-MLO"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = p + "u-boot-spl.bin"
ta = p + "u-boot-latestworking-spl.bin"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = p + "u-boot-spl.map"
ta = p + "u-boot-latestworking-spl.System.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

tb.end_tc(True)
