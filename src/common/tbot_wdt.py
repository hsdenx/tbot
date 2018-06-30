#!/usr/bin/python
#
# SPDX-License-Identifier: GPL-2.0
#
import os, sys, signal
import time

# ToDo add logging

wdtfile = sys.argv[1]
master_pid = int(sys.argv[2])
logfilename = sys.argv[3]
timeout = int(sys.argv[4])

if timeout == 0:
    sys.exit(0)

try:
    fd = open(wdtfile, 'r')
except IOError:
    sys.exit(1)

run = True
while run:
    time.sleep(1)
    try:
        fd = open(wdtfile, 'r')
    except IOError:
        sys.exit(1)
    fd.seek(0, 0)
    line = fd.readline()
    if line == '':
        continue
    oldvalue = int(line.strip())
    newvalue = int(time.time())
    if newvalue > oldvalue + timeout:
        print("************ WDT Timeout")
        os.kill(master_pid, signal.SIGTERM) #or signal.SIGKILL 
        run = False
    fd.close()
