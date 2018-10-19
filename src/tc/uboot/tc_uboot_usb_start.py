# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# call "usb start" command
#
# used variable
#
# - tb.config.tc_uboot_usb_start_expect
#| strings which must come back from "usb start" command
#| default: 'Storage Device(s) found'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_uboot_usb_start_expect', '["Storage Device(s) found"]')

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# set env var
c = tb.c_con

l = tb.config.tc_uboot_usb_start_expect
tb.eof_write(c, "usb reset")
tb.tbot_rup_check_all_strings(c, l, endtc=True)

tb.end_tc(True)
