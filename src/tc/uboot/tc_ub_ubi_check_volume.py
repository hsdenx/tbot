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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_check_volume.py
# - checks if ubi volume tb.config.tc_ub_ubi_load_name exists
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.config.tc_ub_ubi_load_addr, tb.config.tc_ub_ubi_load_name)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = "if ubi check  " + tb.config.tc_ub_ubi_load_name + "; then; echo OK; else; echo FAIL; fi"
tb.eof_write(tb.c_con, tmp)
ret = tb.tbot_expect_string(tb.c_con, 'FAIL')
if ret == 'prompt':
    tb.end_tc(True)

tb.tbot_expect_prompt(tb.c_con)
tb.end_tc(False)
