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
# Description:
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_bdi_upd_uboot.py
# update u-boot with BDI
# - send BDI cmd: "res halt"
# - send BDI cmd: "era"
# - send BDI cmd:
#   tb.lab_bdi_upd_uboot_bdi_prog + ' ' + tb.lab_bdi_upd_uboot_bdi_file + ' BIN'
# - send BDI cmd: tb.lab_bdi_upd_uboot_bdi_run
# End:
from tbotlib import tbot

logging.info("args: %s %s %s", tb.boardname, tb.lab_bdi_upd_uboot_bdi_cmd, tb.lab_bdi_upd_uboot_bdi_prompt)
logging.info("%s %s %s", tb.lab_bdi_upd_uboot_bdi_era, tb.lab_bdi_upd_uboot_bdi_prog, tb.lab_bdi_upd_uboot_bdi_file)
logging.info("%s", tb.lab_bdi_upd_uboot_bdi_run)

c = tb.workfd

# check if we are in the BDI
if c.get_prompt() != tb.lab_bdi_upd_uboot_bdi_prompt:
    ret = tb.call_tc("tc_lab_bdi_connect.py")
    if ret != True:
        tb.end_tc(False)

# -> res;h
tb.write_stream(c, 'res halt')
ret = tb.tbot_expect_string(c, 'processing target startup passed')
while (ret != '0'):
    ret = tb.tbot_expect_string(c, 'processing target startup passed')
tb.tbot_expect_prompt(c)

# -> era
tb.write_stream(c, 'era')
ret = tb.tbot_expect_string(c, 'Erasing flash passed')
while (ret != '0'):
    ret = tb.tbot_expect_string(c, 'Erasing flash passed')
tb.tbot_expect_prompt(c)

# -> program bin
tmp = tb.lab_bdi_upd_uboot_bdi_prog + ' ' + tb.lab_bdi_upd_uboot_bdi_file + ' BIN'
tb.write_stream(c, tmp)
ret = tb.tbot_expect_string(c, 'Programming flash passed')
while (ret != '0'):
    ret = tb.tbot_expect_string(c, 'Programming flash passed')
tb.tbot_expect_prompt(c)

tb.write_stream(c, tb.lab_bdi_upd_uboot_bdi_run)
ret = tb.tbot_expect_string(c, 'resetting target passed')
while (ret != '0'):
    ret = tb.tbot_expect_string(c, 'resetting target passed')
tb.tbot_expect_prompt(c)

tb.eof_call_tc("tc_lab_bdi_disconnect.py")
tb.end_tc(True)
