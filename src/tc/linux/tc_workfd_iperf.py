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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_iperf.py
#
# make a minimal iperf check
# starts an iperf server on tb.tc_workfd_c_sr connection
#   with ip addr tb.tc_workfd_iperf_sip
# starts an iperf "slave" on tb.tc_workfd_c_sl
# waiting for the first result of iperf measure and
# check if the resulting speed is bigger then
# tb.config.tc_workfd_iperf_minval
#
# if you have not the iperf cmd instead iperf 3, you can
# set
# tb.config.tc_workfd_c_sr_vers or tb.config.tc_workfd_c_sl_vers
# to '3'
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_c_sr_vers
except:
    tb.config.tc_workfd_c_sr_vers = ''

try:
    tb.config.tc_workfd_c_sl_vers
except:
    tb.config.tc_workfd_c_sl_vers = ''

logging.info("args: workfd %s %s %s %s", tb.tc_workfd_c_sr.name, tb.tc_workfd_c_sl.name, tb.tc_workfd_iperf_sip, tb.config.tc_workfd_iperf_minval)
logging.info("args: %s %s", tb.config.tc_workfd_c_sr_vers, tb.config.tc_workfd_c_sl_vers)

tb.set_board_state("linux")

c_s = tb.tc_workfd_c_sr
c_t = tb.tc_workfd_c_sl

cmd_sr = 'iperf' + tb.config.tc_workfd_c_sr_vers + ' -s'
cmd_sl = 'iperf' + tb.config.tc_workfd_c_sl_vers + ' -c ' + tb.tc_workfd_iperf_sip

tb.eof_write(c_s, cmd_sr)
searchlist = ["Server listening", "TCP window size"]
s_st = False
tmp = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c_s, searchlist)
    if tb.config.tc_workfd_c_sr_vers == '3':
        if ret == '0':
            tmp = False
            s_st = True
    if ret == '1':
        tmp = False
        s_st = True
    elif ret == 'prompt':
        tmp = False

if s_st != True:
    tb.end_tc(False)

tb.eof_write(c_t, cmd_sl)
if tb.config.tc_workfd_c_sl_vers == '3':
    searchlist = ["connected", "Bandwidth", "\n"]
else:
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
        if tb.config.tc_workfd_c_sl_vers == '3':
            timestring = '0.00-10.00'
        else:
            timestring = '0.0-10.0'

        if tmp2[2] == timestring:
            val = float(tmp2[6])
            if val > tb.config.tc_workfd_iperf_minval:
                result = True
    elif ret == 'prompt':
        tmp = False

tb.send_ctrl_c(c_s)
c_s.expect_prompt()

if result != True:
    tb.end_tc(False)
tb.end_tc(True)
