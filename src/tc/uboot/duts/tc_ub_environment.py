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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_environment.py
# convert duts tests from:
# http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootEnvironment.tc;h=18d235f427e3efe9e6a04f870a3c5426d719ec58;hb=101ddd5dbd547d5046363358d560149d873b238a
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

cmdlist = [
"help printenv",
"printenv ipaddr hostname netmask",
"printenv",
"help saveenv",
"saveenv",
"help setenv",
"setenv foo This is an example value.",
"printenv foo",
"setenv foo",
"printenv foo",
"setenv bar",
"printenv bar",
"setenv bar This is a new example.",
"printenv bar",
"setenv bar",
"setenv cons_opts 'console=tty0 console=ttyS0,\${baudrate}'",
"printenv cons_opts",
"setenv cons_opts"
]

tb.eof_write_cmd_list(tb.c_con, cmdlist)
tb.end_tc(True)
