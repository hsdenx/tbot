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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_tftp_file.py

from tbotlib import tbot

#here starts the real test
logging.info("u-boot tftp testcase")
#set board state for which the tc is valid
tb.set_board_state("u-boot")

# set necessary u-boot env variables
# just a demo of call_tc.pc testcase, you could of course
# build the complete command string for tftp
# and send it to the board ...
tb.setenv_name = 'tftp_addr_r'
tb.setenv_value = tb.tftp_addr_r
tb.eof_call_tc('tc_ub_setenv.py')
tb.setenv_name = 'tftp_file'
tb.setenv_value = tb.tftp_file
tb.eof_call_tc('tc_ub_setenv.py')

tb.eof_write_con('tftp ${tftp_addr_r} ${tftp_file}')
ret = tb.wait_answer(tb.channel_con, 'Bytes', 30)
if ret == False:
    tb.end_tc(False)
tb.eof_read_end_state_con(2)
tb.end_tc(True)
