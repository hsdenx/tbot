# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
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
