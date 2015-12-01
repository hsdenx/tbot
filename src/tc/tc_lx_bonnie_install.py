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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_bonnie_install.py
# get bonnie source and install it
from tbotlib import tbot

logging.info("args: %s", tb.tc_lx_work_dir)

#set board state for which the tc is valid
tb.set_board_state("linux")

tb.eof_call_tc("tc_lx_goto_tbot_workdir.py")

# check if bonnie exist
tb.workfd = tb.channel_con
tb.tc_workfd_check_if_cmd_exist_cmdname = 'bonnie++'
tb.eof_call_tc("tc_workfd_check_if_cmd_exist.py")
if tb.tc_return == True:
    tb.end_tc(True)

#if not download it
tb.tc_workfd_check_if_file_exists_name = "bonnie++-1.03e.tgz"
tb.eof_call_tc("tc_workfd_check_if_file_exist.py")
if tb.tc_return == False:
    #wget http://www.coker.com.au/bonnie++/bonnie++-1.03e.tgz
    tmp = 'wget http://www.coker.com.au/bonnie++/bonnie++-1.03e.tgz'
    tb.eof_write_con(tmp)
    tb.eof_read_end_state_con(1)
    tb.workfd = tb.channel_con
    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

#untar it
tmp = 'tar xvzf ' + tb.tc_workfd_check_if_file_exists_name
tb.eof_write_con(tmp)
tb.workfd = tb.channel_con
tb.eof_call_tc("tc_workfd_check_cmd_success.py")
#check if dir exists
tb.eof_write_con_lx_cmd('cd bonnie++-1.03e')
tb.eof_write_con_lx_cmd('pwd')
oldretry = tb.read_end_state_retry
tb.read_end_state_retry = 100
tb.eof_write_con_lx_cmd('./configure')
tb.eof_write_con_lx_cmd('make')
tb.eof_write_con_lx_cmd('make install')
tb.read_end_state_retry = oldretry

#now check if it exists
tb.workfd = tb.channel_con
tb.eof_call_tc("tc_workfd_check_if_cmd_exist.py")
tb.eof_read_end_state_con(1)
tb.end_tc(tb.tc_return)
