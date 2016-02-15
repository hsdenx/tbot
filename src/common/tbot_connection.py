#
# SPDX-License-Identifier:     GPL-2.0+
#
# connection class
# simple handle a connection
import logging
import pexpect

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
        self.lineend = '\r\n'
        self.created = False

    def create(self, cmd, logfilename, prompt):
        """create a new connection

        :param cmd: cmd which is spawned
        :param logfilename: name of the logfile
        :return:
        """
        self.h = pexpect.spawn(cmd)
        if not self.h:
            return False
        self.logfilename = logfilename
        self.h.logfile = open(self.logfilename, "w")
        self.h.timeout = None
        self.maxread = 200
        self.prompt = prompt
        self.created = True
        return True

    def close(self):
        """close the opened connection

        :return:
        """

    def get_log(self):
        """ read the content of the logfile
        """
        try:
            self.logfilefd
        except:
            self.logfilefd = open(self.logfilename, 'r')
            self.logfilefd_pos = 0

        self.logfilefd.seek(self.logfilefd_pos)
        data = self.logfilefd.read()
        self.logfilefd_pos = self.logfilefd.tell()
        return data

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

    def send(self, string):
        """ send a string to the connection
        """
        se = string + self.lineend
        self.h.send(se)
        return True

    def sendcmd(self, cmd):
        """send a cmd to the connection

        :param cmd:
        :return:
        """
        cmdsend = cmd + self.lineend
        self.h.send(cmdsend)
        self.tb.event.create_event_log(self, "w", cmdsend)
        self.get_log()
        try:
            print("CCCCCCCCC sendcmd before", ret)
            print(str(self.h))
            ret = self.h.expect(cmd)
            print("CCCCCCCCC sendcmd", ret)
            print(str(self.h))
        except:
            print("Exception was thrown")
            print("debug information:")
            print(str(self.h))
            self.tb.end_tc(False)

        if ret == 0:
            return True

        return False

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

    def expect_string(self, string):
        """expect a string

        :param string:
        :return: return 'prompt' if prompt found
                        else string index
        """
        se = self._tolist(self.prompt, string)
        try:
            i = self.h.expect(se)
        except:
            if self.h.timeout == None:
                print("Exception was thrown")
                print("debug information:")
                print(str(self.h))
            return 'exception'

        if i == 0:
            return 'prompt'

        return str(i - 1)

    def flush(self):
        """ read out all bytes from connection
        """
        print("Connection flush ToDo")
