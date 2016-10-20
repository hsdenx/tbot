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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_cp_file.py
# simple copy  file from arg.get('s')
# to arg.get('t') on the channel arg.get('ch')
# End:

from tbotlib import tbot

args = ['ch', 's', 't']
arg = tb.check_args(args)

tmp = "cp " + arg.get('s') + " " + arg.get('t')
tb.write_lx_cmd_check(arg.get('ch'), tmp)
tb.end_tc(True)
