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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_connect_with_conmux.py
# connect to console with conmux
# Never tested !!!
# End:

from tbotlib import tbot

logging.info("args: workdfd: %s", tb.workfd)

tmp = "conmux-console " + tb.config.boardlabname
ret = tb.write_stream(tb.workfd, tmp)
if not ret:
    tb.end_tc(False)

# search for error/success strings (from connmux-console if there are ??)
# If no output from connmux for error/success, delete the follwoing lines
# just end with "tb.end_tc(True)"
# here if "Unknown target" read -> fail
# "Connect" -> success
searchlist = ["Unknown target", "Connect"]
tmp = True
connected = True
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(tb.c_con, searchlist)
    if ret == '0':
        connected = False
    elif ret == '1':
        tmp = False

if not connected:
    tb.end_tc(False)

tb.end_tc(True)
