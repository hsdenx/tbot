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
# python2.7 src/common/tbot.py -c tbot_zug.cfg -t tc_bmp.py
#ToDo: rework tc

from tbotlib import tbot

#here starts the real test
logging.info("u-boot bmp testcase")
#set board state for which the tc is valid
tb.set_board_state("u-boot")

ret = tb.write_stream("setenv tc_addr " + tb.ub_bmp_addr)
if not ret:
    tb.end_tc(False)

ret = tb.write_stream("setenv tc_file " + tb.ub_bmp_file)
if not ret:
    tb.end_tc(False)

ret = tb.call_tc("tc_ub_tftp_file.py")
if ret == False:
    tb.end_tc(False)

ret = tb.write_stream("bmp info ${tc_addr}")
if not ret:
    tb.end_tc(False)
ret = tb.wait_answer('Compression', 30)
if ret == False:
    tb.end_tc(False)
ret = tb.read_end_state(2)
if ret == False:
    tb.end_tc(False)

ret = tb.write_stream("bmp display ${tc_addr} 10 10")
if not ret:
    tb.end_tc(False)

tb.end_tc(True)
