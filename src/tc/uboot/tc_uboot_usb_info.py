# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# call "usb info" command
#
# used variables:
#
# - tb.config.tc_uboot_usb_info_expect
#| strings which must come from "usb info" command
#| default: "['Hub,  USB Revision 2.0', 'Mass Storage,  USB Revision 2.0']"
#
# End:

from tbotlib import tbot

tb.define_variable('tc_uboot_usb_info_expect', "['Hub,  USB Revision 2.0', 'Mass Storage,  USB Revision 2.0']")

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# set env var
c = tb.c_con

l = tb.config.tc_uboot_usb_info_expect
tb.eof_write(c, "usb info")
tb.tbot_rup_check_all_strings(c, l, endtc=True)

tb.end_tc(True)
