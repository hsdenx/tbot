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
# python2.7 src/common/tbot.py -c tbot_aristainetos2.cfg -t tc_aristainetos2_ubi.py
# ubi testcases for the aristainetos2 board
#
import time
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

#this board needs some time to settle
time.sleep(10)

#load ub tbot environment
tb.eof_call_tc("tc_ub_load_board_env.py")

tb.eof_write_con("sf probe")
#nand tests
tb.tc_ub_ubi_prep_offset = '4096'
tb.tc_ub_ubi_prep_partname = 'ubi'
tb.eof_call_tc("tc_ub_ubi_prepare.py")

#nor tests
tb.tc_ub_ubi_prep_offset = '64'
tb.tc_ub_ubi_prep_partname = 'rescue-system'
tb.tc_ub_ubi_load_name = 'kernel'
tb.eof_call_tc("tc_ub_ubi_prepare.py")
tb.eof_call_tc("tc_ub_ubi_check_volume.py")

#write file into kernel volume
tb.tftp_addr_r = tb.tc_ub_ubi_write_addr
tb.tftp_file = '/tftpboot/aristainetos/tbot/aristainetos2.itb'
tb.eof_call_tc("tc_ub_tftp_file.py")

read_line_retry_save=tb.read_line_retry
tb.read_line_retry=1000
tb.tc_ub_ubi_write_vol_name = 'kernel'
tb.eof_call_tc("tc_ub_ubi_write.py")

#read file from kernel partition
tb.tc_ub_ubi_load_addr = '11000000'
tb.eof_call_tc("tc_ub_ubi_load.py")

#compare it with original
#tmp = "cmp.b 11000000 14000000 ${filesize}"
# does not work ... console hangs
tmp = "run tbot_cmp_ubi"
tb.eof_write_con(tmp)
tb.eof_search_str_in_readline_end_con("!=")
tb.read_line_retry=read_line_retry_save

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
