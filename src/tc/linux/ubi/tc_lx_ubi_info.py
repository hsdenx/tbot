# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_ubi_info.py
# ubinfo tb.config.tc_ubi_ubi_dev
# End:
from tbotlib import tbot
import re

# here starts the real test
logging.info("args: %s %s", tb.config.tc_ubi_cmd_path, tb.config.tc_ubi_ubi_dev)

# set board state for which the tc is valid
tb.set_board_state("linux")

def create_ubi_cmd(tb, cmd):
    tmp = tb.config.tc_ubi_cmd_path + '/' + cmd
    return tmp

tmp = create_ubi_cmd(tb, 'ubi-utils/ubinfo ' + tb.config.tc_ubi_ubi_dev)
c = tb.c_con
tb.eof_write(c, tmp)

searchlist = ["Present volumes", "error"]
tmp = True
volume_list = ""
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        ret = tb.tbot_expect_string(c, '\n')
        if ret == 'prompt':
            tb.end_tc(False)
        tmp2 = tb.buf.split(":")[1]
        tmp2 = tmp2[1:]
        tmp2 = tmp2.strip()
        volume_list = tmp2.split(",")
    elif ret == '1':
        tb.tbot_expect_prompt(c)
        tb.end_tc(False)
    elif ret == 'prompt':
        tmp = False

if volume_list != "":
    for vol in volume_list:
        vol = vol.lstrip()
        tmp = create_ubi_cmd(tb, 'ubi-utils/ubinfo ' + tb.config.tc_ubi_ubi_dev + '_' + vol)
        tb.eof_write(c, tmp)
        tb.tbot_expect_prompt(c)

tb.end_tc(True)
