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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_switch_su.py
# switch to supoeruser
#
from tbotlib import tbot

logging.info("args: workfd %s", tb.workfd)

#switch to root
tb.eof_write_ctrl("su")
tb.eof_search_str_in_readline_ctrl("Password")
tb.eof_write_ctrl_passwd("root", "lab")
tb.eof_write_ctrl("PS1='ttbott su # '")

tb.eof_read_end_state_ctrl(1)
tb.flush_fd(tb.workfd)
tb.end_tc(True)
