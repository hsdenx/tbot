# SPDX-License-Identifier: GPL-2.0
#
# Description:
# - rm old u-boot tree (if there is one)
# - tc_lab_get_uboot_source.py
# End:

from tbotlib import tbot

# delete old u-boot source tree
tb.eof_call_tc("tc_workfd_rm_uboot_code.py")

# call get u-boot source
tb.statusprint("get u-boot source")
tb.eof_call_tc("tc_lab_get_uboot_source.py")
tb.end_tc(True)
