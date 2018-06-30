# SPDX-License-Identifier: GPL-2.0
#
# Description:
# checks if the default values in reg file tb.config.tc_ub_create_reg_file_name
# on the tbot host in tb.workdir have the same values, as the
# registers on the board
# format of the regfile:
# regaddr mask type defval
# ToDo: use the file from the lab host, not the tbot host
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_create_reg_file_name', '')

# set board state for which the tc is valid
tb.set_board_state("u-boot")

c = tb.c_con
fname = tb.workdir + "/" + tb.config.tc_ub_create_reg_file_name
try:
    fd = open(fname, 'r')
except IOError:
    logging.warning("Could not open: %s", fname)
    tb.end_tc(False)

retval = True
for line in fd.readlines():
    cols = line.split()
    if cols[0] == '#':
        continue
    val = cols[0]
    tmp = 'md.'+ cols[2] + ' ' + val + ' 1'
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
        logging.warn("args: %s %s %s & %s != %s", tb.config.tc_ub_create_reg_file_name, cols[0], val, cols[1], cols[3])
        retval = False

tb.end_tc(retval)
