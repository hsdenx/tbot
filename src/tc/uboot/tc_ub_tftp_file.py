# SPDX-License-Identifier: GPL-2.0
#
# Description:
# load file tb.config.tc_ub_tftp_file_name to tb.config.tc_ub_tftp_file_addr
# with tftp command in uboot
#
# used variables
#
# - tb.config.tc_ub_tftp_file_addr
#| ram address to which the file gets loaded
#| default: tb.config.ub_load_board_env_addr
#
# - tb.config.tc_ub_tftp_file_name
#| file name for the tftp command
#| default: ''
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_tftp_file_addr', tb.config.ub_load_board_env_addr)
tb.define_variable('tc_ub_tftp_file_name', '')

# set board state for which the tc is valid
tb.set_board_state("u-boot")

c = tb.c_con
tmp = 'tftp ' + tb.config.tc_ub_tftp_file_addr + ' ' + tb.config.tc_ub_tftp_file_name
tb.eof_write(c, tmp)
searchlist = ["Bytes transferred", "error", "Retry count exceeded", "ERROR", "0 Bytes/s", "File not found"]
tmp = True
load_fail = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        load_fail = False
    elif ret == '1':
        load_fail = True
    elif ret == '2':
        load_fail = True
        # send Ctrl-C
        self.send_ctrl_c(c)
    elif ret == '3':
        load_fail = True
    elif ret == '4':
        load_fail = True
    elif ret == '5':
        load_fail = True
    elif ret == 'prompt':
        tmp = False

if load_fail == True:
    tb.end_tc(False)

tb.end_tc(True)
