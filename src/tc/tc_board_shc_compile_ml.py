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
# python2.7 src/common/tbot.py -c tbot_shc.cfg -t tc_board_shc_compile_ml.py
# compile ML linux kernel for the shc board
#
from tbotlib import tbot

tb.statusprint("shc compile linux mainline kernel")

#delete old source tree
tb.eof_call_tc("tc_workfd_rm_linux_code.py")

tb.eof_call_tc("tc_workfd_get_linux_source.py")

tb.eof_call_tc("tc_workfd_goto_linux_code.py")

#compile it
tb.tc_lab_toolchain_rev = '5.4'
tb.tc_lab_toolchain_name = 'armv5te'
tb.tc_workfd_compile_linux_clean = 'no'
tb.tc_workfd_compile_linux_boardname = 'shc'
tb.tc_workfd_compile_linux_load_addr = '0x80008000'
tb.tc_workfd_compile_linux_modules ='yes'
tb.tc_workfd_compile_linux_modules_path ='/opt/eldk-5.5/armv5te/rootfs-qte-sdk/home/hs/shc/modules'
tb.tc_workfd_compile_linux_dt_name = 'am335x-shc.dtb'
tb.tc_workfd_compile_linux_fit_its_file = 'no'
tb.tc_workfd_compile_linux_fit_file = 'shc.itb'
tb.tc_workfd_compile_linux_append_dt = 'no'

tb.eof_call_tc("tc_workfd_compile_linux.py")

# copy files to tftpdir
tb.statusprint("copy files")
tb.tc_lab_cp_file_a = "/work/hs/tbot/linux-shc/arch/arm/boot/uImage"
tb.tc_lab_cp_file_b = "/tftpboot/shc/tbot/uImage-hs-cur"
tb.eof_call_tc("tc_lab_cp_file.py")
tb.tc_lab_cp_file_a = "/work/hs/tbot/linux-shc/arch/arm/boot/dts/" + tb.tc_workfd_compile_linux_dt_name
tb.tc_lab_cp_file_b = "/tftpboot/shc/tbot/shc.dtb"
tb.eof_call_tc("tc_lab_cp_file.py")

tb.end_tc(True)
