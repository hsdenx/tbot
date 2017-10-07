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
# - set jumper to normal
# - boot sd card image
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_board_bootmode_tc
except:
    tb.end_tc(False)

tb.config.tc_board_bootmode = 'normal'
tb.eof_call_tc(tb.config.tc_board_bootmode_tc)

tb.config.uboot_prompt = '=> '
time.sleep(2)
tb.eof_call_tc("tc_lab_poweron.py")
tb.set_board_state("u-boot")

tb.config.linux_user = tb.config.linux_user_yoctorootfs
tb.config.ub_boot_linux_cmd = 'run mmc_mmc'
tb.config.bbb_check_crng_init = 'no'
tb.set_board_state("linux")

tb.eof_call_tc("tc_board_yocto_check_rootfs.py")
tb.end_tc(True)
