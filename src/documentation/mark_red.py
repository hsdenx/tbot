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
import textwrap

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
 
mark_red_list = [
	'$TBOT_BASEDIR_YOCTO',
	'$TBOT_BASEDIR',
	'TBOT_BASEDIR_YOCTO',
	'TBOT_BASEDIR',
	'TBOT_YOCTO_PATH',
	'TBOT_YOCTO_DLDIR',
	'TBOT_YOCTO_SSTATEDIR',
]

prepend = ') Tj 1 0 0 rg ('
postpend = ') Tj 0 0 0 rg ('

fi = open(options.ifile, 'r')
fo = open(options.ofile, 'w')

linenr = 0
line = True
while line:
    line = fi.readline()
    linenr += 1
#    if len(line) < 2:
#        fo.write(line)
#        continue
#    if line[0] != ' ' and line[1] != ' ':
#        fo.write(line)
#        continue
    for se in mark_red_list:
        index = 0
        while index < len(line):
            found = line.find(se, index)
            if found == -1:
                break
            else:
                if line[found - 1] == '(':
                    break
                tmp = line[0:found]
                tmp += prepend
                tmp += se
                tmp += postpend
                found += len(se)
                tmp += line[found:]
                line = tmp
                index = found + len(prepend) + len(postpend)

    fo.write(line)

fi.close()
fo.close()
