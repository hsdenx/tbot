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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_iperf.py
# make a minimal iperf check
# starts an iperf server on tb.tc_workfd_c_sr connection
#   with ip addr tb.tc_workfd_iperf_sip
# starts an iperf "slave" on tb.tc_workfd_c_sl
# waiting for the first result of iperf measure and
# check if the resulting speed is bigger then
# tb.tc_workfd_iperf_minval
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s %s %s", tb.tc_workfd_c_sr.name, tb.tc_workfd_c_sl.name, tb.tc_workfd_iperf_sip, tb.tc_workfd_iperf_minval)

tb.set_board_state("linux")

c_s = tb.tc_workfd_c_sr
c_t = tb.tc_workfd_c_sl

cmd = 'iperf -s'
cmd_sl = 'iperf -c ' + tb.tc_workfd_iperf_sip

tb.eof_write(c_s, cmd)
searchlist = ["Server listening", "TCP window size"]
s_st = False
tmp = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c_s, searchlist)
    if ret == '1':
        tmp = False
        s_st = True
    elif ret == 'prompt':
        tmp = False

if s_st != True:
    tb.end_tc(False)

tb.eof_write(c_t, cmd_sl)
searchlist = ["connected with", "Bandwidth", "\n"]
got_line = False
result = False
tmp = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c_t, searchlist)
    if ret == '1':
        got_line = True
    if ret == '2':
        if got_line == False:
            continue

        if tb.buf.find("sec") == -1:
            continue

        tmp2 = tb.buf.split()
        if len(tmp2) < 8:
            continue
        if tmp2[2] == '0.0-10.0':
            val = float(tmp2[6])
            if val > tb.tc_workfd_iperf_minval:
                result = True
    elif ret == 'prompt':
        tmp = False

tb.send_ctrl_c(c_s)
c_s.expect_prompt()

if result != True:
    tb.end_tc(False)
tb.end_tc(True)
