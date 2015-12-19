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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_boot_linux.py
# load u-boot environment
# boots currently with "run net_nfs"
from tbotlib import tbot

#here starts the real test
logging.info("args: %s", tb.ub_boot_linux_cmd)
#set board state for which the tc is valid
tb.set_board_state("u-boot")

# load U-Boot environment variables for tbot
tb.eof_call_tc("tc_ub_load_board_env.py")

#run tbot_boot_linux
tb.eof_write_con(tb.ub_boot_linux_cmd)

#read until 'login:'
ret = False
i = 0
while ret != True:
    ret = tb.search_str_in_readline_con("login:")
    i += 1
    if i >= tb.tc_ub_boot_linux_retry:
        tb.end_tc(False)

tmp = 'root'
tb.eof_write_con(tmp)

tb.set_board_state("linux")

tb.end_tc(True)
