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
import commands
from time import gmtime, strptime, mktime
from junit_xml import TestSuite, TestCase

class junit_backend(object):
    """create a junit xml file after tbot hs finished

       Install junit-xml python modul. This is used here
       for creating junit xml files.

       pip install junit-xml

       jenkins setup:

       install jenkins plugin:
         - execute shell script with another user (not jenkins)
           - setup a ssh agent, which connects you to the machine
             which runs tbot (You also need this, if jenkins
             is running on the same machine, or tbot runs with
             user jenkins ...)
         - storing ssh credentials (for connecting to tbot machine)
           https://plugins.jenkins.io/ssh-credentials
         - storing attachments in jenkins (results from tbot backends)
           https://wiki.jenkins.io/display/JENKINS/JUnit+Attachments+Plugin

       resulting xml file is stored from tbot into
       '$WORKSPACE'

       files resulting from tbot backens are stored into
       '$WORKSPACE/' + self.testclass + '/'

       make sure, jenkins set the environment variable $WORKSPACE !

       Running Jenkins behind Apache
       follow the instructions on:
       https://wiki.jenkins.io/display/JENKINS/Running+Jenkins+behind+Apache

    - **parameters**, **types**, **return** and **return types**::
    :param arg1: tb
    :param arg2: filename which gets created, place tb.workdir
    :param arg2: testcases, which are put into the xmls file
    """
    def __init__(self, tb, junitfile, tclist, ignlist):
        self.tb = tb
        self.ev = self.tb.event
        self.junitfile = junitfile
        self.fd = open(self.tb.resultdir + '/' + self.junitfile, 'w')
        self.testclass = 'tbot'
        self.uboot_src_path = ''
        self.tclist = tclist
        self.ignoretclist = ignlist
        self.record_log = False

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
                    ntyp = self._get_event_id(el)
                    if ntyp == 'none':
                        continue
                    newname = self._get_event_name(el)
                    if newname == name and ntyp == 'End':
                        return 'ignore'

        return 'ok'

    def _get_event_id(self, el):
        if el['id'] == 'WDT':
            return el['id']
        if el['id'] == 'ERROR_STRING':
            return el['id']
        if el['id'] == 'BoardnameEnd':
            return el['id']
        if el['id'] == 'Start':
            return el['id']
        if el['id'] == 'StartFkt':
            return el['id']
        if el['id'] == 'End':
            return el['id']
        if el['id'] == 'log':
            if self.record_log == True:
                return el['id']
        return 'none'

    def _get_next_event(self, el):
        if len(el) == 0:
            return ''

        ret = el[0]
        el.pop(0)
        return ret

    def _get_event_name(self, el):
        return el['fname']

    def _get_state(self):
        evl = list(self.tb.event.event_list)
        el = 'start'
        self.error_string = ''
        while el != '':
            el = self._get_next_event(evl)
            if el == '':
                continue
            if el['typ'] != 'EVENT':
                continue
            if el['id'] == 'UBOOT_SRC_PATH':
                self.uboot_src_path = el['val']
            eid = self._get_event_id(el)
            if eid == 'none':
                continue
            newname = self._get_event_name(el)
            if eid == 'WDT':
                self.error_string += 'WDT triggered\n'
            if eid == 'ERROR_STRING':
                self.error_string += '\n\nError String ' + el['val'] + ' found\n\n'
            if eid == 'BoardnameEnd':
                if el['val'] == 'False':
                    self.error_string += 'Failed\n'

    def _get_testcases(self, testcases):
        for cur_tclist in self.tclist:
            evl = list(self.tb.event.event_list)
            el = 'start'
            error_string = ''
            logct = ''
            tcname = ''
            while el != '':
                el = self._get_next_event(evl)
                if el == '':
                    continue
                if el['typ'] != 'EVENT':
                    continue
                eid = self._get_event_id(el)
                if eid == 'none':
                    continue
                name = self._get_event_name(el)
                ret = self._check_ignore_list(eid, name, evl)
                if ret == 'ignore':
                    continue
                if eid == 'WDT':
                    error_string += 'WDT triggered\n'
                if eid == 'Start':
                    if self.tb.starttestcase == name:
                        continue
                    if self.record_log == False:
                        if name in cur_tclist:
                            self.record_log = True
                            logct = ''
                            tcname = name
                            stime = strptime(el['time'], "%Y-%m-%d %H:%M:%S")
                if eid == 'End':
                    if self.record_log == True and name == tcname:
                        self.record_log = False
                        etime = strptime(el['time'], "%Y-%m-%d %H:%M:%S")
                        diff = mktime(etime) - mktime(stime)
                        if el['val'] == 'False':
                            error_string += 'Failed\n'
                        tc = TestCase(self.testgrp, tcname.replace(".py", ""), float(diff), logct, '')
                        if error_string != '':
                            tc.add_error_info(error_string)
                        testcases.append(tc)
                if eid == 'log':
                    if self.record_log == True:
                        logline = el['val']
                        if logline[0] == 'r':
                            logline = logline[2:]
                            # convert to unicode
                            # see
                            # https://stackoverflow.com/questions/21129020/how-to-fix-unicodedecodeerror-ascii-codec-cant-decode-byte
                            if isinstance(logline, str):
                                logline = logline.decode('ascii', 'ignore').encode('ascii') #note: this removes the character and encodes back to string.
                            elif isinstance(logline, unicode):
                                logline = logline.encode('ascii', 'ignore') 
                            logct += logline

    def create_junit_file(self):
        """create the junit file
        """
        test_cases = []
        try:
            self.testgrp = self.tb.starttestcase
        except:
            return
        self._get_state()
        tc = TestCase(self.testgrp, self.testclass, 0, '', '')
        if self.error_string != '':
            tc.add_error_info(self.error_string)
        test_cases.append(tc)
        self._get_testcases(test_cases)

        ts = TestSuite("tbot test results", test_cases)
        # prettyprinting is on by default but can be disabled using prettyprint=False
        # print(TestSuite.to_xml_string([ts]))

        TestSuite.to_file(self.fd, [ts], prettyprint=False)
        self.fd.close()

        # can we use here a jenkins env var ?
        # no, as copy_file does not see $WORKSPACE
        cmd = 'printenv WORKSPACE'
        status, output = commands.getstatusoutput(cmd)
        logging.info("jenkins status %s", status)
        logging.info("jenkins WORKSPACE %s", output)
        if status != 0:
            return

        newdirtmp = output
        newdirtmptbot = newdirtmp + '/' + self.testclass + '/'
        # check if newdirtmptbot exists
        # if not try to create it
        tmp = 'mkdir ' + newdirtmptbot
        os.system(tmp)
        tmp = "cp " + self.tb.resultdir + "/" + self.junitfile + " " + newdirtmp + "/" + self.junitfile
        os.system(tmp)

        tmp = "cp " + self.tb.logfilen + " " + newdirtmptbot + "tbot.log"
        os.system(tmp)

        if self.uboot_src_path != '':
            rem = self.uboot_src_path + '/.config'
            loc = newdirtmptbot + '/defconfig.txt'
            self.tb.c_ctrl.copy_file(rem, loc)
        if (self.tb.config.create_statistic == 'yes'):
            tmp = "cp " + self.tb.resultdir + "/output.jpg " + newdirtmptbot + "tbot_stat.jpg"
            os.system(tmp)
        if (self.tb.config.create_dot == 'yes'):
            tmp = "cp " + self.tb.resultdir + "/tc.png " + newdirtmptbot + "graph.png"
            os.system(tmp)
        # copy eventually created xenomai stats
        try:
            self.tb.config.tc_xenomai_latency_opt
            files = ['lat_tbot-t2.png', 'lat_tbot.png', 'lat_tbot.dat.loc', 'lat_tbot.dat-t2.loc']
            for f in files:
                n = f
                n = n.replace('lat_tbot', 'xenomai-latency')
                if 'loc' in n:
                    n = n.replace('loc', 'txt')
                tmp = "cp " + self.tb.resultdir + '/' + f + ' ' + newdirtmptbot + n
                os.system(tmp)
        except:
            pass
        if (self.tb.config.create_html_log == 'yes'):
            tmp = "cp " + self.tb.resultdir + "/html_log.html " + newdirtmptbot + "/html_log.html"
            os.system(tmp)
            tmp = "cp " + self.tb.resultdir + "/multiplexed_tbotlog.css " + newdirtmptbot + "/multiplexed_tbotlog.css"
            os.system(tmp)
            tmp = "cp " + self.tb.resultdir + "/myscript.js " + newdirtmptbot + "/myscript.js"
            os.system(tmp)
        if self.tb.config.create_documentation == 'yes':
            if self.tb.config.create_documentation_op != '':
                op = self.tb.config.create_documentation_op
                docname = self.tb.config.create_documentation_docname
                tmp = "cp " + op + "/pdf/" + docname + " " + newdirtmptbot + "/" + docname
                os.system(tmp)
