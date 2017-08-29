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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_i2c_help.py
# simple prints "help i2c" cmd
# End:

from tbotlib import tbot

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
