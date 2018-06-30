# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_create_reg_file.py
# creates a reg file tb.tc_ub_create_reg_file_name on the tbot host
# in tb.workdir
# read from tb.tc_ub_create_reg_file_start to tb.tc_ub_create_reg_file_stop
# and writes the results in the regfile tb.tc_ub_create_reg_file_name
# format of the regfile:
# regaddr mask type defval
# This reg file can be used as a default file, how the
# registers must be setup, check it with testcase
# tc_ub_check_reg_file.py
# ToDo: use the file from the lab host, not the tbot host
# End:

import datetime
from tbotlib import tbot

logging.info("args: %s %s %s %s %s %s %s", tb.config.tc_ub_create_reg_file_name,
             tb.config.tc_ub_create_reg_file_start,
             tb.config.tc_ub_create_reg_file_stop,
             tb.config.tc_ub_readreg_mask, tb.config.tc_ub_readreg_type,
             tb.config.tc_ub_create_reg_file_mode, tb.config.tc_ub_create_reg_file_comment)

#set board state for which the tc is valid
tb.set_board_state("u-boot")

fname = tb.workdir + "/" + tb.config.tc_ub_create_reg_file_name
try:
    fd = open(fname, tb.config.tc_ub_create_reg_file_mode)
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

if tb.config.tc_ub_create_reg_file_comment != '':
    fd.write('# ' + tb.config.tc_ub_create_reg_file_comment + '\n')
fd.write("# Date: " + datetime.datetime.now().ctime() + "\n")
fd.write("# U-Boot    : %s\n" % vers)
fd.write("# regaddr mask type defval\n")


#read from - to
tb.config.tc_ub_readreg_mask = '0xffffffff'
start = int(tb.config.tc_ub_create_reg_file_start, 16)
stop = int(tb.config.tc_ub_create_reg_file_stop, 16)

if tb.config.tc_ub_readreg_type == 'l':
    step = 4
if tb.config.tc_ub_readreg_type == 'w':
    step = 2
if tb.config.tc_ub_readreg_type == 'b':
    step = 1

#read register value
for i in xrange(start, stop, step):
    val = str(hex(i))
    tmp = 'md.' + tb.config.tc_ub_readreg_type + " " + val + ' 1'
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
    fd.write('%-10s %10s %10s %10s\n' % (hex(i), tb.config.tc_ub_readreg_mask, tb.config.tc_ub_readreg_type, val))

fd.close()
tb.end_tc(True)
