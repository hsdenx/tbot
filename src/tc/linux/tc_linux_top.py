# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# This testcase starts the linux "top" command
# with the top cmdline arguments tb.config.tc_linux_top_count
# and tb.config.tc_linux_top_sec
#
# and analyses the output and write them into the file
# tb.config.tc_linux_top_filename in a gnuplot format.
#
# create the images with gnuplot:
#
# gnuplot src/files/top_plot_mem.sem
# result image
# top-mem-output.jpg
# gnuplot src/files/top_plot_cpu.sem
# result image
# top-cpu-output.jpg
# gnuplot src/files/top_plot_load.sem
# result image
# top-load-output.jpg
#
# !! may you need to adapt path in src/files/top_plot*.sem files
# ToDo: pass paramter workdir to gnuplot
#
# While at it, include a demo for adding it to the dashboard
# backend and create a demo documentation.
#
# If you use this testcase in conjunction with other testcases
# you should remove the line
# tb.config.create_documentation_auto = 'linux_top'
#
# used variables
#
# - tb.config.tc_linux_top_count
#| top count argument
#| default: '10'
#
# - tb.config.tc_linux_top_sec
#| top seconds argument
#| default: '2'
#
# - tb.config.tc_linux_top_filename
#| filename where the results are stored
#| default: 'top-stat.dat'
#
#
# End:

from tbotlib import tbot
import re

tb.define_variable('tc_linux_top_count', '100')
tb.define_variable('tc_linux_top_sec', '2')
tb.define_variable('tc_linux_top_filename', 'top-stat.dat')

logging.info("arg: %s", tb.workfd.name)

self.event.create_event('main', self.config.boardname, "DUTS_LINUX_TOP_COUNT", tb.config.tc_linux_top_count)
self.event.create_event('main', self.config.boardname, "DUTS_LINUX_TOP_SEC", tb.config.tc_linux_top_sec)

def tbot_get_line(tb, c):
    ret = tb.tbot_rup_and_check_strings(c, '\n')
    if ret == 'prompt':
        tb.enc_tc(False)
    return tb.buf

def string_to_dict(string, pattern):
    regex = re.sub(r'{(.+?)}', r'(?P<_\1>.+)', pattern)
    values = list(re.search(regex, string).groups())
    keys = re.findall(r'{(.+?)}', pattern)
    _dict = dict(zip(keys, values))
    return _dict

# tbot.py -s lab_tbot2go -c beagleboneblack-yocto -t tc_linux_top.py -l log/tbot_bb_tc_top.log -v -w /home/pi/tbot2go/tbot

tb.config.bbb_check_crng_init = 'no'
tb.config.create_documentation_auto = 'linux_top'

tb.set_board_state("linux")

c = tb.workfd
cmd = 'top -n' + tb.config.tc_linux_top_count + ' -d' + tb.config.tc_linux_top_sec
tb.eof_write(c, cmd)
s = ['Mem:', 'CPU:', 'Load average:']
mem = []
cpu = []
load = []
loop = True
while loop == True:
    ret = tb.tbot_rup_and_check_strings(c, s)
    if ret == '0':
        # Mem: 26504K used, 477812K free, 144K shrd, 2340K buff, 7872K cached
        tmp = tbot_get_line(tb, c)
        format = '{used} used, {free} free, {shrd} shrd, {buff} buff, {cached} cached'
        dict = string_to_dict(tmp, format)
        mem.append(dict)
        self.tbot_trigger_wdt()
    elif ret == '1':
        #CPU:   0% usr   0% sys   0% nic  99% idle   0% io   0% irq   0% sirq
        tmp = tbot_get_line(tb, c)
        format = '{usr}% usr {sys}% sys {nic}% nic {idle}% idle {io}% io {irq}% irq {sirq}% sirq'
        dict = string_to_dict(tmp, format)
        cpu.append(dict)
    elif ret == '2':
        #Load average: 0.00 0.00 0.00 1/69 495
        tmp = tbot_get_line(tb, c)
        format = '{l1} {l5} {l20} {d1} {d2}'
        dict = string_to_dict(tmp, format)
        load.append(dict)
    elif ret == 'prompt':
        loop = False
    else:
        print("uncatched return ", ret)

# create file
step = int(tb.config.tc_linux_top_sec)
start = 0
count = 0
max = int(tb.config.tc_linux_top_count)

# write values into file
fd = open(tb.workdir + '/' + tb.config.tc_linux_top_filename, 'w')
fd.write('time mem_used mem_free mem_shrd mem_buff mem_cached cpu_usr cpu_sys cpu_nic cpu_idle cpu_io cpu_irq cpu_sirq load_l1 load_l5 load_l20\n')
while (count < max):
    m = mem[count]
    cp = cpu[count]
    l = load[count]
    fd.write("%d %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n" %(
	start, m['used'], m['free'], m['shrd'], m['buff'], m['cached'],
        cp['usr'], cp['sys'], cp['nic'], cp['idle'], cp['io'], cp['irq'], cp['sirq'],
        l['l1'], l['l5'], l['l20']
	))
    count += 1
    start += step

fd.close()

tb.end_tc(True)
