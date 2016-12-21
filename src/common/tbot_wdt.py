#!/usr/bin/python
#
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
