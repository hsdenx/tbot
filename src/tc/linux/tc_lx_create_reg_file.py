# SPDX-License-Identifier: GPL-2.0
#
# Description:
# creates a reg file tb.config.tc_lx_create_reg_file_name on the tbot host
# in tb.workdir
# read from tb.config.tc_lx_create_reg_file_start to tb.config.tc_lx_create_reg_file_stop
# and writes the results in the regfile
# format of the regfile:
# regaddr mask type defval
# This reg file can be used as a default file, how the
# registers must be setup, check it with testcase
# tc_lx_check_reg_file.py
#
# If you have to call devmem2 with a "header"
# set it through tb.config.devmem2_pre
# so on the bbb with original rootfs -> no devmem2 installed
# so to use tc which use devmem2 you have to copy devmem2
# bin to the rootfs, and start it with 'sudo ...'
#
# ToDo: use the file from the lab host, not the tbot host
#
# used variables
#
# - tb.config.tc_lx_create_reg_file_name
#| name of the register file
#| default: 'pinmux.reg'
#
# - tb.config.tc_lx_create_reg_file_start
#| start address of registerdump
#| default: '0x44e10800'
#
# - tb.config.tc_lx_create_reg_file_stop
#| end address for register dump
#| default: '0x44e10a34'
#
# - tb.config.tc_lx_readreg_mask
#| used mask
#| default: '0xffffffff'
#
# - tb.config.tc_lx_readreg_type
#| devmem2 type for reading register
#| default: 'w'
#
# End:

from tbotlib import tbot

tb.workfd = tb.c_con

tb.define_variable('tc_lx_create_reg_file_name', 'pinmux.reg')
tb.define_variable('tc_lx_create_reg_file_start', '0x44e10800')
tb.define_variable('tc_lx_create_reg_file_stop', '0x44e10a34')
tb.define_variable('tc_lx_readreg_mask', '0xffffffff')
tb.define_variable('tc_lx_readreg_type', 'w')
tb.define_variable('devmem2_pre', '')

# set board state for which the tc is valid
tb.set_board_state("linux")

fname = tb.workdir + "/" + tb.config.tc_lx_create_reg_file_name
try:
    fd = open(fname, 'w')
except IOError:
    logging.warning("Could not open: %s", fname)
    tb.end_tc(False)

c = tb.workfd
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
pre = tb.config.devmem2_pre
strings = ['Value at address', 'Read at address']
for i in xrange(start, stop, step):
    tmp = pre + 'devmem2 ' + hex(i) + " " + tb.config.tc_lx_readreg_type
    tb.eof_write(c, tmp)
    ret = tb.tbot_expect_string(c, 'opened')
    if ret == 'prompt':
        tb.end_tc(False)

    ret = tb.tbot_rup_and_check_strings(c, strings)
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
