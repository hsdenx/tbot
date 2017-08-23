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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_create_volume.py
# - create ubi volume tb.config.tc_ub_ubi_create_vol_name with size
# tb.config.tc_ub_ubi_create_vol_sz
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.config.tc_ub_ubi_create_vol_name, tb.config.tc_ub_ubi_create_vol_sz)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tmp = 'ubi create ' + tb.config.tc_ub_ubi_create_vol_name + ' ' + tb.config.tc_ub_ubi_create_vol_sz
tb.eof_write(tb.c_con, tmp)
ret = tb.tbot_expect_string(tb.c_con, 'exit not allowed')
if ret == 'prompt':
    tb.end_tc(True)

tb.tbot_expect_prompt(tb.c_con)
tb.end_tc(True)
