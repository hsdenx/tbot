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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubifs_ls.py
# - ls ubifs tb.tc_ub_ubifs_ls_dir
# End:

from tbotlib import tbot

logging.info("args: %s", tb.tc_ub_ubifs_ls_dir)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

c = tb.c_con
tmp = 'ubifsls ' + tb.tc_ub_ubifs_ls_dir
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'File not')
if ret == 'prompt':
    tb.end_tc(True)

tb.tbot_expect_prompt(c)
tb.end_tc(False)
