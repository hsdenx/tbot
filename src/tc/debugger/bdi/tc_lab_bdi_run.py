# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_bdi_upd_uboot.py
# BDI run
# - send "res halt" to workfd
# - send BDI cmd tb.config.lab_bdi_upd_uboot_bdi_run
# End:

from tbotlib import tbot
from lab_bdi import bdi_class

logging.info("args: %s %s %s", tb.workfd.name,
             tb.config.lab_bdi_upd_uboot_bdi_prompt, tb.config.lab_bdi_upd_uboot_bdi_run)

c = tb.workfd

# check if we are in the BDI
if c.get_prompt() != tb.config.lab_bdi_upd_uboot_bdi_prompt:
    tb.end_tc(False)

# -> res;h
tb.write_stream(c, 'res halt')

ret = tb.tbot_expect_string(c, 'processing target startup passed')
while (ret != '0'):
    ret = tb.tbot_expect_string(c, 'processing target startup passed')

tb.tbot_expect_prompt(c)

cmdlist = tb.config.lab_bdi_upd_uboot_bdi_run
for bl in cmdlist:
    tb.write_stream(c, bl['cmd'])
    ret = tb.tbot_expect_string(c, bl['val'])
    while (ret != '0'):
        ret = tb.tbot_expect_string(c, bl['val'])

tb.tbot_expect_prompt(c)
tb.end_tc(True)
