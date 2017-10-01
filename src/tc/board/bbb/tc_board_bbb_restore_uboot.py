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
# we boot from emmc, if it is broken, we boot
# from sdcard and restore a known working uboot on
# the emmc.
#
# To switch between botmodes we can use the PIN P8_43
# attached to GND -> boot from emmc, floating -> boot
# from sd card.

import time
from tbotlib import tbot

try:
    tb.config.tc_board_bootmode_tc
except:
    tb.end_tc(False)

tb.config.tc_board_bootmode = 'recovery'
tb.eof_call_tc(tb.config.tc_board_bootmode_tc)

tb.config.uboot_prompt = '=> '
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

p = tb.config.tftpdir + '/' + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir + '/'
ret = tc_ub_testfkt.ub_setenv(tb, tb.c_con, 'ubfile', p + 'latestworking-u-boot.img')
tc_ub_testfkt.ub_setenv(tb, tb.c_con, 'mlofile', p + 'latestworking-MLO')

# call upd_uboot
tb.eof_call_tc("tc_ub_upd_uboot.py")

# call upd_spl
tb.eof_call_tc("tc_ub_upd_spl.py")

tb.config.tc_board_bootmode = 'normal'
tb.eof_call_tc(tb.config.tc_board_bootmode_tc)

tb.config.uboot_prompt = '=> '
time.sleep(2)
tb.eof_call_tc("tc_lab_poweron.py")
tb.set_board_state("u-boot")

tb.end_tc(True)
