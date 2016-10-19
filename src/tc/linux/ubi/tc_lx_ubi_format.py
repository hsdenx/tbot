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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_ubi_format.py
# ubiformat tb.config.tc_ubi_mtd_dev with tb.config.tc_lx_ubi_format_filename
# End:

from tbotlib import tbot
import re

# here starts the real test
logging.info("args: %s %s %s", tb.config.tc_ubi_cmd_path, tb.config.tc_ubi_mtd_dev,
             tb.config.tc_lx_ubi_format_filename)

# set board state for which the tc is valid
tb.set_board_state("linux")

def create_ubi_cmd(tb, cmd):
    tmp = tb.config.tc_ubi_cmd_path + '/' + cmd
    return tmp

tmp = create_ubi_cmd(tb, 'ubi-utils/ubiformat ' + tb.config.tc_ubi_mtd_dev +
                     ' -y -f ' + tb.config.tc_lx_ubi_format_filename)
tb.eof_write_con_lx_cmd(tmp)
tb.end_tc(True)
