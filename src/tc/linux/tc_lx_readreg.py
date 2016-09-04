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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_readreg.py
# read with devmem2 a register in linux
# readaddr: tb.tc_lx_readreg_addr
# tb.tc_lx_readreg_type: access operation type : [b]yte, [h]alfword, [w]ord
# mask it with tb.tc_lx_readreg_mask
# and compare it with tb.tc_lx_readreg_value
# if it is the same tc is True
# else eof
#end:

from tbotlib import tbot

logging.info("args: %s %s %s %s", tb.tc_lx_readreg_addr, tb.tc_lx_readreg_mask,
             tb.tc_lx_readreg_type, tb.tc_lx_readreg_value)

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.c_con
tmp = 'devmem2 ' + tb.tc_lx_readreg_addr + " " + tb.tc_lx_readreg_type
tb.eof_write(c, tmp)

# read register value
ret = tb_tbot_expect_string(c, 'opened')
if ret = 'prompt':
    tb.end_tc(False)
ret = tb_tbot_expect_string(c, 'Value at address')
if ret = 'prompt':
    tb.end_tc(False)
tmp = self.buf.split(":")[1]
tmp = tmp[1:]
logging.debug("args: readval: %s masked: %x == %x", tmp, int(tmp, 16) & int(tb.tc_lx_readreg_mask, 16), int(tb.tc_lx_readreg_value, 16))
tb_tbot_expect_prompt(c)

if (int(tmp, 16) & int(tb.tc_lx_readreg_mask, 16)) != int(tb.tc_lx_readreg_value, 16):
    tb.end_tc(False)

tb.end_tc(True)
