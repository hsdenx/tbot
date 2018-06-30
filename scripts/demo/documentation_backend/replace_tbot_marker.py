#!/usr/bin/python
#
# SPDX-License-Identifier: GPL-2.0
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
 
searchstring = 'tbot_ref:'

delete_list = ['\x1b[01;31m\x1b[K',
	' \x1b[m\x1b[K',
	'\x1b[1;34m[\x1b[1;32m',
	'\x1b[1;34m]\x1b[0;39m',
	'\x1b[1A\x1b[J'
]

fi = open(options.ifile, 'r')
fo = open(options.ofile, 'w')
line = fi.readline()

# remove yocto workdir
if options.replace:
    tbot_wdir = '/work/hs/tbot'
    tbot_first = False

def write_line(fo, wl):
    cur = len(wl)
    maxlen = int(options.wrap)
    if cur < maxlen:
        fo.write('  ' + wl)
    else:
        tmp = textwrap.wrap(wl, width=maxlen)
        cur = len(tmp)
        first = True
        for ln in tmp:
            if first:
                fo.write('  ' + ln + '\\\n')
                first = False
            else:
                if cur > 1:
                    fo.write('    ' + ln + '\\\n')
                else:
                    fo.write('    ' + ln + '\n')
            cur -= 1

lastline_has_tbotmarker = False
linenr = 0
while line:
    linenr += 1
    found = line.find(searchstring)
    if found != -1:
        if lastline_has_tbotmarker == False:
            if options.literal == 'rst':
                fo.write("\n::\n\n")
            else:
                fo.write('\n.. code-block:: ' + options.literal + '\n\n')

        # get filename
        logfile = line.split(searchstring)
        logfile = logfile[1]
        logfile = logfile.replace('\n', '')
        # open filename
        try:
            fl = open(options.tcpath + logfile, 'r')
        except:
            print("Error: %s in line %d not found\n" %(options.tcpath + logfile, linenr))
            sys.exit(1)
        # write line by line + 2 ' ' before the original line
        # also remove all lines with '^C'
        # and replace 'ttbott>' with '$'
        ln = fl.readline()
        pr_str = 'ttbott>'
        while ln:
            if '^C' in ln:
                ln = fl.readline()
                continue
            if pr_str in ln:
                pos = ln.find(pr_str)
                pos += len(pr_str)
                tmp = ln[pos:]
                ln = '$' + tmp
            for ds in delete_list:
                if ds in ln:
                    ln = ln.replace(ds, "")
            if options.replace:
                if tbot_wdir in ln:
                    if tbot_first:
                        ln = ln.replace(tbot_wdir, '$TBOT_BASEDIR')
                    tbot_first = True
            ln = ln.replace('\r\n','\n')
            ln = ln.replace('\r','\n  ')
            write_line(fo, ln)
            ln = fl.readline()

        fo.write("\n")
        fl.close()
        lastline_has_tbotmarker = True
    else:
        lastline_has_tbotmarker = False
        fo.write(line)
    line = fi.readline()

fi.close()
fo.close()
