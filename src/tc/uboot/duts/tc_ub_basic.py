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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_basic.py
# convert duts tests from:
# http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/02_UBootBasic.tc;h=5503cc6c716d2748732d30d63b0801e651fe1706;hb=101ddd5dbd547d5046363358d560149d873b238a
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

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
"help reset",
]

c = tb.c_con
tb.eof_write_cmd_list(c, cmdlist, create_doc_event=True)

self.event.create_event('main', 'tc_ub_basic.py', 'SET_DOC_FILENAME', 'version')
tb.eof_write(c, 'version')
searchlist = ["U-Boot "]
tmp = True
cmd_ok = False
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        cmd_ok = True
    elif ret == 'prompt':
        tmp = False

self.event.create_event('main', 'tc_ub_basic.py', 'SET_DOC_FILENAME', 'reset')
tb.c_con.set_check_error(False)
tb.eof_write(c, 'reset')
tb.set_board_state("u-boot")
tb.c_con.set_check_error(True)

# restore our U-Boot Env we need
tb.eof_call_tc("tc_ub_load_board_env.py")

tb.end_tc(cmd_ok)
