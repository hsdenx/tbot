# SPDX-License-Identifier: GPL-2.0
#
# Description:
# - install mtd utils if needed with tc_lx_mtdutils_install.py
# - attach ubi device with tc_lx_ubi_attach.py
# - get info with tc_lx_ubi_info.py
# - get parameters with tc_lx_get_ubi_parameters.py
# End:

from tbotlib import tbot

# get all default values
tb.eof_call_tc("tc_lx_ubi_def.py")

# set board state for which the tc is valid
tb.set_board_state("linux")

tb.eof_call_tc("tc_lx_mtdutils_install.py")
tb.eof_call_tc("tc_lx_ubi_attach.py")
tb.eof_call_tc("tc_lx_ubi_info.py")
tb.eof_call_tc("tc_lx_get_ubi_parameters.py")

tb.end_tc(True)
