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
# Test U-Boot / Linux bootcounter functionality
# - go into U-Boot
# - get bootcounter value
# - reset
# - get bootcounter value (must be previous + 1)
# - reset
# - get bootcounter value (must be previous + 1)
# - boot linux
# - get bootcounter value (must be the same as in U-Boot)
# - set bootcounter value in linux
# - power off the board
# - power on the board
# - go into U-Boot
# - get bootcounter value (must be +1 the value set in linux)
# - power off the board
# - power on the board
# - go into U-Boot
# - get bootcounter value (must be 1)

# End:

from tbotlib import tbot

tb.config.ub_boot_linux_cmd = 'run bootcmd'
tb.config.state_linux_timeout = 20

tb.eof_call_tc("tc_ub_get_bc.py")
old = tb.ub_bc
tb.eof_call_tc("tc_ub_reset.py")
tb.eof_call_tc("tc_ub_get_bc.py")
val = tb.ub_bc
if int(val) != int(old) + 1:
    logging.warn("args: u-boot bc val after reset not OK %s != %s + 1", val, old)
    tb.end_tc(False)

old = val
tb.eof_call_tc("tc_ub_reset.py")
tb.eof_call_tc("tc_ub_get_bc.py")
val = tb.ub_bc
if int(val) != int(old) + 1:
    logging.warn("args: u-boot bc val after reset not OK %s != %s + 1", val, old)
    tb.end_tc(False)

tb.eof_call_tc("tc_workfd_lx_get_bc.py")
if int(tb.lx_bc) != int(tb.config.tc_set_bc_val):
    logging.warn("args: linux bc %s != u-boot bc %s", tb.lx_bc, tb.config.tc_set_bc_val)
    tb.end_tc(False)

tb.lx_bc = '4'
tb.eof_call_tc("tc_workfd_lx_set_bc.py")
tb.eof_call_tc("tc_ub_get_bc.py")
if int(tb.ub_bc) != int(tb.lx_bc) + 1:
    logging.warn("args: linux bc %s  + 1 != u-boot bc %s", tb.lx_bc, tb.ub_bc)
    tb.end_tc(False)

tb.eof_call_tc("tc_lab_poweroff.py")
time.sleep(2)
tb.eof_call_tc("tc_ub_get_bc.py")
if int(tb.ub_bc) != 1:
    logging.warn("args: u-boot bc val after reset must be 1 is %s", tb.ub_bc)
    tb.end_tc(False)

tb.end_tc(True)
