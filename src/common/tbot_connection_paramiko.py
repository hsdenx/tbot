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
        self.lastpos = 0
        # list of strings, which get ignored
        self.ign = ['==>', 'INIT: Id "O0" respawning too fast: disabled for 5 minutes']
        self.cnt_ign = len(self.ign)
        # list of strings, which are not allowed
        # ToDo make them configurable and make this
        # option enable/disable
        self.check_error = True
        self.error = ['Resetting CPU']
        self.cnt_error = len(self.error)
        self.send_prompt = False

    def open_paramiko(self, user, ip, passwd, port='22'):
        # look in paramiko/demos/demo_simple.py
        po = int(port)
        logging.debug("try to open ssh connection")
        if not self.ssh:
            self.ssh = paramiko.SSHClient()
        self.opened = False
        if self.accept_all == True:
            #accept all host keys
            logging.debug("AutoAddPolicy")
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        logging.debug("try connection for %s@%s port: %d", user, ip, po)
        try:
            tmp = passwd[:4]
            if tmp == 'key:':
                k = paramiko.RSAKey.from_private_key_file(passwd[4:])
                self.ssh.connect(ip, port=po, username=user, pkey=k)
            else:
                self.ssh.connect(ip, port=po, username=user, password=passwd)
        except BaseException as e:
            logging.warning("no connection for %s@%s string: %s", user, ip, str(e))
            self.ssh.close()
            return None

        self.opened = True
        self.data = ''

        # open shell
        self.channel = self.ssh.invoke_shell()
        logging.debug(self.ssh.get_transport())
        self.channel.settimeout(self.channel_timeout)
        return True

    def lab_recv(self, fix_power_off=False):
        """ get bytes from connection
        """
        try:
            self.channel
        except:
            logging.debug("No channel")
            self.data = ''
            return None

        try:
            tmp = self.channel.recv(self.maxread)
        except socket.timeout:
            logging.debug("read_bytes: Timeout")
            return None

        if fix_power_off == True:
            hexstr = tmp.encode("hex")
            if '000000' in hexstr:
                logging.warning("got a lof 00 on channel %s", self.name)
                return False

        logging.debug("%s read: %s", self.name, tmp)

        self.data += tmp
        se = tmp.rstrip()
        se = se.lstrip()
        self.tb.verboseprint("%s: %s" % (self.name, se))
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

    def create(self, cmd, logfilename, prompt, user, ip, passwd, port='22'):
        """create a new connection

        :param cmd: cmd which is spawned
        :param logfilename: name of the logfile
        :return:
        """
        ret = self.open_paramiko(user, ip, passwd, port)
        if ret != True:
            return False

        self.logfilename = logfilename
        self.maxread = 1024
        self.prompt = prompt
        self.created = True
        return True

    def cleanup(self):
        if self.ssh:
           self.ssh.close()

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

    def get_prompt_type(self):
        """simple return the current prompt type

        :return: string of current prompt type
        """
        return self.prompt_type

    def set_prompt(self, newprompt, type):
        """set the new prompt string

        :param newprompt: string of new prompt
        :return:
        """
        self.prompt = newprompt
        self.prompt_type = type
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
        # from where comes the '\r' ?
        ret = self.expect_string(cmd + '\r' + self.lineend)
        if ret == 'prompt':
            return False
        if ret == 'exception':
            return False

        return True

    def sendcmd_prompt(self, cmd):
        """send a string to the connection
           add lineend, and check if string is
           reread.

        :param cmd: command to send
        :return: True if cmd is reread False else
        """
        ret = self.send(cmd)
        if ret != True:
            return ret
        if ret == 'exception':
            return False
        self.send_prompt = True

        return True


    def expect_prompt(self):
        """expect prompt, search endless for prompt
           true if found
           false if not
        """
        ret = self.expect_string(self.prompt, promptonly = True)
        self.tb.gotprompt = True
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
        # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP START", self.name)
        # print("buf", buf)
        # print("string", string)
        # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
        lens = len(string)
        bufl = len(buf)
        if bufl < lens:
            return 'none'
        # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", lens, bufl)
        while (i < bufl):
            if buf[i] == string[0]:
                if lens == 1:
                    # print("EEEEEEEEEEEEEEEEE", str(i))
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
                        # print("EEEEEEEEEEEEEEEEE", str(i))
                        return str(i)
                    s += 1
                    if s == bufl:
                        return 'none'
            i += 1

        # print("EEEEEEEEEEEEEEEEE none ")
        return 'none'

    def search_one_strings(self, se):
        """ search in self.data if a string from se is found
        :return: 'none' if nothing is found, else str(index)
        """
        i = 0
        # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP START")
        # print("buf", self.data)
        # print("se", se)
        # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
        lastpos = []
        for tmp in se:
            ret = self.__search_string(self.data, tmp)
            # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP ret", ret, i)
            if ret == 'none':
                lastpos.append('none')
                i += 1
                continue

            # save position
            lastpos.append(str(int(ret) + len(tmp)))

        # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP lastpos", lastpos)
        i = 0
        f = 0
        p = 0
        init = 'no'
        for tmp in se:
            if lastpos[i] != 'none':
                if init == 'no':
                    p = int(lastpos[i])
                    f = i
                    init = 'yes'
                else:
                    if (int(lastpos[i]) < p):
                        p = int(lastpos[i])
                        f = i
            i += 1

        if init == 'no':
            # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP ret none")
            return 'none'
        else:
            self.lastpos = p
            # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP lastpos ", self.lastpos)
            return str(f)

    def copy_data(self, pos):
        # copy self.data from 0 - index
        self.logbuf = self.data[0:pos]
        self.data = self.data[pos:]

    def set_check_error(self, value):
        self.check_error = value

    def __search_strings(self, se, promptonly = False):
        """ search in self.data if a string from se is found
        :return: 'none' if nothing is found,
                 else str(index) is found
        """
        # if we need to check for error strings, this is
        # first we search. If found we return immediately
        if self.check_error:
            reterr = self.search_one_strings(self.error)
            if reterr != 'none':
                return 'error'

        # search for the strings we want to find
        # if we want to search for prompt only, do not search
        if promptonly == False:
            ret_str = self.search_one_strings(se)
            lp_str = self.lastpos
        else:
            ret_str = 'none'
            lp_str = 0

        # we always check for strings we want to ignore
        ret_ign = self.search_one_strings(self.ign)
        lp_ign = self.lastpos
        if ret_ign != 'none':
            len_ign = len(self.ign[int(ret_ign)])
            try:
                print("ret_str ", ret_str, lp_str)
            except:
                pass
            pos = self.lastpos
        else:
            len_ign = 0

        # also, check for prompt
	ret_pro = self.search_one_strings(self._tolist(self.prompt))
        if ret_pro == '0':
            lp_pro = self.lastpos
        else:
            lp_pro = 0

        # now, find out, what we return
        logging.debug("----------------------------------------------------------------------")
        logging.debug("con name ", self.name)
        logging.debug("DATA ", self.data)
        logging.debug("SE ", se)
        logging.debug("IGN ", self.ign)
        logging.debug("PROMPT ", self._tolist(self.prompt))
        logging.debug("PRO ONLY ", promptonly, self.send_prompt)
        logging.debug("STR ", lp_str, ret_str)
        logging.debug("IGN ", lp_ign, ret_ign)
        logging.debug("PRO ", lp_pro, ret_pro)

        # check if we found nothing
        if ret_str == 'none' and ret_ign == 'none' and ret_pro == 'none':
            return 'none'

        # the easy case: one catch

        if ret_str != 'none' and ret_ign == 'none' and ret_pro == 'none':
            self.copy_data(lp_str)
            return ret_str

        if ret_str == 'none' and ret_ign != 'none' and ret_pro == 'none':
            if lp_ign > len_ign:
                self.copy_data(lp_ign - len_ign)
                return 'ign_pre'
            self.copy_data(lp_ign)
            return 'ign'

        if ret_str == 'none' and ret_ign == 'none' and ret_pro != 'none':
            if self.send_prompt == True:
                self.copy_data(lp_pro)
                return ret_pro
            else:
                self.copy_data(lp_pro)
                self.tb.gotprompt = True
                return 'prompt'

        # two finds

        if ret_str != 'none' and ret_ign != 'none' and ret_pro == 'none':
            # first ign found ?
            if lp_ign < lp_str:
                # return ign
                if lp_ign > len_ign:
                    self.copy_data(lp_ign - len_ign)
                    return 'ign_pre'

                self.copy_data(lp_ign)
                return 'ign'
            else:
                self.copy_data(lp_str)
                return ret_str

        if ret_str == 'none' and ret_ign != 'none' and ret_pro != 'none':
            # ign found, before prompt
            if lp_ign < lp_pro:
                # return ign
                if lp_ign > len_ign:
                    self.copy_data(lp_ign - len_ign)
                    return 'ign_pre'

                self.copy_data(lp_ign)
                return 'ign'
            else:
                self.copy_data(lp_pro)
                self.tb.gotprompt = True
                return 'prompt'

        if ret_str != 'none' and ret_ign == 'none' and ret_pro != 'none':
            # search strings found, before prompt
            if lp_str < lp_pro:
                self.copy_data(lp_str)
                return ret_str
            if lp_str == lp_pro:
                # Ok, we search for prompt also in se
                # This can happen when we want to switch
                # between board modes.
                # Simply return str
                self.copy_data(lp_str)
                return ret_str
            else:
                # puh, should only happen, when we set a new prompt ...
                if self.send_prompt == True:
                    self.copy_data(lp_pro)
                    return ret_pro
                else:
                    logging.warn("May a problem, found prompt before string")
                self.copy_data(lp_pro)
                self.tb.gotprompt = True
                return 'prompt'

        # at last, we found all ...
        if lp_ign < lp_str and lp_ign < lp_pro:
                # return ign
                if lp_ign > len_ign:
                    self.copy_data(lp_ign - len_ign)
                    return 'ign_pre'

                self.copy_data(lp_ign)
                return 'ign'

        if lp_str < lp_ign and lp_str < lp_pro:
            self.copy_data(lp_str)
            return ret_str

        if lp_pro < lp_ign and lp_pro < lp_str:
            self.copy_data(lp_pro)
            self.tb.gotprompt = True
            return 'prompt'

        logging.error("Reached end of __search_strings !! ")
        logging.error("str  ", lp_str, ret_str)
        logging.error("pro  ", lp_pro, ret_pro)
        logging.error("ign  ", lp_ign, ret_ign)
        logging.error("data ", self.data)

    def expect_string(self, string, promptonly = False):
        """expect a string

        :param string:
        :return: return 'prompt' if prompt found
                        'exception' if exception occured
                        else string index
        """
        # search first ignore strings, then the string to
        # search, and at the end, search the prompt
        # se = self._tolist(ign, error, string, self.prompt)
        se = self._tolist(string)
        # print("EEEEEEEEEEEEEEEEEE expectstring", se, len(self.logbuf), self.data, promptonly)
        if self.data == '':
            # if we have no data, read it
            tmp = self.lab_recv()
            self.logbuf = self.data
            # print("CCCCCC expectstring now", tmp, self.data)
            # print("CCCC timeout", self.timeout)
            if tmp == None and self.timeout != None:
                # ToDo give paramiko the timeout
                # print("CCCCCCC expectsrting labrecv", ret)
                self.tb.event.create_event_log(self, "re", 'exception')
                return 'exception'

        loop = True
        while(loop == True):
            ret = self.__search_strings(se, promptonly)
            # print("EEEEEEE expectstring ret", ret, self.data, self.logbuf, self.send_prompt)
            if ret == 'none':
                tmp = self.lab_recv()
                # print("CCCCC expectstring tmp", tmp, self.timeout, self.data)
                if tmp == None and self.timeout != None:
                    # ToDo give paramiko the timeout
                    # print("CCCCCCC expectsrting labrecv second", ret)
                    self.tb.event.create_event_log(self, "re", self.data)
                    return 'exception'
                self.logbuf = self.data
            elif ret == 'ign':
                self.tb.event.create_event_log(self, "ig", self.data)
                continue
            elif ret == 'ign_pre':
                self.tb.event.create_event_log(self, "r", self.logbuf)
                continue
            elif ret == 'error':
                self.tb.event.create_event_log(self, "er", self.data)
                self.tb.end_tc(False)
            elif ret == 'prompt':
                self.tb.gotprompt = True
                loop = False
            else:
                if self.send_prompt == False:
                    loop = False
                else:
                    self.send_prompt = False
                    self.tb.event.create_event_log(self, "r", self.logbuf)
        
        self.tb.event.create_event_log(self, "r", self.logbuf)
        # print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC ret", ret)
        return ret

    def flush(self):
        """ read out all bytes from connection
        """
        ret = True
        while (ret):
            ret = self.lab_recv(fix_power_off=True)
        self.tb.event.create_event_log(self, "rf", self.data)
        self.data = ''
        return True

    def copy_file(self, remotepath, localpath):
        try:
            ### Copy remote file to server        
            logging.debug("sftp rem: %s loc: %s", remotepath, localpath)
            sftp = self.ssh.open_sftp()
            sftp.get(remotepath, localpath)
            sftp.close()
            return True
        except IOError as e:
            logging.error("sftp IOError rem: %s loc: %s %s", remotepath, localpath, str(e))
            return False
        except Exception as e:
            logging.error("sftp Exception rem: %s loc: %s %s", remotepath, localpath, str(e))
            return False

    def copy_file_tolabpc(self, localpath, remotepath):
        try:
            ### Copy remote file to server        
            logging.debug("sftp tolabpc rem: %s loc: %s", remotepath, localpath)
            sftp = self.ssh.open_sftp()
            sftp.put(localpath, remotepath)
            sftp.close()
            return True
        except IOError as e:
            logging.error("sftp IOError rem: %s loc: %s %s", remotepath, localpath, str(e))
            return False
        except Exception as e:
            logging.error("sftp Exception rem: %s loc: %s %s", remotepath, localpath, str(e))
            return False
