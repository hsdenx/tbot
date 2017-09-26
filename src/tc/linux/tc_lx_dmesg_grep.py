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
#
# check if string tb.config.tc_lx_dmesg_grep_name is in dmesg output.
# make the grep options configurable through tb.config.tc_lx_dmesg_grep_options
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_lx_dmesg_grep_options
except:
    tb.config.tc_lx_dmesg_grep_options = '--color=never'

# here starts the real test
logging.info("args: %s %s", tb.config.tc_lx_dmesg_grep_name, tb.config.tc_lx_dmesg_grep_options)

tb.workfd = tb.c_con
c = tb.workfd
# set board state for which the tc is valid
tb.set_board_state("linux")

tmp = 'dmesg | grep ' + tb.config.tc_lx_dmesg_grep_options + ' \'' + tb.config.tc_lx_dmesg_grep_name + '\''
tb.eof_write(c, tmp)
tb.tbot_expect_prompt(c)
#tb.eof_expect_string(c, tb.config.tc_lx_dmesg_grep_name)
tb.eof_call_tc("tc_workfd_check_cmd_success.py")
tb.end_tc(True)
