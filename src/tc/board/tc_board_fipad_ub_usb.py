# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# do some simple usb test
# - usb start
# - usb info (check some output)
# - list root dir on the stick
#   (ext2 formatted stick)
# - load test.bin from this partition with ext2load
# - check if test.bin has the crc32 sum 0x2144df1c
#
# used variables
#
# - tb.config.tc_board_fipad_uboot_ext2load_files
#| list of files which get load and crc32 tested
#| default: '[]'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_board_fipad_uboot_ext2load_files', '[]')
tb.eof_call_tc("tc_uboot_usb_start.py")
tb.eof_call_tc("tc_uboot_usb_info.py")

tb.eof_call_tc("tc_uboot_ext2ls.py")

tb.config.tc_uboot_ext2load_check = 'yes'
for files in tb.config.tc_board_fipad_uboot_ext2load_files:
    tb.config.tc_uboot_ext2load_file = files
    tb.eof_call_tc("tc_uboot_ext2load.py")

tb.end_tc(True)
