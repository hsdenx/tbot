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
import subprocess
import atexit
import time
import importlib
import inspect
import pexpect
from tbot_event import events
from tbot_connection_paramiko import Connection
sys.path.append("src/lab_api/")
from state_uboot import u_boot_set_board_state
from state_linux import linux_set_board_state

escape_dict={'\a':r'\a',
           '\"':r'\"',
           '|':r'\|',
           '[':r'\[',
           ']':r'\]',
           '^':r'\^',
           '$':r'\$',
           '*':r'\*',
           '?':r'\?',
           ';':r'\;',
           '&':r'\&',
           '+':r'\+',
           '{':r'\{',
           '}':r'\}',
           '(':r'\(',
           ')':r'\)',
           '\0':r'\0',
           '\1':r'\1',
           '\2':r'\2',
           '\3':r'\3',
           '\4':r'\4',
           '\5':r'\5',
           '\6':r'\6',
           '\7':r'\7',
           '\8':r'\8',
           '\9':r'\9'}

def raw(text):
    """Returns a raw string representation of text"""
    return "".join([escape_dict.get(char,char) for char in text])

class tbot(object):
    """ The tbot class

    more details follow
    """
    def __init__(self, workdir, cfgfile, logfilen, verbose):
        """
        :param workdir: workdir for tbot
        :param cfgfile: board config file
        :param logfilen: name of logfile
        :param verbose: be verbose
        :return:
        """
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
        self.power_state = 'undef'
        self.tc_stack = []
        self.donotlog = False

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

        sys.path.append(self.workdir + "/src/lab_api")
        # open configuration file
        try:
            fd = open(self.workdir + '/' + self.cfgfile, 'r')
        except:
            # try in 'config'
            try:
                fd = open(self.workdir + '/config/' + self.cfgfile, 'r')
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

        self.con_loglevel = 25
        logging.addLevelName(self.con_loglevel, "CON")
        if (self.loglevel == 'CON'):
            logformat = '# %(message)s'
        else:
            logformat = '%(asctime)s:%(levelname)-7s:%(module)-10s# %(message)s'

        logging.basicConfig(format=logformat, filename=self.logfilen, filemode='w')
        l = logging.getLogger()
        l.setLevel(self.loglevel)
        logging.info("*****************************************")
        logging.info('Started logging @  %s', now.strftime("%Y-%m-%d %H:%M"))
        logging.info('working directory %s', self.workdir)
        logging.info('testcase directory %s', self.tc_dir)
        sys.path.append(self.workdir)

        # create connection handles
        self.c_con = Connection(self, "tb_con")
        self.c_ctrl = Connection(self, "tb_ctrl")

        self.event = events(self, 'log/event.log')
        self.event.create_event('main', self.boardname, "Boardname", True)

        self.wdtfile = self.workdir + "/" + self.cfgfile + ".wdt"
        self.tbot_start_wdt()

        # try to connect with ssh
        self.check_open_fd(self.c_ctrl)
        self.check_open_fd(self.c_con)

        # try to get the console of the board
        ret = self.connect_to_board(self.boardname)
        if ret == False:
            sys.exit(1)

    def __del__(self):
        """
        cleanup
        :return:
        """
        time.sleep(1)

    def cleanup(self):
        """
        cleanup
        :return:
        """
        self.c_ctrl.cleanup()
        self.c_con.cleanup()

    def get_power_state(self, boardname):
        """ Get powerstate of the board in the lab
        """
        tmp = "get power state " + boardname + " using tc " + self.tc_lab_denx_get_power_state_tc
        logging.info(tmp)

        self.call_tc(self.tc_lab_denx_get_power_state_tc)
        if self.power_state == 'on':
            return True
        return False

    def set_power_state(self, boardname, state):
        """ set powerstate for the board in the lab
        """
        tmp = "get power state " + boardname + " using tc " + self.tc_lab_denx_power_tc
        logging.info(tmp)

        self.power_state = state
        self.call_tc(self.tc_lab_denx_power_tc)
        ret = self.get_power_state(boardname)
        return ret

    def connect_to_board(self, boardname):
        """ connect to the board
        """
        if self.do_connect_to_board == False:
            tmp = "do not connect tot board"
            logging.debug(tmp)
            return True

        tmp = "connect to board " + boardname + " using tc " + self.tc_lab_denx_connect_to_board_tc
        logging.debug(tmp)

        try:
            save_workfd = self.workfd
        except AttributeError:
            save_workfd = self.c_ctrl

        self.workfd = self.c_con
        #self.tbot_expect_prompt(self.workfd)
        ret = self.call_tc(self.tc_lab_denx_connect_to_board_tc)
        self.workfd = save_workfd
        return ret

    def disconnect_from_board(self, boardname):
        """ disconnect from the board
        """
        tmp = "disconnect from board " + boardname + " using tc " + self.tc_lab_denx_disconnect_from_board_tc
        logging.debug(tmp)

        try:
            save_workfd = self.workfd
        except AttributeError:
            save_workfd = self.c_ctrl

        self.workfd = self.c_con
        ret = self.call_tc(self.tc_lab_denx_disconnect_from_board_tc)
        self.workfd = save_workfd
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
            ret = u_boot_set_board_state(self, state, 8)

        if state == 'lab':
            return True

        if state == 'linux':
            ret = linux_set_board_state(self, state, 5)

        if ret == None:
            logging.info("Unknown boardstate: %s", state)
            self.failure()

        if ret == False:
            self.failure()

        return True

    def tbot_get_password(self, user, board):
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
        filename = self.workdir + "/password.py"
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
            logging.error("no password found for %s", user)
            self.end_tc(False)

        return password

    def tbot_start_wdt(self):
        """
        start the WDT process
        :return:
        """
        filepath = self.workdir + "/src/common/tbot_wdt.py"
        self.own_pid = str(os.getpid())
        self.tbot_trigger_wdt()
        self.wdt_process = subprocess.Popen(['python2.7', filepath, self.wdtfile, self.own_pid, self.logfilen, self.wdt_timeout], close_fds=True)
        atexit.register(self.wdt_process.terminate)

    def tbot_trigger_wdt(self):
        """
        trigger the WDT
        :return:
        """
        try:
            fd = open(self.wdtfile, 'w')
        except IOError:
            logging.warning("Could not open: %s", self.wdtfile)
            sys.exit(1)
        fd.seek(0, 0)
        line = str(int(time.time()))
        fd.write(line)
        fd.close()

    def check_debugger(self):
        """
        checks if a debugger is attached, and if so,
        run the target. For this tc "tc_lab_bdi_run.py"
        is called.
        :return: True
        """
        if self.board_has_debugger:
            self.eof_call_tc("tc_lab_bdi_connect.py")
            self.eof_call_tc("tc_lab_bdi_run.py")
            self.eof_call_tc("tc_lab_bdi_disconnect.py")
        return True

    def failure(self):
        logging.info('End of TBOT: failure %s', sys.exc_info()[0])
        self.statusprint("End of TBOT: failure")
        #traceback.print_stack()
        self._ret = False
        self.cleanup()
        sys.exit(1)

    def end_tc(self, ret):
        """ end testcase.
            ret contains True if testcase
            ended successfully, False if not.
            Return: calls sys.exit(0 if ret == True 1 else)
        """
        self._ret = ret
        if self._main == 0:
            self.event.create_event('main', self.boardname, "BoardnameEnd", True)
            if self._ret:
                logging.info('End of TBOT: success')
                self.statusprint("End of TBOT: success")
                self.cleanup()
                sys.exit(0)
            else:
                self.failure()
        else:
            name = self.tc_stack.pop()
            if self._ret:
                logging.info('End of TC: %s success', name)
                logging.info('-----------------------------------------')
                sys.exit(0)
            logging.info('End False')
            sys.exit(1)

    def verboseprint(self, *args):
        if self.verbose:
            print("%s" % (args))

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

    def con_log(self, *args):
        """
        logs a console string
        :param args: console string
        :return:
        """
        logging.log(self.con_loglevel, *args)

    def check_open_fd(self, c):
        """check, if stream is open.
           return:
           True: If open
           False: If stream open failed
        """
        if c.created == True:
            return True

        if c == self.c_con:
            logname = 'log/ssh_tb_con.log'
        else:
            logname = 'log/ssh_tb_ctrl.log'

        passwd = self.tbot_get_password(self.user, self.ip)
        self.donotlog = True
        ret = c.create('not needed', logname, self.labprompt, self.user, self.ip, passwd)
        c.set_timeout(None)
        c.set_prompt(self.labsshprompt)
        self.tbot_expect_prompt(c)
        self.donotlog = False
        self.set_prompt(c, self.linux_prompt, 'linux')

        self.set_term_length(c)
        return True

    def read_line(self, c):
        """read a line. line end detected through '\n'
           return:
           True: if a line is read
                 self.buf contains the line
           False :if prompt read
        """
        ret = c.expect_string(c.lineend)
        self.buf = c.get_log()
        if ret == '0':
            return True
        return False

    def flush(self, c):
        """ read out all bytes from connection
        """
        c.flush()
        log = c.get_log()

    def write_stream(self, c, string):
        """write a string to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        self.tbot_trigger_wdt()
        c.send(string)
        return True

    def write_stream_passwd(self, c, user, board):
        """write a passwd for user to the opened stream
           If stream is not open, try to open it
           Do not log it.
           return:
           True: if write was successful
           None: not able to open the stream
        """
        self.tbot_trigger_wdt()

        string = self.tbot_get_password(user, board)
        c.send(string)
        self.event.create_event_log(c, "w", "password ********")
        try:
            c.expect_string(string)
        except:
            print("Exception was thrown")
            print("debug information:")
            print(str(self.h))
            return False

        # read until timeout
        oldt = c.get_timeout()
        c.set_timeout(2)
        try:
            c.expect_string('#\$')
        except:
            loggin.debug("got prompt after passwd")
        
        c.set_timeout(oldt)
        return True

    def write_stream_con(self, string):
        """write a string to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.write_stream(self.c_con, string)
        return ret

    def write_stream_ctrl(self, string):
        """write a string to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.write_stream(self.c_ctrl, string)
        return ret

    def send_console_end(self, c):
        """write Ctrl-C to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.check_open_fd(c)
        if not ret:
            logging.debug("send_Ctrl_console_end: not open")
            return None
        string = pack('h', 29)
        string = string[:1]
        logging.debug("send Ctrl-console_end %s", string)
        self.write_stream(c, string)
        return True

    def send_ctrl_c(self, c):
        """write Ctrl-C to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.check_open_fd(c)
        if not ret:
            logging.debug("send_Ctrl_C: not open")
            return None
        string = pack('h', 3)
        string = string[:1]
        logging.debug("send Ctrl-C %s", string)
        c.send_raw(string)
        return True

    def send_ctrl_c_con(self):
        """write Ctrl-C to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.send_ctrl_c(self.c_con)
        return ret
 
    def send_ctrl_m(self, c):
        """write Ctrl-M to the opened stream
           If stream is not open, try to open it
           return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.check_open_fd(c)
        if not ret:
            logging.debug("send_ctrl_M: not open")
            return None
        string = pack('h', 10)
        string = string[:1]
        logging.debug("send Ctrl-M %s", string)
        self.write_stream(c, string)
        return True

    def set_prompt(self, c, prompt, ptype):
        """set the prompt on the target.
           True: If setting the prompt was successful
           False: If settting the prompt failed
        """
        if ptype == 'linux':
            header = 'export PS1="\u@\h [\$(date +%k:%M:%S)] ' 
            end = '"'
        else:
            header = ''
            end = ''

        # contains the current prompt
        c.set_prompt(prompt)
        if ptype == 'linux':
            cmd = header + prompt + end
            logging.debug("Prompt CMD:%s", cmd)
            ret = c.sendcmd(cmd)
            if ret:
                logging.info("set prompt:%s", cmd)

        c.expect_prompt()
        return ret

    def call_tc(self, name):
        """Call another testcase. Search for the TC name
           through all subdirs in 'src/tc'.
           return:
           False: If testcase was not found
                  or testcase raised an execption
           ! called testcase sets the ret variable, which
             this function returns. If called testcase
             not set the ret variable default is false!
        """
        for root, dirs, files in os.walk(self.tc_dir):
            filepath = root + "/" + name
            logging.debug("call_tc filepath %s", filepath)
            try:
                fd = open(filepath, 'r')
                if fd:
                    break
            except IOError:
                logging.debug("not found %s", filepath)

        try:
            if not fd:
                logging.warning("Could not find tc name: %s", name)
                return False
        except:
            logging.warning("Could not find tc name: %s", name)
            return False

        tb = self
        ret = False
        logging.info("*****************************************")
        logging.info("Starting with tc %s", filepath)
        self.tc_stack.append(filepath)
        self._main += 1
        pfname = inspect.getouterframes( inspect.currentframe() )[1][3]

        self.event.create_event(pfname, name, "Start", True)
        try:
            exec(fd)
        except SystemExit:
            ret = self._ret
            logging.debug("tc %s SystemExit exception ret: %s", name, ret)
        except:
            logging.debug("tc %s exception", name)
            traceback.print_exc(file=sys.stdout)
            ret = False

        fd.close()
        self._main -= 1
        self.event.create_event(pfname, name, "End", ret)
        logging.debug("End of tc %s with ret: %s", name, ret)
        return ret

    def eof_write(self, c, string):
        """ write a string to connection c
            If write_stream returns not True, end tc
            with failure
        """
        ret = c.sendcmd(string)
        if ret == True:
            return True
        self.end_tc(False)

    def eof_write_con(self, string):
        """ write a string to console.
            If write_stream returns not True, end tc
            with failure
        """
        ret = self.eof_write(self.c_con, string)
        return True
  
    def eof_write_cmd(self, c, command):
        """
        write a command to fd, wait for prompt
        :param fd: filedescriptor
        :param command: commandstring
        :return: True if prompt read
        end testcase with False else
        """
        self.eof_write(c, command)
        self.tbot_expect_prompt(c)
        return True

    def eof_write_cmd_list(self, c, cmdlist):
        """
        send a list of cmd to fd and wait for end
        :param fd: filedescriptor
        :param cmdlist: list of commandstrings
        :return: True if prompt found
        else endtestcase with False
        """
        for tmp_cmd in cmdlist:
            self.eof_write_cmd(c, tmp_cmd)

    def eof_write_lx_cmd_check(self, c, command):
        """
        write a linux command to console.
        :param fd: filedescriptor
        :param command: commandstring
        :return: True if linux command ended succesful
        else testase fails with False
        """
        self.eof_write_cmd(c, command)
        tmpfd = self.workfd
        self.workfd = c
        self.eof_call_tc("tc_workfd_check_cmd_success.py")
        self.workfd = tmpfd
        return True

    def eof_write_con_lx_cmd(self, command):
        """
        write a linux command to console.
        :param command: commandstring
        :return: True if linux command was successful
        else end testcase with False
        """
        self.eof_write_lx_cmd_check(self.c_con, command)
        return True
 
    def eof_write_ctrl(self, string):
        """ write a string to control.
            If write_stream returns not True, end tc
            with failure
        """
        ret = self.eof_write(self.c_ctrl, string)
        return True

    def eof_write_con_passwd(self, user, board):
        """ write a passwd to console. Do not log it.
            If write_stream returns not True, end tc
            with failure
        """
        ret = self.write_stream_passwd(self.c_con, user, board)
        return True

    def eof_write_ctrl_passwd(self, user, board):
        """ write a password to control. Do not log it.
            If write_stream returns not True, end tc
            with failure
        """
        ret = self.write_stream_passwd(self.c_ctrl, user, board)
        return True

    def eof_write_workfd_passwd(self, user, board):
        """ write a password to workfd. Do not log it.
            If write_stream returns not True, end tc
            with failure
        """
        ret = self.write_stream_passwd(self.workfd, user, board)
        return True

    def set_term_length(self, c):
        """
        set terminal line length
        ToDo How could this be set longer and do this correct
        :param fd: filedescritor
        :return:
        """
        tmp = 'stty cols ' + self.term_line_length
        self.eof_write(c, tmp)
        self.tbot_expect_prompt(c)
        self.eof_write(c, "export TERM=vt200")
        self.tbot_expect_prompt(c)
        self.eof_write(c, "echo $COLUMNS")
        self.tbot_expect_prompt(c)

    def eof_call_tc(self, name):
        """ call tc name, end testcase on failure
        """
        ret = self.call_tc(name)
        if ret == True:
            return True
        self.end_tc(False)

    def write_cmd_check(self, c, cmd, string):
        """
        send a cmd and check if a string is read.
        :param fd: filedescriptor
        :param cmd: commandstring
        :param string: string which must be read
        :return: True if prompt and string is read
        else False
        """
        self.eof_write(c, cmd)
        searchlist = [string]
        tmp = True
        cmd_ok = False
        while tmp == True:
            ret = self.tbot_read_line_and_check_strings(c, searchlist)
            if ret == '0':
                cmd_ok = True
            elif ret == 'prompt':
                tmp = False
        return cmd_ok

    def eof_write_cmd_check(self, c, cmd, string):
        """
        send a cmd and check if a string is read.
        :param fd: filedescriptor
        :param cmd: commandstring
        :param string: string which must be read
        :return: True if prompt and string is read
        else end Testcase with False
        """
        ret = self.write_cmd_check(c, cmd, string)
        if ret == False:
            self.end_tc(False)

    def tbot_read_line_and_check_strings(self, c, strings):
        """
        read a line and search, if it contains a string
        in strings. If found, return index
        if read some chars, but no line, check if it
        is a prompt, return 'prompt' if it is a prompt.
        if a string in strings found return index
        else return None
        :param c: filedescriptor used
        :param strings: a list of strings
        :return: index of string which is found
                 'prompt' if prompt found
        """
        ret = c.expect_string(strings)
        self.buf = c.get_log()
        return ret

    def tbot_expect_prompt(self, c):
        """ searches for prompt, endless
        """
        c.expect_prompt()
        self.buf = c.get_log()
        return True

    def tbot_expect_string(self, c, string):
        """ expect a string

        :return : 'prompt' if prompt found
                  string index which string is found
        """
        ret = c.expect_string(string)
        self.buf = c.get_log()
        return ret

    def eof_expect_string(self, c, string):
        """ expet a string, if prompt read end tc False
        """
        ret = self.tbot_expect_string(c, string)
        if ret == 'prompt':
            self.end_tc(False)
        self.tbot_expect_prompt(c)
        return True
