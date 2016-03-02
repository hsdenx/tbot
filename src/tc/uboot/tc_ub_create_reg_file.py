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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_create_reg_file.py
# creates a reg file tb.tc_ub_create_reg_file_name on the tbot host
# in tb.workdir
# read from tb.tc_ub_create_reg_file_start to tb.tc_ub_create_reg_file_stop
# and writes the results in the regfile
# format of the regfile:
# regaddr mask type defval
# This reg file can be used as a default file, how the
# registers must be setup, check it with testcase
# src/tc/tc_ub_check_reg_file.py
# ToDo: use the file from the lab host, not the tbot host
from tbotlib import tbot

logging.info("args: %s %s %s %s %s", tb.tc_ub_create_reg_file_name, tb.tc_ub_create_reg_file_start, tb.tc_ub_create_reg_file_stop, tb.tc_ub_readreg_mask, tb.tc_ub_readreg_type)

#set board state for which the tc is valid
tb.set_board_state("u-boot")

fname = tb.workdir + "/" + tb.tc_ub_create_reg_file_name
try:
    fd = open(fname, 'r+')
except IOError:
    logging.warning("Could not open: %s", fname)
    tb.end_tc(False)

c = tb.c_con
#write comment
# get U-Boot version
tmp='vers'
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'U-Boot')
if ret == 'prompt':
    tb.end_tc(False)
tb.tbot_expect_string(c, '\n')
tmp = tb.buf.replace('\r','')
tmp = tmp.replace('\n','')
vers = tmp.lstrip()
tb.tbot_expect_prompt(c)

fd.write("# pinmux\n")
fd.write("# U-Boot    : %s\n" % vers)
fd.write("# regaddr mask type defval\n")

#read from - to
tb.tc_ub_readreg_mask = '0xffffffff'
start = int(tb.tc_ub_create_reg_file_start, 16)
stop = int(tb.tc_ub_create_reg_file_stop, 16)

if tb.tc_ub_readreg_type == 'l':
    step = 4
if tb.tc_ub_readreg_type == 'w':
    step = 2
if tb.tc_ub_readreg_type == 'b':
    step = 1

#read register value
for i in xrange(start, stop, step):
    val = str(hex(i))
    tmp = 'md.' + tb.tc_ub_readreg_type + " " + val + ' 1'
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
    fd.write('%-10s %10s %10s %10s\n' % (hex(i), tb.tc_ub_readreg_mask, tb.tc_ub_readreg_type, val))

fd.close()
tb.end_tc(True)
