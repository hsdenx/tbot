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

def state_lx_parse_input(tb, c, retry):
    sl = [pexpect.EOF, 'login']
    i = 0
    oldt = c.h.timeout
    c.h.timeout = 4
    while(i < retry):
        ret = tb.tbot_read_line_and_check_strings(c, sl)
        if ret == '1':
            tb.write_stream(c, 'root')
            i = 0
        if ret == 'exception':
            tb.send_ctrl_c(c)
        if ret == 'prompt':
            c.h.timeout = oldt
            return True
        i += 1

    c.h.timeout = oldt
    return False
 
def linux_set_board_state(tb, state, retry):
    """ set the connection state to the board
    """
    ret = False
    tmp = "switch state to " + state
    logging.info(tmp)
    c = tb.c_con

    # set new prompt
    tb.send_ctrl_c(c)
    sl = [tb.linux_prompt, tb.linux_prompt_default, tb.uboot_prompt]
    ret = tb.tbot_read_line_and_check_strings(c, sl)
    if ret == '0':
        return True

    if ret == '1':
        tb.set_prompt(c, tb.linux_prompt, "", "")
        tb.set_term_length(c)
        return True

    if ret == '2':
        tb.eof_call_tc("tc_ub_boot_linux.py")

    #terminal line length
    tb.set_term_length(c)

    return True
