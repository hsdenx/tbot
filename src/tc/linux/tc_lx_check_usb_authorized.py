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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_check_usb_authorized.py
# check if usb device tb.config.tc_lx_check_usb_authorized needs authorizing
# End:

import time
from tbotlib import tbot

logging.info("%s", tb.config.tc_lx_check_usb_authorized)

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.c_con
tmp = 'dmesg | grep "' + tb.config.tc_lx_check_usb_authorized + '"'
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'Device is not authorized for usage')
if ret == 'prompt':
    # no authorization needed
    tb.end_tc(True)

tb.tbot_expect_prompt(c)

# check how authorized is set
tmp = "cat /sys/bus/usb/drivers/" + tb.config.tc_lx_check_usb_authorized[:3] + "/" + tb.config.tc_lx_check_usb_authorized[4:] + "/authorized"
tb.eof_write(c, tmp)
tb.tbot_expect_prompt(c)
# echo 1 > /sys/bus/usb/drivers/usb/1-1/authorized
tmp = "echo 1 > /sys/bus/usb/drivers/" + tb.config.tc_lx_check_usb_authorized[:3] + "/" + tb.config.tc_lx_check_usb_authorized[4:] + "/authorized"
tb.eof_write(c, tmp)
tb.eof_expect_string(c, 'authorized to connect')

time.sleep(4)
tb.end_tc(True)
