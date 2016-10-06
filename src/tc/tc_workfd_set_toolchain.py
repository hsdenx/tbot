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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_set_toolchain.py
# set the toolchain, dependend on the architecture setting in
# tb.tc_workfd_set_toolchain_arch
# supported toolchains defined in
# tb.tc_workfd_set_toolchain_t_p and tb.tc_workfd_set_toolchain_cr_co
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.workfd.name, tb.tc_workfd_set_toolchain_arch)

c = tb.workfd

try:
    tb.tc_workfd_set_toolchain_t_p
except:
    logging.error("tb.tc_workfd_set_toolchain_t_p not set")
    tb.end_tc(False)

try:
    tb.tc_workfd_set_toolchain_cr_co
except:
    logging.error("tb.tc_workfd_set_toolchain_cr_co not set")
    tb.end_tc(False)

if tb.tc_workfd_set_toolchain_arch in tb.tc_workfd_set_toolchain_t_p:
    path = tb.tc_workfd_set_toolchain_t_p[tb.tc_workfd_set_toolchain_arch]
else:
    logging.error("args: %s unknown architecture %s", tb.workfd.name, tb.tc_workfd_set_toolchain_arch)
    tb.end_tc(False)

if tb.tc_workfd_set_toolchain_arch in tb.tc_workfd_set_toolchain_cr_co:
    cross = tb.tc_workfd_set_toolchain_cr_co[tb.tc_workfd_set_toolchain_arch]
else:
    logging.error("args: %s unknown architecture %s", tb.workfd.name, tb.tc_workfd_set_toolchain_arch)
    tb.end_tc(False)

if tb.tc_workfd_set_toolchain_arch == 'sandbox':
    tmp = 'export PATH=/bin:$PATH'
    tb.event.create_event('main', tb.boardname, "Toolchain", tmp)
    tb.eof_write_cmd(c, tmp)
    tb.end_tc(True)

tmp = "printenv PATH | grep --color=never " + path
ret = tb.write_lx_cmd_check(c, tmp, endTC=False)
if ret == False:
    tmp = 'export PATH=' + path + ':$PATH'
    tb.event.create_event('main', tb.boardname, "Toolchain", path)
    tb.eof_write_cmd(c, tmp)

tmp = 'export CROSS_COMPILE=' + cross
tb.eof_write_cmd(c, tmp)
tb.end_tc(True)
