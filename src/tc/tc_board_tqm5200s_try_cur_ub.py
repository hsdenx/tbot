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
# python2.7 src/common/tbot.py -c tbot_tqm5200s.cfg -t tc_board_tqm5200s_try_cur_ub.py
# remove current u-boot code on the lab PC
# then call tc tc_board_tqm5200s_ub_comp_install.py
#
from tbotlib import tbot

tb.tc_lab_rm_dir = tb.tc_lab_source_dir + '/u-boot-' + tb.boardlabname
tb.eof_call_tc("tc_lab_rm_dir.py")
tb.eof_call_tc("tc_board_tqm5200s_ub_comp_install.py")

tb.end_tc(True)
