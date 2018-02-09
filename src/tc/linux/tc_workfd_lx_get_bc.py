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
# get in linux bootcount value
# if not found testcases end with failure
# value returned in var tb.lx_bc
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_lx_get_bc_file
except:
    tb.config.tc_workfd_lx_get_bc_file = '/sys/devices/soc0/soc/2100000.aips-bus/21a0000.i2c/i2c-0/0-0008/bootcount'

logging.info("args: workfd %s %s", tb.workfd.name, tb.config.tc_workfd_lx_get_bc_file)

tb.set_board_state("linux")
c = tb.workfd
tb.eof_write_cmd_get_line(c, "cat " + tb.config.tc_workfd_lx_get_bc_file)

tb.lx_bc = tb.ret_write_cmd_get_line
tb.lx_bc = tb.lx_bc.replace('\r\n', '')

logging.info("args: linux bc value: %s", tb.lx_bc)
tb.end_tc(True)
