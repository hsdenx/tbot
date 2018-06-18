# SPDX-License-Identifier: GPL-2.0
#
# Description:
# checks if the default values in reg file tb.config.tc_lx_create_i2c_reg_file_name
# on the tbot host in tb.workdir have the same values, as the
# the values on the board.
#
# bus and addr of the i2c device comes from the register
# file.
#
# you should create the register file with testcase
# tc_lx_create_i2c_reg_file.py
#
# used variables:
#
# - tb.config.i2c_pre
#   string added before 'i2cget' command
#   default: ''
#
# - tb.config.tc_lx_create_i2c_reg_file_name
#   register dump file name
#
# End:

from tbotlib import tbot

try:
    tb.config.i2c_pre
except:
    tb.config.i2c_pre = ''

logging.info("args: %s", tb.config.tc_lx_create_i2c_reg_file_name)

# set board state for which the tc is valid
tb.set_board_state("linux")

pre = tb.config.i2c_pre
c = tb.c_con
fname = tb.workdir + "/" + tb.config.tc_lx_create_i2c_reg_file_name
try:
    fd = open(fname, 'r')
except IOError:
    logging.warning("Could not open: %s", fname)
    tb.end_tc(False)

isuboot = 0

def get_type(t, ub):
    if ub == 0:
        return t
    if t == 'l':
        return 'w'
    if t == 'w':
        return 'w'
    if t == 'b':
        return 'b'
    logging.error("U-Boot Type %s not implemented.", t)
    tb.end_tc(False)

foundbus = False
foundaddr = False
for line in fd.readlines():
    cols = line.split()
    if cols[0] == '#':
        if 'U-Boot' in line:
            # we have a register dump from U-Boot, so we have
            # to adapt register length marker
            isuboot = 1
        if 'bus' in line and foundbus == False:
            foundbus = True
            tmp = line.split('bus: ')
            tmp = tmp[1].split(' addr: ')
            bus = tmp[0]
        if 'addr' in line and foundaddr == False:
            foundaddr = True
            tmp = line.split('addr: ')
            addr = tmp[1].split()
            addr = addr[0]
        continue
    tmp = pre + 'i2cget -f -y ' + bus + ' ' + addr + ' ' + cols[0] + " " + get_type(cols[2], isuboot)
    tb.eof_write(c, tmp)
    ret = tb.tbot_get_line(c)
    val = ret.strip()
    if (int(val, 16) & int(cols[1], 16)) != (int(cols[3], 16) & int(cols[1], 16)):
        logging.warning("pinmux diff args: %s %s@%s & %s != %s", tb.config.tc_lx_create_i2c_reg_file_name, val, cols[0], cols[1], cols[3])
        #tb.end_tc(False)

tb.gotprompt = True
tb.end_tc(True)
