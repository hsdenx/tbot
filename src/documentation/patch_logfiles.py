#!/usr/bin/python
#
# SPDX-License-Identifier: GPL-2.0
#

import os, sys
import os.path
from optparse import OptionParser
import shutil

class patch_logfiles(object):
    """ patch logfiles in idir
    """

    def __init__(self, options):
        self.options = options
        self.list_of_files = os.listdir(self.options.idir)
        # print("FILES ", self.list_of_files)

    def do_work(self):
        print("DIR", self.options.idir)
        for s in self.list_of_files:
            if 'loadb_send_file_tb_con' in s:
                print("S ", s)
                # ansi2txt removes the "send... line"
                # Fix this
                # open file and search line with "C-Kermit>send /protocol="
                fd = open (self.options.idir + "/" + s, 'r')
                if not fd:
                    print("Could not open ", self.options.idir, s)
                # remove ^M from this line
                i = 1
                nl = ''
                for line in fd:
                    if "C-Kermit>send /protocol=" in line:
                        line = line.replace('\r', '')
                    if "C-Kermit 9.0.302 OPEN SOURCE:, 20 Aug 2011, raspberrypitbot2go" in line:
                        pos = line.find("C-Kermit 9.0.302 OPEN SOURCE:, 20 Aug 2011, raspberrypitbot2go")
                        line = line[pos:]
                    nl += line
                    i = i + 1
                fd.close()
                fd = open (self.options.idir + "/" + s, 'w')
                if not fd:
                    print("Could not open for write", self.options.idir, s)
                fd.write(nl)
                fd.close()

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i", "--idir",
       dest="idir", default="none",
       help="input path")
    (options, args) = parser.parse_args()

    work = patch_logfiles(options)
    work.do_work()
