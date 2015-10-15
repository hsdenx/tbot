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

try:
    tb
except:
    parser = OptionParser()
    parser.add_option("-c", "--cfgfile",
           dest="cfgfile", default="none",
           help="the tbot common configfilename")
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
    print("**** option cfg: %s log: %s tc: %s v %d" % (options.cfgfile, options.logfile, options.tc, options.verbose))
    tb = tbot(options.workdir, options.cfgfile, options.logfile, options.verbose)

ret = tb.call_tc(options.tc)
if ret == False:
    tb.end_tc(False)

tb.end_tc(True)
