#
# SPDX-License-Identifier:     GPL-2.0+
#
# connection class with paramiko
# simple handle a connection
import logging
import paramiko
import socket
import traceback

class Connection(object):
    """ The connection class

    More details follow
    """
    def __init__(self, tb, name):
        """init of Connection class

        :param tb: tbot handle
        :param name: name of connection
        :return:
        """
        self.tb = tb
        self.name = name
        self.prompt = ''
        self.logfilename = ''
        self.lineend = '\n'
        self.created = False
        self.timeout = None
        self.keepalivetimeout = 1
        self.default_channel_timeout = 0.5
        self.channel_timeout = self.default_channel_timeout
        self.line_length = 200
        self.logbuf = ''
        self.ssh = False
        self.accept_all = True

    def open_paramiko(self, user, ip, passwd):
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

        logging.debug("try connection for %s@%s", user, ip)
        try:
            self.ssh.connect(ip, username=user, password=passwd)
        except:
            logging.warning("no connection for %s@%s", user, ip)
            self.ssh.close()
            return None

        self.opened = True
        self.data = ''

        # open shell
        self.channel = self.ssh.invoke_shell()
        logging.debug(self.ssh.get_transport())
        self.channel.settimeout(self.channel_timeout)
        return True

    def lab_recv(self):
        """ get bytes from connection
        """
        try:
            tmp = self.channel.recv(self.maxread)
        except socket.timeout:
            logging.debug("read_bytes: Timeout")
            return None

        logging.debug("%s read: %s", self.name, tmp)
        self.data += tmp
        return True

    def lab_write(self, string):
        if (len(string) > self.line_length):
            logging.debug("%s tooo long to write %s > %s", self.name,
                          len(string), self.line_length)
            return False

        se = string + self.lineend
        logging.debug("write %s: %s", self.name, se)
        self.channel.send(se)
        return True

    def lab_write_no_ret(self, string):
        if (len(string) > self.line_length):
            logging.debug("%s tooo long to write %s > %s", self.name,
                          len(string), self.line_length)
            return False

        logging.debug("write no ret %s: %s", self.name, string)
        self.channel.send(string)
        return True

    def create(self, cmd, logfilename, prompt, user, ip, passwd):
        """create a new connection

        :param cmd: cmd which is spawned
        :param logfilename: name of the logfile
        :return:
        """
        ret = self.open_paramiko(user, ip, passwd)
        if ret != True:
            return False

        self.logfilename = logfilename
        self.maxread = 1024
        self.prompt = prompt
        self.created = True
        return True

    def set_timeout(self, timeout):
        self.timeout = timeout
        if timeout != None:
            self.channel_timeout = timeout
            self.channel.settimeout(self.channel_timeout)
        else:
            self.channel_timeout = self.default_channel_timeout
            self.channel.settimeout(self.channel_timeout)

    def get_timeout(self):
        return self.timeout

    def set_line_length(self, length):
        self.line_length = length

    def get_line_length(self):
        return self.line_length

    def close(self):
        """close the opened connection

        :return:
        """

    def get_log(self):
        """ read the content of the logfile
        """
        ret = self.logbuf
        self.logbuf = ''
        return ret

    def get_prompt(self):
        """simple return the current prompt

        :return: string of current prompt
        """
        return self.prompt

    def set_prompt(self, newprompt):
        """set the new prompt string

        :param newprompt: string of new prompt
        :return:
        """
        self.prompt = newprompt
        return

    def set_lineend(self, lineend):
        """ set a new lineend

        :param lineend: the lineend
        :return:
        """
        self.lineend = lineend
        return

    def send_raw(self, string):
        """ send a string to the connection
            add no lineend
        """
        self.tb.event.create_event_log(self, "wr", string)
        return self.lab_write_no_ret(string)

    def send(self, string):
        """ send a string to the connection
            add lineend
        """
        se = string
        self.tb.event.create_event_log(self, "w", se + self.lineend)
        return self.lab_write(se)

    def sendcmd(self, cmd):
        """send a string to the connection
           add lineend, and check if string is
           reread.

        :param cmd: command to send
        :return: True if cmd is reread False else
        """
        ret = self.send(cmd)
        if ret != True:
            return ret
        ret = self.expect_string(cmd)
        if ret == 'prompt':
            return False
        if ret == 'exception':
            return False

        return True

    def expect_prompt(self):
        """expect prompt
        """
        ret = self.expect_string(self.prompt)
        return ret

    def _tolist(self, *args):
        x=[]
        for i in args:
            if isinstance(i, str):
                x.append(i)
            else:
                x += list(i)
        return x

    def __search_string(self, buf, string):
        """ search a string string in buf
        :return: string(index) where found, 'none'
        """
        i = 0
        #print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP START", self.name)
        #print("buf", buf)
        #print("string", string)
        #print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
        lens = len(string)
        bufl = len(buf)
        if bufl < lens:
            return 'none'
        #print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", lens, bufl)
        while (i < bufl):
            if buf[i] == string[0]:
                if lens == 1:
                    #print("EEEEEEEEEEEEEEEEE", str(i))
                    return str(i)

                s = i + 1
                j = 1
                while(j < lens):
                    if (s >= bufl):
                        return 'none'
                    if (j >= lens):
                        return 'none'
                    if buf[s] != string[j]:
                        break
                    j += 1
                    if j == lens:
                        #print("EEEEEEEEEEEEEEEEE", str(i))
                        return str(i)
                    s += 1
                    if s == bufl:
                        return 'none'
            i += 1

        #print("EEEEEEEEEEEEEEEEE none ")
        return 'none'

    def __search_strings(self, se):
        """ search in self.data if a string from se is found
        :return: 'none' if nothing is found, else str(index)
        """
        i = 0
        for tmp in se:
            ret = self.__search_string(self.data, tmp)
            if ret == 'none':
                i += 1
                continue
            # found index in self.data
            # copy self.data from 0 - index
            ind = int(ret)
            ind += len(tmp)
            self.logbuf = self.data[0:ind]
            self.data = self.data[ind:]
            return str(i)

        return 'none'

    def expect_string(self, string):
        """expect a string

        :param string:
        :return: return 'prompt' if prompt found
                        'exception' if exception occured
                        else string index
        """
        ign = ['==>']
        cnt_ign = len(ign)
        # search first ignore strings, then the string to
        # search, and at the end, search the prompt
        se = self._tolist(ign, string, self.prompt)
        #print("CCCCCC expectstring", se, cnt_ign)
        if self.data == '':
            # if we have no data, read it
            tmp = self.lab_recv()
            self.logbuf += self.data
            #print("CCCCCC expectstring now", ret, self.data)
            #print("CCCC timeout", self.timeout)
            if tmp == None and self.timeout != None:
                # ToDo give paramiko the timeout
                #print("CCCCCCC expectsrting labrecv", ret)
                self.tb.event.create_event_log(self, "re", 'exception')
                return 'exception'

        loop = True
        while(loop == True):
            ret = self.__search_strings(se)
            #print("CCCCC expectstring ret", ret)
            if ret == 'none':
                tmp = self.lab_recv()
                self.logbuf += self.data
                #print("CCCCC expectstring tmp", tmp, self.data)
                if tmp == None and self.timeout != None:
                    # ToDo give paramiko the timeout
                    #print("CCCCCCC expectsrting labrecv second", ret)
                    self.tb.event.create_event_log(self, "re", self.data)
                    return 'exception'
            elif ret < cnt_ign:
                self.tb.event.create_event_log(self, "ig", self.data)
            else:
                loop = False
        
        self.tb.event.create_event_log(self, "r", self.logbuf)
        count = len(se)
        count -= 1
        #print("CCCCCC ret", ret, count, cnt_ign, str(int(ret) - cnt_ign))
        if ret == str(count):
            return 'prompt'

        return str(int(ret) - cnt_ign)

    def flush(self):
        """ read out all bytes from connection
        """
        ret = True
        while (ret):
            ret = self.lab_recv()
        self.tb.event.create_event_log(self, "rf", self.data)
        self.data = ''
        return True
