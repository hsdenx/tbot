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
# nowadays after booting into linux there comes the message
# "random: crng init done"
#
# This pos in, and may disturb a current running test ...
#
# so call this testcase after logging into linux
# and wait until this string is read ...
#
# End:

from tbotlib import tbot

tb.c_con.expect_string('crng init')

tb.end_tc(True)
