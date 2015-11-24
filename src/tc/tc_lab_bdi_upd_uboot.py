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
from lab_bdi import bdi_class

logging.info("args: %s %s %s", tb.boardname, tb.lab_bdi_upd_uboot_bdi_cmd, tb.lab_bdi_upd_uboot_bdi_prompt)
logging.info("%s %s %s", tb.lab_bdi_upd_uboot_bdi_era, tb.lab_bdi_upd_uboot_bdi_prog, tb.lab_bdi_upd_uboot_bdi_file)
logging.info("%s", tb.lab_bdi_upd_uboot_bdi_run)

bdi = bdi_class(tb)

# -> connect to bdi
bdi.bdi_connect()

# -> res;h
bdi.send_bdi_cmd_wait_prompt("res halt")

# -> era
bdi.send_bdi_cmd_wait_string_and_prompt(tb.lab_bdi_upd_uboot_bdi_era, 'Erasing flash passed')

# -> program bin
tmp=tb.lab_bdi_upd_uboot_bdi_prog + ' ' + tb.lab_bdi_upd_uboot_bdi_file + ' BIN'
bdi.send_bdi_cmd_wait_string_and_prompt(tmp, 'Programming flash passed')

#read all pending chars from console
tb.flush_con()

# run the binary
bdi.send_bdi_cmd_wait_prompt(tb.lab_bdi_upd_uboot_bdi_run)

bdi.bdi_quit()
tb.end_tc(True)
