# SPDX-License-Identifier: GPL-2.0
#
import sys
import re
import logging
import time

def state_lx_parse_input(tb, c, retry, sl):
    i = 0
    # print("PPPPPPPPPPPP START", sl, c.name, c.data, c.logbuf, tb.config.state_linux_timeout)
    ctrlc_send = 0
    ctrlm_send = 0
    oldt = c.get_timeout()
    c.set_timeout(tb.config.state_linux_timeout)
    while(i < retry):
        ret = tb.tbot_rup_and_check_strings(c, sl)
        # print("PPPPPPPPPPPP", i, retry, ret, sl, c.data, c.logbuf, ctrlc_send)
        if ret == 'exception':
            if ctrlc_send == 0:
                # try to get the linux prompt via ctrl-c
                tb.send_ctrl_c(c)
                ctrlc_send = 1
                i = 0
            if ctrlm_send == 0:
                #try to get the linux prompt via ctrl-m
                tb.send_ctrl_m(c)
                ctrlm_send = 1
                i = 0
            else:
                # we get nothing -> power off / on the board
                ret = tb.set_power_state(tb.config.boardlabpowername, "off")
                if ret == False:
                    time.sleep(2)
                    tb.c_con.set_check_error(False)
                    ret = tb.set_power_state(tb.config.boardlabpowername, "on")
                    # set old timeout (wait endless)
                    # if after a power on not comes at least U-Boot
                    # prompt, wait endless until tbot WDT triggers ...
                    c.set_timeout(oldt)
                    i = 0
            continue
 
        elif ret == 'prompt':
            c.set_timeout(oldt)
            tb.c_con.set_check_error(True)
            return True

        elif ret == '0':
            # we got our tbot linux prompt
            c.set_prompt(tb.config.linux_prompt, 'linux')
            c.set_timeout(oldt)
            tb.c_con.set_check_error(True)
            return True

        elif ret == '1':
            # we got the default linux prompt
            tb.set_prompt(c, tb.config.linux_prompt, 'linux')
            c.set_timeout(oldt)
            tb.c_con.set_check_error(True)
            return True

        elif ret == '2':
            # we got u-boot prompt
            c.set_timeout(oldt)
            tb.eof_call_tc("tc_ub_boot_linux.py")
            tb.c_con.set_check_error(True)
            return True

        elif ret == '3':
            # we got login
            tb.write_stream(c, tb.config.linux_user, send_console_start=False)
            i = 0

        elif ret == '4':
            # we got password
	    tb.write_stream_passwd(c, tb.config.linux_user, tb.config.boardname)
            i = 0

        elif (ret == '5') or (ret == '6') or (ret == '7'):
            # U-Boot autobooting, try to stop it
            tb.send_ctrl_c(c)
            tb.c_con.set_check_error(True)
            i = 0
        else:
            # if we have trigger strings, we land here
            i = 0

        i += 1

    c.set_timeout(oldt)
    return False
 
def linux_set_board_state(tb, state, retry):
    """ set the connection state to the board
    """
    if tb.in_state_linux:
        return True

    try:
        tb.config.state_linux_trigger_list
    except:
        tb.config.state_linux_trigger_list = []

    ret = False
    tmp = "switch state to " + state
    logging.info(tmp)
    c = tb.c_con

    # set new prompt
    tb.send_ctrl_c(c)
    sl = [tb.config.linux_prompt, tb.config.linux_prompt_default, tb.config.uboot_prompt, 'login', 'assword', 'Autobooting in', 'noautoboot',  'autoboot']
    sl = sl + tb.config.uboot_strings
    sl = sl + tb.config.state_linux_trigger_list

    state_lx_parse_input(tb, c, retry, sl)

    #terminal line length
    tb.set_term_length(c)

    if tb.config.tb_set_after_linux != '':
        if tb.in_state_linux == 0:
            tb.in_state_linux = 1
            tb.eof_call_tc(tb.config.tb_set_after_linux)
            tb.in_state_linux = 2
    return True
