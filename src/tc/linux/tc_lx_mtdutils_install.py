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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_mtdutils_install.py
# check if mtdutils are installed. If not, clone the code with
# git clone git://git.infradead.org/mtd-utils.git mtd-utils
# and install it
# End:

from tbotlib import tbot

logging.info("args: %s", tb.tc_workfd_work_dir)

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.c_con
# check if mtdinfo exist
tb.tc_workfd_check_if_cmd_exist_cmdname = 'mtdinfo'
tb.workfd = tb.c_con
ret = tb.call_tc("tc_workfd_check_if_cmd_exist.py")
if ret == True:
    # check if mtdinfo exist
    tb.tc_workfd_check_if_cmd_exist_cmdname = 'ubinfo'
    tb.tc_ubi_cmd_path = ''
    ret = tb.call_tc("tc_workfd_check_if_cmd_exist.py")
    if ret == True:
        tb.end_tc(True)

tb.eof_call_tc("tc_workfd_goto_tbot_workdir.py")

# if not download it
# git clone git://git.infradead.org/mtd-utils.git mtd-utils
tb.workfd = tb.c_con
tb.tc_workfd_check_if_dir_exists_name = "mtd-utils"
ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
if ret == False:
    tmp = 'git clone git://git.infradead.org/mtd-utils.git mtd-utils'
    tb.eof_write(c, tmp)
    tb.tbot_expect_prompt(c)
    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

# cd into dir
tb.eof_write_con_lx_cmd('cd mtd-utils')

# if code is compiled, exit
tb.tc_workfd_check_if_file_exists_name = 'ubi-utils/mtdinfo'
ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
if ret == True:
    tb.tc_ubi_cmd_path = tb.tc_workfd_work_dir + '/mtd-utils'
    tb.end_tc(True)

# apply patches if any
# use src/tc/tc_lab_apply_patches.py
# but this is for ctrl fd ...

# compile it
tb.eof_write_con_lx_cmd('make')

# install it ...
# tb.eof_write_con_lx_cmd('cp devmem2 /usr/local/bin')
# tb.workfd = tb.c_con
# tb.eof_call_tc("tc_workfd_check_cmd_success.py")
tb.tc_ubi_cmd_path = tb.tc_workfd_work_dir + '/mtd-utils'
tb.end_tc(True)
