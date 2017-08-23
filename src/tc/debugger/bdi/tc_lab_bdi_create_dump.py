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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_bdi_create_dump.py
#
# check if we are on the BDI already, if not switch to it
# with tc_lab_bdi_connect.py
#
# - send "halt"
# - dump registers from tb.config.tc_lab_bdi_create_dump_start
#   to tb.config.tc_lab_bdi_create_dump_stop with mask
#   tb.config.tc_lab_bdi_create_dump_mask and stepsize
#   tb.config.tc_lab_bdi_create_dump_type into the file
#   tb.config.tc_lab_bdi_create_dump_filename
# End:

from tbotlib import tbot

tb.workfd = tb.c_ctrl

logging.info("args: %s", tb.workfd.name)
logging.info("args: %s %s %s %s %s", tb.config.tc_lab_bdi_create_dump_filename, tb.config.tc_lab_bdi_create_dump_start, tb.config.tc_lab_bdi_create_dump_stop, tb.config.tc_lab_bdi_create_dump_mask, tb.config.tc_lab_bdi_create_dump_type)

c = tb.workfd

# check if we are in the BDI
if c.get_prompt() != tb.config.lab_bdi_upd_uboot_bdi_prompt:
    # try to get into BDI
    tb.eof_call_tc('tc_lab_bdi_connect.py')

# -> halt the board
tb.write_stream(c, 'halt', send_console_start=False)

ret = tb.tbot_expect_string(c, 'Current LR')
if ret == False:
    tb.end_tc(False)
tb.tbot_expect_prompt(c)

fname = tb.workdir + "/" + tb.config.tc_lab_bdi_create_dump_filename
try:
    fd = open(fname, 'w')
except IOError:
    logging.warning("Could not open: %s", fname)
    tb.end_tc(False)

fd.write("# regaddr mask type defval\n")

#read from - to
tb.config.tc_lab_bdi_create_dump_mask = '0xffffffff'
start = int(tb.config.tc_lab_bdi_create_dump_start, 16)
stop = int(tb.config.tc_lab_bdi_create_dump_stop, 16)

if tb.config.tc_lab_bdi_create_dump_type == 'w':
    step = 4
    pre_cmd = 'md '
if tb.config.tc_lab_bdi_create_dump_type == 'h':
    step = 2
    pre_cmd = 'mdh '
if tb.config.tc_lab_bdi_create_dump_type == 'b':
    step = 1
    pre_cmd = 'mdb '

# now read the registers
for i in xrange(start, stop, step):
    cmd = pre_cmd + hex(i) + ' 1'
    tb.write_stream(c, cmd, send_console_start=False)
    tmp = c.lineend
    c.lineend = '\n'
    ret = tb.read_line(c)
    if ret == False:
        tb.tbot_expect_prompt(c)
        tb.end_tc(False)

    ret = tb.read_line(c)
    if ret == True:
        val = tb.buf.split()[2]
        fd.write('%-10s %10s %10s %10s\n' % (hex(i), tb.config.tc_lab_bdi_create_dump_mask, tb.config.tc_lab_bdi_create_dump_type, val))
    c.lineend = tmp
    tb.tbot_expect_prompt(c)

tb.end_tc(True)
