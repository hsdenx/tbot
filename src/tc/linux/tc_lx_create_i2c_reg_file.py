# SPDX-License-Identifier: GPL-2.0
#
# Description:
# create with i2cget tool a register dump of
# i2c device on bus tb.config.tc_lx_create_i2c_reg_file_bus
# with addr tb.config.tc_lx_create_i2c_reg_file_bus
#
# dump registers from tb.config.tc_lx_create_i2c_reg_file_start
# until tb.config.tc_lx_create_i2c_reg_file_stop
# with accessmode tb.config.tc_lx_i2c_readreg_type
# into file with name
# tb.config.tc_lx_create_i2c_reg_file_name
#
# used variables
#
# - tb.config.tc_lx_create_i2c_reg_file_name
#| filename to which registerdump get written
#| default: 'i2c_dump.txt'
#
# - tb.config.tc_lx_create_i2c_reg_file_start
#| start offset from which get read
#| default: '0x0'
#
# - tb.config.tc_lx_create_i2c_reg_file_stop
#| stop offset until to which get read
#| default: '0x10'
#
# - tb.config.tc_lx_create_i2c_reg_file_bus
#| i2c bus number from which get read
#| default: '0x0'
#
# - tb.config.tc_lx_create_i2c_reg_file_addr
#| i2c address from which get read
#| default: '0x8'
#
# - tb.config.tc_lx_i2c_readreg_mask
#| mask which get written into dump file
#| default: ''
#
# - tb.config.tc_lx_i2c_readreg_type
#| read type (types from i2c_get util)
#| default: 'b'
#
# End:

from tbotlib import tbot

save = tb.workfd
tb.workfd = tb.c_con

tb.define_variable('tc_lx_create_i2c_reg_file_name', 'i2c_dump.txt')
tb.define_variable('tc_lx_create_i2c_reg_file_start', '0x0')
tb.define_variable('tc_lx_create_i2c_reg_file_stop', '0x10')
tb.define_variable('tc_lx_i2c_readreg_mask', '0xff')
tb.define_variable('tc_lx_i2c_readreg_type', 'b')
tb.define_variable('tc_lx_create_i2c_reg_file_bus', '0x0')
tb.define_variable('tc_lx_create_i2c_reg_file_addr', '0x8')

logging.info("args: %s", tb.config.i2c_pre)

# set board state for which the tc is valid
tb.set_board_state("linux")

fname = tb.workdir + "/" + tb.config.tc_lx_create_i2c_reg_file_name
try:
    fd = open(fname, 'w')
except IOError:
    logging.warning("Could not open: %s", fname)
    tb.workfd = save
    tb.end_tc(False)

c = tb.workfd
# write comment
# get Processor, Hardware
tmp = 'cat /proc/cpuinfo'
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'model name\t:')
if ret == 'prompt':
    processor = 'unknown'
    tmp = 'cat /proc/cpuinfo'
    tb.eof_write(c, tmp)
else:
    ret = tb.tbot_expect_string(c, '\n')
    if ret == 'prompt':
        tb.workfd = save
        tb.end_tc(False)
    tmp = tb.buf
    processor = tmp.rstrip()

ret = tb.tbot_expect_string(c, 'Hardware\t:')
if ret == 'prompt':
    tb.workfd = save
    tb.end_tc(False)
ret = tb.tbot_expect_string(c, '\n')
if ret == 'prompt':
    tb.workfd = save
    tb.end_tc(False)
hw = tb.buf.rstrip()
tb.tbot_expect_prompt(c)
tmp = 'cat /proc/version'
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'Linux version')
if ret == 'prompt':
    tb.workfd = save
    tb.end_tc(False)
ret = tb.tbot_expect_string(c, '\n')
if ret == 'prompt':
    tb.workfd = save
    tb.end_tc(False)
vers = tb.buf.rstrip()
tb.tbot_expect_prompt(c)

bus = tb.config.tc_lx_create_i2c_reg_file_bus
addr = tb.config.tc_lx_create_i2c_reg_file_addr
fd.write("# i2c register dump bus: %s addr: %s\n" % (bus, addr))
fd.write("# processor: %s\n" % processor)
fd.write("# hardware : %s\n" % hw)
fd.write("# Linux    : %s\n" % vers)
fd.write("# regaddr mask type defval\n")

# read from - to
start = int(tb.config.tc_lx_create_i2c_reg_file_start, 16)
stop = int(tb.config.tc_lx_create_i2c_reg_file_stop, 16)

if tb.config.tc_lx_i2c_readreg_type == 'w':
    step = 4
if tb.config.tc_lx_i2c_readreg_type == 'b':
    step = 1

# read register value
pre = tb.config.i2c_pre
for i in xrange(start, stop, step):
    tmp = pre + 'i2cget -f -y ' + bus + ' ' + addr + ' ' + hex(i) + ' ' + tb.config.tc_lx_i2c_readreg_type
    tb.eof_write(c, tmp)
    ret = tb.tbot_get_line(c)
    fd.write('%-10s %10s %10s %10s\n' % (hex(i), tb.config.tc_lx_i2c_readreg_mask, tb.config.tc_lx_i2c_readreg_type, ret.strip()))

fd.close()
tb.gotprompt = True
tb.workfd = save
tb.end_tc(True)
