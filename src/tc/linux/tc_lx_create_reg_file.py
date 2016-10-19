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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_create_reg_file.py
# creates a reg file tb.config.tc_lx_create_reg_file_name on the tbot host
# in tb.workdir
# read from tb.config.tc_lx_create_reg_file_start to tb.config.tc_lx_create_reg_file_stop
# and writes the results in the regfile
# format of the regfile:
# regaddr mask type defval
# This reg file can be used as a default file, how the
# registers must be setup, check it with testcase
# tc_lx_check_reg_file.py
# ToDo: use the file from the lab host, not the tbot host
# End:

from tbotlib import tbot

logging.info("args: %s %s %s %s %s", tb.config.tc_lx_create_reg_file_name, tb.config.tc_lx_create_reg_file_start, tb.config.tc_lx_create_reg_file_stop, tb.config.tc_lx_readreg_mask, tb.config.tc_lx_readreg_type)

#set board state for which the tc is valid
tb.set_board_state("linux")

fname = tb.workdir + "/" + tb.config.tc_lx_create_reg_file_name
try:
    fd = open(fname, 'w')
except IOError:
    logging.warning("Could not open: %s", fname)
    tb.end_tc(False)

c = tb.c_con
#write comment
# get Processor, Hardware
tmp='cat /proc/cpuinfo'
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'model name\t:')
if ret == 'prompt':
    processor = 'unknown'
    tmp = 'cat /proc/cpuinfo'
    tb.eof_write(c, tmp)
else:
    ret = tb.tbot_expect_string(c, '\n')
    if ret == 'prompt':
        tb.end_tc(False)
    tmp = tb.buf
    processor = tmp.rstrip()

ret = tb.tbot_expect_string(c, 'Hardware\t:')
if ret == 'prompt':
    tb.end_tc(False)
ret = tb.tbot_expect_string(c, '\n')
if ret == 'prompt':
    tb.end_tc(False)
hw = tb.buf.rstrip()
tb.tbot_expect_prompt(c)
tmp = 'cat /proc/version'
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'Linux version')
if ret == 'prompt':
    tb.end_tc(False)
ret = tb.tbot_expect_string(c, '\n')
if ret == 'prompt':
    tb.end_tc(False)
vers = tb.buf.rstrip()
tb.tbot_expect_prompt(c)

fd.write("# pinmux\n")
fd.write("# processor: %s\n" % processor)
fd.write("# hardware : %s\n" % hw)
fd.write("# Linux    : %s\n" % vers)
fd.write("# regaddr mask type defval\n")

#read from - to
tb.config.tc_lx_readreg_mask = '0xffffffff'
start = int(tb.config.tc_lx_create_reg_file_start, 16)
stop = int(tb.config.tc_lx_create_reg_file_stop, 16)

if tb.config.tc_lx_readreg_type == 'w':
    step = 4
if tb.config.tc_lx_readreg_type == 'h':
    step = 2
if tb.config.tc_lx_readreg_type == 'b':
    step = 1

#read register value
for i in xrange(start, stop, step):
    tmp = 'devmem2 ' + hex(i) + " " + tb.config.tc_lx_readreg_type
    tb.eof_write(c, tmp)
    ret = tb.tbot_expect_string(c, 'opened')
    if ret == 'prompt':
        tb.end_tc(False)
    ret = tb.tbot_expect_string(c, 'Value at address')
    if ret == 'prompt':
        tb.end_tc(False)
    ret = tb.tbot_expect_string(c, '\n')
    if ret == 'prompt':
        tb.end_tc(False)
    tmp = tb.buf.split(":")[1]
    tmp = tmp[1:]
    fd.write('%-10s %10s %10s %10s\n' % (hex(i), tb.config.tc_lx_readreg_mask, tb.config.tc_lx_readreg_type, tmp.rstrip()))
    tb.tbot_expect_prompt(c)

fd.close()
tb.end_tc(True)
