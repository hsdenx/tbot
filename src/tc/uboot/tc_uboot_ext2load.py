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
# python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_uboot_ext2load.py
#
# load a file from ext2 into ram with ext2ls cmd.
# check if the file has crc32 checksum 0x2144df1c
#
# How to create such a file, which has crc32 checksum of 0x2144df1c ?
#
# $ dd if=/dev/urandom of=test.bin bs=1M count=1
# $ crc32 test.bin
# 4f3fef33
# $ perl -e 'print pack "H*", "33ef3f4f"' >> test.bin
# $ crc32 test.bin
# 2144df1c
#
# https://stackoverflow.com/questions/28591991/crc32-of-already-crc32-treated-data-with-the-crc-data-appended
#
# !! Don;t forget Big into little endian conversion
#
# used vars:
# tc_uboot_ext2load_interface = 'usb'
# tc_uboot_ext2load_dev = '0:1'
# tc_uboot_ext2load_addr = '10000000'
# tc_uboot_ext2load_file = '/test.bin'
# tc_uboot_ext2load_check = 'no'
#   if 'yes' check if the file tc_uboot_ext2load_file
#   has the checksum 0x2144df1c
# End:

from tbotlib import tbot

try:
    tb.config.tc_uboot_ext2load_interface
except:
    tb.config.tc_uboot_ext2load_interface = 'usb'

try:
    tb.config.tc_uboot_ext2load_dev
except:
    tb.config.tc_uboot_ext2load_dev = '0:1'

try:
    tb.config.tc_uboot_ext2load_addr
except:
    tb.config.tc_uboot_ext2load_addr = '10000000'

try:
    tb.config.tc_uboot_ext2load_file
except:
    tb.config.tc_uboot_ext2load_file = '/test.bin'

try:
    tb.config.tc_uboot_ext2load_check
except:
    tb.config.tc_uboot_ext2load_check = 'no'

# here starts the real test
logging.info("testcase arg: %s %s %s %s %s",
  tb.config.tc_uboot_ext2load_interface, tb.config.tc_uboot_ext2load_dev,
  tb.config.tc_uboot_ext2load_addr, tb.config.tc_uboot_ext2load_file,
  tb.config.tc_uboot_ext2load_check)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# set env var
c = tb.c_con

tb.eof_write(c, "ext2load " + tb.config.tc_uboot_ext2load_interface +
  " " + tb.config.tc_uboot_ext2load_dev +
  " " + tb.config.tc_uboot_ext2load_addr +
  " " + tb.config.tc_uboot_ext2load_file)

l = ['bytes read in']
ret = tb.tbot_rup_check_all_strings(c, l)
if ret == False:
    tb.end_tc(False)

if tb.config.tc_uboot_ext2load_check == 'no':
    tb.end_tc(True)

# now check, if the image has a checksum of 0x2144df1c
# get length of file
tb.eof_call_tc("tc_ub_get_filesize.py")
file_len = tb.ub_filesize

# calc crc32
tb.eof_write(c, "crc32 " + tb.config.tc_uboot_ext2load_addr +
  " " + file_len)

l = ['2144df1c']
ret = tb.tbot_rup_check_all_strings(c, l)
if ret == False:
    tb.end_tc(False)

tb.end_tc(True)
