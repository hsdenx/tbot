# SPDX-License-Identifier: GPL-2.0
#
# Description:
# convert duts tests from:
#
# http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootFlinfo.tc;h=f5b728258250211d86dc9c6a9208639d8542b845;hb=101ddd5dbd547d5046363358d560149d873b238a
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

cmdlist = [
"help flinfo",
"flinfo",
]

tb.eof_write_cmd_list(tb.c_con, cmdlist, create_doc_event=True)
tb.end_tc(True)
