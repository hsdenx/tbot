# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_rm_uboot_code.py
# rm U-Boot source tb.config.tc_lab_source_dir + '/u-boot-' + tb.config.boardlabname
# End:

from tbotlib import tbot

logging.info("args: %s", tb.workfd.name)

tb.config.tc_lab_rm_dir = tb.config.tc_lab_source_dir + '/u-boot-' + tb.config.boardlabname
tb.eof_call_tc("tc_workfd_rm_dir.py")

tb.end_tc(True)
