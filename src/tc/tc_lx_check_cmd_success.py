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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_check_cmd_success.py
# simple check if previous shell command was succesful
#
from tbotlib import tbot

#we can not check if we are in linux, as this deletes
#the state of the last command...
tb.eof_write_con("if [ $? -ne 0 ]; then echo 'FAILED'; fi")
tb.eof_search_str_in_readline_end_con("FAILED")

tb.end_tc(True)
