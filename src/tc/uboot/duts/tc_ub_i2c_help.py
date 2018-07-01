# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple prints "help i2c" cmd
#
# used variables
#
# - tb.config.tc_ub_i2c_help_with_bus
#| if 'yes' i2c help output with "i2c bus"
#| default: 'no'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_i2c_help_with_bus', 'no')

# set board state for which the tc is valid
tb.set_board_state("u-boot")

ret = tb.write_cmd_check(tb.c_con, "help i2c", "Unknown command")
if ret == True:
    tb.end_tc(True)

if tb.config.tc_ub_i2c_help_with_bus == 'yes':
    searchlist = ["i2c bus", "crc32", "i2c dev", "i2c loop chip", "i2c md chip address",
              "i2c mm chip address", "i2c mw chip address", "i2c nm chip address",
              "i2c probe", "i2c read chip address", "i2c write memaddress",
              "i2c reset", "i2c speed"]
    ok_list = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    count = 14
else:
    searchlist = ["i2c crc32", "i2c loop chip", "i2c md chip address",
              "i2c mm chip address", "i2c mw chip address", "i2c nm chip address",
              "i2c probe", "i2c read chip address", "i2c write memaddress",
              "i2c reset", "i2c speed"]
    ok_list = [False, False, False, False, False, False, False, False, False, False, False]
    count = 12

self.event.create_event('main', 'tc_ub_i2c_help.py', 'SET_DOC_FILENAME', 'help_i2c')
tb.eof_write(tb.c_con, 'help i2c')
tmp = True
cmd_ok = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(tb.c_con, searchlist)
    if ret == 'prompt':
        tmp = False
    else:
        cnt = int(ret)
        if tmp in range(0, count):
            ok_list[cnt] = True
            if cnt > 0:
                if ok_list[cnt - 1] != True:
                    logging.info("%d : %s not found", cnt - 1, searchlist[cnt - 1])
                    cmd_ok = False

tb.end_tc(cmd_ok)
