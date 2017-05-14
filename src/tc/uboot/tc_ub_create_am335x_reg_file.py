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
# python2.7 src/common/tbot.py -s lab_denx -c tbot.cfg -t tc_ub_create_am335x_reg_file.py
#
# creates U-Boot register dump files for an am335x based board.
# using testcase tc_ub_create_reg_file.py
#
# dumps:
# - pinmux  44e10000 - 44e10004
# - pinmux  44e10010 - 44e10010 
# - pinmux  44e10040 - 44e10040
# - pinmux  44e10110 - 44e10110
# - pinmux  44e10428 - 44e11440
# - cm per  44e00000 - 44e00150
# - cm wkup 44e00400 - 44e004d0
# - cm dpll 44e00500 - 44e0053c
# - cm mpu  44e00600 - 44e00604
# - cm device 44e00700 - 44e00700
# - emif    4c000000 - 4c000120
# - ddr     44e12000 - 44e121dc
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
tb.config.tc_ub_create_reg_file_start = '44e10000'
tb.config.tc_ub_create_reg_file_stop = '44e10008'
tb.config.tc_ub_readreg_mask = '0xffffffff'
tb.config.tc_ub_create_reg_file_mode = 'w+'
tb.config.tc_ub_readreg_type = 'l'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_pinmux_2.reg'
tb.config.tc_ub_create_reg_file_comment = 'new pinmux part2'
tb.config.tc_ub_create_reg_file_start = '44e10010'
tb.config.tc_ub_create_reg_file_stop = '44e10014'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_pinmux_3.reg'
tb.config.tc_ub_create_reg_file_comment = 'new pinmux part3'
tb.config.tc_ub_create_reg_file_start = '44e10040'
tb.config.tc_ub_create_reg_file_stop = '44e10044'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_pinmux_4.reg'
tb.config.tc_ub_create_reg_file_comment = 'new pinmux part4'
tb.config.tc_ub_create_reg_file_start = '44e10110'
tb.config.tc_ub_create_reg_file_stop = '44e10114'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_pinmux_5.reg'
tb.config.tc_ub_create_reg_file_comment = 'new pinmux part5'
tb.config.tc_ub_create_reg_file_start = '44e10428'
tb.config.tc_ub_create_reg_file_stop = '44e11448'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_cm_per.reg'
tb.config.tc_ub_create_reg_file_comment = 'new cm per'
tb.config.tc_ub_create_reg_file_start = '44e00000'
tb.config.tc_ub_create_reg_file_stop = '44e00154'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_cm_wkup.reg'
tb.config.tc_ub_create_reg_file_comment = 'new cm wkup'
tb.config.tc_ub_create_reg_file_start = '44e00400'
tb.config.tc_ub_create_reg_file_stop = '44e004dc'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_cm_dpll.reg'
tb.config.tc_ub_create_reg_file_comment = 'new cm dpll'
tb.config.tc_ub_create_reg_file_start = '44e00500'
tb.config.tc_ub_create_reg_file_stop = '44e00540'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_cm_mpu.reg'
tb.config.tc_ub_create_reg_file_comment = 'new cm mpu'
tb.config.tc_ub_create_reg_file_start = '44e00600'
tb.config.tc_ub_create_reg_file_stop = '44e00608'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_cm_device.reg'
tb.config.tc_ub_create_reg_file_comment = 'new cm device'
tb.config.tc_ub_create_reg_file_start = '44e00700'
tb.config.tc_ub_create_reg_file_stop = '44e00704'
tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_emif.reg'
tb.config.tc_ub_create_reg_file_comment = 'new emif'
tb.config.tc_ub_create_reg_file_start = '4c000000'
tb.config.tc_ub_create_reg_file_stop = '4c000124'
tb.eof_call_tc("tc_ub_create_reg_file.py")

# This registers are write only because of a silicon bug :-(
#
# tb.config.tc_ub_create_reg_file_name = 'src/files/ub_new_ddr.reg'
# tb.config.tc_ub_create_reg_file_comment = 'new ddr'
# tb.config.tc_ub_create_reg_file_start = '44e12000'
# tb.config.tc_ub_create_reg_file_stop = '44e121e0'
# tb.eof_call_tc("tc_ub_create_reg_file.py")

tb.end_tc(True)
