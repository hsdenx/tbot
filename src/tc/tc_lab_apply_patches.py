# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# set workfd to c_ctrl
# call  tc_workfd_apply_patches.py
# restore old workfd
#
# used variables:
#
# tb.config.tc_lab_apply_patches_dir
#
# End:

from tbotlib import tbot

logging.info("args: %s", tb.config.tc_lab_apply_patches_dir)

if tb.config.tc_lab_apply_patches_dir == 'none':
    tb.end_tc(True)

save = tb.workfd
tb.workfd = tb.c_ctrl

tb.eof_call_tc("tc_workfd_apply_patches.py")

tb.workfd = save

tb.end_tc(True)
