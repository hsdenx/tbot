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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_environment.py
# convert duts tests from:
# http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootEnvironment.tc;h=18d235f427e3efe9e6a04f870a3c5426d719ec58;hb=101ddd5dbd547d5046363358d560149d873b238a
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

cmdlist = [
"help printenv",
"printenv ipaddr hostname netmask",
"printenv"
]

cmdlist_saveenv = [
"help saveenv",
"saveenv"
]

cmdlist_setenv_1 = [
"setenv foo This is an example value.",
"printenv foo",
"setenv foo",
"printenv foo"
]

cmdlist_setenv_2 = [
"printenv bar",
"setenv bar This is a new example.",
"printenv bar",
"setenv bar"
]

cmdlist_setenv_3 = [
"setenv cons_opts 'console=tty0 console=ttyS0,\${baudrate}'",
"printenv cons_opts",
"setenv cons_opts"
]

tb.eof_write_cmd_list(tb.c_con, cmdlist, create_doc_event=True)
tb.eof_write_cmd_list(tb.c_con, cmdlist_saveenv, create_doc_event=True)

tb.event.create_event('main', 'tc_ub_environment.py', 'SET_DOC_FILENAME', 'help_setenv')
tb.eof_write_cmd(tb.c_con, "help setenv")

tb.event.create_event('main', 'tc_ub_environment.py', 'SET_DOC_FILENAME', 'setenv_example_1')
tb.eof_write_cmd_list(tb.c_con, cmdlist_setenv_1)

tb.eof_write_cmd(tb.c_con, "setenv bar", create_doc_event=True)

tb.event.create_event('main', 'tc_ub_environment.py', 'SET_DOC_FILENAME', 'setenv_example_2')
tb.eof_write_cmd_list(tb.c_con, cmdlist_setenv_2)

tb.event.create_event('main', 'tc_ub_environment.py', 'SET_DOC_FILENAME', 'setenv_example_3')
tb.eof_write_cmd_list(tb.c_con, cmdlist_setenv_3)

tb.end_tc(True)
