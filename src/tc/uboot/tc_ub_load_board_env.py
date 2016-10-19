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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_load_board_env.py
# load U-Boot Environment for the board tb.config.tftpboardname
# tb.config.ub_load_board_env_addr and tb.config.ub_load_board_env_subdir
# End:

from tbotlib import tbot

logging.info("args: %s %s %s", tb.config.tftpboardname, tb.config.ub_load_board_env_addr, tb.config.ub_load_board_env_subdir)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# load U-Boot Env only if allowed
if tb.config.tc_ub_boot_linux_load_env != 1:
    tb.end_tc(True)

tb.config.tc_ub_tftp_file_addr = tb.config.ub_load_board_env_addr
tb.config.tc_ub_tftp_file_name = '/tftpboot/' + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir + '/env.txt'

c = tb.c_con
i = 0
retry = 2
load_fail = False
while load_fail == False:
    if i >= retry:
        tb.end_tc(False)

    tmp = 'mw ' + tb.config.ub_load_board_env_addr + ' 0 0x4000'
    tb.eof_write(c, tmp)
    tb.tbot_expect_prompt(c)
    load_fail = tb.call_tc("tc_ub_tftp_file.py")
    i += 1

tmp = 'env import -t ' + tb.config.ub_load_board_env_addr
tb.eof_write(c, tmp)
tb.tbot_expect_prompt(c)

tb.end_tc(True)
