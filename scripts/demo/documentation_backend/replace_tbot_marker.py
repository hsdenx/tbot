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
from optparse import OptionParser

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
(options, args) = parser.parse_args()
 
searchstring = 'tbot_ref:'

fi = open(options.ifile, 'r')
fo = open(options.ofile, 'w')
line = fi.readline()

# remove yocto workdir
if options.replace:
    tbot_wdir = '/work/hs/tbot'
    tbot_first = False

while line:
    found = line.find(searchstring)
    if found != -1:
        if options.literal == 'rst':
            fo.write("\n::\n\n")
        else:
            fo.write('\n.. code-block:: ' + options.literal + '\n\n')
        # get filename
        logfile = line.split(searchstring)
        logfile = logfile[1]
        logfile = logfile.replace('\n', '')
        # open filename
        fl = open(options.tcpath + logfile, 'r')
        if not fl:
            print("Error: %s not found\n" %(options.tcpath + logfile))
            sys.exit(1)
        # write line by line + 2 ' ' before the original line
        # also remove all lines with '^C'
        # and replace 'ttbott>' with '$'
        ln = fl.readline()
        pr_str = 'ttbott>'
        # replace col_str with ':redtext:`'
        col_str = '\x1b[01;31m\x1b[K'
        # and replace end_str with '`'
        end_str = ' \x1b[m\x1b[K'
        while ln:
            if '^C' in ln:
                ln = fl.readline()
                continue
            if pr_str in ln:
                pos = ln.find(pr_str)
                pos += len(pr_str)
                tmp = ln[pos:]
                ln = '$' + tmp
            if col_str in ln:
                #ln = ln.replace(col_str, ':redtext:`')
                #ln = ln.replace(end_str, '`')
                ln = ln.replace(col_str, "'")
                ln = ln.replace(end_str, "'")
            if options.replace:
                if tbot_wdir in ln:
                    if tbot_first:
                        ln = ln.replace(tbot_wdir, '$TBOT_WORKDIR')
                    tbot_first = True
            ln = ln.replace('\r\n','\n')
            ln = ln.replace('\r','\n  ')
            fo.write('  ' + ln)
            ln = fl.readline()

        fo.write("\n")
        fl.close()
    else:
        fo.write(line)
    line = fi.readline()

fi.close()
fo.close()
