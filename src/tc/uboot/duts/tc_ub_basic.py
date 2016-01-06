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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_basic.py
# convert duts tests from:
# http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/02_UBootBasic.tc;h=5503cc6c716d2748732d30d63b0801e651fe1706;hb=101ddd5dbd547d5046363358d560149d873b238a
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

def tbot_send_wait(tb, cmd):
    tb.eof_write_con(cmd)
    tb.eof_read_end_state_con(1);

cmdlist = [
"help",
"help help",
"help printenv tftp",
"help tftpboot",
"help setenv printenv",
"help echo",
"echo The quick brown fox jumped over the lazy dog.",
"help sleep",
"sleep 5",
"help version",
]

for tmp_cmd in cmdlist:
    tbot_send_wait(tb, tmp_cmd)

cmd = "version"
tb.eof_write_con(cmd)
searchlist = ["U-Boot"]
tmp = True
cmd_ok = False
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
    if tmp == 0:
        tmp = True
        cmd_ok = True
    elif tmp == None:
        # ! endless loop ...
        tmp = True
    elif tmp == 'prompt':
        tmp = False

tb.end_tc(cmd_ok)
