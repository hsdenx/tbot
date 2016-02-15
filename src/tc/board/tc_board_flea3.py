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
# python2.7 src/common/tbot.py -c tbot_flea3.cfg -t tc_board_flea3.py
# start all testcases for the flea3 board
# currently only test the nor unprotect with linux
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")
tb.eof_write_cmd(tb.c_con, "version")

tb.tc_board_flea3_nor_start_addr = 'a00a0000'
tb.tc_board_flea3_nor_start_len = 'a0000'
tb.tc_board_flea3_nor_ram_addr = '80800000'
tb.tc_board_flea3_nor_ram_addr_alt = '81000000'
tb.tc_board_flea3_nor_file = '/tftpboot/flea3/tbot/nor_random'

#generate a random file
tb.eof_call_tc("tc_workfd_generate_random_file.py")
cmdlist = [
"protect off " + tb.tc_board_flea3_nor_start_addr + " +" + tb.tc_board_flea3_nor_start_len,
"tftp " + tb.tc_board_flea3_nor_ram_addr + " " + tb.tc_board_flea3_nor_file,
"erase " + tb.tc_board_flea3_nor_start_addr + " +" + tb.tc_board_flea3_nor_start_len,
"cp.b " + tb.tc_board_flea3_nor_ram_addr + " " + tb.tc_board_flea3_nor_start_addr + " " + tb.tc_board_flea3_nor_start_len,
"md " + tb.tc_board_flea3_nor_start_addr,
"protect on " + tb.tc_board_flea3_nor_start_addr + " +" + tb.tc_board_flea3_nor_start_len,
"erase " + tb.tc_board_flea3_nor_start_addr + " +" + tb.tc_board_flea3_nor_start_len,
"md " + tb.tc_board_flea3_nor_start_addr,
"cp.b "+ tb.tc_board_flea3_nor_start_addr + " " + tb.tc_board_flea3_nor_ram_addr_alt + " " + tb.tc_board_flea3_nor_start_len
]
tb.eof_write_cmd_list(tb.c_con, cmdlist)

tb.tc_ub_cmp_addr1 = tb.tc_board_flea3_nor_ram_addr_alt
tb.tc_ub_cmp_addr2 = tb.tc_board_flea3_nor_ram_addr
tb.tc_ub_cmp_len = tb.tc_board_flea3_nor_start_len
tb.eof_call_tc("tc_ub_cmp.py")

tb.set_board_state("linux")
tb.workfd = tb.c_con
tb.eof_write_lx_cmd_check(tb.workfd, "cd /home/hs/flea3")
tb.eof_write_lx_cmd_check(tb.workfd, "./load_can.sh")

cmdlist = [
"./mtd-utils/misc-utils/flash_unlock --version",
"./mtd-utils/misc-utils/flash_unlock -i /dev/mtd3 0 10",
"mtd_debug read /dev/mtd3 0 0x" + tb.tc_board_flea3_nor_start_len + " gnlmpf",
"hexdump -C -n 48 gnlmpf",
"./mtd-utils/misc-utils/flash_erase /dev/mtd3 0 10",
"mtd_debug read /dev/mtd3 0 0x" + tb.tc_board_flea3_nor_start_len + " gnlmpf",
"hexdump -C -n 48 gnlmpf",
"./mtd-utils/misc-utils/flash_unlock -u /dev/mtd3 0 10",
"./mtd-utils/misc-utils/flash_unlock -i /dev/mtd3 0 10",
"./mtd-utils/misc-utils/flash_erase /dev/mtd3 0 10",
"mtd_debug read /dev/mtd3 0 0x" + tb.tc_board_flea3_nor_start_len + " gnlmpf",
"hexdump -C -n 48 gnlmpf",
]

for tmp_cmd in cmdlist:
    tb.eof_write_lx_cmd_check(tb.workfd, tmp_cmd)

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
