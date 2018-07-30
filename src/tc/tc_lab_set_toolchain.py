# SPDX-License-Identifier: GPL-2.0
#
# Description:
# set eldk toolchain with eldk-switch
# works only on tb.c_ctrl (change this)
#
# used variables
#
# - tb.config.tc_lab_toolchain_rev
#| toolchain revision
#| default: '5.4'
#
# - tb.config.tc_lab_toolchain_name
#| toolchain name
#| default: 'armv5te'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lab_toolchain_rev', '5.4')
tb.define_variable('tc_lab_toolchain_name', 'armv5te')
c = tb.c_ctrl
tmp = "eldk-switch -m -r " + tb.config.tc_lab_toolchain_rev + " " + tb.config.tc_lab_toolchain_name
tb.event.create_event('main', tb.config.boardname, "Toolchain", tmp)
tb.eof_write(c, tmp)
tb.eof_expect_string(c, 'using ELDK')
tb.end_tc(True)
