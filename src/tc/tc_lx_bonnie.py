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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_bonnie.py
# run a bonnie test
from tbotlib import tbot

logging.info("args: %s %s", tb.tc_lx_bonnie_dev, tb.tc_lx_bonnie_sz)

#set board state for which the tc is valid
tb.set_board_state("linux")

tb.tc_workfd_check_tc_time_tcname = 'bonnie'
ret = tb.call_tc("tc_workfd_check_tc_time.py")
if ret == False:
    # do not start bonnie, timer is not expired
    tb.end_tc(True)

#check if bonnie exist
#if not download it, and try to install
tb.eof_call_tc("tc_lx_bonnie_install.py")

#start test
# detect tc_lx_bonnie_sz ... should be 2*RAM size
tmp = "bonnie++ -d " + tb.tc_lx_bonnie_dev + " -s " + tb.tc_lx_bonnie_sz + " -f -b -u root -m " + tb.boardname

tb.eof_write_con(tmp)
#bonnie takes loooong
oldretry = tb.read_end_state_retry
tb.read_end_state_retry = 1000
tb.eof_read_end_state_con(1)
tb.read_end_state_retry = oldretry
tb.end_tc(True)
