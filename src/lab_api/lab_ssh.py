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
# This is not a complete lab_api!
# It just colelcts ssh specific tasks, so real lab_api
# which uses ssh connection to the lab host pc can reuse
# this code.
#
import paramiko
import logging
import socket
import datetime
import re
import sys
import os
from time import sleep
from struct import *
import time
from tbotlib import tbot
import state_uboot
import state_linux

def _lab_open_ssh(self):
    # look in paramiko/demos/demo_simple.py
    # for more infos how to use host keys ToDo
    logging.debug("try to open ssh connection")
    if not self.ssh:
        self.ssh = paramiko.SSHClient()
    self.opened = False
    if self.accept_all == True:
        #accept all host keys
        logging.debug("AutoAddPolicy")
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    logging.debug("try connection for %s@%s", self.tb.user, self.tb.ip)
    pword = self.get_password(self.tb.user, "lab")
    try:
        self.ssh.connect(self.tb.ip, username=self.tb.user, password=pword)
    except:
        logging.warning("no connection for %s@%s", self.tb.user, self.tb.ip)
        self.ssh.close()
        return None

    self.opened = True
    self.chan = []

    # ToDo cleanup this
    self.channel_ctrl = 0
    self.channel_con = 1
    # channel 0 for power
    self.lab_open_fd()
    # channel 1 for "console"
    self.lab_open_fd()

    logging.info("got connection for %s@%s", self.tb.user, self.tb.ip)
    self.count = 0
    # http://www.lag.net/paramiko/docs/paramiko.Transport-class.html#set_keepalive
    self.tr = self.ssh.get_transport()
    self.tr.set_keepalive(self.tb.keepalivetimeout)
    return True

def lab_get_password(self, user, board):
    """ get the password for the user
        return password if found
        end tc if not
        The passwords are in the password.py file
        in the working directory. For example:
        if (user == 'passwordforuserone'):
            password = 'gnlmpf'
        if (user == 'anotheruser'):
            password = 'passwordforanotheruser'
    """
    filename = self.tb.workdir + "/password.py"
    try:
        fd = open(filename, 'r')
    except:
        logging.warning("Could not find %s", filename)
        sys.exit(1)

    exec(fd)
    fd.close()
    try:
        password
    except NameError:
        logging.info("no password found for %s", user)
        self.tb.end_tc(False)

    return password

def lab_get_lab_connect_state(self):
    """ get state of the connection to the lab
    """
    if self.opened == True:
        logging.debug("get connection state to lab OK")
    else:
        logging.debug("get connection state to lab False")
# TODO check it really !!
    return self.opened

def lab_connect_lab(self):
    """ connect to the lab and set lab prompt
        return:
        True, if connect
        False else
    """
    logging.debug("connecting to lab")
    st = self.get_lab_connect_state()
    if st == True:
        return True

    ret = self._open_ssh()
    if ret != True:
        return ret

    # set prompt for the power channel
    ret = self.tb.set_prompt(self.channel_ctrl, self.tb.labprompt, 'export PS1="\u@\h [\$(date +%k:%M:%S)] ', ' >"')
    return ret

def lab_lab_open_fd(self):
    """ open a filedescriptor
        return here the fd !! ToDo
    """
    print(self, self.tb, self.opened)
    channel = self.ssh.invoke_shell()
    self.chan.append(channel)
    if self.tb.debug:
        print repr(self.ssh.get_transport())
    logging.debug(self.ssh.get_transport())
    channel.settimeout(self.tb.channel_timeout)
    self.data.append('')
    self.old.append('')
    self.fdcount += 1

    return True

def lab_lab_check_fd(self, fd):
    """ check if  filedescriptor is valid
        ToDo
    """
    return True

def lab_lab_close_fd(self):
    """ close a filedescriptor
        ToDo
    """
    return True

def lab_recv(self, fd):
    try:
        self.data[fd] = self.chan[fd].recv(1024)
    except socket.timeout:
        logging.debug("read_bytes: Timeout")
        return None
    return True

def lab_get_bytes(self, fd):
    self.old[fd] = self.data[fd]
    self.data[fd] = ''
    return self.old[fd]

def lab_write(self, fd, string):
    if (len(string) > self.tb.term_line_length):
        self.tb.debugprint("tooo long to write %s > %s", len(string), self.tb.term_line_length)
        logging.debug("tooo long to write %s > %s", len(string), self.tb.term_line_length)
        self.tb.tc_end(False)

    logging.debug("write: %s@%s: %s", self.tb.user, self.tb.ip, string)
    self.tb.debugprint("str: %s len: %d\n", string, len(string))
    # send the complete bytes in 
    # self.chan[fd].send(string)
    # leads in errors, as the serial connection
    # to the console is to slow ...
    #for i in range(0, len(string)):
    #    self.chan[fd].send(string[i])
    #    sleep(0.2)

    self.chan[fd].send(string)
    # add here a return too ... ToDo: why?
    self.chan[fd].send('\n')
    self.chan[fd].send('\n')

    return True

def lab_write_no_ret(self, fd, string):
    logging.debug("write: %s@%s: %s", self.tb.user, self.tb.ip, string)
    self.chan[fd].send(string)
    return True
