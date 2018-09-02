# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# call testcases:
# - tc_board_yocto_get_and_bake.py
# - tc_board_yocto_install_nfs.py
# - tc_board_yocto_boot_nfs.py
# - tc_board_yocto_boot_sdcard.py
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_board_bootmode_tc
except:
    tb.end_tc(False)

logging.info("args: %s %s", tb.workfd.name, tb.config.tc_board_bootmode_tc)

tb.eof_call_tc("tc_board_yocto_get_and_bake.py")
tb.eof_call_tc("tc_board_yocto_install_nfs.py")
tb.eof_call_tc("tc_board_yocto_boot_nfs.py")
tb.eof_call_tc("tc_board_yocto_boot_sdcard.py")

tb.config.state_linux_timeout = str(float(tb.config.state_linux_timeout) / 2)
tb.config.tc_demo_linux_tc_boot_lx = 'no'
#tb.eof_call_tc("tc_demo_linux_testcases.py")

# create yocto documentation
tb.config.create_documentation_auto = 'yocto'
tb.end_tc(True)
