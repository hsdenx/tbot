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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_create_reg_file.py
# creates a reg file tb.tc_lx_create_reg_file_name on the tbot host
# in tb.workdir
# read from tb.tc_lx_create_reg_file_start to tb.tc_lx_create_reg_file_stop
# and writes the results in the regfile
# format of the regfile:
# regaddr mask type defval
# This reg file can be used as a default file, how the
# registers must be setup, check it with testcase
# src/tc/tc_lx_check_reg_file.py
# ToDo: use the file from the lab host, not the tbot host
from tbotlib import tbot

logging.info("args: %s %s %s %s %s", tb.tc_lx_create_reg_file_name, tb.tc_lx_create_reg_file_start, tb.tc_lx_create_reg_file_stop, tb.tc_lx_readreg_mask, tb.tc_lx_readreg_type)

#set board state for which the tc is valid
tb.set_board_state("linux")

fname = tb.workdir + "/" + tb.tc_lx_create_reg_file_name
try:
    fd = open(fname, 'r+')
except IOError:
    logging.warning("Could not open: %s", fname)
    tb.end_tc(False)

#write comment
fd.write("# pinmux reg am335x\n")
fd.write("# regaddr mask type defval\n")

#read from - to
# 0x44e10800 - 0x44e10a34
tb.tc_lx_readreg_mask = '0xffffffff'
start = int(tb.tc_lx_create_reg_file_start, 16)
stop = int(tb.tc_lx_create_reg_file_stop, 16)

if tb.tc_lx_readreg_type == 'w':
    step = 4
if tb.tc_lx_readreg_type == 'h':
    step = 2
if tb.tc_lx_readreg_type == 'b':
    step = 1

#read register value
for i in xrange(start, stop, step):
    tmp = 'devmem2 ' + hex(i) + " " + tb.tc_lx_readreg_type
    tb.eof_write_con(tmp)
    tb.eof_search_str_in_readline_con("opened")
    tb.eof_search_str_in_readline_con("Value at address")
    tmp=self.buf[1].split(":")[1]
    tmp=tmp[1:]
    fd.write('%-10s %10s %10s %10s\n' % (hex(i), tb.tc_lx_readreg_mask, tb.tc_lx_readreg_type, tmp))

fd.close()
tb.end_tc(True)
