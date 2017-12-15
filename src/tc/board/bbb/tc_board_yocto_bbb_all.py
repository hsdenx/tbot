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

tb.config.state_linux_timeout = tb.config.state_linux_timeout / 2
tb.config.tc_demo_linux_tc_boot_lx = 'no'
#tb.eof_call_tc("tc_demo_linux_testcases.py")

# create yocto documentation
tb.config.create_documentation_auto = 'yocto'
tb.end_tc(True)
