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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_devmem2_install.py
# get devmem2 source from www.lartmaker.nl/lartware/port/devmem2.c
# and install it
# End:
from tbotlib import tbot

logging.info("args: %s", tb.config.tc_workfd_work_dir)

# set board state for which the tc is valid
tb.set_board_state("linux")

tb.eof_call_tc("tc_workfd_goto_tbot_workdir.py")

# check if bonnie exist
save = tb.workfd
tb.workfd = tb.c_con
c = tb.c_con
tb.config.tc_workfd_check_if_cmd_exist_cmdname = 'devmem2'
tb.eof_call_tc("tc_workfd_check_if_cmd_exist.py")
if tb.config.tc_return == True:
    tb.workfd = save
    tb.end_tc(True)

# if not download it
tb.config.tc_workfd_check_if_file_exists_name = "devmem2.c"
ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
if ret == False:
    # wget www.lartmaker.nl/lartware/port/devmem2.c
    tmp = 'www.lartmaker.nl/lartware/port/devmem2.c'
    tb.eof_write(c, tmp)
    tb.tbot_expect_prompt(c)
    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

# apply patch
tmp = 'patch -p1 < 0001-devmem2-without-a-lot-of-output.patch'
tb.eof_write(c, tmp)
tb.eof_call_tc("tc_workfd_check_cmd_success.py")
# compile it
tb.eof_write_con_lx_cmd('gcc -o devmem2 devmem2.c')
tb.eof_call_tc("tc_workfd_check_cmd_success.py")
# compile it
tb.eof_write_con_lx_cmd('cp devmem2 /usr/local/bin')
tb.eof_call_tc("tc_workfd_check_cmd_success.py")

tb.end_tc(True)
