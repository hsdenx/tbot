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
# start with
# tbot.py -s lab_denx -c beagleboneblack -t tc_demo_part1.py -l log/tbot_demo_part1.log -v
#
# we boot from sd card, if it is broken, we boot
# from emmc and restore a known working uboot on
# the sdcard.
#
# To switch between botmodes we can use the PIN P8_43
# attached to GND -> boot from emmc, floating -> boot
# from sd card.

import time
from tbotlib import tbot

# switch to bootmode emmc
tb.write_lx_cmd_check(tb.c_ctrl, 'relais   relsrv-02-02  1  on')
tb.eof_call_tc("tc_lab_poweroff.py")
time.sleep(2)
tb.eof_call_tc("tc_lab_poweron.py")
tb.set_board_state("u-boot")

# set latest, so we do not load uboot env, nor do we reset
# in tc_ub_upd_uboot.py and tc_ub_upd_spl.py
tb.config.tc_ub_upd_uboot_latest = 'yes'
tb.config.tc_ub_upd_spl_latest = 'yes'

# call tc tc_ub_load_board_env.py
tb.eof_call_tc("tc_ub_load_board_env.py")

# set latest images
import tc_ub_testfkt

tc_ub_testfkt.ub_setenv(tb, tb.c_con, 'ubfile', 'bbb/tbot/latestworking-u-boot.img')
tc_ub_testfkt.ub_setenv(tb, tb.c_con, 'mlofile', 'bbb/tbot/latestworking-MLO')

# call upd_uboot
tb.eof_call_tc("tc_ub_upd_uboot.py")

# call upd_spl
tb.eof_call_tc("tc_ub_upd_spl.py")


# switch to bootmode sdcard
tb.write_lx_cmd_check(tb.c_ctrl, 'relais   relsrv-02-02  1  off')
tb.eof_call_tc("tc_lab_poweroff.py")
time.sleep(2)
tb.eof_call_tc("tc_lab_poweron.py")
tb.set_board_state("u-boot")

tb.end_tc(True)
