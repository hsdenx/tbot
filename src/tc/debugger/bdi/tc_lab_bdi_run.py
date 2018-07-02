# SPDX-License-Identifier: GPL-2.0
#
# Description:
# BDI run
# - send "res halt" to workfd
# - send BDI cmd tb.config.lab_bdi_upd_uboot_bdi_run
#
# used variables
#
# - tb.config.lab_bdi_upd_uboot_bdi_run
#| command for resetting U-Boot
#| default: "[{'cmd':'res run', 'val':'resetting target passed'}]"
#
# End:

from tbotlib import tbot
from lab_bdi import bdi_class

tb.define_variable('lab_bdi_upd_uboot_bdi_run', "[{'cmd':'res run', 'val':'resetting target passed'}]")
logging.info("args: %s %s", tb.workfd.name,
             tb.config.lab_bdi_upd_uboot_bdi_prompt)

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
