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
#
# simply call U-Boots reset command
# This testcase works only on the console connection c_con
#
# End:

from tbotlib import tbot

# do not check error strings, as we want to reboot U-Boot
tb.c_con.set_check_error(False)

# reset the board
tb.eof_write(tb.c_con, "res")
tb.gotprompt = True

# get u-boot login
tb.set_board_state("u-boot")

# enable error strng checking now again
tb.c_con.set_check_error(True)

tb.end_tc(True)
