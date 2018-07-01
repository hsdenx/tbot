# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# simply call ext2ls U-Boot command and check if
# all strings in tb.config.tc_uboot_ext2ls_expect
# come back from the command.
#
# used variables
#
# - tb.config.tc_uboot_ext2ls_expect
#| list of strings, which should come back from
#| command 'ext2ls'
#| default: "['lost+found']"
#
# - tb.config.tc_uboot_ext2ls_interface
#| used interface for ext2ls command
#| default: 'usb'
#
# - tb.config.tc_uboot_ext2ls_dev
#| device used for ext2ls command
#| default: '0:1'
#
# - tb.config.tc_uboot_ext2ls_dir
#| directory, which gets dumped
#| default: '/'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_uboot_ext2ls_expect', "['lost+found']")
tb.define_variable('tc_uboot_ext2ls_interface', 'usb')
tb.define_variable('tc_uboot_ext2ls_dev', '0:1')
tb.define_variable('tc_uboot_ext2ls_dir', '/')

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# set env var
c = tb.c_con

l = tb.config.tc_uboot_ext2ls_expect
tb.eof_write(c, "ext2ls " + tb.config.tc_uboot_ext2ls_interface + " " +
  tb.config.tc_uboot_ext2ls_dev + " " + tb.config.tc_uboot_ext2ls_dir)
tb.tbot_rup_check_all_strings(c, l, endtc=True)

tb.end_tc(True)
