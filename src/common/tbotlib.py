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
import imp
import importlib
import inspect
import pexpect
from tbot_event import events
from tbot_connection_paramiko import Connection

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

    all begins here ...


    - **parameters**, **types**, **return** and **return types**::
    :param arg1: workdir for tbot
    :param arg2: labfile
    :param arg3: board config file
    :param arg4: name of logfile
    :param arg5: be verbose
    """
    def __init__(self, workdir, labfile, cfgfile, logfilen, verbose):
        ## enable verbose output
        self.verbose = verbose
        self.cfgfile = cfgfile
        self.workdir = workdir
        self.power_state = 'undef'
        self.tc_stack = []
        self.tc_stack_arg = []
        self.donotlog = False

        print("CUR WORK PATH: ", self.workdir)
        print("CFGFILE ", self.cfgfile)
        # add config to sys path
        sys.path.append(self.workdir + '/config')

        # load board config
        try:
            self.config = importlib.import_module(cfgfile)
        except ImportError:
            print("board cfg file %s not found" % cfgfile)
            sys.exit(1)

        # load lab settigs ...
        self.overwrite_config(labfile)

        # load default settigs ...
        self.overwrite_config('default_vars')

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
        from state_uboot import u_boot_set_board_state
        from state_linux import linux_set_board_state
        self.setboardstate_uboot = locals()['u_boot_set_board_state']
        self.setboardstate_linux = locals()['linux_set_board_state']
        try:
            self.tc_dir
        except AttributeError:
            self.tc_dir = self.workdir + '/src/tc'

        self._main = 0
        self._ret = False

        self.con_loglevel = 25
        logging.addLevelName(self.con_loglevel, "CON")
        if (self.config.loglevel == 'CON'):
            logformat = '# %(message)s'
        else:
            logformat = '%(asctime)s:%(levelname)-7s:%(module)-10s# %(message)s'

        logging.basicConfig(format=logformat, filename=self.logfilen, filemode='w')
        l = logging.getLogger()
        l.setLevel(self.config.loglevel)
        logging.info("*****************************************")
        logging.info('Started logging @  %s', now.strftime("%Y-%m-%d %H:%M"))
        logging.info('working directory %s', self.workdir)
        logging.info('testcase directory %s', self.tc_dir)
        sys.path.append(self.workdir)

        # create connection handles
        self.c_con = Connection(self, "tb_con")
        self.c_ctrl = Connection(self, "tb_ctrl")

        self.event = events(self, 'log/event.log')
        self.event.create_event('main', self.config.boardname, "Boardname", True)

        self.wdtdir = self.workdir + "/wdt"
        if not os.path.exists(self.wdtdir):
            os.makedirs(self.wdtdir)

        self.wdtfile = self.wdtdir + "/" + self.cfgfile + ".wdt"
        self.tbot_start_wdt()

        # try to connect with ssh
        self.check_open_fd(self.c_ctrl)
        self.check_open_fd(self.c_con)

        # try to get the console of the board
        ret = self.connect_to_board(self.config.boardname)
        if ret == False:
            sys.exit(1)

    def __del__(self):
        time.sleep(1)

    def overwrite_config(self, filename):
        try:
            overwrite_config = importlib.import_module(filename)
        except ImportError:
            print("cfg %s not found" % filename)
            sys.exit(1)

        # fix 'config.'
        for ov in overwrite_config.__dict__.items():
            found = False
            if not ov[0].startswith('__'):
                # search ov[0] in config
                for cf in self.config.__dict__.items():
                    if cf[0] == ov[0]:
                        # found, do not overwrite
                        found = True
                        break
            else:
                continue

            if found:
                continue

            self.config.__dict__.update({ov[0] : ov[1]})

        for ov in self.config.__dict__.items():
            tmp = ov[1]
            if type(ov[1]) is str:
                if ov[1].startswith('config.'):
                    tp = tmp.split('.')
                    fd = False
                    for cf in self.config.__dict__.items(): 
                        if cf[0] == tp[1]:
                            tmp = cf[1]
                            fd = True
                            break

                    if fd == False:
                        print("Error with config %s not found" % tp[1])
                    else:
                        self.config.__dict__.update({ov[0] : tmp})

    def cleanup(self):
        self.c_ctrl.cleanup()
        self.c_con.cleanup()

    def get_power_state(self, boardname):
        """ Get powerstate of the board in the lab

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: boardname
        :return: True if power state is on, else False
        """
        tmp = "get power state " + boardname + " using tc " + self.config.tc_lab_denx_get_power_state_tc
        logging.info(tmp)

        self.eof_call_tc(self.config.tc_lab_denx_get_power_state_tc)
        if self.power_state == 'on':
            return True
        return False

    def set_power_state(self, boardname, state):
        """ set powerstate for the board in the lab

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: boardname
        :param arg1: state on/off
        :type arg1: string
        :return: True if setting state was successful, else False
        """
        tmp = "get power state " + boardname + " using tc " + self.config.tc_lab_denx_power_tc
        logging.info(tmp)

        self.power_state = state
        self.eof_call_tc(self.config.tc_lab_denx_power_tc)
        ret = self.get_power_state(boardname)
        return ret

    def connect_to_board(self, boardname):
        """ connect to the board

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: boardname
        """
        if self.config.do_connect_to_board == False:
            tmp = "do not connect tot board"
            logging.debug(tmp)
            return True

        tmp = "connect to board " + boardname + " using tc " + self.config.tc_lab_denx_connect_to_board_tc
        logging.debug(tmp)

        try:
            save_workfd = self.workfd
        except AttributeError:
            save_workfd = self.c_ctrl

        self.workfd = self.c_con
        #self.tbot_expect_prompt(self.workfd)
        ret = self.call_tc(self.config.tc_lab_denx_connect_to_board_tc)
        self.workfd = save_workfd
        return ret

    def disconnect_from_board(self, boardname):
        """ disconnect from the board

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: boardname
        """
        tmp = "disconnect from board " + boardname + " using tc " + self.config.tc_lab_denx_disconnect_from_board_tc
        logging.debug(tmp)

        try:
            save_workfd = self.workfd
        except AttributeError:
            save_workfd = self.c_ctrl

        self.workfd = self.c_con
        ret = self.call_tc(self.config.tc_lab_denx_disconnect_from_board_tc)
        self.workfd = save_workfd
        return ret

    def get_board_state(self, name):
        tmp = "get board state " + name
        logging.info(tmp)
        return True

    def set_board_state(self, state):
        """ set the board to a state

        currrent states supported:
        'lab'
        'u-boot'
        'linux'

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: state string
        :return: True if switching to state had success
        else testcase fails.
        """
        tmp = "set board to state " + state
        logging.debug(tmp)
        ret = None

        if state == 'u-boot':
            ret = self.setboardstate_uboot(self, state, 5)

        if state == 'lab':
            return True

        if state == 'linux':
            ret = self.setboardstate_linux(self, state, 5)

        if ret == None:
            logging.info("Unknown boardstate: %s", state)
            self.end_tc(False)

        if ret == False:
            self.end_tc(False)

        return True

    def tbot_get_password(self, user, board):
        """get the password for the user/board

            The passwords are in the password.py file
            in the working directory. For example:
            if (user == 'passwordforuserone'):
                password = 'gnlmpf'
            if (user == 'anotheruser'):
                password = 'passwordforanotheruser'

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: user
        :param arg2: board
        :return:
            return password if found
            end tc if not
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
            logging.error("no password found for %s board: %s" % (user, board))
            print("no password found for %s board: %s" % (user, board))
            self.end_tc(False)

        return password

    def tbot_start_wdt(self):
        """start the WDT process

        """
        filepath = self.workdir + "/src/common/tbot_wdt.py"
        self.own_pid = str(os.getpid())
        self.tbot_trigger_wdt()
        self.wdt_process = subprocess.Popen(['python2.7', filepath, self.wdtfile, self.own_pid, self.logfilen, self.config.wdt_timeout], close_fds=True)
        atexit.register(self.wdt_process.terminate)

    def tbot_trigger_wdt(self):
        """trigger the WDT

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
        """checks if a debugger is attached

        If so, run the target. For this tc "tc_lab_bdi_run.py"
        is called.

        - **parameters**, **types**, **return** and **return types**::
        :return: True
        """
        if self.config.board_has_debugger:
            self.eof_call_tc("tc_lab_bdi_connect.py")
            self.eof_call_tc("tc_lab_bdi_run.py")
            self.eof_call_tc("tc_lab_bdi_disconnect.py")
        return True

    def failure(self):
        self.event.create_event('main', self.config.boardname, "BoardnameEnd", False)
        logging.info('End of TBOT: failure')
        self.statusprint("End of TBOT: failure")
        # traceback.print_stack()
        self._ret = False
        self.cleanup()
        sys.exit(1)

    def end_tc(self, ret):
        """ end testcase.

        simple end a testcase.

        ret contains True if testcase
        ended successfully, False if not.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: return value True/False
        :return: calls sys.exit(0 if ret == True 1 else)
        """
        self._ret = ret
        if self._main == 0:
            if self._ret:
                self.event.create_event('main', self.config.boardname, "BoardnameEnd", True)
                logging.info('End of TBOT: success')
                self.statusprint("End of TBOT: success")
                self.cleanup()
                sys.exit(0)
            else:
                self.failure()
        else:
            self.tc_stack_arg.pop()
            name = self.tc_stack.pop()
            if self._ret:
                logging.info('End of TC: %s success', name)
                logging.info('-----------------------------------------')
                sys.exit(0)
            logging.info('End False')
            sys.exit(1)

    def verboseprint(self, *args):
        """ print a verbose string on stdout.

            This output can be enabled through self.config.debug

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: argument list
        """
        if self.verbose:
            print("%s" % (args))

    def debugprint(self, *args):
        """ print a debug string on stdout.

            This output can be enabled through self.config.debug

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: argument list
        """
        if self.config.debug:
            print("%s" % (args))

    def statusprint(self, *args):
        """ print a status string on stdout.

            This output can be enabled through self.config.debugstatus

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: argument list
        """
        if self.config.debugstatus:
            print("%s" % (args))

    def con_log(self, *args):
        """logs a console string

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: console string
        :return:
        """
        logging.log(self.con_loglevel, *args)

    def check_open_fd(self, c):
        """check, if stream is open.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :return:
           True: If open
           False: If stream open failed
        """
        if c.created == True:
            return True

        if c == self.c_con:
            logname = 'log/ssh_tb_con.log'
        else:
            logname = 'log/ssh_tb_ctrl.log'

        passwd = self.tbot_get_password(self.config.user, self.config.ip)
        self.donotlog = True
        try:
            self.config.port
        except:
            self.config.port = '22'

        ret = c.create('not needed', logname, self.config.labprompt, self.config.user, self.config.ip, passwd, self.config.port)
        c.set_timeout(None)
        c.set_prompt(self.config.labsshprompt)
        self.tbot_expect_prompt(c)
        self.donotlog = False
        self.set_prompt(c, self.config.linux_prompt, 'linux')

        self.set_term_length(c)
        return True

    def read_line(self, c):
        """read a line. line end detected through '\n'

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :return:
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

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        """
        c.flush()
        log = c.get_log()

    def write_stream(self, c, string, send_console_start=True):
        """write a string to connection

           If stream is not open, try to open it

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: string
        :param arg3: call send_console_start before sending string, default True
        :return:
           True: if write was successful
           None: not able to open the stream
        """
        self.tbot_trigger_wdt()
        if send_console_start:
            self.send_console_start(c)
        c.send(string)
        return True

    def write_stream_passwd(self, c, user, board):
        """write a passwd for user to connection

           If stream is not open, try to open it
           Do not log it.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: user
        :param arg3: board
        :return:
           return:
           True: if write was successful
           None: not able to open the stream
        """
        self.tbot_trigger_wdt()

        string = self.tbot_get_password(user, board)
        c.send(string)
        self.event.create_event_log(c, "w", "password ********")
        # read until timeout
        #oldt = c.get_timeout()
        #c.set_timeout(2)
        #try:
        #    c.expect_string('#\$')
        #except:
        #    logging.debug("got prompt after passwd")

        #c.set_timeout(oldt)
        return True

    def write_stream_con(self, string):
        """write a string to console connection

           If stream is not open, try to open it

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: string
        :return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.write_stream(self.c_con, string)
        return ret

    def write_stream_ctrl(self, string):
        """write a string to the ctrl connection

           If stream is not open, try to open it

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: string
        :return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.write_stream(self.c_ctrl, string)
        return ret

    def send_console_start(self, c):
        """task before starting a tc

           send Ctrl-C besfore starting a Testcase

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :return:
           True: if write was successful
           None: not able to open the stream
        """
        self.send_ctrl_c(c)
        c.expect_prompt()
        return True

    def send_ctrl_c(self, c):
        """write Ctrl-C to the opened stream

           If stream is not open, try to open it

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :return:
        :return:
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

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :return:
           True: if write was successful
           None: not able to open the stream
        """
        ret = self.send_ctrl_c(self.c_con)
        return ret
 
    def send_ctrl_m(self, c):
        """write Ctrl-M to the opened stream

           If stream is not open, try to open it

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :return:
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
        """set the prompt for the connection c.

        If ptype = 'linux' add some special settings to the prompt.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: new promt string
        :param arg3: prompt type 'linux'
        :type arg3: string
        :return: True: If setting the prompt was successful
        False: If settting the prompt failed
        """
        ret = True
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
        try:
            c.termlength_set
        except:
            c.termlength_set = False
        c.termlength_set = False

        return ret

    def check_args(self, args):
        """Check if the args are in current argumentstack

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: args
        :return: If args no found, end testcase with False
        else return args argument
        """
        arg = self.tc_stack_arg[-1]
        name = self.tc_stack[-1]
        ok = True
        if arg is not None:
            for key in args:
                if arg.get(key) == None:
                    ok = False
                    print("%s arg %s not found" % (name, key))
                    logging.error("%s arg %s not found" % (name, key))

        if not ok:
            self.end_tc(False)

        return arg

    def call_tc(self, name, **kwargs):
        """Call another testcase.

           Search for the TC name
           through all subdirs in 'src/tc'.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: name of testcase
        :param arg2: optional testcase argumentlist
        :return:
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
        args = {}
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                args.update({key : value})

        self.tc_stack_arg.append(args)
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

    def eof_write(self, c, string, start=True):
        """ write a string to connection c

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: string
        :param arg3: start boolean, True, send console start before the
        cmdstring.
        :return: If write_stream returns not True, end tc
        with failure
        """
        if start:
            self.send_console_start(c)
        ret = c.sendcmd(string)
        self.tbot_trigger_wdt()
        if ret == True:
            return True
        self.end_tc(False)

    def eof_write_con(self, string, start=True):
        """ write a string to console.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: commandstring
        :param arg2: start boolean, True, send console start before the
        cmdstring.
        :return: True if write_stream returns True, else end testcase with False
        """
        ret = self.eof_write(self.c_con, string, start)
        return True
  
    def eof_write_cmd(self, c, command, start=True):
        """write a command to fd, wait for prompt

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: commandstring
        :param arg3: start boolean, True, send console start before the
        cmdstring.
        :return: True if prompt read, else end testcase with False
        """
        self.eof_write(c, command, start)
        self.tbot_expect_prompt(c)
        return True

    def eof_write_cmd_list(self, c, cmdlist, start=True):
        """send a list of cmd to fd and wait for end

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: list of commandstrings
        :param arg3: start boolean, True, send console start before the
        cmdstring.
        :return: True if prompt found else endtestcase with False
        """
        for tmp_cmd in cmdlist:
            self.eof_write_cmd(c, tmp_cmd, start)

    def write_lx_cmd_check(self, c, command, endTC=True, start=True):
        """write a linux command to console.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: commandstring
        :param arg3: if True and linux cmd ended False end TC
               with end_tc(False), else return True
        :param arg4: start boolean, True, send console start before the
        cmdstring.
        :return: if linux cmd ended successful True, else False
        """
        self.eof_write_cmd(c, command, start)
        tmpfd = self.workfd
        self.workfd = c
        ret = self.call_tc("tc_workfd_check_cmd_success.py")
        self.workfd = tmpfd
        if endTC == True:
            if ret == False:
                self.end_tc(False)
        return ret

    def eof_write_con_lx_cmd(self, command, start=True):
        """write a linux command to console.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: commandstring
        :return: True if linux command was successful
        else end testcase with False
        :param arg2: start boolean, True, send console start before the
        cmdstring.
        """
        self.write_lx_cmd_check(self.c_con, command, start)
        return True
 
    def eof_write_ctrl(self, string, start=True):
        """ write a string to control connection.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: commandstring
        :return: If write_stream returns not True, end tc with failure
        :param arg2: start boolean, True, send console start before the
        cmdstring.
        """
        ret = self.eof_write(self.c_ctrl, string, start)
        return True

    def eof_write_workfd_passwd(self, user, board):
        """ write a password to workfd. Do not log it.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: username
        :param arg2: board
        :return: If write_stream returns not True, end tc with failure
        """
        ret = self.write_stream_passwd(self.workfd, user, board)
        return True

    def set_term_length(self, c):
        """set terminal line length

        ToDo How could this be set longer and do this correct
        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :return: no return value
        """
        try:
            c.termlength_set
        except:
            c.termlength_set = False
        if c.termlength_set == False:
            tmp = 'stty cols ' + self.config.term_line_length
            self.eof_write(c, tmp, False)
            self.tbot_expect_prompt(c)
            self.eof_write(c, "export TERM=vt200", False)
            self.tbot_expect_prompt(c)
            self.eof_write(c, "echo $COLUMNS", False)
            self.tbot_expect_prompt(c)
            c.termlength_set = True

    def eof_call_tc(self, name, **kwargs):
        """ call tc name, end testcase on failure

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: name of Testcase
        :param arg2: optional argument list
        :return: True if called testcase ends True, als call end_tc(False)
        """
        ret = self.call_tc(name, **kwargs)
        if ret == True:
            return True
        self.end_tc(False)

    def write_cmd_check(self, c, cmd, string, start=True):
        """send a cmd and check if a string is read.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: command send over connection
        :param arg3: string which must be read
        :param arg4: start boolean, True, send console start before the
        cmdstring.
        :return: True if prompt and string is read
        else False
        """
        self.eof_write(c, cmd, start)
        searchlist = [string]
        tmp = True
        cmd_ok = False
        while tmp == True:
            ret = self.tbot_rup_and_check_strings(c, searchlist)
            if ret == '0':
                cmd_ok = True
            elif ret == 'prompt':
                tmp = False
        return cmd_ok

    def eof_write_cmd_check(self, c, cmd, string, start=True):
        """send a cmd and check if a string is read.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: commandstring
        :param arg3: string which must be read
        :param arg4: start boolean, True, send console start before the
        cmdstring.
        :return: True if prompt and string is read
        else end Testcase with False
        """
        ret = self.write_cmd_check(c, cmd, string, start)
        if ret == False:
            self.end_tc(False)

    def tbot_rup_and_check_strings(self, c, strings):
        """read until prompt and search, if a string in strings is found.

        If found, return index if read some chars, but no line,
        check if it is a prompt, return 'prompt' if it is a prompt.
        if a string in strings found return index
        else return None

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: a list of strings
        :return: index of string which is found
                 'prompt' if prompt found
        """
        ret = c.expect_string(strings)
        self.buf = c.get_log()
        return ret

    def tbot_fakult(self, n):
        if n < 0:
            raise ValueError
        if n == 0:
            return 1
        else:
            save = 1
            for i in range(2,n+1):
                save *= i
            return save

    def tbot_rup_check_all_strings(self, c, strings, endtc=False):
        """read until prompt, and check if all strings in list strings are found

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: a list of strings
        :return: returns False, if not all strings in list are
        found, or end tbot if endtc = True.
        """
        tmp = True
        cnt = len(strings)
        found = 0
        res = 0
        target = self.tbot_fakult(cnt)
        while tmp == True:
            ret = self.tbot_rup_and_check_strings(c, strings)
            if ret == 'prompt':
                tmp = False
            else:
                try:
                    nr = int(ret)
                except:
                    continue
                found += 1
                if res == 0:
                    res = (nr + 1)
                else:
                    res *= (nr + 1)

        if cnt != found:
            logging.error("Could not find all strings %d != %d", cnt, found)
            if endtc == True:
                self.end_tc(False)
            return False

        if res != target:
            logging.error("Could not find %d != %d", res, target)
            if endtc == True:
                self.end_tc(False)
            return False

        if endtc == True:
            self.end_tc(True)
        return True

    def tbot_rup_error_on_strings(self, c, strings, endtc=False):
        """read until prompt and check, if a string in list is found.

        If a string is found, end False.

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: list of strings
        :param arg3: if endtc = True end with calling end_tc(True/False)
        :return: True if prompt and no string is found.
        """
        tmp = True
        notfound = True
        while tmp == True:
            ret = self.tbot_rup_and_check_strings(c, strings)
            if ret == 'prompt':
                tmp = False
            else:
                try:
                    nr = int(ret)
                except:
                    continue
                logging.error("found string %d %s", nr, strings[nr])
                notfound = False

        if endtc == True:
            self.end_tc(notfound)

        return notfound

    def tbot_expect_prompt(self, c):
        """ searches for prompt, endless

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        """
        c.expect_prompt()
        self.buf = c.get_log()
        return True

    def tbot_expect_string(self, c, string):
        """ expect a string

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: string expected
        :return: 'prompt' if prompt found, True if string is found, else False
        """
        ret = c.expect_string(string)
        self.buf = c.get_log()
        return ret

    def eof_expect_string(self, c, string, wait_prompt=True):
        """ expect a string, if prompt read end tc False

        - **parameters**, **types**, **return** and **return types**::
        :param arg1: connection
        :param arg2: string expected
        :param arg3: boot If True wait after string is found for prompt
        """
        ret = self.tbot_expect_string(c, string)
        if ret == 'prompt':
            self.end_tc(False)
        if wait_prompt:
            self.tbot_expect_prompt(c)
        return True
