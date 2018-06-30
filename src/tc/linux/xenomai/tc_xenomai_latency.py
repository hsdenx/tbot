# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# start latency command tb.config.tc_xenomai_latency_lcmd from the xenomai
# tools. Use paramter -g for creating histogram to file
# tb.config.tc_xenomai_latency_tmpfile in gnuplot format.
# Save this file into tb.config.tc_xenomai_latency_datfile2
# on the lab PC.
#
# While latency test is running, extract the content of the
# line starting with "RTD" into the file
# tb.config.tc_xenomai_latency_datfile
#
# This testcase runs the latency tool until tb.config.tc_xenomai_latency_count
# lines are read. While running it checks if the value
# of the column "lat max" is lower than tb.config.tc_xenomai_latency_max
# Than this testcase ends with True, else Testcase ends with False.
# 
# At the end of this tetscase, it creates the png images
# of the files tb.config.tc_xenomai_latency_datfile
# and tb.config.tc_xenomai_latency_datfile2 on the host PC
# using gnuplot tool.
#
# Therefore the files
# src/files/balkenplot_lat_tbot.sem
# src/files/balkenplot_latency.sem
# are used.
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_xenomai_latency_lcmd
except:
    tb.config.tc_xenomai_latency_lcmd = '/usr/xenomai/bin/latency'

try:
    tb.config.tc_xenomai_latency_tmpfile
except:
    tb.config.tc_xenomai_latency_tmpfile = '/tmp/latency.dat'

try:
    tb.config.tc_xenomai_latency_datfile
except:
    tb.config.tc_xenomai_latency_datfile = 'lat_tbot.dat'

try:
    tb.config.tc_xenomai_latency_datfile2
except:
    tb.config.tc_xenomai_latency_datfile2 = 'latency_tbot.dat'

try:
    tb.config.tc_xenomai_latency_count
except:
    tb.config.tc_xenomai_latency_count = '100'

try:
    tb.config.tc_xenomai_latency_max
except:
    tb.config.tc_xenomai_latency_max = '42'

try:
    tb.config.tc_xenomai_latency_opt
except:
    tb.config.tc_xenomai_latency_opt = ''

logging.info("arg: %s cmd: %s", tb.workfd.name, tb.config.tc_xenomai_latency_lcmd)
logging.info("arg: tmpfile: %s", tb.config.tc_xenomai_latency_tmpfile)
logging.info("arg: datfile: %s", tb.config.tc_xenomai_latency_datfile)
logging.info("arg: datfile2: %s", tb.config.tc_xenomai_latency_datfile2)
logging.info("arg: count: %s", tb.config.tc_xenomai_latency_count)
logging.info("arg: max: %s", tb.config.tc_xenomai_latency_max)
logging.info("arg: opt: %s", tb.config.tc_xenomai_latency_opt)

tb.set_board_state("linux")
save = tb.workfd
tb.workfd = tb.c_con
c = tb.workfd
tb.config.tc_workfd_check_if_cmd_exist_cmdname = tb.config.tc_xenomai_latency_lcmd
tb.eof_call_tc("tc_workfd_check_if_cmd_exist.py")

cmd = tb.config.tc_xenomai_latency_lcmd
if tb.config.tc_xenomai_latency_tmpfile != '':
    cmd += ' -g ' + tb.config.tc_xenomai_latency_tmpfile

if tb.config.tc_xenomai_latency_opt != '':
    cmd += ' ' + tb.config.tc_xenomai_latency_opt

tb.eof_write(c, cmd)

# RTT|  00:00:01  (periodic user-mode task, 1000 us period, priority 99)
# RTH|----lat min|----lat avg|----lat max|-overrun|---msw|---lat best|--lat worst
# RTD|     11.458|     16.702|     39.250|       0|     0|     11.458|     39.250
rtd_format = 'RTD\|{min}\|{avg}\|{max}\|{overrun}\|{msw}\|{best}\|{worst}\r\n'

loop = True
count = 0
rtd = []
result = True
once = 0
while loop == True:
    ret = tb.tbot_get_line(c)
    if ret != '':
        # Type of line
        # we are interested in "RTD" lines only
        if 'RTD' in ret:
            rtd_dict = tb.string_to_dict(ret, rtd_format)
            rtd.append(rtd_dict)
            if float(tb.config.tc_xenomai_latency_max) < float(rtd_dict['max']):
                logging.error("latency max too bad: %s > %s", rtd_dict['max'], tb.config.tc_xenomai_latency_max)
                result = False
            if float(rtd_dict['overrun']) != 0:
                logging.error("overrun ", float(rtd_dict['overrun']))
                result = False

            count = count + 1
            
        # check end
        if int(tb.config.tc_xenomai_latency_count) < count:
            # Send Ctrl-C
            if once == 0:
                tb.send_ctrl_c(c)
                once = 1
    else:
        # got prompt -> end
        loop = False

max_count = count
df = tb.resultdir + '/' + tb.config.tc_xenomai_latency_datfile
fd = open(df, 'w')
fd.write('step lat_min lat_avg lat_max overrun msw lat_best lat_worst\n')
count = 0
while (count < max_count):
    d = rtd[count]
    fd.write("%d %s %s %s %s %s %s %s\n" %(count, d['min'], d['avg'], d['max'], d['overrun'], d['msw'], d['best'], d['worst']))
    count = count + 1
fd.close()

if df != '':
    loc = tb.resultdir + '/' + os.path.basename(df) + tb.config.tc_xenomai_latency_opt.replace(' ', '_') + '.loc'
    cmd = 'rm -rf ' + loc
    os.system(cmd)
    print("CMD ", cmd)
    tb.c_ctrl.copy_file(df, loc)
    of = tb.resultdir + '/lat_tbot' + tb.config.tc_xenomai_latency_opt.replace(' ', '_') + '.png'
    cmd = 'gnuplot -e \'input_file="' + loc + '";output_file="' + of + '";graph_title="' + tb.config.boardname + ' latency statistic"\' ' + tb.workdir + '/src/files/balkenplot_lat_tbot.sem'
    os.system(cmd)

if tb.config.tc_xenomai_latency_datfile2 != '':
    of = tb.resultdir + '/' + tb.config.tc_xenomai_latency_datfile2
    fd = open(of, 'w')
    cmd = 'cat ' + tb.config.tc_xenomai_latency_tmpfile
    tb.eof_write(c, cmd)
    loop = True
    while loop == True:
        ret = tb.tbot_get_line(c)
        if ret != '':
            fd.write(ret)
        else:
            # got prompt -> end
            loop = False
    fd.close()

    # create png files (on host!)
    loc = tb.resultdir + '/' + os.path.basename(of) + tb.config.tc_xenomai_latency_opt.replace(' ', '_') + '.loc'
    cmd = 'rm -rf ' + loc
    os.system(cmd)
    tb.c_ctrl.copy_file(of, loc)
    oft = tb.resultdir + '/latency' + tb.config.tc_xenomai_latency_opt.replace(' ', '_') + '.png'
    cmd = 'gnuplot -e \'input_file="' + loc + '";output_file="' + oft + '";graph_title="' + tb.config.boardname + ' latency"\' ' + tb.workdir + '/src/files/balkenplot_latency.sem'
    os.system(cmd)

tb.workfd = save
tb.end_tc(result)
