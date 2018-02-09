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
# get in uboot bootcount value
# if not found testcases end with failure
# value returned in var tb.ub_bc
# End:

from tbotlib import tbot

tb.set_board_state("u-boot")
c = tb.workfd
tb.eof_write_cmd_get_line(c, "printenv bootcount")

tb.ub_bc = 'not found'
if 'bootcount' in tb.ret_write_cmd_get_line:
    tmp = tb.ret_write_cmd_get_line.split('=')
    tb.ub_bc = tmp[1]
    tb.ub_bc = tb.ub_bc.replace('\r\n', '')

logging.info("args: u-boot bc value: %s", tb.ub_bc)
tb.end_tc(True)
