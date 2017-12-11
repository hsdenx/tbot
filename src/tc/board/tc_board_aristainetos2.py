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
# tbot.py -s lab_denx -c aristainetos2 -t tc_board_aristainetos2.py
# start all testcases for the aristainetos2 board
# tc_board_aristainetos2_linux_tests.py
# tc_workfd_set_toolchain.py
# End:

import time
from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# this board needs some time to settle
time.sleep(10)

tb.config.tc_lab_apply_patches_dir = '/work/hs/tbot/patches/u-boot-aristainetos'

tb.workfd = tb.c_ctrl
# delete old u-boot source tree
tb.eof_call_tc("tc_workfd_rm_uboot_code.py")

# call get u-boot source
tb.eof_call_tc("tc_lab_get_uboot_source.py")

# call set toolchain
tb.eof_call_tc("tc_workfd_set_toolchain.py")

# apply local patches
tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# add patchwork patches
tb.statusprint("apply patchwork patches")
tb.config.tc_workfd_apply_patchwork_patches_list = tb.config.tc_workfd_apply_patchwork_patches_list_hand
tb.eof_call_tc("tc_workfd_apply_patchwork_patches.py")

# call compile u-boot
tb.eof_call_tc("tc_lab_compile_uboot.py")

# copy files to tbot dir
c = tb.workfd
so = "u-boot.bin"
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

so = "System.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

so = "u-boot.imx"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

# check U-Boot version
tb.workfd = tb.c_ctrl
tb.tc_ub_get_version_file = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/u-boot.bin'
tb.tc_ub_get_version_string = 'U-Boot 20'
tb.eof_call_tc("tc_ub_get_version.py")
tb.uboot_vers = tb.config.tc_return

#call upd_uboot
tb.eof_call_tc("tc_ub_upd_uboot.py")

#this board needs some time to settle
time.sleep(10)

#call ubi aristainetos2
tb.eof_call_tc("tc_ub_aristainetos2_ubi.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
