# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c ccu1 -t tc_board_ccu1_tests.py
# start all testcases for the ccu1 board
# End:

from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.statusprint("tc_ccu1 u-boot setenv")
#call ubot setenv
tb.eof_call_tc("tc_ub_setenv.py")

tb.statusprint("tc_ccu1 linux dmesg checks")
tb.config.tc_lx_dmesg_grep_name = "CCU1"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.config.tc_lx_dmesg_grep_name = "nand: ST Micro NAND 256MiB 1,8V 8-bit"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.config.tc_lx_dmesg_grep_name = "smsc911x 2c000000.ethernet eth0: attached PHY driver"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.config.tc_lx_dmesg_grep_name = "smsc911x 2c000000.ethernet eth0: SMSC911x/921x identified at 0xd0942000, IRQ: 288"
tb.eof_call_tc("tc_lx_dmesg_grep.py")
tb.config.tc_lx_dmesg_grep_name = "twl_rtc 48070000.i2c"
tb.eof_call_tc("tc_lx_dmesg_grep.py")

tb.statusprint("tc_ccu1 pinmux check")
tb.eof_call_tc("tc_lx_check_reg_file.py")
tb.config.tc_lx_create_reg_file_name = 'src/files/ccu1_pinmux_gpmc.reg'
tb.eof_call_tc("tc_lx_check_reg_file.py")

tb.statusprint("tc_ccu1 ubi check")
tb.eof_call_tc("tc_lx_ubi_tests.py")

tb.statusprint("tc_ccu1 partition check")
#call linux tc_lx_partition_check.py
#for testing usb memstick
#check if usb stick is authorized
tb.eof_call_tc("tc_lx_partition_check.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
