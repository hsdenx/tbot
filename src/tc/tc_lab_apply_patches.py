# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_apply_patches.py
#
# set workfd to c_ctrl
# call  tc_workfd_apply_patches.py
# restore old workfd
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
