# SPDX-License-Identifier: GPL-2.0
#
# Description:
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
#
# used variables
#
# - tb.config.tc_workfd_c_sr
#| tbot connection where iperf server is started
#| default: ''
#
# - tb.config.tc_workfd_c_sl
#| tbot connection where iperf slave is started
#| default: ''
#| default: ''
#
# - tb.config.tc_workfd_iperf_sip
#| iperf server ip used for iperf slave
#| default: ''
#
# - tb.config.tc_workfd_iperf_minval
#| if iperf result is greater than tb.config.tc_workfd_iperf_minval
#| testcase tc_workfd_iperf.py returns True
#| default: ''
#
# - tb.config.tc_workfd_c_sr_vers
#| iperf version
#| default: ''
#
# - tb.config.tc_workfd_c_sl_vers
#| iperf version
#| default: ''
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_c_sr', '')
tb.define_variable('tc_workfd_c_sl', '')
tb.define_variable('tc_workfd_iperf_sip', '')
tb.define_variable('tc_workfd_iperf_minval', '')
tb.define_variable('tc_workfd_c_sr_vers', '')
tb.define_variable('tc_workfd_c_sl_vers', '')

logging.info("args: workfd %s %s", tb.config.tc_workfd_c_sr.name, tb.config.tc_workfd_c_sl.name)

tb.set_board_state("linux")

c_s = tb.config.tc_workfd_c_sr
c_t = tb.config.tc_workfd_c_sl

cmd_sr = 'iperf' + tb.config.tc_workfd_c_sr_vers + ' -s'
cmd_sl = 'iperf' + tb.config.tc_workfd_c_sl_vers + ' -c ' + tb.config.tc_workfd_iperf_sip

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
