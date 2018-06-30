# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_bdi_upd_uboot.py
# update u-boot with BDI
# - send BDI cmd: "res halt"
# - send BDI cmd: "era"
# - send BDI cmd:
#   tb.config.lab_bdi_upd_uboot_bdi_prog + ' ' + tb.config.lab_bdi_upd_uboot_bdi_file + ' BIN'
# - send BDI cmd: tb.config.lab_bdi_upd_uboot_bdi_run
# End:
from tbotlib import tbot

logging.info("args: %s %s", tb.config.lab_bdi_upd_uboot_bdi_cmd, tb.config.lab_bdi_upd_uboot_bdi_prompt)
logging.info("%s %s %s", tb.config.lab_bdi_upd_uboot_bdi_era, tb.config.lab_bdi_upd_uboot_bdi_prog, tb.config.lab_bdi_upd_uboot_bdi_file)
logging.info("%s", tb.config.lab_bdi_upd_uboot_bdi_run)

c = tb.workfd

# check if we are in the BDI
if c.get_prompt() != tb.config.lab_bdi_upd_uboot_bdi_prompt:
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
tmp = tb.config.lab_bdi_upd_uboot_bdi_prog + ' ' + tb.config.lab_bdi_upd_uboot_bdi_file + ' BIN'
tb.write_stream(c, tmp)
ret = tb.tbot_expect_string(c, 'Programming flash passed')
while (ret != '0'):
    ret = tb.tbot_expect_string(c, 'Programming flash passed')
tb.tbot_expect_prompt(c)

cmdlist = tb.config.lab_bdi_upd_uboot_bdi_run
for bl in cmdlist:
    tb.write_stream(c, bl['cmd'])
    ret = tb.tbot_expect_string(c, bl['val'])
    while (ret != '0'):
        ret = tb.tbot_expect_string(c, bl['val'])

tb.tbot_expect_prompt(c)

tb.eof_call_tc("tc_lab_bdi_disconnect.py")
tb.end_tc(True)
