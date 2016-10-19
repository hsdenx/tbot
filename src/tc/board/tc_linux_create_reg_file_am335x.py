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
# tbot.py -s lab_denx -c aristainetos2 -t tc_linux_create_reg_file_am335x.py
# create a regfile for am335x SoC registers
# End:

from tbotlib import tbot
import time

tb.workfd = tb.c_ctrl

tb.config.tc_lx_create_reg_file_name = 'am335x_ctrl_module.reg'
tb.config.tc_lx_create_reg_file_start = '0x44e10000'
tb.config.tc_lx_create_reg_file_stop = '0x44e11448'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

tb.config.tc_lx_create_reg_file_name = 'am335x_display.reg'
tb.config.tc_lx_create_reg_file_start = '0x4830e000'
tb.config.tc_lx_create_reg_file_stop = '0x4830e074'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_PER
tb.config.tc_lx_create_reg_file_name = 'am335x_cm_per.reg'
tb.config.tc_lx_create_reg_file_start = '0x44e00000'
tb.config.tc_lx_create_reg_file_stop = '0x44e00154'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_WKUP
tb.config.tc_lx_create_reg_file_name = 'am335x_cm_wkup.reg'
tb.config.tc_lx_create_reg_file_start = '0x44e00400'
tb.config.tc_lx_create_reg_file_stop = '0x44e004dc'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_DPLL
tb.config.tc_lx_create_reg_file_name = 'am335x_cm_dpll.reg'
tb.config.tc_lx_create_reg_file_start = '0x44e00500'
tb.config.tc_lx_create_reg_file_stop = '0x44e00540'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_MPU
tb.config.tc_lx_create_reg_file_name = 'am335x_cm_mpu.reg'
tb.config.tc_lx_create_reg_file_start = '0x44e00600'
tb.config.tc_lx_create_reg_file_stop = '0x44e00608'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_DEVICE
tb.config.tc_lx_create_reg_file_name = 'am335x_cm_dev.reg'
tb.config.tc_lx_create_reg_file_start = '0x44e00700'
tb.config.tc_lx_create_reg_file_stop = '0x44e00704'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_RTC
tb.config.tc_lx_create_reg_file_name = 'am335x_cm_rtc.reg'
tb.config.tc_lx_create_reg_file_start = '0x44e00800'
tb.config.tc_lx_create_reg_file_stop = '0x44e00808'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_GFX
tb.config.tc_lx_create_reg_file_name = 'am335x_cm_gfx.reg'
tb.config.tc_lx_create_reg_file_start = '0x44e00900'
tb.config.tc_lx_create_reg_file_stop = '0x44e00918'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

tb.end_tc(True)
