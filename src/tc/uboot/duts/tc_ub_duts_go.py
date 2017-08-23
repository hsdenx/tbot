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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_duts_go.py
# do the commands needed for:
# http://www.denx.de/wiki/view/DULG/UBootCmdGroupExec#Section_5.9.4.3.
# U-Boots go command
#
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.eof_call_tc("tc_workfd_get_uboot_config_vars.py")

cmdlist = [
"help go",
]

tb.eof_write_cmd_list(tb.c_con, cmdlist, create_doc_event=True)

tb.end_tc(True)
