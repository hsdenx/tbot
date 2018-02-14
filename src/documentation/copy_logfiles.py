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
import os.path
from optparse import OptionParser
import shutil

class copy_logfiles(object):
    """ copy logfiles from idir into odir
        also rename c_cpc into c_ctrl
    """

    def __init__(self, options):
        self.options = options
        self.list_of_files = os.listdir(self.options.idir)
        # print("FILES ", self.list_of_files)
        self.list_of_ofiles = os.listdir(self.options.odir)
        # print("FILES ", self.list_of_ofiles)

    def do_work(self):
        for s in self.list_of_files:
            if 'tb_cpc' in s:
                # print("S ", s)
                t = s.replace('tb_cpc', 'tb_ctrl')
                # print("T ", t)
            else:
                t = s

            t = t.replace('$', '')
            # find t in ofile list
            if t in self.list_of_ofiles:
                # copy file
                # print(" COPY ", self.options.idir + '/' + s, self.options.odir + '/' + t)
                shutil.copy2(self.options.idir + '/' + s, self.options.odir + '/' + t)
            else:
                #print("%s not found in odir %s" % (t, self.options.odir))
                if self.options.force:
                    #print("force")
                    shutil.copy2(self.options.idir + '/' + s, self.options.odir + '/' + t)
                pass

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i", "--idir",
       dest="idir", default="none",
       help="input path")
    parser.add_option("-o", "--odir",
       dest="odir", default="none",
       help="output path")
    parser.add_option("-f", "--force",
       dest="force", default=False,
       action="store_true",
       help="copy files to odir")
    (options, args) = parser.parse_args()

    work = copy_logfiles(options)
    work.do_work()
