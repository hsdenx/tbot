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
# Copyright tbot Team Members
#
import paramiko
import logging
import socket
import datetime
import re
import sys
import os
from struct import *
import time
#import serial

# paramiko/paramiko/packet.py
class tbot(object):
    def __init__(self, cfgfile, logfilen):
	self.cfgfile = cfgfile
        self.workdir = os.getcwd()

        print("CUR WORK PATH: ", os.getcwd())
        print("CFGFILE ", self.cfgfile)
        now = datetime.datetime.now()
	if logfilen == 'default':
            self.logfilen = 'log/' + now.strftime("%Y-%m-%d-%H-%M") + '.log'
	else:
            self.logfilen = logfilen
        if self.logfilen[0] != '/':
            # not absolute path, add workdir
            self.logfilen = self.workdir + '/' + self.logfilen
        print("LOGFILE ", self.logfilen)
	try:
            fd = open(self.workdir + '/' + self.cfgfile, 'r')
	except:
            logging.warning("Could not find %s", self.cfgfile)
            sys.exit(1)
	exec(fd)
        fd.close()
        self.__remainder = ''
        self.ssh = None
        self._main = 0
        self._ret = False
	self.debug = 0
	self.debugstatus = 0

        self.numeric_level = getattr(logging, self.loglevel.upper(), None)
        if not isinstance(self.numeric_level, int):
            raise ValueError('Invalid log level: %s' % self.loglevel)
        logging.basicConfig(format='%(asctime)s:%(levelname)-7s:%(module)-10s# %(message)s',
            filename=self.logfilen, filemode='w', level=self.numeric_level)
        logging.info("*****************************************")
        logging.info('Started logging @  %s', now.strftime("%Y-%m-%d %H:%M"))
        self.opened = False
        self.reg = re.compile(self.prompt)
        sys.path.append(self.workdir)

    def __del__(self):
        # without this timeout paramiko crashes sometimes with
        #   File "/usr/lib/python2.7/threading.py", line 551, in __bootstrap_inner
        #   File "/usr/lib/python2.7/dist-packages/paramiko/transport.py", line 1574, in run
        # <type 'exceptions.AttributeError'>: 'NoneType' object has no attribute 'error'
        # strange thing here, paramiko crashes before this code is reached
        # comment out this code also did not help ...
        time.sleep(1)

    def end_tc(self, ret):
        """ end testcase. ret contains True if testcase
            ended successfully, False if not.
            Return: calls sys.exit(0 if ret == True 1 else)
        """
        self._ret = ret
        if self._main == 0:
            if self.opened:
                if self.use_tty:
                    pass
                else:
                    self.ssh.close()
            self.opened = False
            if self._ret:
                logging.info('End of TBOT: success')
                sys.exit(0)
            else:
                logging.info('End of TBOT: failure')
                sys.exit(1)
        else:
            if self._ret:
                logging.info('End of TC: success')
                sys.exit(0)
            logging.info('End False')
            sys.exit(1)

    def debugprint(self, *args):
        if self.debug:
            print(args)

    def statusprint(self, *args):
        if self.debugstatus:
            print(args)

    def _open_ssh(self):
        # look in paramiko/demos/demo_simple.py
        # for more infos how to use host keys ToDo
        if not self.ssh:
            self.ssh = paramiko.SSHClient()
        self.opened = False
        self.__remainder = ''
        if self.accept_all == True:
            #accept all host keys
            logging.info("AutoAddPolicy")
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.ssh.connect(self.ip, username=self.user, password=self.password)
        except:
            logging.info("no connection for %s@%s", self.user, self.ip)
            self.ssh.close()
            return None

        self.opened = True
        self.chan = self.ssh.invoke_shell()
        if self.debug:
            print repr(self.ssh.get_transport())
        logging.debug(self.ssh.get_transport())
        self.chan.settimeout(self.channel_timeout)

        logging.info("got connection for %s@%s", self.user, self.ip)
        self.count = 0
        # http://www.lag.net/paramiko/docs/paramiko.Transport-class.html#set_keepalive
        self.tr = self.get_transport()
        self.tr.set_keepalive(self.keepalivetimeout)
        self.set_prompt()
        self.ser = None
        return True

    def _search_str(self, retry, string):
        """ search string retry times
	    return:
	    True, if string found
	    False if something read, but string not found
	    None if nothing read, nothing found
	"""
        reg = re.compile(string)
	self.debugprint("search_str: str: ", string)
        i = 0
        while i < retry:
            res = None
            ret = self.read_line(1)
            self.debugprint ("search_str ret, buf: ", ret, self.buf)
            if ret:
                res = reg.search(self.buf)
		if res:
		    return True
	        else:
		    ret = False
	    elif ret == False:
                res = reg.search(self.buf)
		if res:
		    return True
            self.debugprint("RES: ", res)
            i += 1
        return ret

    def wait_answer(self, answer, retry):
	""" wait for answer retry times
	    return: True if found
	            else False
	"""
        i = 0
        while i < retry:
            ret = self._search_str(2, answer)
            if ret:
                return True
	    if ret == False:
	        i = 0
            i += 1
	return False

    def _login(self):
        # check if we need to login
        # if we logged in, set prompt
        # if we get no login, send ctrl-m ...
        j = 0
        retry = 5
        retry2 = 5
        while j < retry:
            self.send_ctrl_m()
            i = 0
            while i < retry2:
                ret = self._search_str(5, 'login')
                if ret:
                    i = retry2
                i += 1
            if ret:
                j = retry
            j += 1
        # got login
        # send user
        self.write_stream(self.user)
        # send passwd
        ret = self._search_str(5, 'login')
        return ret

    def _open_tty(self):
        self.ssh = None
        print("OPEN TTY")
        self.ser = serial.Serial(
            port=self.port,
            baudrate=self.baud,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1, # 0=nonblocking mode, n>0 seconds timeout
            bytesize=serial.SEVENBITS
        )
        self.ser.open()
        self.ser.isOpen()
        print("IS OPEN", self.ser.isOpen())
        print("READABLE: ", self.ser.readable())
        print("WRITEABLE: ", self.ser.writable())
        self.opened = True
        return self._login()

    def get_transport(self):
        if self.use_tty:
            print("get_transport ToDo")
        else:
            return self.ssh.get_transport()

    def is_active(self):
        if self.use_tty:
            return self.ser.isOpen()
        else:
            return self.tr.is_active()

    def get_channel(self):
        if not self.use_tty:
            return self.ssh.chan

    def _open_stream(self):
        if self.use_tty:
            ret = self._open_tty()
        else:
            ret = self._open_ssh()
        return ret

    def check_open_fd(self):
        """check, if stream is open.
           return:
           True: If open
           False: If stream open failed
        """
        ret = True
        if self.opened == False:
            logging.debug("channel not open")
            ret = self._open_stream()
        elif self.is_active() == False:
            logging.debug("channel not active")
            ret = self._open_stream()
	return ret

    def read_bytes(self):
        """read bytes from stream.
           if stream is not open, open it
           return:
           True: If bytes read
           None: Timeout, no bytes read
           self.__data contains the read bytes
        """
        logging.debug("read_bytes: rem: %s", self.__remainder)
        if self.__remainder != '':
            self.__data = self.__remainder
            self.__remainder = ''
            logging.debug("read_bytes: rem: %s after", self.__remainder)
            return True
        self.__data = ''
        ret = self.check_open_fd()
        if not ret:
            logging.debug("read_bytes: Could not open")
            return None
        if self.use_tty:
            try:
                print("REading")
                self.__data = self.ser.read(100)
                print("READ ", self.__data)
                if self.__data == '':
                    print("TIMEOUT")
                    return None
            except:
                logging.debug("read_bytes: Timeout")
                return None
        else:
            try:
                self.__data = self.chan.recv(1024)
            except socket.timeout:
                logging.debug("read_bytes: Timeout")
                return None
        return True

    def read_line(self, retry):
        """read a line. line end detected through '\n'
           return:
           True: if a line is read
                 self.buf contains the line
           False:if timeout while reading, and some bytes
                 are read
           None: Timeout, no line read
        """
        i = 0
        self.buf = ''
        while not '\n' in self.buf:
            ret = self.read_bytes()
            logging.debug("read_line i: %d re: %d ret: %s", i, retry, ret)
            if ret:
                self.buf += self.__data
                i = 0
            else:
		i += 1
                if (i > retry):
                    if (len(self.buf) > 0):
                        logging.info("read %s@%s: %s", self.user, self.ip,
				self.buf)
                        return False
                    return None

        n = self.buf.index('\n')
        self.__remainder = self.buf[n+1:]
        self.buf = self.buf[:n]
        if (len(self.buf) > 0) and (self.buf[-1] == '\r'):
            self.buf = self.buf[:-1]
        logging.info("read_line %s@%s: %s", self.user, self.ip, self.buf)
        return True

    def read_end(self, retry):
        """read until end is detected. End is detected if
           shell prompt is read.
        """
        ret = True
        while ret:
            ret = self.read_line(retry)
            logging.debug("read_end ret: %s buf: %s", ret, self.buf)
        ret = self.send_ctrl_m()
        if not ret:
            return ret
        while True:
            ret = self.read_line(retry)
            logging.debug("read_end rl ret: %s buf: %s", ret, self.buf)
            if not ret:
                if (len(self.buf)) == 0:
                    return False
            ret = self.is_end(self.buf)
            if ret:
                return True

    def is_end(self, string):
        """check, if string contains a prompt
           return:
           True: if prompt is found
           False: if not found a prompt in string
        """
        res = self.reg.search(string)
        if res:
            logging.debug("Found end")
        return res
    
    def write_stream(self, string):
        """write a string to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.check_open_fd()
        if not ret:
            logging.debug("write_stream: not open")
            return None

        logging.info("write %s@%s: %s", self.user, self.ip, string)
        if self.use_tty:
            self.ser.write(string + '\n')
        else:
            self.chan.send(string + '\n')
        return True

    def send_console_end(self):
        """write Ctrl-C to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.check_open_fd()
        if not ret:
            logging.debug("send_Ctrl_console_end: not open")
            return None
        string = pack('h', 29)
        logging.debug("send Ctrl-console_end %s", string)
        if self.use_tty:
            self.ser.write(string)
        else:
            self.chan.send(string)
        return True


    def send_ctrl_c(self):
        """write Ctrl-C to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.check_open_fd()
        if not ret:
            logging.debug("send_Ctrl_C: not open")
            return None
        string = pack('h', 3)
        logging.debug("send Ctrl-C %s", string)
        if self.use_tty:
            self.ser.write(string)
        else:
            self.chan.send(string)
        return True

    def send_ctrl_m(self):
        """write Ctrl-M to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.check_open_fd()
        if not ret:
            logging.debug("send_ctrl_M: not open")
            return None
        string = pack('h', 13)
        logging.debug("send Ctrl-M %s", string)
        if self.use_tty:
            self.ser.write(string)
        else:
            self.chan.send(string)
        return True

    def put(self, fr, to):
        """put the file fr to the target with file
           to.
           return:
           True: If put was successful
           False: If put failed
        """
        logging.debug("try put %s %s", fr, to)
        t = self.get_transport()
        sftp = paramiko.SFTPClient.from_transport(t)
        try:
            ret = sftp.put(fr, to)
        except:
            ret = False
		
        logging.info("sftp put %s -> %s ret: %s\n", fr, to, ret)
        return ret

    def set_prompt(self):
        """set the prompt on the target.
           True: If setting the prompt was successful
           False: If settting the prompt failed
        """
        ret = True
        while ret:
            ret = self.read_line(1)
        cmd = 'export PS1="\u@\h [\$(date +%k:%M:%S)] ' + self.prompt + '> "'
        logging.debug("Prompt CMD:%s", cmd)
        ret = self.write_stream(cmd)
        if not ret:
            return ret
        ret = self.read_end(1)
        if ret:
            logging.info("set prompt:%s", cmd)
        return ret

    def call_tc(self, name):
        """Call another testcase.
           return:
           False: If Calling the testcase was not found
                  or testcase raised an execption
           ! called testcase sets the ret variable, which
             this function returns. If called testcase
             not set the ret variable default is false!
        """
        filepath = self.workdir + "/" + name
	try:
            fd = open(filepath, 'r')
	except:
            logging.warning("Could not find tc name: %s", name)
            return False
        tb = self
        ret = False
        logging.info("Starting with tc %s", name)
        logging.info("*****************************************")
        self._main += 1
        try:
	    exec(fd)
        except SystemExit:
            ret = self._ret
            logging.debug("tc %s exception ret: %s", name, ret)
        except:
            logging.debug("tc %s exception", name)
            fd.close()
            self._main -= 1
            return False

        fd.close()
        self._main -= 1
        logging.info("End of tc %s with ret: %s", name, ret)
        return ret
