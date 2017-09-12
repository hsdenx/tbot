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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_get_version.py
# get the U-Boot and/or SPL version from a binary
# and save it in tb.uboot_vers or tb.spl_vers
# End:

from tbotlib import tbot

logging.info("arg: %s %s %s", tb.workfd.name, tb.tc_ub_get_version_file, tb.tc_ub_get_version_string)

# set board state for which the tc is valid
tb.set_board_state("lab")

# set env var
c = tb.workfd

sf = tb.tc_ub_get_version_file
se = tb.tc_ub_get_version_string

cmd = 'strings -a ' + sf + ' | grep "' + se + '" --color=never'
tb.eof_write_cmd_get_line(c, cmd)
tb.config.tc_return = tb.ret_write_cmd_get_line.strip()
tb.event.create_event('main', tb.config.boardname, "UBOOT_VERSION", tb.config.tc_return)

tb.end_tc(True)
