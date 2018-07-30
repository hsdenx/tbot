# SPDX-License-Identifier: GPL-2.0
#
# Description:
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
# tb.config.ub_load_board_env_testcase != 'none'
# call a board specific testcase, whichs name is defined in
# tb.config.ub_load_board_env_testcase for setting U-Boot
# Env. If this testcase succeeds, end True.
#
# used variables
#
# - tb.config.ub_load_board_env_testcase
#| if != 'none' call testcase with this name for
#| for setting U-Boot Environment
#| default: 'none'
#
# - tb.config.ub_load_board_env_addr
#| ram address to which the env.txt file gets loaded
#| default: '0x81000000'
#
# - tb.config.ub_load_board_env_subdir
#| subdir name in which env.txt file is found
#| default: 'tbot'
#
# - tb.config.tc_ub_boot_linux_load_env
#| value
#| 'no'      no Environment gets loaded
#| 'set'     load Environment from tb.config.ub_load_board_env_set
#| 'setend'  same as 'set' just end testcase after
#|           Environment is set from tb.config.ub_load_board_env_set
#| 'load'    tftp a 'env.txt' file and import it with
#|           'env import -t'
#| default: 'load'
#
# - tb.config.ub_load_board_env_set
#| list of Environment settings
#| default: '[]'
#
# End:

from tbotlib import tbot

tb.define_variable('ub_load_board_env_testcase', 'none')
tb.define_variable('ub_load_board_env_addr', '0x81000000')
tb.define_variable('ub_load_board_env_subdir', 'tbot')
tb.define_variable('tc_ub_boot_linux_load_env', 'load')
tb.define_variable('ub_load_board_env_set', '[]')

logging.info("args: %s", tb.config.tftpboardname)
logging.info("args: %s", tb.config.tftpboardrootdir)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

if tb.config.ub_load_board_env_testcase != 'none':
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

if tb.config.tftpboardrootdir != 'none':
    r = tb.config.tftpboardrootdir
else:
    r = ''
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
