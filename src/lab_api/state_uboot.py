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
import sys
import re
import logging
import time
import pexpect
from struct import pack

def u_boot_parse_input(tb, c, retry):
    logging.debug("------------------- parse input")
    sl = tb.config.uboot_strings
    i = 0
    oldt = c.get_timeout()
    c.set_timeout(1)
    while(i < retry):
        ret = tb.tbot_rup_and_check_strings(c, sl)
        if ret == '0':
            # send ESC ESC
            string = pack('h', 27)
            string = string[:1]
            c.send_raw(string)
            c.send_raw(string)
            i = 0
        if ret == '1':
            ret = tb.write_stream(c, "noautoboot")
            i = 0
        if ret == '2':
            if tb.config.uboot_autoboot_key != '':
		c.send_raw(tb.config.uboot_autoboot_key)
            else:
                tb.send_ctrl_m(c)
            i = 0
        if ret == '3' or ret == 'exception':
            tb.send_ctrl_c(c)
            tb.send_ctrl_m(c)
        if ret == '4':
            i = 0
        if ret == 'prompt':
            tb.flush(c)
            c.set_timeout(oldt)
            return True
        i += 1

    c.set_timeout(oldt)
    return False

def u_boot_login(tb, state, retry):
    # check, if we get a prompt
    # problem, what sending to u-boot, to get back a prompt?
    logging.debug("------------------- u_boot_login")
    c = tb.c_con
    ret = u_boot_parse_input(tb, c, retry)
    return ret

def u_boot_set_board_state(tb, state, retry):
    """ set the connection state to the board
    """
    logging.debug("------------------- set board state")
    ret = False
    tmp = "switch state to " + state
    logging.info(tmp)

    # set default values
    tb.eof_call_tc("tc_def_ub.py")

    # set new prompt
    try:
        tb.config.uboot_prompt
    except AttributeError:
        tb.config.uboot_prompt = 'U-Boot#'

    tb.c_con.set_prompt(tb.config.uboot_prompt)

    ret = tb.get_power_state(tb.config.boardlabpowername)
    if ret:
        # check, if we get a correct prompt
        ret = u_boot_login(tb, state, retry)
        if ret == True:
            return True

    # now the easiest way ... simple power off/on
    ret = tb.set_power_state(tb.config.boardlabpowername, "off")
    if ret == False:
        time.sleep(2)
        ret = tb.set_power_state(tb.config.boardlabpowername, "on")
        if ret != True:
            logging.error("------------------- set board state failure")
            tb.end_tc(False)
            return False
        tb.check_debugger()

    ret = u_boot_login(tb, state, retry)
    if ret == True:
        return True

    logging.error("------------------- set board state failure end")
    # maybe connect to a BDI ?
    # currently failure
    tb.end_tc(False)
    return False
