# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_uboot_usb_start.py
#
# call "usb start" command
#
# used vars:
# tb.config.tc_uboot_usb_start_expect = ['Storage Device(s) found']
# End:

from tbotlib import tbot

try:
    tb.config.tc_uboot_usb_start_expect
except:
    tb.config.tc_uboot_usb_start_expect = ['Storage Device(s) found']

# here starts the real test
logging.info("testcase arg: %s", tb.config.tc_uboot_usb_start_expect)
# set board state for which the tc is valid
tb.set_board_state("u-boot")

# set env var
c = tb.c_con

l = tb.config.tc_uboot_usb_start_expect
tb.eof_write(c, "usb reset")
tb.tbot_rup_check_all_strings(c, l, endtc=True)

tb.end_tc(True)
