# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c shc -t tc_board_shc_compile_ml.py
# compile ML linux kernel for the shc board
# End:

from tbotlib import tbot

tb.statusprint("shc compile linux mainline kernel")

#delete old source tree
tb.eof_call_tc("tc_workfd_rm_linux_code.py")

tb.eof_call_tc("tc_workfd_get_linux_source.py")

tb.eof_call_tc("tc_workfd_goto_linux_code.py")

tb.eof_call_tc("tc_workfd_compile_linux.py")

# copy files to tftpdir
tb.statusprint("copy files")
c = tb.workfd
so = "/work/hs/tbot/linux-shc/arch/arm/boot/uImage"
ta = "/tftpboot/shc/tbot/uImage-hs-cur"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "/work/hs/tbot/linux-shc/arch/arm/boot/dts/" + tb.config.tc_workfd_compile_linux_dt_name
ta = "/tftpboot/shc/tbot/shc.dtb"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

tb.end_tc(True)
