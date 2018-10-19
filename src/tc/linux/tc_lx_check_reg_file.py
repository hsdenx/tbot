# SPDX-License-Identifier: GPL-2.0
#
# Description:
# checks if the default values in reg file tb.config.tc_lx_create_reg_file_name
# on the tbot host in tb.workdir have the same values, as the
# registers on the board. Needs devmem2 installed.
# format of the regfile:
# regaddr mask type defval
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
# - tb.config.devmem2_pre
#| path to devmem2 command
#| default: ''
#
# End:

from tbotlib import tbot

logging.info("args: %s", tb.config.tc_lx_create_reg_file_name)
logging.info("args: %s", tb.config.devmem2_pre)

# set board state for which the tc is valid
tb.set_board_state("linux")

pre = ''
if tb.config.devmem2_pre != 'none':
    pre = tb.config.devmem2_pre

c = tb.c_con
fname = tb.workdir + "/" + tb.config.tc_lx_create_reg_file_name
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
        return 'h'
    if t == 'b':
        return 'b'
    logging.error("U-Boot Type %s not implemented.", t)
    tb.end_tc(False)

for line in fd.readlines():
    cols = line.split()
    if cols[0] == '#':
        if 'U-Boot' in line:
            # we have a register dump from U-Boot, so we have
            # to adapt register length marker
            isuboot = 1
        continue
    tmp = pre + 'devmem2 ' + cols[0] + " " + get_type(cols[2], isuboot)
    tb.eof_write(c, tmp)
    ret = tb.tbot_expect_string(c, 'opened')
    if ret == 'prompt':
        tb.end_tc(False)
    sl = ['Value at address', 'Read at address']
    ret = tb.tbot_rup_and_check_strings(c, sl)
    if ret == 'prompt':
        tb.end_tc(False)
    ret = tb.tbot_expect_string(c, '\n')
    if ret == 'prompt':
        tb.end_tc(False)
    tmp = tb.buf.split(":")[1]
    tmp = tmp[1:]
    tmp = tmp.strip()
    tb.tbot_expect_prompt(c)
    if (int(tmp, 16) & int(cols[1], 16)) != (int(cols[3], 16) & int(cols[1], 16)):
        logging.warning("pinmux diff args: %s %s@%s & %s != %s", tb.config.tc_lx_create_reg_file_name, tmp, cols[0], cols[1], cols[3])
        #tb.end_tc(False)

tb.end_tc(True)
