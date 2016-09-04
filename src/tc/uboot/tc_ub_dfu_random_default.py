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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_dfu_random_default.py
# test a U-Boot dfu alt setting tb.tc_ub_dfu_dfu_util_alt_setting
# with reading / writing different sizes
# End:

from tbotlib import tbot

# here starts the real test
logging.info("args: %s %s %s %s", tb.tc_ub_dfu_dfu_util_path,
	tb.tc_ub_dfu_dfu_util_ssh, tb.tc_ub_dfu_dfu_util_alt_setting,
	tb.tc_ub_dfu_rand_ubcmd)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

for size in tb.dfu_test_sizes_default:
    tb.tc_ub_dfu_rand_size = str(size)
    ret = tb.call_tc("tc_ub_dfu_random.py")
    if ret != True:
        tb.end_tc(False)

tb.end_tc(True)
