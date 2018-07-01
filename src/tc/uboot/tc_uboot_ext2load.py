# SPDX-License-Identifier: GPL-2.0
#
# Description:
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
# used variables
#
# - tb.config.tc_uboot_ext2load_check
#| if == 'no' do not check crc
#| default: 'no'
#
# - tb.config.tc_uboot_ext2load_file
#| name of file, which gets loaded
#| default: '/test.bin'
#
# - tb.config.tc_uboot_ext2load_addr
#| RAM address to which the file get loaded
#| default: '10000000'
#
# - tb.config.tc_uboot_ext2load_dev
#| device from which the file get loaded
#| default: '0:1'
#
# - tb.config.tc_uboot_ext2load_interface
#| device from which the file get loaded
#| default: 'usb'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_uboot_ext2load_check', 'no')
tb.define_variable('tc_uboot_ext2load_file', '/test.bin')
tb.define_variable('tc_uboot_ext2load_addr', '10000000')
tb.define_variable('tc_uboot_ext2load_dev', '0:1')
tb.define_variable('tc_uboot_ext2load_interface', 'usb')

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
