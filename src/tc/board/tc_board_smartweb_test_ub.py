# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start all ub testcases for the smartweb board
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# call set toolchain
tb.statusprint("set toolchain")
tb.call_tc("tc_workfd_set_toolchain.py")
#tb.eof_call_tc("tc_lab_set_toolchain.py")

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
so = "boot.bin"
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

# call upd_spl
tb.eof_call_tc("tc_ub_upd_spl.py")

# call upd_uboot
tb.eof_call_tc("tc_ub_upd_uboot.py")

tb.workfd = tb.c_ctrl
tb.statusprint("start all DUTS testcases")
tb.eof_call_tc("uboot/duts/tc_ub_start_all_duts.py")

# call test/py
tb.statusprint("u-boot test/py test")
tb.eof_call_tc("tc_ub_test_py.py")

# call upd_dfu
tb.statusprint("u-boot dfu test")
tb.eof_call_tc("tc_ub_dfu.py")

tb.end_tc(True)
