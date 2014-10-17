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

class tbot_lab_api(object):
    def __init__(self, tb):
        logging.info("setup with denx API")
        self.tb = tb
        self.ssh = False
        self.opened = False
        self.accept_all = True
        self.fdcount = 0
        self.__data = []
        self.__old = []

    def __del__(self):
        time.sleep(1)

    def _open_ssh(self):
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

    def get_password(self, user, board):
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

    def get_lab_connect_state(self):
        """ get state of the connection to the lab
        """
        if self.opened == True:
            logging.debug("get connection state to lab OK")
        else:
            logging.debug("get connection state to lab False")
# TODO check it really !!
        return self.opened

    def connect_lab(self):
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

    def lab_open_fd(self):
        """ open a filedescriptor
            return here the fd !! ToDo
        """
        channel = self.ssh.invoke_shell()
        self.chan.append(channel)
        if self.tb.debug:
            print repr(self.ssh.get_transport())
        logging.debug(self.ssh.get_transport())
        channel.settimeout(self.tb.channel_timeout)
        self.__data.append('')
        self.__old.append('')
        self.fdcount += 1

        return True

    def lab_check_fd(self, fd):
        """ check if  filedescriptor is valid
            ToDo
        """
        return True

    def lab_close_fd(self):
        """ close a filedescriptor
            ToDo
        """
        return True

    def recv(self, fd):
        try:
            self.__data[fd] = self.chan[fd].recv(1024)
        except socket.timeout:
            logging.debug("read_bytes: Timeout")
            return None
        return True

    def get_bytes(self, fd):
        self.__old[fd] = self.__data[fd]
        self.__data[fd] = ''
        return self.__old[fd]

    def write(self, fd, string):
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

    def write_no_ret(self, fd, string):
        logging.debug("write: %s@%s: %s", self.tb.user, self.tb.ip, string)
        self.chan[fd].send(string)
        return True

    def get_power_state(self, boardname):
        """ Get powerstate of the board in the lab
        """
        tmp = "get power state " + boardname
        logging.info(tmp)

        tmp = "remote_power " + boardname + " -l"
        ret = self.tb.write_stream(self.channel_ctrl, tmp)
        if not ret:
            self.tb.read_end(self.channel_ctrl, 1, self.tb.labprompt)
            return ret

        ret = self.tb.wait_answer(self.channel_ctrl, boardname, 2)
        if ret:
            reg = re.compile("ON")
            res = reg.search(self.tb.buf[self.channel_ctrl])
            if res:
                self.tb.read_end(self.channel_ctrl, 1, self.tb.labprompt)
                return True
        
        self.tb.read_end(self.channel_ctrl, 1, self.tb.labprompt)
        return False

    def set_power_state(self, boardname, state):
        """ set powerstate for the board in the lab
        """
        tmp = "set power state " + boardname + " to " + state
        logging.info(tmp)

        tmp = "remote_power " + boardname + " " + state
        ret = self.tb.write_stream(self.channel_ctrl, tmp)
        if not ret:
            return ret
        ret = self.tb.read_end(self.channel_ctrl, 2, self.tb.labprompt)

        ret = self.get_power_state(boardname)
        return ret

#TODO not finish tested yet, as board was not accesible
    def connect_to_laptop(self, board_prompt):
        """ connect to a board over an laptop starting
            kermit on it.
            return: True on success
            False else
        """
        self.tb.lab_con_laptop_ip = "hs@onb"
        logging.info("Connect to Laptop")
        self.tb.write_stream("ssh " + self.tb.lab_con_laptop_ip)
        ret = self.tb.wait_answer('password:', 2)
        self.tb.debugprint ("RET ssh " + self.tb.lab_con_laptop_ip + " :", ret)
        if ret == False:
            logging.error("No ssh to %s", self.tb.lab_con_laptop_ip)
            self.tb.failure()

        self.tb.write_stream(self.tb.lab_con_laptop_pwd)
        ret = self.tb.wait_answer(self.tb.lap_prompt, 2)
        if ret == False:
            logging.error("No ssh to ",self.tb.lab_con_laptop_ip)
            self.tb.failure()

        # start kermit
        logging.debug("Start Kermit")

        self.tb.write_stream("kermit")
        ret = self.tb.wait_answer('C-Kermit>', 10)
        if ret == False:
            logging.error("Could not start kermit")
            self.tb.failure()

        self.tb.write_stream("set line " + self.tb.kermit_line)
        ret = self.tb.wait_answer('C-Kermit>', 2)
        if ret == False:
            logging.error("Could not set line %s", self.tb.kermit_line)
            self.tb.failure()

        self.tb.write_stream("set speed " + self.tb.kermit_speed)
        ret = self.tb.wait_answer('C-Kermit>', 2)
        if ret == False:
            logging.error("Could not set speed %s", self.tb.kermit_speed)
            self.tb.failure()

        self.tb.write_stream("set flow-control none")
        ret = self.tb.wait_answer('C-Kermit>', 2)
        if ret == False:
            logging.error("Could not set flow")
            self.tb.failure()

        self.tb.write_stream("set carrier-watch off")
        ret = self.tb.wait_answer('C-Kermit>', 2)
        if ret == False:
            loggging.error("Could not set carrier")
            self.tb.failure()

        self.tb.write_stream("connect")
        ret = self.tb.wait_answer('options', 2)
        if ret == False:
            loggging.error("Could not connect")
            self.tb.failure()
        return True

    def connect_to_board(self, boardname):
        """ connect to the board
        """
        tmp = "connect to board " + boardname
        logging.debug(tmp)

	if boardname == 'pxm50':
            ret = self.connect_to_laptop(boardname)
            return ret

        tmp = "connect " + boardname
        ret = self.tb.write_stream(self.channel_con, tmp)
        if not ret:
            return ret

        ret = self.tb.wait_answer(self.channel_con, "Connect", 50)
        if not ret:
            return ret

        reg = re.compile("not accessible")
        reg2 = re.compile("Locked by process")
        reg3 = re.compile("noautoboot")
        reg4 = re.compile("autoboot")
        reg5 = re.compile("Connection closed")
        i = 0
        retry = 3
        while(i < retry):
            ret = self.tb.read_line(self.channel_con, 1)
            if ret == None:
                i += 1
                continue

            res = reg.search(self.tb.buf[self.channel_con])
            if res:
                return False
            res = reg2.search(self.tb.buf[self.channel_con])
            if res:
                return False
            res = reg3.search(self.tb.buf[self.channel_con])
            if res:
                tmp = 'noautoboot'
                ret = self.tb.write_stream(self.channel_con, tmp)
                i = 0
                continue

            res = reg4.search(self.tb.buf[self.channel_con])
            if res:
                i = 0
                self.tb.send_ctrl_m(self.tb.channel_con)

            res = reg5.search(self.tb.buf[self.channel_con])
            if res:
                return False

        logging.info("connected to %s", boardname)
        return True

    def get_board_connection_state(self, boardname):
        """ get the connection state to the board ToDo
        """
        ret = True
        tmp = "connection state to board " + boardname + " is " + ret
        logging.debug(tmp)
        return ret

    def get_board_state(self, name):
        """ Get boardstate of the board in the lab
            if it send a response if return is pressed
        """
        tmp = "get board state " + name
        logging.info(tmp)
        return True

    def set_board_state(self, state):
        """ set the board to a state
        """
        tmp = "set board to state " + state
        logging.debug(tmp)
        ret = None

        if state == 'u-boot':
            ret = state_uboot.u_boot_set_board_state(self.tb, state, 10)

        if state == 'lab':
            return True

        if state == 'linux':
            ret = state_linux.linux_set_board_state(self.tb, state, 10)

        if ret == None:
            logging.info("Unknown boardstate: %s", state)
            self.failure()

        if ret == False:
            self.failure()

        return True
