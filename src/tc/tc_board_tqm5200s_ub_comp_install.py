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
# python2.7 src/common/tbot.py -c tbot_tqm5200s.cfg -t tc_board_tqm5200s_ub_comp_install.py
# compile and install U-Boot for the tqm5200s board
# install U-Boot with BDI
#
from tbotlib import tbot

#cloning needs a bigger timeout, (git clone has no output)
read_line_retry_save=tb.read_line_retry
tb.read_line_retry=500
#call get u-boot source
tb.statusprint("get u-boot source")
tb.eof_call_tc("tc_lab_get_uboot_source.py")
tb.read_line_retry=read_line_retry_save

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
#call cp files
tb.eof_call_tc("tc_lab_cp_file.py")

tb.tc_lab_cp_file_a = "System.map"
#call cp files
tb.eof_call_tc("tc_lab_cp_file.py")

#call upd_uboot
tb.eof_call_tc("tc_lab_bdi_upd_uboot.py")

#check if u-boot works
tb.set_board_state("u-boot")

tb.end_tc(True)
