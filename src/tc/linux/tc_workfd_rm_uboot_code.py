# SPDX-License-Identifier: GPL-2.0
#
# Description:
# rm U-Boot source tb.config.tc_lab_source_dir + '/u-boot-' + tb.config.boardlabname
# End:

from tbotlib import tbot

tb.config.tc_lab_rm_dir = tb.config.tc_lab_source_dir + '/u-boot-' + tb.config.boardlabname
tb.eof_call_tc("tc_workfd_rm_dir.py")

tb.end_tc(True)
