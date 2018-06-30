# SPDX-License-Identifier: GPL-2.0
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
