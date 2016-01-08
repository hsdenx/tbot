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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_date.py
# convert duts tests from:
# http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootDate.tc;h=03b7d53fd93bd61381db4095a4bff58b1d1efff7;hb=101ddd5dbd547d5046363358d560149d873b238a
from tbotlib import tbot
from time import gmtime, strftime

#set board state for which the tc is valid
tb.set_board_state("u-boot")

ret = tb.write_cmd_check(tb.channel_con, "help date", "Unknown command")
if ret == True:
    tb.end_tc(True)

tb.eof_write_cmd(tb.channel_con, "date reset")
time=strftime("%m%d%H%M%Y.%S", gmtime())
tb.eof_write_cmd(tb.channel_con, "date " + time)
tb.eof_write_cmd_check(tb.channel_con, "date", "Date:")

tb.end_tc(True)
