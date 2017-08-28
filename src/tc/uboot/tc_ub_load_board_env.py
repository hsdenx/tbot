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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_load_board_env.py
#
# task: load U-Boot Environment env.txt file with tftp for the
# board tb.config.tftpboardname to the addr tb.config.ub_load_board_env_addr
# from subdir tb.config.ub_load_board_env_subdir
# and imports the the textfile with 'env import'
#
# options:
# if tb.config.tc_ub_boot_linux_load_env == 'no' than TC does nothing
#
# if tb.config.tc_ub_boot_linux_load_env == 'set' or == 'setend'
# than TC executes the cmds in list tb.config.ub_load_board_env_set
#
# if tb.config.tc_ub_boot_linux_load_env == 'setend' TC returns
# after executing the commands with True
#
# else TC executes the steps described in 'task'
#
# tb.config.ub_load_board_env_testcase != ''
# call a board specific testcase, whichs name is defined in
# tb.config.ub_load_board_env_testcase for setting U-Boot
# Env. If this testcase succeeds, end True.
# End:

from tbotlib import tbot

try:
    tb.config.ub_load_board_env_testcase
except:
    tb.config.ub_load_board_env_testcase = ''

logging.info("args: %s %s %s", tb.config.tftpboardname, tb.config.ub_load_board_env_addr, tb.config.ub_load_board_env_subdir)
logging.info("args: %s", tb.config.tc_ub_boot_linux_load_env)
logging.info("args: %s", tb.config.tftpboardrootdir)
logging.info("args: %s", tb.config.ub_load_board_env_set)
logging.info("args: %s", tb.config.ub_load_board_env_testcase)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

if tb.config.ub_load_board_env_testcase != '':
    tb.eof_call_tc(tb.config.ub_load_board_env_testcase)
    tb.end_tc(True)

# load U-Boot Env only if allowed
if tb.config.tc_ub_boot_linux_load_env == 'no':
    tb.end_tc(True)

c = tb.c_con
if (tb.config.tc_ub_boot_linux_load_env == 'set') or (tb.config.tc_ub_boot_linux_load_env == 'setend'):
    for cmd in tb.config.ub_load_board_env_set:
        tb.eof_write(c, cmd)
        tb.tbot_expect_prompt(c)
    if tb.config.tc_ub_boot_linux_load_env == 'setend':
        tb.end_tc(True)

r = tb.config.tftpboardrootdir
tb.config.tc_ub_tftp_file_addr = tb.config.ub_load_board_env_addr
tb.config.tc_ub_tftp_file_name = r + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir + '/env.txt'

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
