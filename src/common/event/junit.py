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
    """
    def __init__(self, tb, junitfile):
        self.tb = tb
        self.ev = self.tb.event
        self.junitfile = junitfile
        self.fd = open(self.tb.workdir + '/' + self.junitfile, 'w')
        self.testclass = 'tbot'
        self.uboot_src_path = ''

    def _get_event_id(self, el):
        if el['id'] == 'WDT':
            return el['id']
        if el['id'] == 'ERROR_STRING':
            return el['id']
        if el['id'] == 'BoardnameEnd':
            return el['id']
        return 'none'

    def _get_next_event(self, el):
        if len(el) == 0:
            return ''

        ret = el[0]
        el.pop(0)
        return ret

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
            if eid == 'WDT':
                self.error_string += 'WDT triggered\n'
            if eid == 'ERROR_STRING':
                self.error_string += '\n\nError String ' + el['val'] + ' found\n\n'
            if eid == 'BoardnameEnd':
                if el['val'] == 'False':
                    self.error_string += 'Failed\n'

    def create_junit_file(self):
        """create the junit file
        """
        test_cases = []
        self.testgrp = self.tb.starttestcase
        self._get_state()
        tc = TestCase(self.testgrp, self.testclass, 12, 'I am stdout!', 'I am stderr!')
        if self.error_string != '':
            tc.add_error_info(self.error_string)
        test_cases.append(tc)
        # only example, how to add more results
        # example for a bad result
        #tc = TestCase(self.testgrp, 'Error-Message')
        #tc.add_error_info("error message")
        #test_cases.append(tc)
        # example for a failure result
        #tc = TestCase(slef.testgrp, 'Failure Message')
        #tc.add_failure_info('This is a failure')
        #test_cases.append(tc)

        ts = TestSuite("tbot test results", test_cases)
        # prettyprinting is on by default but can be disabled using prettyprint=False
        # print(TestSuite.to_xml_string([ts]))

        TestSuite.to_file(self.fd, [ts], prettyprint=False)
        self.fd.close()

        # can we use here a jenkins env var ?
        # no, as copy_file does not see $WORKSPACE
        cmd = 'printenv WORKSPACE'
        status, output = commands.getstatusoutput(cmd)
        logging.info("jenkins status ", status)
        logging.info("jenkins WORKSPACE ", output)
        if status != 0:
            return

        newdirtmp = output
        newdirtmptbot = newdirtmp + '/' + self.testclass + '/'
        # check if newdirtmptbot exists
        # if not try to create it
        tmp = 'mkdir ' + newdirtmptbot
        os.system(tmp)
        tmp = "cp " + self.tb.workdir + "/log/tbot_results.xml " + newdirtmp + "/tbot_results.xml"
        os.system(tmp)

        tmp = "cp " + self.tb.logfilen + " " + newdirtmptbot + "tbot.log"
        os.system(tmp)

        if self.uboot_src_path != '':
            rem = self.uboot_src_path + '/.config'
            loc = newdirtmptbot + '/defconfig'
            self.tb.c_ctrl.copy_file(rem, loc)
        if (self.tb.config.create_statistic == 'yes'):
            tmp = "cp " + self.tb.workdir + "/output.jpg " + newdirtmptbot + "tbot_stat.jpg"
            os.system(tmp)
        if (self.tb.config.create_dot == 'yes'):
            tmp = "cp " + self.tb.workdir + "/tc.png " + newdirtmptbot + "graph.png"
            os.system(tmp)
        if (self.tb.config.create_html_log == 'yes'):
            tmp = "cp " + self.tb.workdir + "/log/html_log.html " + newdirtmptbot + "/html_log.html"
            os.system(tmp)
            tmp = "cp " + self.tb.workdir + "/log/multiplexed_tbotlog.css " + newdirtmptbot + "/multiplexed_tbotlog.css"
            os.system(tmp)
        if self.tb.config.create_documentation == 'yes':
            tmp = "cp " + self.tb.workdir + "/src/documentation/u-boot/pdf/dulg_bbb.pdf " + newdirtmptbot + "/bbb.pdf"
            os.system(tmp)
