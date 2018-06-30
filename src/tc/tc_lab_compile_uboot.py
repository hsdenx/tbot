# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# set workfd to c_ctrl
# call tc_workfd_compile_uboot.py
# restore old workfd
#
# End:

from tbotlib import tbot

savefd = tb.workfd
tb.workfd = tb.c_ctrl

tb.eof_call_tc("tc_workfd_compile_uboot.py")

tb.workfd = savefd
tb.end_tc(True)
