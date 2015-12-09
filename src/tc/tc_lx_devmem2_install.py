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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_devmem2_install.py
# get bonnie source and install it
from tbotlib import tbot

logging.info("args: %s", tb.tc_workfd_work_dir)

#set board state for which the tc is valid
tb.set_board_state("linux")

tb.eof_call_tc("tc_workfd_goto_tbot_workdir.py")

# check if bonnie exist
tb.workfd = tb.channel_con
tb.tc_workfd_check_if_cmd_exist_cmdname = 'devmem2'
tb.eof_call_tc("tc_workfd_check_if_cmd_exist.py")
if tb.tc_return == True:
    tb.end_tc(True)

#if not download it
tb.tc_workfd_check_if_file_exists_name = "devmem2.c"
ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
if ret == False:
    #wget www.lartmaker.nl/lartware/port/devmem2.c
    tmp = 'www.lartmaker.nl/lartware/port/devmem2.c'
    tb.eof_write_con(tmp)
    tb.eof_read_end_state_con(1)
    tb.workfd = tb.channel_con
    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

#apply patch
tmp = 'patch -p1 < 0001-devmem2-without-a-lot-of-output.patch'
tb.eof_write_con(tmp)
tb.workfd = tb.channel_con
tb.eof_call_tc("tc_workfd_check_cmd_success.py")
#compile it
oldretry = tb.read_end_state_retry
tb.read_end_state_retry = 50
tb.eof_write_con_lx_cmd('gcc -o devmem2 devmem2.c')
tb.read_end_state_retry = oldretry
tb.workfd = tb.channel_con
tb.eof_call_tc("tc_workfd_check_cmd_success.py")
#compile it
tb.eof_write_con_lx_cmd('cp devmem2 /usr/local/bin')
tb.workfd = tb.channel_con
tb.eof_call_tc("tc_workfd_check_cmd_success.py")

tb.eof_read_end_state_con(1)
tb.end_tc(tb.tc_return)
