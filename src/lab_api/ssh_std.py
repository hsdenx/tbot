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
# standard lab API
# use ssh for connecting to Lab PC
# call tb.tc_lab_denx_get_power_state_tc for getting Power state
# call tb.tc_lab_denx_get_power_tc for setting Power state
# call tb.tc_lab_denx_connect_to_board_tc for connecting to the board
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
from lab_ssh import _lab_open_ssh
from lab_ssh import lab_get_password
from lab_ssh import lab_get_lab_connect_state
from lab_ssh import lab_connect_lab
from lab_ssh import lab_lab_open_fd
from lab_ssh import lab_lab_check_fd
from lab_ssh import lab_lab_close_fd
from lab_ssh import lab_recv
from lab_ssh import lab_get_bytes
from lab_ssh import lab_write
from lab_ssh import lab_write_no_ret

class tbot_lab_api(object):
    def __init__(self, tb):
        logging.info("setup with ssh standard API")
        self.tb = tb
        self.ssh = False
        self.opened = False
        self.accept_all = True
        self.fdcount = 0
        self.data = []
        self.old = []

    def __del__(self):
        time.sleep(1)

    def _open_ssh(self):
        _lab_open_ssh(self)
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
        return lab_get_password(self, user, board)

    def get_lab_connect_state(self):
        """ get state of the connection to the lab
        """
        return lab_get_lab_connect_state(self)

    def connect_lab(self, fd):
        """ connect to the lab and set lab prompt
            return:
            True, if connect
            False else
        """
        ret = lab_connect_lab(self, fd)
        if ret != True:
            return ret
        return True

    def lab_open_fd(self):
        """ open a filedescriptor
            return here the fd !! ToDo
        """
        return lab_lab_open_fd(self)

    def lab_check_fd(self, fd):
        """ check if  filedescriptor is valid
            ToDo
        """
        return lab_lab_check_fd(self, fd)

    def lab_close_fd(self):
        """ close a filedescriptor
            ToDo
        """
        return lab_lab_close_fd(self, fd)

    def recv(self, fd):
        return lab_recv(self, fd)

    def get_bytes(self, fd):
        return lab_get_bytes(self, fd)

    def write(self, fd, string):
        return lab_write(self, fd, string)

    def write_no_ret(self, fd, string):
        return lab_write_no_ret(self, fd ,string)

    def get_power_state(self, boardname):
        """ Get powerstate of the board in the lab
        """
        tmp = "get power state " + boardname + " using tc " + self.tb.tc_lab_denx_get_power_state_tc
        logging.info(tmp)

        self.tb.call_tc(self.tb.tc_lab_denx_get_power_state_tc)
        if self.tb.power_state == 'on':
            return True
        return False

    def set_power_state(self, boardname, state):
        """ set powerstate for the board in the lab
        """
        tmp = "get power state " + boardname + " using tc " + self.tb.tc_lab_denx_power_tc
        logging.info(tmp)

        self.tb.power_state = state
        self.tb.call_tc(self.tb.tc_lab_denx_power_tc)
        ret = self.get_power_state(boardname)
        return ret

    def connect_to_board(self, boardname):
        """ connect to the board
        """
        tmp = "connect to board " + boardname + " using tc " + self.tb.tc_lab_denx_connect_to_board_tc
        logging.debug(tmp)

        try:
            save_workfd = self.tb.workfd
        except AttributeError:
            save_workfd = self.tb.channel_ctrl

        self.tb.workfd = self.tb.channel_con
        self.tb.eof_read_end_state(self.tb.workfd)
        ret = self.tb.call_tc(self.tb.tc_lab_denx_connect_to_board_tc)
        self.tb.workfd = save_workfd
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
