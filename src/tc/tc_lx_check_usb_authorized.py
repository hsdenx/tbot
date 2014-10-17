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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_check_usb_authorized.py
# check if usb device needs authorizing
#
from tbotlib import tbot

logging.info("%s", tb.tc_lx_check_usb_authorized)

#set board state for which the tc is valid
tb.set_board_state("linux")


tmp = 'dmesg | grep "' + tb.tc_lx_check_usb_authorized + '"'
tb.eof_write_con(tmp)
ret = tb.search_str_in_readline_con("Device is not authorized for usage")
if ret == False:
    #no authorization needed
    tb.end_tc(True)

tb.eof_read_end_state_con(1)

#check how authorized is set
tmp = "cat /sys/bus/usb/drivers/" + tb.tc_lx_check_usb_authorized[:3] + "/" + tb.tc_lx_check_usb_authorized[4:] + "/authorized"
tb.eof_write_con(tmp)
tb.eof_read_end_state_con(1)
#echo 1 > /sys/bus/usb/drivers/usb/1-1/authorized
tmp = "echo 1 > /sys/bus/usb/drivers/" + tb.tc_lx_check_usb_authorized[:3] + "/" + tb.tc_lx_check_usb_authorized[4:] + "/authorized"
tb.eof_write_con(tmp)
#usb 1-1: authorized to connect 
tb.eof_search_str_in_readline_con("authorized to connect")

tb.eof_read_end_state_con(1)
tb.end_tc(True)
