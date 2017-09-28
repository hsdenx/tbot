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
import os, sys
import logging
from optparse import OptionParser
from tbotlib import tbot
import signal

try:
    tb
except:
    parser = OptionParser()
    parser.add_option("-c", "--cfgfile",
           dest="cfgfile", default="none",
           help="the tbot board configfilename")
    parser.add_option("-s", "--slabfile",
           dest="labfile", default="none",
           help="the tbot lab configfilename")
    parser.add_option("-a", "--arguments",
           dest="arguments", default="",
           help="arguments for the testcase")
    parser.add_option("-l", "--logfile",
           dest="logfile", default="default",
           help="the tbot logfilename, if default, tbot creates a defaultnamelogfile")
    parser.add_option("-t", "--testcase",
           dest="tc", default="none",
           help="the testcase which should be run")
    parser.add_option("-v", "--verbose",
           action="store_true", dest="verbose", default=False,
           help="be verbose, print all read/write to stdout")
    parser.add_option("-w", "--workdir",
           dest="workdir", default=os.getcwd(),
           help="set workdir, default os.getcwd()")
    (options, args) = parser.parse_args()
    print("**** option lab: %s cfg: %s log: %s tc: %s v %d a %s" % (options.labfile, options.cfgfile, options.logfile, options.tc, options.verbose, options.arguments))
    tb = tbot(options.workdir, options.labfile, options.cfgfile, options.logfile, options.verbose, options.arguments)

def signal_term_handler(signal, frame):
    print ("GOT signal ", tb)
    tb.log.error("WDT Timeout")
    tb.end_tc(False)

signal.signal(signal.SIGTERM, signal_term_handler)

tb.starttestcase = options.tc
ret = tb.call_tc(options.tc)
if ret == False:
    tb.end_tc(False)

tb.end_tc(True)
