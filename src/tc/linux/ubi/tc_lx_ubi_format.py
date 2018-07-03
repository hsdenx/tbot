# SPDX-License-Identifier: GPL-2.0
#
# Description:
# ubiformat tb.config.tc_ubi_mtd_dev with tb.config.tc_lx_ubi_format_filename
# End:

from tbotlib import tbot
import re

# get all default values
tb.eof_call_tc("tc_lx_ubi_def.py")

# set board state for which the tc is valid
tb.set_board_state("linux")

def create_ubi_cmd(tb, cmd):
    tmp = tb.config.tc_ubi_cmd_path + '/' + cmd
    return tmp

tmp = create_ubi_cmd(tb, 'ubi-utils/ubiformat ' + tb.config.tc_ubi_mtd_dev +
                     ' -y -f ' + tb.config.tc_lx_ubi_format_filename)
tb.eof_write_con_lx_cmd(tmp)
tb.end_tc(True)
