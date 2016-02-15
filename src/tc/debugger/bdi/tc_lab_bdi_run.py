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

logging.info("args: %s %s %s %s", tb.board_has_debugger, tb.workfd.name,
             tb.lab_bdi_upd_uboot_bdi_prompt, tb.lab_bdi_upd_uboot_bdi_run)

c = tb.workfd

# check if we are in the BDI
if c.get_prompt() != tb.lab_bdi_upd_uboot_bdi_prompt:
    tb.end_tc(False)

# -> res;h
tb.write_stream(c, 'res halt')

ret = tb.tbot_expect_string(c, 'processing target startup passed')
while (ret != '0'):
    ret = tb.tbot_expect_string(c, 'processing target startup passed')

tb.tbot_expect_prompt(c)

tb.write_stream(c, tb.lab_bdi_upd_uboot_bdi_run)
ret = tb.tbot_expect_string(c, 'processing target startup passed')
while (ret != '0'):
    ret = tb.tbot_expect_string(c, 'processing target startup passed')
tb.tbot_expect_prompt(c)
tb.end_tc(True)
