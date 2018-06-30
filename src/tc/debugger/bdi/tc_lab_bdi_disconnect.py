# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_bdi_disconnect.py
# disconnect from the BDI
# - send bdi command "quit"
# - set tb.config.linux_prompt
# End:

from tbotlib import tbot

logging.info("args: %s %s %s", tb.config.board_has_debugger, tb.workfd.name,
             tb.config.lab_bdi_upd_uboot_bdi_prompt)

c = tb.workfd

# check if we are in the BDI
if c.get_prompt() != tb.config.lab_bdi_upd_uboot_bdi_prompt:
    tb.end_tc(False)

tb.write_stream(c, 'quit')
c.set_prompt(tb.config.linux_prompt, 'linux')
tb.tbot_expect_prompt(c)
c.lineend = '\n'

tb.end_tc(True)
