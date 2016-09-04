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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_denx_connect_to_board.py
# connect to board with connect
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.workfd.name, tb.boardlabname)

tmp = "connect " + tb.boardlabname
tb.eof_write(tb.workfd, tmp)

searchlist = ["Unknown target", "Connect", "not accessible", "Locked by process", "Connection closed by"]
tmp = True
connected = True
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
        connected = False
    elif ret == '1':
        tmp = False
    elif ret == '2':
        connected = False
    elif ret == '3':
        connected = False
    elif ret == '4':
        connected = False

if not connected:
    tb.end_tc(False)

# check for 'not accessible'
tb.workfd.set_timeout(2)
tmp_ign = tb.workfd.ign
tb.workfd.ign = ['==>', 'rlogin']
tb.workfd.cnt_ign = len(tb.workfd.ign)

tmp = tb.tbot_read_line_and_check_strings(tb.workfd, searchlist)
ret = True
if tmp == '2':
    logging.error("not accessible")
    ret = False
if tmp == '3':
    logging.error("Locked by process")
    ret = False
if tmp == '4':
    logging.error("Conection closed")
    ret = False

tb.workfd.set_timeout(None)

tb.workfd.ign = tmp_ign
tb.workfd.cnt_ign = len(tb.workfd.ign)
tb.end_tc(ret)
