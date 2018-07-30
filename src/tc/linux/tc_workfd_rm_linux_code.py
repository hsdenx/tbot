# SPDX-License-Identifier: GPL-2.0
#
# Description:
# rm linux source tb.config.tc_lab_source_dir + '/linux-' + tb.config.boardlabname
# End:

from tbotlib import tbot

logging.info("args: %s", tb.workfd)

tb.config.tc_lab_rm_dir = tb.config.tc_lab_source_dir + '/linux-' + tb.config.boardlabname
tb.eof_call_tc("tc_workfd_rm_dir.py")

tb.end_tc(True)
