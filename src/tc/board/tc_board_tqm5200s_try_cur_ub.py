# SPDX-License-Identifier: GPL-2.0
#
# Description:
# remove current u-boot code on the lab PC
# then call tc tc_board_tqm5200s_ub_comp_install.py
# End:

from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_rm_uboot_code.py")
tb.eof_call_tc("tc_board_tqm5200s_ub_comp_install.py")
tb.statusprint("start all DUTS testcases")
tb.eof_call_tc("uboot/duts/tc_ub_start_all_duts.py")

#save working u-boot bin
c = tb.workfd
ta = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + "/u-boot-latestworking.bin"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s="u-boot.bin", t=ta)

tb.end_tc(True)
