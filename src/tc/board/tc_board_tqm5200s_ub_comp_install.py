# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c tqm5200s -t tc_board_tqm5200s_ub_comp_install.py
# compile and install U-Boot for the tqm5200s board
# install U-Boot with BDI
# End:

from tbotlib import tbot

# call get u-boot source
tb.workfd = tb.c_ctrl
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
ta = "System.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# check U-Boot version
tb.workfd = tb.c_ctrl
tb.config.tc_ub_get_version_file = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/u-boot.bin'
tb.config.tc_ub_get_version_string = 'U-Boot 20'
tb.eof_call_tc("tc_ub_get_version.py")
tb.uboot_vers = tb.config.tc_return

#call upd_uboot
tb.eof_call_tc("tc_lab_bdi_upd_uboot.py")

#check if u-boot works
tb.set_board_state("u-boot")

tb.end_tc(True)
