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
# python2.7 src/common/tbot.py -c tbot_aristainetos2.cfg -t tc_board_aristainetos2.py
# start all testcases for the aristainetos2 board
#
import time
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

#this board needs some time to settle
time.sleep(10)

#delete old u-boot source tree
tb.tc_lab_rm_dir = tb.tc_lab_source_dir + '/u-boot-' + tb.boardlabname
tb.eof_call_tc("tc_lab_rm_dir.py")

#call get u-boot source
#cloning needs a bigger timeout, (git clone has no output)
read_line_retry_save=tb.read_line_retry
tb.read_line_retry=500
tb.eof_call_tc("tc_lab_get_uboot_source.py")
tb.read_line_retry=read_line_retry_save

#call set toolchain
tb.eof_call_tc("tc_lab_set_toolchain.py")

#call compile u-boot
tb.eof_call_tc("tc_lab_compile_uboot.py")

#copy files to tbot dir
tb.tc_lab_cp_file_a = "u-boot.bin"
tb.tc_lab_cp_file_b = "/tftpboot/" + tb.tftpboardname + "/" + tb.ub_load_board_env_subdir
#call cp files
tb.eof_call_tc("tc_lab_cp_file.py")

tb.tc_lab_cp_file_a = "System.map"
tb.eof_call_tc("tc_lab_cp_file.py")

tb.tc_lab_cp_file_a = "u-boot.imx"
tb.eof_call_tc("tc_lab_cp_file.py")

#call upd_uboot
tb.eof_call_tc("tc_ub_upd_uboot.py")

#this board needs some time to settle
time.sleep(10)

#call ubi aristainetos2
tb.eof_call_tc("tc_ub_aristainetos2_ubi.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
