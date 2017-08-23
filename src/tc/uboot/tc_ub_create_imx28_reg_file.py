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
# python2.7 src/common/tbot.py -s lab_denx -s labconfigname -c boardconfigname -t tc_ub_create_imx28_reg_file.py
#
# creates U-Boot register dump files for an imx28 based board.
# using testcase tc_ub_create_reg_file.py
#
# dumps:
# - pinmux  80018000 - 80018b40
# - clkctrl 80044000 - 80044170
# - emi     800e0000 - 800e02ec
# - gpmi    8000c000 - 8000c0d4
# - enet 0  800f0000 - 800f0684
# - enet 1  800f4000 - 800f4684
#
# into files found in src/files/
# create for your board a subdir in the directory,
# and move the new created files into it, so you have
# them as a base for comparing further use.
#
# End:

import datetime
from tbotlib import tbot

logging.info("args: none")

# set board state for which the tc is valid
tb.set_board_state("u-boot")
tb.workfd = tb.c_con

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_pinmux.reg'
tb.config.tc_ub_create_reg_file_comment = 'new pinmux'
tb.config.tc_ub_create_reg_file_start = '80018000'
tb.config.tc_ub_create_reg_file_stop = '80018b44'
tb.config.tc_ub_readreg_mask = '0xffffffff'
tb.config.tc_ub_create_reg_file_mode = 'w+'
tb.config.tc_ub_readreg_type = 'l'

tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_clkctrl.reg'
tb.config.tc_ub_create_reg_file_comment = 'new clkctrl'
tb.config.tc_ub_create_reg_file_start = '80040000'
tb.config.tc_ub_create_reg_file_stop = '80040204'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_power.reg'
tb.config.tc_ub_create_reg_file_comment = 'new power'
tb.config.tc_ub_create_reg_file_start = '80044000'
tb.config.tc_ub_create_reg_file_stop = '80044174'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_emi.reg'
tb.config.tc_ub_create_reg_file_comment = 'new emi'
tb.config.tc_ub_create_reg_file_start = '800e0000'
tb.config.tc_ub_create_reg_file_stop = '800e02f0'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_gpmi.reg'
tb.config.tc_ub_create_reg_file_comment = 'new gpmi'
tb.config.tc_ub_create_reg_file_start = '8000c000'
tb.config.tc_ub_create_reg_file_stop = '8000c0d4'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_enet0.reg'
tb.config.tc_ub_create_reg_file_comment = 'new enet 0'
tb.config.tc_ub_create_reg_file_start = '800f0000'
tb.config.tc_ub_create_reg_file_stop = '800f0688'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_enet1.reg'
tb.config.tc_ub_create_reg_file_comment = 'new enet 1'
tb.config.tc_ub_create_reg_file_start = '800f4000'
tb.config.tc_ub_create_reg_file_stop = '800f4688'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.end_tc(True)
