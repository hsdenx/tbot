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
import logging
import sys
import os

class doc_backend(object):
    """extract from all executed testcases the logs from tbots connection.

    Format of the created filenames:

    testcasename_connectionname_index_incnumber.txt

      testcasename:   Name of TC

      connectionname: Name of the tbot connection

      index: counts, how often the TC was called, starts with 1

      incnumber: each switch to another connection increments this number
                 starts with 1
 
    This files could be used to create documentation
    files, which contains logs.

    You can set a own "testcasename" if you create the event:
    SET_DOC_FILENAME. 

    You can set a own "testcasename" which collects all output
    until the END SET_DOC_FILENAME_NOIRQ_END marker is found with
    SET_DOC_FILENAME_NOIRQ. This is in experimental state,
    and need some ideas, how to display output from different
    connections.

    enable this backend with "create_documentation = 'yes'"

    created files are stored in tb.workdir + '/logfiles/
    so, be sure you have created this directory.

    Configuration Variable:
    tb.config.event_documentation_strip_list
      list of strings. If a line in the logfile is found, which contains
      a string of this list. This line is deleted, and replaced by a
      "[...]". If more lines are found in a row, only one "[...]"
      is inserted.

    tools/scripts:

    replace_tbot_marker.py searches for tbot markers "tbot_ref:[filename]"
    in textfiles, and replaces them with the content of the file [filename]

    ::

     $ python2.7 ../scripts/demo/documentation_backend/replace_tbot_marker.py --help
       Usage: replace_tbot_marker.py [options]
       Options:
         -h, --help            show this help message and exit
         -i IFILE, --inputfile=IFILE
                               input file
         -o OFILE, --outputfile=OFILE
                               output file
         -t TCPATH, --tcpatch=TCPATH
                               path to logfiles.
         -r REPLACE, --replace=REPLACE
                               replace some tbot paths
         -l LITERAL, --literal=LITERAL
                               type of literal block (bash or rst)
         -w WRAP, --wrap=WRAP  wrap lines after n characters


    see https://github.com/hsdenx/tbot/blob/testing/scripts/demo/documentation_backend/README
    for a demo, how you can create a html/pdf/man page, which
    contains content of tbot logfiles and text around it.

    - **parameters**, **types**, **return** and **return types**::
    :param arg1: tb
    :param arg2: list of strings, containing testcasesnames, which get ignored
    """
    def __init__(self, tb, ignorelist):
        self.dotnr = 0
        self.tb = tb
        self.ev = self.tb.event
        self.tc_list = []
        self.ignoretclist = ignorelist
        # ignore lines which contain the follwoing strings
        self.striplist = tb.config.event_documentation_strip_list
        self.set_noirq = False

    def __del__(self):
        try:
            self.fd_duts.close()
        except:
            self.fd_duts = 'none'

    def _create_pdf(self):
        try:
            self.tb.config.create_documentation_auto
        except:
            self.tb.config.create_documentation_auto = 'no'

        self.tb.config.create_documentation_op = ''
        if self.tb.config.create_documentation_auto == 'no':
            return

        if self.tb.config.create_documentation_auto == 'linux_top':
            file = "/src/files/top_plot_mem.sem"
            cmd = "gnuplot " + self.tb.workdir + file
            ret = os.system(cmd)
            if ret != 0:
                print ("Error gnuplot ", cmd, ret)
                return
            file = "/src/files/top_plot_cpu.sem"
            cmd = "gnuplot " + self.tb.workdir + file
            ret = os.system(cmd)
            if ret != 0:
                print ("Error gnuplot ", cmd, ret)
                return
            file = "/src/files/top_plot_load.sem"
            cmd = "gnuplot " + self.tb.workdir + file
            ret = os.system(cmd)
            if ret != 0:
                print ("Error gnuplot ", cmd, ret)
                return

            docname = "bbb_linux_top.pdf"
            docscript = "make_doku_bbb_top.sh"
            op = "/home/pi/tbot2go/documentation/linux_top/"
            logname = 'logfiles'
        elif self.tb.config.create_documentation_auto == 'uboot':
            docname = "dulg_bbb.pdf"
            docscript = "make_doku_ub.sh"
            op = "/home/pi/tbot2go/documentation/u-boot/"
            logname = 'logfiles'
        elif self.tb.config.create_documentation_auto == 'cuby':
            docname = "cuby_doc.pdf"
            docscript = "make_doku_cuby.sh"
            op = "/home/pi/tbot2go/documentation/cuby/"
            logname = 'logfiles'
            # copy xenomai result images
            cmd = "cp " + self.tb.resultdir + "/latency* " + op + "images"
            ret = os.system(cmd)
            if ret != 0:
                logging.warn("Failed to copy xenomai image %s %d", cmd, ret)
        elif self.tb.config.create_documentation_auto == 'yocto':
            docname = "yocto_bbb.pdf"
            docscript = "make_doku_yocto.sh"
            op = "/home/pi/tbot2go/documentation/yocto/"
            logname = 'logfiles_get_and_bake'
        else:
            logging.warn("unknown create_documentation_auto value", self.tb.config.create_documentation_auto)
            return

        # patch logfiles
        cmd = "python2.7 " + self.tb.workdir + "/src/documentation/patch_logfiles.py -i " + self.tb.workdir + "/logfiles"
        ret = os.system(cmd)
        if ret != 0:
            logging.warn("Patch files %s %d", cmd, ret)
            return
        # copy logfiles to doc dir
        cmd = "python2.7 " + self.tb.workdir + "/src/documentation/copy_logfiles.py -i " + self.tb.workdir + "/logfiles -o " + op + logname
        ret = os.system(cmd)
        if ret != 0:
            logging.warn("Copy files %s %d", cmd, ret)
            return
        # call make_docu
        cmd = self.tb.workdir + "/src/documentation/" + docscript
        ret = os.system(cmd)
        if ret != 0:
            logging.warn("make doc %s %d", cmd, ret)
            return
        self.tb.config.create_documentation_op = op
        self.tb.config.create_documentation_docname = docname

    def create_docfiles(self):
        """create the files
        """
        cmd = "rm -rf " + self.tb.workdir + '/logfiles/*'
        os.system(cmd)
        evl = list(self.tb.event.event_list)
        self._analyse(evl, 'main')
        try:
            self.fd_duts.close()
        except:
            self.fd_duts = 'none'
        self._create_pdf()

    def _get_event_id(self, el):
        if el['id'] == 'Start':
            return el['id']
        if el['id'] == 'StartFkt':
            return el['id']
        if el['id'] == 'End':
            return el['id']
        if el['id'] == 'log':
            return el['id']
        if el['id'] == 'SET_DOC_FILENAME':
            return el['id']
        if el['id'] == 'SET_DOC_FILENAME_NOIRQ':
            return el['id']
        if el['id'] == 'SET_DOC_FILENAME_NOIRQ_END':
            return el['id']
        if 'DUTS' in el['id']:
            return el['id']
        return 'none'

    def _get_event_name(self, el):
        return el['fname']

    def _get_next_event(self, el):
        if el == None:
            return ''

        if len(el) == 0:
            return ''

        ret = el[0]
        el.pop(0)
        return ret

    def _check_ignore_list(self, typ, name, evl):
        if not 'Start' in typ:
            return 'ok'

        for ign in self.ignoretclist:
            if ign == name:
                # search until End event
                el = 'start'
                while el != '':
                    el = self._get_next_event(evl)
                    if el == '':
                        continue
                    if el['typ'] != 'EVENT':
                        continue
                    eid = self._get_event_id(el)
                    if eid == 'none':
                        continue
                    newname = self._get_event_name(el)
                    if newname == name and eid == 'End':
                        return 'ignore'

        return 'ok'

    def _search_in_list(self, name):
        for el in self.tc_list:
            if el[0] == name:
                # tuples are immutable ...
                nr = el[1]
                nr = nr + 1
                # delete element
                self._rm_from_list(name)
                # add element
                self._add_to_list(name, nr)
                return nr

        return 0

    def _add_to_list(self, name, value):
        newel = name, value
        self.tc_list.append(newel)

    def _rm_from_list(self, name):
        new_list = []
        for s in self.tc_list:
            if not s[0] == name:
                new_list.append(s)
        self.tc_list = new_list

    def _create_fn(self, filename, conname, index, lnr):
        fn = filename.replace("/", "_")
        return self.tb.workdir + '/logfiles/' + fn + '_' + conname + '_' + str(index) + '_' + str(lnr) + '.txt'

    def _analyse(self, evl, name):
        filename = name
        stripped = 'yes'
        index = self._search_in_list(name)
        if index == 0:
            self._add_to_list(name, 1)
            index = 1
        lnr = 1
        oldname = 'none'
	end = False
        interrupted = False
        while end != True:
            if self.set_noirq == True:
                filename = self.set_noirq_name
            el = self._get_next_event(evl)
            if el == '':
                end = True
                continue
            if el['typ'] != 'EVENT':
                continue
            eid = self._get_event_id(el)
            if eid == 'none':
                continue
            if 'DUTS' in eid:
                # write it in duts_setting file
                try:
                    self.fd_duts
                except:
                    self.fd_duts = open(self.tb.workdir + '/logfiles/duts_settings.txt', 'w')
                tmp = eid + '\t' +  el['val'] + '\n'
                self.fd_duts.write(tmp)
                continue

            newname = self._get_event_name(el)
            ret = self._check_ignore_list(eid, newname, evl)
            if ret == 'ignore':
                continue
            if eid == 'Start' and self.set_noirq == False:
                interrupted = True
                self._analyse(evl, newname)
                continue
            if eid == 'SET_DOC_FILENAME' and self.set_noirq == False:
                interrupted = True
                self._analyse(evl, el['val'])
                continue
            if eid == 'SET_DOC_FILENAME_NOIRQ' and self.set_noirq == False:
                self.set_noirq = True
                self.set_noirq_name = el['val']
                self.set_noirq_tc_name = newname  
                interrupted = True
                self._analyse(evl, el['val'])
                continue
            if eid == 'SET_DOC_FILENAME_NOIRQ_END' and self.set_noirq == True:
                if newname == self.set_noirq_tc_name:
                    self.set_noirq = False
                else:
                    continue
                try:
                    fd.close()
                except:
                    print("filename noirq entry ", name, index)
                return
            if eid == 'End' and self.set_noirq == False:
                try:
                    fd.close()
                except:
                    print("filename no entry ", name, index)
                return
            tmp = el['val'].split()
            if tmp[0] != 'r':
                continue
            if eid == 'log':
                logline = el['val']
                logline = logline[2:]
                log = logline.split('\r\n')
                logline = ''
                for l in log:
                    add = True
                    for sl in self.striplist:
                        if sl in l:
                            add = False
                            if stripped == 'no':
                                logline += '[...]\n'
                                stripped = 'yes'
                            else:
                                break
                    if add:
                        if l != log[-1]:
                            logline += l + '\n'
                        else:
                            if l != '':
                                logline += l

                if self.set_noirq == True:
                    if oldname == 'none':
                        fd = open(self._create_fn(filename, newname, index, lnr), 'w')
                    oldname = self.set_noirq_name
                    # all in one log ... so different connections
                    # are in one log ... here is some work ToDo
                    newname = oldname
                    interrupted = False

                if oldname == 'none':
                    oldname = newname
                    fd = open(self._create_fn(filename, newname, index, lnr), 'w')
                    fd.write(logline)
                    stripped = 'no'
                    interrupted = False
                elif oldname == newname and interrupted == False:
                    fd.write(logline)
                else:
                    interrupted = False
                    fd.close()
                    lnr = lnr + 1
                    fd = open(self._create_fn(filename, newname, index, lnr), 'w')
                    oldname = newname
                    fd.write(logline)
                    stripped = 'no'
