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
import importlib
sys.path.append("src/common/event/")
from web_patchwork import web_patchwork
from dot import dot

class events(object):
    """ The event class

    more details follow
    """
    def __init__(self, tb, logfile):
        """
        :param workdir: workdir for tbot
        :param cfgfile: board config file
        :param logfilen: name of logfile
        :param verbose: be verbose
        :return:
        """
        self.event_list = []
        self.stack = []
        self.tb = tb
        self.logfile = logfile
        try:
            self.fd = open(tb.workdir + '/' + logfile, 'w')
        except:
            logging.warning("Could not create %s", logfile)
            sys.exit(1)
        self.webpatch = web_patchwork(tb, 'webpatch.html')
        self.ignoretclist = ['tc_workfd_check_cmd_success.py',
             'tc_lab_cp_file.py',
             'tc_workfd_check_if_file_exist.py',
             'tc_workfd_rm_file.py']
        self.dot = dot(tb, 'tc.dot', 'log/event.log', self.ignoretclist)

    def __del__(self):
        """
        cleanup
        :return:
        """

    def create_event(self, pname, name, id, value):
        """
        call it, to create an stat event

	:param id: event id
	:param pname: parent name
	:param name: function name
	:param value: value for event ID
        """
        if id == 'Start':
            self.stack.append(name)
        if id ==  'BoardnameEnd':
            self.webpatch.create_webfile()
            self.dot.create_dotfile()

        if id == 'End':
            self.stack.pop()
            try:
                nametest = self.stack[-1]
            except:
                nametest = 'main'

        tmp = "EVENT " + str(id) + " " + str(pname) + " " + str(name) + " " + str(value) + "\n"
        self.fd.write(tmp)
        self.event_list.append(tmp)

    def create_event_log(self, c, dir, string):
        try:
            name = self.stack[-1]
        except:
            name = 'main'
        tmp = "EVENT log " + name + " " + str(c.name) + " " + str(dir) + " " + string + "\n"
        self.fd.write(tmp)
        self.event_list.append(tmp)
        if dir == 'r':
            se = string.rstrip()
            se = se.lstrip()
            self.tb.con_log("%s: %s", c.name, se)
            self.tb.verboseprint("%s: %s" % (c.name, se))

    def register_backend(self):
        """
        register a backend.
        """

    def list_backend(self):
        """
        lit all registered backends.
        """
