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

class tbot_lab_api(object):
    def __init__(self):
        time.sleep(1)
    def __del__(self):
        time.sleep(1)
    def connect_lab(self):
        """ connect to the lab
            return:
            True, if connect
            False else
        """
        time.sleep(1)
    def get_power_state(self):
        """ Get powerstate of the board in the lab
        """
        time.sleep(1)
    def set_power_state(self, state):
        """ set powerstate for the board in the lab
        """
        time.sleep(1)
    def define_board_state(self):
        """ define a boardstate (press return, you get back a prompt) for the board in the lab
        """
        time.sleep(1)
    def get_board_state(self):
        """ Get boardstate of the board in the lab
            if it send a response if return is pressed
        """
        time.sleep(1)
    def set_board_state(self):
        """ set the board to a state
        """
        time.sleep(1)
