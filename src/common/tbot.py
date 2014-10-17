# start with
# python2.7 common/tbot.py tbot.cfg default tc/tc_call.py

import os, sys
import logging
import argparse
sys.path.append("./tc")
sys.path.append("./lab_api")
from tbotlib import tbot

try:
    tb
except:
    parser = argparse.ArgumentParser()
    parser.add_argument("cfgfile", help="the tbot common configfilename")
    parser.add_argument("logfile", help="the tbot logfilename, if default, tbot creates a defaultnamelogfile")
    parser.add_argument("tc", help="the testcase which should be run")
    args = parser.parse_args()
    tb = tbot(args.cfgfile, args.logfile)

ret = tb.call_tc(args.tc)
if ret == False:
    tb.end_tc(False)

tb.end_tc(True)
