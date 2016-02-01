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
from struct import pack
sys.path.append("./common")
from tbotlib import tbot

def u_boot_parse_input(tb, state):
    logging.debug("------------------- parse input")
    reg3 = re.compile("Autobooting in")
    reg2 = re.compile('noautoboot')
    reg = re.compile('autoboot')
    i = 0
    retry = 5
    use_debugger = 4
    debugger = 0
    while(i < retry):
        ret = tb.read_line(tb.channel_con, 1)
        logging.debug("setb a rl ret: %s buf: %s", ret, tb.buf[tb.channel_con])
        if ret == None:
            logging.debug("------------------- parse input Timeout end False")
            i += 1
            if i < use_debugger:
                # send a Ctrl-C
                tb.send_ctrl_c(tb.channel_con)
                continue
            else:
                if debugger:
                    continue
                else:
                    tb.check_debugger()
                    debugger = 1
                    i = 0
            continue

        res = reg3.search(tb.buf[tb.channel_con])
        if res:
            string = pack('h', 27)
            string = string[:1]
            ret = tb.lab.write_no_ret(tb.channel_con, string)
            ret = tb.lab.write_no_ret(tb.channel_con, string)
            i = 0
            continue
        res = reg2.search(tb.buf[tb.channel_con])
        if res:
            ret = tb.write_stream(tb.channel_con, "noautoboot")
            i = 0
        else:
            res = reg.search(tb.buf[tb.channel_con])
        logging.debug("setb rl ret: %s res: %s buf: %s", ret, res, tb.buf[tb.channel_con])
        if res:
            tb.send_ctrl_m(tb.channel_con)
            i = 0
        else:
            if ret == True:
                # i = 0
                ret2 = tb.is_end_fd(tb.channel_con, tb.buf[tb.channel_con])
                logging.debug("setb T buf: %s ret2: %s", tb.buf[tb.channel_con], ret2)
                if ret2:
                    logging.info("switched to state U-Boot")
                    tb.flush_fd(tb.channel_con)
                    tb.channel_end[tb.channel_con] = '1'
                    return True
                continue
            else:
                if ret == False:
                    ret2 = tb.is_end_fd(tb.channel_con, tb.buf[tb.channel_con])
                    logging.debug("setb T buf: %s ret2: %s", tb.buf[tb.channel_con], ret2)
                    if ret2 == True:
                        logging.debug("------------------- parse input Timeout end True")
                        logging.info("switched to state U-Boot")
                        tb.channel_end[tb.channel_con] = '1'
                        return True
                else:
                    #Timeout
                    logging.debug("------------------- parse input Timeout end False")
        i += 1

    return False

def u_boot_login(tb, state, retry):
    # check, if we get a prompt
    # problem, what sending to u-boot, to get back a prompt?
    logging.debug("------------------- u_boot_login")
    ret = u_boot_parse_input(tb, state)
    return ret

def u_boot_set_board_state(tb, state, retry):
    """ set the connection state to the board
    """
    logging.debug("------------------- set board state")
    ret = False
    tmp = "switch state to " + state
    logging.info(tmp)

    # set new prompt
    try:
        tb.uboot_prompt
    except AttributeError:
        tb.uboot_prompt = 'U-Boot#'

    tb.prompt = tb.uboot_prompt
    # nothing more in u-boot todo, as prompt is fix

    # check, if we get a prompt
    ret = u_boot_login(tb, state, retry)
    if ret == True:
        return True

    # switch to u-boot if not ?? repower ??
    ret = tb.lab.set_power_state(tb.boardlabpowername, "off")
    if ret == False:
        #tb.flush_fd(tb.channel_con)
        time.sleep(2)
        ret = tb.lab.set_power_state(tb.boardlabpowername, "on")
        if ret != True:
            logging.debug("------------------- set board state failure")
            tb.failure()
            return False
        tb.check_debugger()

    ret = u_boot_login(tb, state, retry)
    if ret == True:
        return True

    logging.debug("------------------- set board state failure end")
    # maybe connect to a BDI ?
    # currently failure
    tb.failure()
    return False
