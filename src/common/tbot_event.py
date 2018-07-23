# SPDX-License-Identifier: GPL-2.0
#
import datetime
import logging
import re
import sys
import traceback
import os
from struct import *
import time
from time import gmtime, strftime
import importlib

class events(object):
    """ The event class

    """
    def __init__(self, tb, logfile):
        """innit the event subsystem

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: workdir for tbot
        :param arg2: board config file
        :param arg3: name of logfile
        :param arg4: be verbose
        :return:
        """
        self.event_list = []
        self.stack = []
        self.tb = tb
        self.logfile = logfile
        self.logstart = 'EVVAL'
        self.logend = 'EVEND'

        sys.path.append(tb.workdir +  "/src/common/event")

        try:
            self.fd = open(tb.workdir + '/' + logfile, 'w')
        except:
            logging.warning("Could not create %s", logfile)
            sys.exit(1)

    def __del__(self):
        """
        cleanup
        :return:
        """

    def event_flush(self):
        self.fd.flush()

    def create_event(self, pname, name, id, value):
        """create an event

        - **parameters**, **types**, **return** and **return types**::
	:param arg1: parent name
	:param arg2: function name
	:param arg3: Event ID
	:param arg4: value for event ID
        """
        if id == 'Start':
            self.stack.append(name)
        if id == 'StartFkt':
            self.stack.append(name)
        if id == 'End':
            self.stack.pop()

        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        tmp = "EVENT " + time + " " + str(id) + " " + str(pname) + " " + str(name) + " " + self.logstart + str(value) + self.logend + "\n"
        self.fd.write(tmp)
        event = {'typ' : 'EVENT', 'time': time, 'id': str(id), 'pname' : str(pname), 'fname' : str(name), 'val' : str(value)}
        self.event_list.append(event)

        if id == 'BoardnameEnd':
            self.event_flush()
            print("EVENTLOGFILE ", self.tb.eventsim)
            if self.tb.eventsim != 'none':
                try:
                    self.fdsim = open(self.tb.workdir + '/' + self.tb.eventsim, 'r')
                except:
                    logging.warning("Could not create %s", self.tb.eventsim)
                    sys.exit(1)
                # delete old event list
                self.event_list = []
                # load saved event list
                line = self.fdsim.readline()
                cnt = 1
                event = ''
                id = ''
                time = ''
                pname = ''
                name = ''
                value = ''
                while line:
                    #print("LINE ", line)
                    if 'EVENT' in line:
                        # new event
                        # get info from new line
                        elements = line.split()
                        time = elements[1] + ' ' + elements[2]
                        id = elements[3]
                        pname = elements[4]
                        name = elements[5]
                        tmp = line.split(self.logstart)
                        #print("TMP ", tmp)
                        tmp = tmp[1]
                        if self.logend in tmp:
                            tmp = tmp.split(self.logend)
                            value = tmp[0]
                            #print("VAL END ", value)
                            event = {'typ' : 'EVENT', 'time': time, 'id': str(id), 'pname' : str(pname), 'fname' : str(name), 'val' : str(value)}
                            self.event_list.append(event)
                        else:
                            value = tmp
                            #print("VAL S ", value)
                    else:
                        if self.logend in line:
                            tmp = line.split(self.logend)
                            #print("found EVEND", tmp)
                            value += tmp[0]
                            #print("VAL END 2 ", value)
                            event = {'typ' : 'EVENT', 'time': time, 'id': str(id), 'pname' : str(pname), 'fname' : str(name), 'val' : str(value)}
                            self.event_list.append(event)
                        else:
                            # remove \n only and append to value
                            value += line[:-1]
                            #print("VAL A ", value)

                    line = self.fdsim.readline()
                    cnt += 1

            if (self.tb.config.create_webpatch == 'yes'):
                from web_patchwork import web_patchwork
                self.webpatch = self.web_patchwork(self.tb, 'webpatch.html')
            if (self.tb.config.create_dot == 'yes'):
                from dot import dot
                self.ignoretclist = ['tc_workfd_check_cmd_success.py',
                 'tc_lab_cp_file.py',
                 'tc_dummy.py',
                 'tc_workfd_check_if_file_exist.py',
                 'tc_workfd_rm_file.py']
                self.dot = dot(self.tb, 'tc.dot', self.ignoretclist)
            if (self.tb.config.create_statistic == 'yes'):
                from statisitic_plot import statistic_plot_backend
		self.ignoretclist = ['tc_workfd_check_cmd_success.py',
                 'tc_lab_cp_file.py',
                 'tc_dummy.py',
                 'tc_def_ub.py',
                 'tc_def_tbot.py',
                 'tc_workfd_check_if_file_exist.py',
                 'tc_lab_denx_get_power_state.py',
                 'tc_lab_interactive_get_power_state.py',
                 'tc_workfd_rm_file.py']

                self.statistic = statistic_plot_backend(self.tb, 'stat.dat', self.ignoretclist)
            if (self.tb.config.create_html_log == 'yes'):
                from html_log import html_log
                self.html_log = html_log(self.tb, 'html_log.html')
            try:
                self.tb.config.create_junit
            except:
                self.tb.config.create_junit = 'no'
            if (self.tb.config.create_junit == 'yes'):
                from junit import junit_backend
                try:
                    self.tb.config.junit_tclist
                except:
                    self.tb.config.junit_tclist = ['tc_lab_get_uboot_source.py',
                     'tc_workfd_set_toolchain.py', 'tc_workfd_compile_uboot.py',
                     'tc_workfd_connect_with_kermit.py', 'tc_ub_upd_uboot.py',
                     'tc_ub_upd_spl.py', 'tc_ub_check_version.py']
                    try:
                        self.tb.config.junit_tclist.extend(self.tb.config.duts_junittclist)
                    except:
                        pass
                try:
                    self.tb.config.junit_ignlist
                except:
                    self.tb.config.junit_ignlist = ['tc_workfd_check_cmd_success.py',
                     'tc_dummy.py',
                    ]
                self.junit = junit_backend(self.tb, 'tbot_results.xml', self.tb.config.junit_tclist, self.tb.config.junit_ignlist)
            if (self.tb.config.create_documentation == 'yes'):
                from documentation import doc_backend
                self.ignoretclist = ['tc_workfd_check_cmd_success.py']
                self.doc = doc_backend(self.tb, self.ignoretclist)
            if (self.tb.config.create_dashboard == 'yes'):
                from dashboard import dashboard
                self.dashboard = dashboard(self.tb, 'localhost', 'tbot', 'tbot', 'tbot_root', 'tbot_results')

            # execute the event backends
            if (self.tb.config.create_webpatch == 'yes'):
                self.webpatch.create_webfile()
            if (self.tb.config.create_dot == 'yes'):
                self.dot.create_dotfile()
            if (self.tb.config.create_statistic == 'yes'):
                self.statistic.create_statfile()
            if (self.tb.config.create_html_log == 'yes'):
                self.html_log.create_htmlfile()
            if (self.tb.config.create_documentation == 'yes'):
                self.doc.create_docfiles()
            if (self.tb.config.create_dashboard == 'yes'):
                self.dashboard.insert_test_into_db()
            if (self.tb.config.create_junit == 'yes'):
                self.junit.create_junit_file()

    def create_event_log(self, c, dir, string):
        """create a log event

        - **parameters**, **types**, **return** and **return types**::
	:param arg1: connection
	:param arg2: direction (r or w)
	:param arg3: log string
        """

        if self.tb.donotlog == True:
            return
        try:
            name = self.stack[-1]
        except:
            name = 'main'

        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        tmp = "EVENT " + time + " log " + name + " " + str(c.name) + " "+ self.logstart + str(dir) + " " + string + self.logend + "\n"
        self.fd.write(tmp)
        event = {'typ' : 'EVENT', 'time': time, 'id': 'log', 'pname' : str(name), 'fname' : str(c.name), 'val' : str(dir) + " " + string}
        self.event_list.append(event)

        # flush, so we have written all log data in error case
        self.fd.flush()
        os.fsync(self.fd)
        if dir == 'r' or dir == 're' or dir == 'ig' or dir == 'er' or dir == 'rf':
            se = string.rstrip()
            se = se.lstrip()
            self.tb.con_log("%s: %s", c.name, se)

    def register_backend(self):
        """register a backend.

        ToDo
        """

    def list_backend(self):
        """list all registered backends.

        ToDo
        """
