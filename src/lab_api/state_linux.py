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
sys.path.append("./common")
from tbotlib import tbot

def linux_set_board_state(tb, state, retry):
    """ set the connection state to the board
    """
    ret = False
    tmp = "switch state to " + state
    logging.info(tmp)

    # set new prompt
    try:
        tb.linux_prompt
    except AttributeError:
        tb.linux_prompt = '#'

    # set linux prompt
    # if we cannot set prompt, we are not in linux ...

    # check, if we get a prompt
    ret = tb.send_ctrl_m(tb.channel_con)
    if ret != True:
        return False

    #check also, if we are in linux login shell
    reg = re.compile("login:")
    ret = tb.read_line(tb.channel_con, 1)
    while(ret != None):
        res = reg.search(tb.buf[tb.channel_con])
        if res:
            tmp = 'root'
            tb.write_stream(tb.channel_con, tmp)
        ret = tb.read_line(tb.channel_con, 1)
        logging.debug("state 2 linux get propmt ret: %s buf: %s", ret, tb.buf[tb.channel_con])

    if ret != None:
        return False

    tmp = 'PS1=' + tb.linux_prompt
    ret = tb.eof_write(tb.channel_con, tmp)

    tb.prompt = tb.linux_prompt
    ret = tb.read_end_state(tb.channel_con, 1)
    if ret == True:
        return True

    # switch to linux through tc
    tb.eof_call_tc("tc_ub_boot_linux.py")

    #terminal line length
    tb.set_term_length(tb.channel_con)

    return True
