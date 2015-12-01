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
# This is not a complete lab_api!
# It just colelcts ssh specific tasks, so real lab_api
# which uses ssh connection to the lab host pc can reuse
# this code.
#
import sys
import re
import logging
import time
sys.path.append("./common")
from tbotlib import tbot

# BDI is a little bit tricky. I did not understand
# when to send a "\n" or a "\r\n" at the end, also
# always the "\n" comes in a new ssh packet ... :-(
# and more worser, this leads into coming a BDI prompt
# ???
# doing here a big bad workaround it ...

class bdi_class(object):
    def __init__(self, tb):
        self.tb = tb

    def get_bdi_prompt(self):
        ret = self.tb.read_end(self.tb.channel_ctrl, 1, self.tb.lab_bdi_upd_uboot_bdi_prompt)
        #if ret != True:
        #    self.tb.end_tc(False)

    def read_return_and_prompt(self):
        ret = True
        while ret:
            ret = self.tb.read_end(self.tb.channel_ctrl, 1, '\n')
            # and we get a prompt
            self.get_bdi_prompt()

    def send_bdi_cmd_wait_string_and_prompt(self, cmd, string):
        self.tb.lab.write_no_ret(self.tb.channel_ctrl, cmd + '\r')
        ret = self.tb.read_end(self.tb.channel_ctrl, 1, cmd)
        ret = self.tb.read_end(self.tb.channel_ctrl, 4, string)
        if ret != True:
            self.tb.end_tc(False)
        self.read_return_and_prompt()

    def send_bdi_cmd_wait_prompt(self, cmd):
        self.tb.lab.write_no_ret(self.tb.channel_ctrl, cmd + '\r')
        # wait command repeat
        ret = self.tb.read_end(self.tb.channel_ctrl, 1, cmd)
        self.read_return_and_prompt()

    def bdi_connect(self):
        i = 0
        while i < 3:
            self.tb.lab.write_no_ret(self.tb.channel_ctrl, self.tb.lab_bdi_upd_uboot_bdi_cmd + '\n')
            ret = self.tb.read_end(self.tb.channel_ctrl, 1, self.tb.lab_bdi_upd_uboot_bdi_prompt)
            if ret != True:
                #maybe powered off, power on
                self.tb.set_power_state('on')
                i += 1
            else:
                i = 5

    def bdi_quit(self):
        self.tb.eof_write_ctrl("quit\r\n")
        self.tb.eof_read_end_state_ctrl(3)
        self.get_bdi_prompt()

    def bdi_connect(self):
        i = 0
        while i < 3:
            self.tb.lab.write_no_ret(self.tb.channel_ctrl, self.tb.lab_bdi_upd_uboot_bdi_cmd + '\n')
            ret = self.tb.read_end(self.tb.channel_ctrl, 1, self.tb.lab_bdi_upd_uboot_bdi_prompt)
            if ret != True:
                #maybe powered off, power on
                self.tb.set_power_state('on')
                i += 1
            else:
                i = 5

    def bdi_quit(self):
        self.tb.eof_write_ctrl("quit\r\n")
        self.tb.eof_read_end_state_ctrl(3)
