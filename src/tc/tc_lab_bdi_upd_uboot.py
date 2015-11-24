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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_bdi_upd_uboot.py
# update u-boot with BDI
from tbotlib import tbot

logging.info("args: %s %s %s", tb.boardname, tb.lab_bdi_upd_uboot_bdi_cmd, tb.lab_bdi_upd_uboot_bdi_prompt)
logging.info("%s %s %s", tb.lab_bdi_upd_uboot_bdi_era, tb.lab_bdi_upd_uboot_bdi_prog, tb.lab_bdi_upd_uboot_bdi_file)
logging.info("%s", tb.lab_bdi_upd_uboot_bdi_run)

class bdi_class(object):
    def __init__(self, tb):
        self.tb = tb

    def get_bdi_prompt(self):
        ret = self.tb.read_end(self.tb.channel_ctrl, 1, self.tb.lab_bdi_upd_uboot_bdi_prompt)
        if ret != True:
            self.tb.end_tc(False)

    def send_bdi_cmd_wait_string_and_prompt(self, cmd, string):
        self.tb.eof_write_ctrl(cmd + '\r\n')
        ret = self.tb.read_end(self.tb.channel_ctrl, 4, string)
        if ret != True:
            self.tb.end_tc(False)
        self.get_bdi_prompt()

    def send_bdi_cmd_wait_prompt(self, cmd):
        self.tb.eof_write_ctrl(cmd + '\r\n')
        self.get_bdi_prompt()

bdi = bdi_class(tb)

# -> connect to bdi
bdi.send_bdi_cmd_wait_prompt(tb.lab_bdi_upd_uboot_bdi_cmd)

# -> res;h
bdi.send_bdi_cmd_wait_prompt("res halt")

# -> era
bdi.send_bdi_cmd_wait_string_and_prompt(tb.lab_bdi_upd_uboot_bdi_era, 'Erasing flash passed')

# -> program bin
tmp=tb.lab_bdi_upd_uboot_bdi_prog + ' ' + tb.lab_bdi_upd_uboot_bdi_file + ' BIN'
bdi.send_bdi_cmd_wait_string_and_prompt(tmp, 'Programming flash passed')

# run it
bdi.send_bdi_cmd_wait_prompt(tb.lab_bdi_upd_uboot_bdi_run)

tb.eof_write_ctrl("quit\r\n")
tb.eof_read_end_state_ctrl(1)
tb.end_tc(True)
