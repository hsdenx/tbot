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
# search the input file for "tbot_ref:" markers
# and search for the filename in the tcpath
# replace the marker with the content of the
# filename it refers. Write the new file to
# the outputfile
# 
import os, sys
import os.path
from optparse import OptionParser
import textwrap

class replace_tbot_marker(object):
    """ replace tbot markers
    """

    def __init__(self, options):
        self.options = options
        self.searchstring = 'tbot_ref:'
        self.searchstring_only = 'only::'
        self.searchstring_only_end = 'only_end::'
        self.searchstring_include = 'include::'
        self.list_of_files = []

        self.delete_list = ['\x1b[01;31m\x1b[K',
                            ' \x1b[m\x1b[K',
                            '\x1b[1;34m[\x1b[1;32m',
                            '\x1b[1;34m]\x1b[0;39m',
                            '\x1b[1A\x1b[J'
            ]
        self.delete_line_list = ['^C', 'root@cuby:~#', 'INTERRUPT']
        # remove yocto workdir
        print("OPT in INIT", self.options)
        if self.options.replace:
            self.tbot_wdir = '/work/hs/tbot'
            self.tbot_first = False

        if os.path.isfile(self.options.tcpath + '/duts_settings.txt'):
            self.fd_duts = open(self.options.tcpath + '/duts_settings.txt', 'r')
            # create dictionary
            self.duts_var = []
            self.line = self.fd_duts.readline()
            while self.line:
                tmp = self.line.split('\t')
                tmp[1] = tmp[1].strip('\n')
                newel = {'var' : tmp[0], 'value' : tmp[1]}
                self.duts_var.append(newel)
               
                self.line = self.fd_duts.readline()
            self.fd_duts.close()
            self.fd_duts = True
        else:
            self.fd_duts = False

    def findfilename(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    def check_include(self):
        found = self.line.find(self.searchstring_include)
        if found != -1:
            # get inculdefilename
            tmp = self.line.split(' ')
            tmp = tmp[2].rstrip()
            self.list_of_files.append(tmp)

    def check_only_marker(self):
        # get logfilename we must find
        tmp = self.line.split(' ')
        tmp = tmp[2].rstrip()
        # search logfile name
        foundname = self.findfilename(tmp, self.options.tcpath)
        # foundname = None , if not found
        while self.line:
            self.get_next_line()
            self.linenr += 1
            found = self.line.find(self.searchstring_only_end)
            if found != -1:
                return self.linenr

            if foundname:
                self.check_include()
                found = self.line.find(self.searchstring)
                if found != -1:
                    self.replace_tbot_marker_file()
                else:
                    self.lastline_has_tbotmarker = False
                    self.fo.write(self.line)

        return self.linenr

    def write_line(self, wl):
        cur = len(wl)
        maxlen = int(self.options.wrap)
        if cur < maxlen:
            self.fo.write('  ' + wl)
        else:
            tmp = textwrap.wrap(wl, width=maxlen)
            cur = len(tmp)
            first = True
            for ln in tmp:
                if first:
                    self.fo.write('  ' + ln + '\\\n')
                    first = False
                else:
                    if cur > 1:
                        self.fo.write('    ' + ln + '\\\n')
                    else:
                        self.fo.write('    ' + ln + '\n')
                cur -= 1

    def replace_lf(self, ln):
        n = ln.find('\n')
        p = ln.find('\r')
        while p >= 0:
            if p < n:
                ln = ln[(p+1):]
            elif p > n:
                print("TODO ", p, n)
                if n == -1:
                    ln = ln[(p+1):]
                # may split \n and work all elements
                # and paste it together at the end
            p = ln.find('\r')
            n = ln.find('\n')
        return ln
        # return ln.replace('\r','\n  ')

    def replace_tbot_marker_file(self):
        if self.lastline_has_tbotmarker == False:
            if self.options.literal == 'rst':
                self.fo.write("\n::\n\n")
            else:
                self.fo.write('\n.. code-block:: ' + self.options.literal + '\n\n')

        # get filename
        logfile = self.line.split(self.searchstring)
        logfile = logfile[1]
        logfile = logfile.replace('\n', '')
        # open filename
        try:
            fl = open(self.options.tcpath + logfile, 'r')
        except:
            print("Error: %s in line %d not found\n" %(self.options.tcpath + logfile, self.linenr))
            sys.exit(1)
        # write line by line + 2 ' ' before the original line
        # also remove all lines with '^C'
        # and replace 'ttbott>' with '$'
        ln = fl.readline()
        pr_str = 'ttbott>'
        while ln:
            found_line = False
            for ds in self.delete_line_list:
                if ds in ln:
                    ln = fl.readline()
                    found_line = True
                    break
            if found_line == True:
                continue
            if pr_str in ln:
                pos = ln.find(pr_str)
                pos += len(pr_str)
                tmp = ln[pos:]
                ln = '$' + tmp
            for ds in self.delete_list:
                if ds in ln:
                    ln = ln.replace(ds, "")
            if self.options.replace:
                if self.tbot_wdir in ln:
                    if self.tbot_first:
                        ln = ln.replace(self.tbot_wdir, '$TBOT_BASEDIR')
                    self.tbot_first = True
            ln = ln.replace('\r\n','\n')
            ln = self.replace_lf(ln)
            self.write_line(ln)
            ln = fl.readline()

        self.fo.write("\n")
        fl.close()
        self.lastline_has_tbotmarker = True

    def replace_duts(self):
        if self.fd_duts == False:
            return

        for el in self.duts_var:
            if el['var'] in self.line:
                self.line = self.line.replace(el['var'], el['value'])
            

    def get_next_line(self):
        self.line = self.fi.readline()
        self.replace_duts()

    def do_work(self):
        self.fi = open(self.options.ifile, 'r')
        self.fo = open(self.options.ofile, 'w')
        self.get_next_line()

        self.lastline_has_tbotmarker = False
        self.linenr = 0
        while self.line:
            self.linenr += 1
            self.check_include()
            found = self.line.find(self.searchstring)
            if found != -1:
                self.replace_tbot_marker_file()
            else:
                self.lastline_has_tbotmarker = False
                found = self.line.find(self.searchstring_only)
                if found != -1:
                    self.check_only_marker()
                else:
                    self.fo.write(self.line)
            self.get_next_line()

        self.fi.close()
        self.fo.close()

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i", "--inputfile",
       dest="ifile", default="none",
       help="input file")
    parser.add_option("-o", "--outputfile",
       dest="ofile", default="none",
       help="output file")
    parser.add_option("-t", "--tcpatch",
       dest="tcpath", default="none",
       help="path to logfiles.")
    parser.add_option("-r", "--replace",
       dest="replace", default="False",
       help="replace some tbot paths")
    parser.add_option("-l", "--literal",
       dest="literal", default="bash",
       help="type of literal block (bash or rst)")
    parser.add_option("-w", "--wrap",
       dest="wrap", default=70,
       help="wrap lines after n characters")
    (options, args) = parser.parse_args()

    work = replace_tbot_marker(options)
    work.do_work()
    while work.list_of_files:
        filename = work.list_of_files[0]
        work.options.ifile = filename
        work.options.ofile = 'work/' + filename
        work.do_work()
        work.list_of_files.remove(filename)
