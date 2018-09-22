# SPDX-License-Identifier: GPL-2.0
#
# Description:
# call ubiattach
#
# End:

from tbotlib import tbot
import re

# get all default values
tb.eof_call_tc("tc_lx_ubi_def.py")

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
