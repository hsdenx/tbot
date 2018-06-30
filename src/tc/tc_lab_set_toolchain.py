# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_set_toolchain.py
# set the toolchain
# End:

from tbotlib import tbot

c = tb.c_ctrl
tmp = "eldk-switch -m -r " + tb.config.tc_lab_toolchain_rev + " " + tb.config.tc_lab_toolchain_name
tb.event.create_event('main', tb.config.boardname, "Toolchain", tmp)
tb.eof_write(c, tmp)
tb.eof_expect_string(c, 'using ELDK')
tb.end_tc(True)
