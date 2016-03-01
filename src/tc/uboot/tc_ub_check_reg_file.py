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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_check_reg_file.py
# checks if the default values in reg file tb.tc_ub_create_reg_file_name
# on the tbot host in tb.workdir have the same values, as the
# registers on the board
# format of the regfile:
# regaddr mask type defval
# ToDo: use the file from the lab host, not the tbot host
from tbotlib import tbot

logging.info("args: %s", tb.tc_ub_create_reg_file_name)

#set board state for which the tc is valid
tb.set_board_state("u-boot")

c = tb.c_con
fname = tb.workdir + "/" + tb.tc_ub_create_reg_file_name
try:
    fd = open(fname, 'r')
except IOError:
    logging.warning("Could not open: %s", fname)
    tb.end_tc(False)

for line in fd.readlines():
    cols = line.split()
    if cols[0] == '#':
        continue
    val = cols[0]
    tmp = 'md.'+ cols[2] + ' ' + val
    tb.eof_write(c, tmp)
    val = val.replace('0x','')
    ret = tb.tbot_expect_string(c, val)
    if ret == 'prompt':
        tb.end_tc(False)
    tb.tbot_expect_prompt(c)
    tmp = tb.buf.split(':')
    val = tmp[1].split(' ')
    val = val[1].lstrip('0')
    if val == '':
        val = '0x0'
    else:
        val = '0x' + val

    if (int(val, 16) & int(cols[1], 16)) != (int(cols[3], 16) & int(cols[1], 16)):
        logging.info("args: %s %s & %s != %s", tb.tc_ub_create_reg_file_name, val, cols[1], cols[3])
        tb.end_tc(False)

tb.end_tc(True)
