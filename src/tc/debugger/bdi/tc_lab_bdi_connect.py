# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_bdi_connect.py
# connect to the BDI if tb.config.board_has_debugger != 0
# - send to workfd tb.config.lab_bdi_upd_uboot_bdi_cmd
# - set BDI prompt tb.config.lab_bdi_upd_uboot_bdi_prompt
# - wait for BDI prompt
# End:

from tbotlib import tbot

logging.info("args: %s %s %s", tb.config.board_has_debugger, tb.workfd.name,
             tb.config.lab_bdi_upd_uboot_bdi_prompt)

if tb.config.board_has_debugger == 0:
    tb.end_tc(False)

c = tb.workfd
tb.write_stream(c, tb.config.lab_bdi_upd_uboot_bdi_cmd)
c.set_prompt(tb.config.lab_bdi_upd_uboot_bdi_prompt, 'linux')
searchlist = ["Connection refused", "No route"]
tmp = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0' or ret == '1':
        # back to linux
        c.set_prompt(tb.config.linux_prompt)
        tb.tbot_expect_prompt(c)
        tb.end_tc(False)
    elif ret == 'prompt':
        tmp = False

c.lineend = '\r\0'
tb.end_tc(True)
