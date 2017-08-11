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
# python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_board_fipad_ub_usb.py
#
# do some simple usb test
# - usb start
# - usb info (check some output)
# - list root dir on the stick
#   (ext2 formatted stick)
# - load test.bin from this partition with ext2load
# - check if test.bin has the crc32 sum 0x2144df1c
#
# used vars:
# tb.config.tc_uboot_usb_info_expect = [
#    'Hub,  USB Revision 2.0',
#    'Mass Storage,  USB Revision 2.0',
#    'SMI Corporation USB DISK AA04012900007453',
#    'Vendor: 0x090c  Product 0x1000 Version 17.0'
# ]
# tb.config.tc_board_fipad_uboot_ext2load_files = ['test.bin']
#   list of files which get load and crc32 tested
# End:

from tbotlib import tbot

tb.eof_call_tc("tc_uboot_usb_start.py")
tb.eof_call_tc("tc_uboot_usb_info.py")

tb.eof_call_tc("tc_uboot_ext2ls.py")

tb.config.tc_uboot_ext2load_check = 'yes'
for files in tb.config.tc_board_fipad_uboot_ext2load_files:
    tb.config.tc_uboot_ext2load_file = files
    tb.eof_call_tc("tc_uboot_ext2load.py")

tb.end_tc(True)
