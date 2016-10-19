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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_boot_linux.py
# - load u-boot environment with testcase "tc_ub_load_board_env.py"
# - execute u-boot cmd tb.config.ub_boot_linux_cmd
# End:
from tbotlib import tbot

# here starts the real test
logging.info("args: %s", tb.config.ub_boot_linux_cmd)
# set board state for which the tc is valid
tb.set_board_state("u-boot")

# load U-Boot environment variables for tbot
tb.eof_call_tc("tc_ub_load_board_env.py")

# run tbot_boot_linux
tb.eof_write_con(tb.config.ub_boot_linux_cmd)

# read until 'login:'
ret = tb.tbot_expect_string(tb.c_con, 'login:')
if ret == 'prompt':
    tb.end_tc(False)

tmp = 'root'
tb.eof_write(tb.c_con, tmp)

tb.c_con.set_prompt(tb.config.linux_prompt_default)
tb.tbot_expect_prompt(tb.c_con)

tb.set_prompt(tb.c_con, tb.config.linux_prompt, 'linux')

tb.end_tc(True)
