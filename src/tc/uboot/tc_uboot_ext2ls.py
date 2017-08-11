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
# python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_uboot_ext2ls.py
#
# simply call ext2ls
#
# used vars:
# tb.config.tc_uboot_ext2ls_expect = ['lost+found']
#   strings we expect from the ext2ls command
# tb.config.tc_uboot_ext2ls_interface = 'usb'
# tb.config.tc_uboot_ext2ls_dev = '0:1'
# tb.config.tc_uboot_ext2ls_dir = '/'
# End:

from tbotlib import tbot

try:
    tb.config.tc_uboot_ext2ls_expect
except:
    tb.config.tc_uboot_ext2ls_expect = [
    'lost+found']

try:
    tb.config.tc_uboot_ext2ls_interface
except:
    tb.config.tc_uboot_ext2ls_interface = 'usb'

try:
    tb.config.tc_uboot_ext2ls_dev
except:
    tb.config.tc_uboot_ext2ls_dev = '0:1'

try:
    tb.config.tc_uboot_ext2ls_dir
except:
    tb.config.tc_uboot_ext2ls_dir = '/'

# here starts the real test
logging.info("testcase arg: %s %s %s %s", tb.config.tc_uboot_ext2ls_expect,
  tb.config.tc_uboot_ext2ls_interface, tb.config.tc_uboot_ext2ls_dev,
  tb.config.tc_uboot_ext2ls_dir)
# set board state for which the tc is valid
tb.set_board_state("u-boot")

# set env var
c = tb.c_con

l = tb.config.tc_uboot_ext2ls_expect
tb.eof_write(c, "ext2ls " + tb.config.tc_uboot_ext2ls_interface + " " +
  tb.config.tc_uboot_ext2ls_dev + " " + tb.config.tc_uboot_ext2ls_dir)
tb.tbot_rup_check_all_strings(c, l, endtc=True)

tb.end_tc(True)
