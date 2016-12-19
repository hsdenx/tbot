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

c = tb.c_con
c.set_prompt(tb.config.linux_prompt_default)

tmp = True
sl = ['login:', 'assword']
while (tmp):
    ret = tb.tbot_read_line_and_check_strings(c, sl)
    if ret == '0':
        # login
        tb.write_stream(c, tb.config.linux_user, send_console_start=False)
    if ret == '1':
	tb.write_stream_passwd(c, tb.config.linux_user, tb.config.boardname)
    if ret == 'prompt':
        # we are in linux
        tb.set_prompt(c, tb.config.linux_prompt, 'linux')
        tmp = False

tb.end_tc(True)
