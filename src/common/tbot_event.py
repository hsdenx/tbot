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
        tmp = "EVENT " + time + " " + str(id) + " " + str(pname) + " " + str(name) + " " + str(value) + "\n"
        self.fd.write(tmp)
        event = {'typ' : 'EVENT', 'time': time, 'id': str(id), 'pname' : str(pname), 'fname' : str(name), 'val' : str(value)}
        self.event_list.append(event)

        if id == 'BoardnameEnd':
            self.event_flush()
            if (self.tb.config.create_webpatch == 'yes'):
                from web_patchwork import web_patchwork
                self.webpatch = self.web_patchwork(self.tb, 'webpatch.html')
            if (self.tb.config.create_dot == 'yes'):
                from dot import dot
                self.ignoretclist = ['tc_workfd_check_cmd_success.py',
                 'tc_lab_cp_file.py',
                 'tc_workfd_check_if_file_exist.py',
                 'tc_workfd_rm_file.py']
                self.dot = dot(self.tb, 'tc.dot', self.ignoretclist)
            if (self.tb.config.create_statistic == 'yes'):
                from statisitic_plot import statistic_plot_backend
		self.ignoretclist = ['tc_workfd_check_cmd_success.py',
                 'tc_lab_cp_file.py',
                 'tc_def_ub.py',
                 'tc_def_tbot.py',
                 'tc_workfd_check_if_file_exist.py',
                 'tc_lab_denx_get_power_state.py',
                 'tc_lab_interactive_get_power_state.py',
                 'tc_workfd_rm_file.py']

                self.statistic = statistic_plot_backend(self.tb, 'stat.dat', self.ignoretclist)
            if (self.tb.config.create_html_log == 'yes'):
                from html_log import html_log
                self.html_log = html_log(self.tb, 'log/html_log.html')
            try:
                self.tb.config.create_junit
            except:
                self.tb.config.create_junit = 'no'
            if (self.tb.config.create_junit == 'yes'):
                from junit import junit_backend
                self.junit = junit_backend(self.tb, 'log/tbot_results.xml')
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
        tmp = "EVENT " + time + " log " + name + " " + str(c.name) + " " + str(dir) + " " + string + "\n"
        self.fd.write(tmp)
        event = {'typ' : 'EVENT', 'time': time, 'id': 'log', 'pname' : str(name), 'fname' : str(c.name), 'val' : str(dir) + " " + string}
        self.event_list.append(event)

        # flush, so we have written all log data in error case
        self.fd.flush()
        os.fsync(self.fd)
        if dir == 'r' or dir == 're' or dir == 'ig' or dir == 'er':
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
