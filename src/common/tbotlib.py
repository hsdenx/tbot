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
import socket
import datetime
import re
import sys
import traceback
import os
from struct import *
import time
import importlib
#import serial

# paramiko/paramiko/packet.py
class tbot(object):
    def __init__(self, workdir, cfgfile, logfilen, verbose):
        ## enable debug output
        self.debug = False
        ## enable debugstatus output
        self.debugstatus = False
        ## enable verbose output
        self.verbose = verbose
        ## contains return value from a tc
        self.tc_return = True
        self.cfgfile = cfgfile
        self.workdir = workdir
        self.once = 1

        print("CUR WORK PATH: ", self.workdir)
        print("CFGFILE ", self.cfgfile)
        now = datetime.datetime.now()
        # load config file
        if logfilen == 'default':
            self.logfilen = 'log/' + now.strftime("%Y-%m-%d-%H-%M") + '.log'
        else:
            self.logfilen = logfilen
        if self.logfilen[0] != '/':
            # not absolute path, add workdir
            self.logfilen = self.workdir + '/' + self.logfilen
        print("LOGFILE ", self.logfilen)

        # open configuration file
        try:
            fd = open(self.workdir + '/' + self.cfgfile, 'r')
        except:
            logging.warning("Could not find %s", self.cfgfile)
            sys.exit(1)
        exec(fd)
        fd.close()

        # open defaultsettings for testcase variables
        self.def_var_file = 'tc_default_vars.py'
        try:
            fd = open(self.workdir + '/src/common/' + self.def_var_file, 'r')
        except:
            logging.warning("Could not find %s", self.def_var_file)
            sys.exit(1)
        exec(fd)
        fd.close()

        try:
            self.tc_dir
        except AttributeError:
            self.tc_dir = self.workdir + '/src/tc'

        self._main = 0
        self._ret = False
        self.__data = []
        self.__remainder = []
        self.buf = []

        #HACK
        self.channel_ctrl = 0
        self.channel_con = 1

        self.numeric_level = getattr(logging, self.loglevel.upper(), None)
        if not isinstance(self.numeric_level, int):
            raise ValueError('Invalid log level: %s' % self.loglevel)
        logging.basicConfig(format='%(asctime)s:%(levelname)-7s:%(module)-10s# %(message)s',
            filename=self.logfilen, filemode='w', level=self.numeric_level)
        logging.info("*****************************************")
        logging.info('Started logging @  %s', now.strftime("%Y-%m-%d %H:%M"))
        logging.info('working directory %s', self.workdir)
        logging.info('testcase directory %s', self.tc_dir)
        sys.path.append(self.workdir)

        # import lab api (the responsible python file must be included in *.cfg)
        lab = tbot_lab_api(self)
        self.lab = lab

        # open filedescriptor ToDo per function call also the fd in the lab
        self.__data.append('')
        self.__data.append('')
        self.__remainder.append('')
        self.__remainder.append('')
        self.buf.append('')
        self.buf.append('')

        self.check_state()

    def __del__(self):
        # without this timeout paramiko crashes sometimes with
        #   File "/usr/lib/python2.7/threading.py", line 551, in __bootstrap_inner
        #   File "/usr/lib/python2.7/dist-packages/paramiko/transport.py", line 1574, in run
        # <type 'exceptions.AttributeError'>: 'NoneType' object has no attribute 'error'
        # strange thing here, paramiko crashes before this code is reached
        # comment out this code also did not help ...
        time.sleep(1)

    def set_power_state(self, state):
        """ set the power state to state
            returns the state of the power
            True if on
            False if off
        """
        ret = self.lab.set_power_state(self.boardlabpowername, state)
        return ret

    def check_debugger(self):
        if self.board_has_debugger == 1:
            from lab_bdi import bdi_class
            bdi = bdi_class(self)
            bdi.bdi_connect()
            #read all pending chars from console
            self.read_end_state_con(2)
            bdi.send_bdi_cmd_wait_prompt(self.lab_bdi_upd_uboot_bdi_run)
            bdi.bdi_quit()

    def check_state(self):
        """ check the state of the connection to the board
        """
        # check if we have connection to the lab
        ret = self.lab.get_lab_connect_state()
        if ret == False:
            ret = self.lab.connect_lab()
            if ret != True:
                self.failure()

        # check if we have powered on the board
        ret = self.lab.get_power_state(self.boardlabpowername)
        if ret == False:
            ret = self.lab.set_power_state(self.boardlabpowername, "on")
            if ret != True:
                self.failure()

        # connect to the board
        ret = self.lab.connect_to_board(self.boardlabname)
        if ret == False:
            self.failure()
        return True

    def failure(self):
        logging.info('End of TBOT: failure %s', sys.exc_info()[0])
        self.statusprint("End of TBOT: failure")
        self._ret = False
        sys.exit(1)

    def end_tc(self, ret):
        """ end testcase.
            ret contains True if testcase
            ended successfully, False if not.
            Return: calls sys.exit(0 if ret == True 1 else)
        """
        self._ret = ret
        if self._main == 0:
            if self._ret:
                logging.info('End of TBOT: success')
                self.statusprint("End of TBOT: success")
                sys.exit(0)
            else:
                self.failure()
        else:
            if self._ret:
                logging.info('End of TC: %s success')
                logging.info('-----------------------------------------')
                sys.exit(0)
            logging.info('End False')
            sys.exit(1)

    def debugprint(self, *args):
        """ print a debug string on stdout.
            This output can be enabled through self.debug
        """
        if self.debug:
            print("%s" % (args))

    def statusprint(self, *args):
        """ print a status string on stdout.
            This output can be enabled through self.debugstatus
        """
        if self.debugstatus:
            print("%s" % (args))

    def _search_str(self, fd, retry, string):
        """ search string retry times with read_line
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
            ret = self.read_line(fd, self.read_line_retry)
            self.debugprint ("search_str ret, buf: ", ret, self.buf[fd])
            if ret:
                res = reg.search(self.buf[fd])
                if res:
                    return True
                else:
                    ret = False
            elif ret == False:
                res = reg.search(self.buf[fd])
                if res:
                    return True
            self.debugprint("RES: ", res)
            i += 1
        return ret

    def wait_answer(self, fd, string, retry):
        """ wait for identical answer retry times.
            return: True if found
                    else False
        """
        i = 0
        while (i < retry):
            ret = self.read_line(fd, self.read_line_retry)
            if ret == True:
                if (string == self.buf[fd]):
                    return True
                else:
                    reg = re.compile(string)
                    res = reg.search(self.buf[fd])
		    if res:
		        return True
            if ret == False:
                if (string == self.buf[fd]):
                    return True
                else:
                    reg = re.compile(string)
                    res = reg.search(self.buf[fd])
		    if res:
		        return True
            i += 1
	return False

    def wait_prompt(self, retry):
        """ wait for prompt retry times
            return: True if found
                    else False
        """
        ret = self._search_str(self.channel_con, retry, self.prompt)
        if ret == True:
            return True

	return False

    def eof_wait_prompt(self, retry):
	""" wait for prompt retry times
	    return: True if found
                    else end testcase
	"""
        ret = self._search_str(self.channel_con, retry, self.prompt)
        if ret == True:
            return True

        self.end_tc(False)

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
        self.write_stream(self.channel_con, self.user)
        # send passwd
        ret = self._search_str(5, 'login')
        return ret

    def check_open_fd(self, fd):
        """check, if stream is open.
           return:
           True: If open
           False: If stream open failed
        """
        ret = True
	if self.lab.get_lab_connect_state() == False:
            logging.debug("not connected to lab")
            ret = self.lab.connect_lab()

        #ToDo check here the specific fd
	if self.lab.lab_check_fd(fd) == False:
            logging.debug("fd not valid")
            return False

	return ret

    def read_bytes(self, fd):
        """read bytes from stream.
           if stream is not open, open it
           return:
           True: If bytes read
           None: Timeout, no bytes read
           self.__data contains the read bytes
        """
        logging.debug("read_bytes %d: rem: %s", fd, self.__remainder[fd])
        if self.__remainder[fd] != '':
            self.__data[fd] = self.__remainder[fd]
            self.__remainder[fd] = ''
            logging.debug("read_bytes %d: rem: %s after", fd, self.__remainder[fd])
            return True
        self.__data[fd] = ''
        ret = self.check_open_fd(fd)
        if not ret:
            logging.debug("read_bytes: Could not open")
            return None
        ret = self.lab.recv(fd)
        if ret == True:
            self.__data[fd] = self.lab.get_bytes(fd)
        return ret

    def read_line(self, fd, retry):
        """read a line. line end detected through '\n'
           return:
           True: if a line is read
                 self.buf contains the line
           False:if timeout while reading, and some bytes
                 are read
           None: Timeout, no line read
        """
        i = 0
        self.buf[fd] = ''
        #lineend = '\n'
        lineend = pack('h', 13)
        lineend = lineend[:1]
        logging.debug("------------ lineend %s", lineend)
        while not lineend in self.buf[fd]:
            ret = self.read_bytes(fd)
            logging.debug("read_line i: %d re: %d ret: %s", i, retry, ret)
            if ret:
                logging.debug("read_line data: %s", self.__data[fd])
                self.buf[fd] += self.__data[fd]
                i = 0
            else:
		i += 1
                if (i > retry):
                    if (len(self.buf[fd]) > 0):
                        logging.info("read no ret %s %s", fd, self.buf[fd])
                        if self.verbose:
                            print("read %d: %s" % (fd, self.buf[fd]))
                        return False
                    return None

        n = self.buf[fd].index(lineend)
        self.__remainder[fd] = self.buf[fd][n+1:]
        self.buf[fd] = self.buf[fd][:n]
        # remove previous new line
        if (len(self.buf[fd]) > 1) and (self.buf[fd][0] == '\n'):
            self.buf[fd] = self.buf[fd][1:]
        logging.debug("read_line n: %d rem: %s", n, self.__remainder[fd])
        logging.info("read %d: %s", fd, self.buf[fd])
        if self.verbose:
            print("read %d: %s" % (fd, self.buf[fd].replace("\n", "")))
        return True

    def flush_fd(self, fd):
        while True:
            ret = self.read_line(fd, 1)
            if not ret:
                if (len(self.buf[fd])) == 0:
                    return False

    def flush_con(self):
        """ read out all chars in console fd
        """
        self.flush_fd(self.channel_con)

    def flush_ctrl(self):
        """ read out all chars in ctrl fd
        """
        self.flush_fd(self.channel_ctrl)

    def read_end(self, fd, retry, prompt):
        """read until end is detected. End is detected if
           shell prompt is read.
        """
        while True:
            i = 0
            ret = self.read_line(fd, retry)
            logging.debug("read_end rl ret: %s buf: %s", ret, self.buf[fd])
            if not ret:
                if (len(self.buf[fd])) == 0:
                    if i > retry:
                        return False
                    else:
                        i += 1
                else:
                    ret = self.is_end(self.buf[fd], prompt)
                    if ret:
                        return True
                    else:
                        if i > retry:
                            return False
                        else:
                            i += 1
            else:
                i = 0
                ret = self.is_end(self.buf[fd], prompt)
                if ret:
                    return True

    def read_end_state(self, fd, retry):
        """read until end is detected. End is detected if
           current prompt is read.
        """
        while True:
            ret = self.read_line(fd, self.read_end_state_retry)
            logging.debug("read_end rl ret: %s buf: %s", ret, self.buf[fd])
            if ret == None:
                return False
            ret = self.is_end_fd(fd, self.buf[fd])
            if ret:
                return True

    def read_end_state_con(self, retry):
        ret = self.read_end_state(self.channel_con, retry)
        return ret

    def is_end(self, string, prompt):
        """check, if string contains a prompt
           return:
           True: if prompt is found
           False: if not found a prompt in string
        """
        reg = re.compile(prompt)
        res = reg.search(string)
        if res:
            logging.debug("Found end")
            return True
        return False
 
    def is_end_fd(self, fd, string):
        """check, if string contains a prompt
           return:
           True: if prompt is found
           False: if not found a prompt in string
        """
        if fd == self.channel_ctrl:
            ret = self.is_end(string, self.labprompt)
        if fd == self.channel_con:
            ret = self.is_end(string, self.prompt)

        return ret
    
    def write_stream(self, fd, string):
        """write a string to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.check_open_fd(fd)
        if not ret:
            logging.debug("write_stream: not open")
            return None
        
        self.lab.write(fd, string)
        #self.debugprint("str: %s len: %d\n", string, len(string))
        #for i in range(0, len(string)):
        #    self.lab.write(fd, string[i])

        logging.info("write %d: %s", fd, string)
        if self.verbose:
            print("write %d: %s" % (fd, string))
        # what I send must come also back!
        #ret = self.wait_answer(fd, string, 2)
        ret = self.wait_answer(fd, string, 2)
        #print ("REREAD send", ret)
        #TODO check return value
        return True

    def write_stream_passwd(self, fd, user, board):
        """write a passwd for user to the opened stream
           If stream is not open, try to open it
           Do not log it.
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.check_open_fd(fd)
        if not ret:
            logging.debug("write_stream: not open")
            return None

        string = self.lab.get_password(user, board)
        self.lab.write(fd, string)
        logging.info("write %d: password ********", fd)
        if self.verbose:
            print("write %d: password ********" % (fd))
        # what I send must come also back!
        ret = self.wait_answer(fd, string, 2)
        #TODO check return value
        return True

    def write_stream_con(self, string):
        """write a string to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.write_stream(self.channel_con, string)
        return ret

    def write_stream_ctrl(self, string):
        """write a string to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.write_stream(self.channel_ctrl, string)
        return ret

    def send_console_end(self, fd):
        """write Ctrl-C to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.check_open_fd(fd)
        if not ret:
            logging.debug("send_Ctrl_console_end: not open")
            return None
        string = pack('h', 29)
        string = string[:1]
        logging.debug("send Ctrl-console_end %s", string)
        self.lab.write_no_ret(string, fd)
        return True

    def send_ctrl_c(self, fd):
        """write Ctrl-C to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.check_open_fd(fd)
        if not ret:
            logging.debug("send_Ctrl_C: not open")
            return None
        string = pack('h', 3)
        string = string[:1]
        logging.debug("send Ctrl-C %s", string)
        self.lab.write_no_ret(fd, string)
        return True

    def send_ctrl_c_con(self):
        """write Ctrl-C to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.send_ctrl_c(self.channel_con)
        return ret
 
    def send_ctrl_m(self, fd):
        """write Ctrl-M to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.check_open_fd(fd)
        if not ret:
            logging.debug("send_ctrl_M: not open")
            return None
        string = pack('h', 10)
        string = string[:1]
        logging.debug("send Ctrl-M %s", string)
        self.lab.write_no_ret(fd, string)
        return True

    def set_prompt(self, fd, prompt, header, end):
        """set the prompt on the target.
           True: If setting the prompt was successful
           False: If settting the prompt failed
        """
        ret = True
        while ret:
            ret = self.read_line(fd, 1)
        # contains the current prompt
        self.prompt = prompt
        cmd = header + self.prompt + end
        logging.debug("Prompt CMD:%s", cmd)
        ret = self.write_stream(fd, cmd)
        if not ret:
            return ret
        ret = self.read_end(fd, 2, prompt)
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
        filepath = self.tc_dir + "/" + name
        logging.debug("call_tc filepath %s", filepath)
	try:
            fd = open(filepath, 'r')
	except IOError:
            logging.warning("Could not find tc name: %s", name)
            return False
        tb = self
        ret = False
        logging.info("*****************************************")
        logging.info("Starting with tc %s", name)
        self._main += 1
        try:
	    exec(fd)
        except SystemExit:
            ret = self._ret
            logging.debug("tc %s exception ret: %s", name, ret)
        except:
            logging.debug("tc %s exception", name)
            traceback.print_exc(file=sys.stdout)
            fd.close()
            self._main -= 1
            return False

        fd.close()
        self._main -= 1
        logging.debug("End of tc %s with ret: %s", name, ret)
        return ret

    def set_board_state(self, state):
        """ set the board in a state
        """
        tmp = "set board to state " + state
        logging.debug(tmp)

        ret = self.lab.set_board_state(state)
        if ret == True:
            return True

        self.failure()

    def eof_write(self, fd, string):
        """ write a string to filedescriptor fd.
            If write_stream returns not True, end tc
            with failure
        """
        self.read_end_state(fd, 1)
        ret = self.write_stream(fd, string)
        if ret == True:
            return True
        self.end_tc(False)

    def eof_wait_string(self, string, retry):
        """ wait for a string, until prompt is read
	    return: True if found
	            else False
        """
        ret = wait_answer(self, self.channel_con, string, retry)
        return ret

    def eof_write_con(self, string):
        """ write a string to console.
            If write_stream returns not True, end tc
            with failure
        """
        ret = self.eof_write(self.channel_con, string)
        if self.once == 0:
            ret = self.eof_write(self.channel_con, string)
            self.once = 1

        return True

    def eof_write_con_lx_cmd(self, command):
        """ write a linux command to console.
            If linux command has success return True,
            else end tc with failure
        """
        self.eof_write_con(command)
        self.eof_read_end_state_con(1)
        self.eof_call_tc("tc_lx_check_cmd_success.py")
        return True
 
    def eof_write_ctrl(self, string):
        """ write a string to control.
            If write_stream returns not True, end tc
            with failure
        """
        ret = self.eof_write(self.channel_ctrl, string)
        return True

    def eof_write_con_passwd(self, user, board):
        """ write a passwd to console. Do not log it.
            If write_stream returns not True, end tc
            with failure
        """
        ret = self.write_stream_passwd(self.channel_con, user, board)
        return True

    def eof_write_ctrl_passwd(self, user, board):
        """ write a password to control. Do not log it.
            If write_stream returns not True, end tc
            with failure
        """
        ret = self.write_stream_passwd(self.channel_ctrl, user, board)
        return True

    def eof_read_end_state(self, fd, retry):
        """ read until end is detected. End is detected if
            current prompt is read. End testcase if read_end_state
            not returns True.
        """
        ret = self.read_end_state(fd, retry)
        if ret == True:
            return True
        self.end_tc(False)

    def eof_read_end_state_con(self, retry):
        """ read until end is detected. End is detected if
            current prompt is read. End testcase if read_end_state
            not returns True.
        """
        ret = self.eof_read_end_state(self.channel_con, retry)
        return True

    def eof_read_end_state_ctrl(self, retry):
        """ read until end is detected. End is detected if
            current prompt is read. End testcase if read_end_state
            not returns True.
        """
        ret = self.eof_read_end_state(self.channel_ctrl, retry)
        return True

    def eof_search_str_in_readline(self, fd, string, endtc):
        """ call read_line and search if it contains string
            return True if found, False if prompt found
            else end testcase
        """
        ret = self._search_str(fd, 1, string)
        while ret != None:
            if ret == True:
                return True
            if ret == False:
                #check if it is a prompt
                ret = self.is_end_fd(fd, self.buf[fd])
                if ret == True:
                    if endtc == 1:
                        self.end_tc(False)
                    else:
                        return False
            ret = self._search_str(fd, 1, string)

        if endtc == 1:
            self.end_tc(False)

        return None
 
    def eof_search_str_in_readline_lines(self, fd, lines, string):
        """ call read_line lines time and search if it contains string
            return True if found, end testcase if not
        """
        ret = self._search_str(fd, lines, string)
        if ret == True:
            return True
        self.end_tc(False)

    def eof_search_str_in_readline_lines_con(self, lines, string):
        """ call read_line lines time and search if it contains string
            return True if found, end testcase if not
        """
        ret = self.eof_search_str_in_readline_lines(self.channel_con, lines, string)
        return True

    def eof_search_str_in_readline_lines_ctrl(self, lines, string):
        """ call read_line lines time and search if it contains string
            return True if found, end testcase if not
        """
        ret = self.eof_search_str_in_readline_lines(self.channel_ctrl, lines, string)
        return True

    def eof_search_str_in_readline_con(self, string):
        """ call read_line and search string.
            if it contains string
            return True
            else end testcase
        """
        ret = self.eof_search_str_in_readline(self.channel_con, string, 1)
        return ret

    def eof_search_str_in_readline_ctrl(self, string):
        """ call read_line and search string.
            if it contains string
            return True
            else end testcase
        """
        ret = self.eof_search_str_in_readline(self.channel_ctrl, string, 1)
        return ret

    def search_str_in_readline_con(self, string):
        """ call read_line and search if it contains string
            return True if found, False if prompt found
            None if nothing found, timeout
        """
        ret = self.eof_search_str_in_readline(self.channel_con, string, 0)
        return ret

    def search_str_in_readline_ctrl(self, string):
        """ call read_line and search if it contains string
            return True if found, False if prompt found
            None if nothing found, timeout
        """
        ret = self.eof_search_str_in_readline(self.channel_ctrl, string, 0)
        return ret

    def eof_search_str_in_readline_end_con(self, string):
        """ call read_line and search if it contains string
            endtestcase if found, or timeout
            if prompt found True
        """
        ret = self.search_str_in_readline_con(string)
        if ret == True:
            self.end_tc(False)
        if ret == None:
            self.end_tc(False)

        return True

    def eof_search_str_in_readline_end_ctrl(self, string):
        """ call read_line and search if it contains string
            endtestcase if found, or timeout
            if prompt found True
        """
        ret = self.search_str_in_readline_ctrl(string)
        if ret == True:
            self.end_tc(False)
        if ret == None:
            self.end_tc(False)

        return True

    def readline_and_search_strings(self, fd, strings):
        """ read a line and search, if it contains a string
            in strings. If found, return index
            if read some chars, but no line, check if it
            is a prompt, return False if it is a prompt.
            else return None
        """
        ret = True
        while ret == True:
            ret = self.read_line(fd, self.read_line_retry)
            if ret == True:
                i = 0
                for string in strings:
                    reg = re.compile(string)
                    res = reg.search(self.buf[fd])
                    if res:
                        return i
                    i += 1
                ret = self.is_end_fd(fd, self.buf[fd])
                if ret == True:
                    return 'prompt'
                ret = True
            elif ret == False:
                #check if it is a prompt
                ret = self.is_end_fd(fd, self.buf[fd])
                if ret == True:
                    return 'prompt'
            elif ret == None:
                return None

    def set_term_length(self, fd):
        #terminal line length
        #ToDo How could this be set longer and do this correct
        #
        tmp = 'stty cols ' + self.term_line_length
        self.eof_write(fd, tmp)
        self.eof_read_end_state(fd, 1)
        self.eof_write(fd, "export TERM=vt200")
        self.eof_read_end_state(fd, 1)
        self.eof_write(fd, "echo $COLUMNS")
        self.eof_read_end_state(fd, 1)

    def eof_call_tc(self, name):
        """ call tc name, end testcase on failure
        """
        ret = self.call_tc(name)
        if ret == True:
            return True
        self.end_tc(False)
