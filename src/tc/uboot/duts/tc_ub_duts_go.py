# SPDX-License-Identifier: GPL-2.0
#
# Description:
# do the commands needed for:
#
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
