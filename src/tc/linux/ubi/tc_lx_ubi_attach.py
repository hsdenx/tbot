# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_ubi_attach.py
# End:

from tbotlib import tbot
import re

# here starts the real test
logging.info("args: %s %s %s %s", tb.workfd.name, tb.config.tc_ubi_cmd_path,
             tb.config.tc_ubi_mtd_dev, tb.config.tc_ubi_vid_hdr_offset)

mtd_dev_nr = re.sub("[^0-9]", "", tb.config.tc_ubi_mtd_dev)
logging.info("mtd_dev_nr: %s", mtd_dev_nr)

# set board state for which the tc is valid
tb.set_board_state("linux")

def create_ubi_cmd(tb, cmd):
    tmp = tb.config.tc_ubi_cmd_path + '/' + cmd
    return tmp

cmd = create_ubi_cmd(tb, 'ubi-utils/ubiattach /dev/ubi_ctrl -m ' + mtd_dev_nr)
if tb.config.tc_ubi_vid_hdr_offset != 'default':
    cmd += ' -O ' + tb.config.tc_ubi_vid_hdr_offset

ret = tb.write_cmd_check(tb.workfd, cmd, "error")
if ret:
    tb.eof_call_tc("tc_lx_ubi_detach.py")
    ret = tb.write_cmd_check(tb.workfd, cmd, "error")
    if ret:
        tb.end_tc(False)

tb.end_tc(True)
