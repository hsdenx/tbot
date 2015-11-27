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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_mtdutils_install.py
# get mtdutil source and install it
from tbotlib import tbot

logging.info("args: %s", tb.tc_lx_work_dir)

#set board state for which the tc is valid
tb.set_board_state("linux")

# check if mtdinfo exist
tb.tc_lx_check_if_cmd_exist_cmdname = 'mtdinfo'
tb.eof_call_tc("tc_lx_check_if_cmd_exist.py")
if tb.tc_return == True:
    # check if mtdinfo exist
    tb.tc_lx_check_if_cmd_exist_cmdname = 'ubinfo'
    tb.eof_call_tc("tc_lx_check_if_cmd_exist.py")
    if tb.tc_return == True:
        tb.end_tc(True)

tb.eof_call_tc("tc_lx_goto_tbot_workdir.py")

#if not download it
#git clone git://git.infradead.org/mtd-utils.git mtd-utils
tb.tc_lx_check_if_dir_exists_name = "mtd-utils"
tb.eof_call_tc("tc_lx_check_if_dir_exist.py")
if tb.tc_return == False:
    tmp = 'git clone git://git.infradead.org/mtd-utils.git mtd-utils'
    tb.eof_write_con(tmp)
    tb.eof_read_end_state_con(1)
    tb.workfd = tb.channel_con
    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

#cd into dir
tb.eof_write_con_lx_cmd('cd mtd-utils')
tb.workfd = tb.channel_con
tb.eof_call_tc("tc_workfd_check_cmd_success.py")

#if code is compiled, exit
tb.tc_lx_check_if_file_exists_name = 'ubi-utils/mtdinfo'
tb.eof_call_tc("tc_lx_check_if_file_exist.py")
if tb.tc_return == True:
    tb.end_tc(True)

#apply patches if any
# use src/tc/tc_lab_apply_patches.py
# but this is for ctrl fd ...

#compile it
oldretry = tb.read_end_state_retry
tb.read_end_state_retry = 50
tb.eof_write_con_lx_cmd('make')
tb.read_end_state_retry = oldretry
tb.workfd = tb.channel_con
tb.eof_call_tc("tc_workfd_check_cmd_success.py")

#install it ...
#tb.eof_write_con_lx_cmd('cp devmem2 /usr/local/bin')
#tb.workfd = tb.channel_con
#tb.eof_call_tc("tc_workfd_check_cmd_success.py")
tb.tc_ubi_cmd_path = tb.tc_lx_work_dir + '/mtd-utils'

tb.eof_read_end_state_con(0)
tb.end_tc(tb.tc_return)
