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
# python2.7 src/common/tbot.py -c tbot_aristainetos2.cfg -t tc_linux_create_reg_file_am335x.py
# create a regfile for am335x SoC registers
# End:

from tbotlib import tbot
import time

tb.workfd = tb.c_ctrl

tb.tc_lx_create_reg_file_name = 'am335x_ctrl_module.reg'
tb.tc_lx_create_reg_file_start = '0x44e10000'
tb.tc_lx_create_reg_file_stop = '0x44e11448'
tb.tc_lx_readreg_mask = 0xffffffff
tb.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

tb.tc_lx_create_reg_file_name = 'am335x_display.reg'
tb.tc_lx_create_reg_file_start = '0x4830e000'
tb.tc_lx_create_reg_file_stop = '0x4830e074'
tb.tc_lx_readreg_mask = 0xffffffff
tb.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_PER
tb.tc_lx_create_reg_file_name = 'am335x_cm_per.reg'
tb.tc_lx_create_reg_file_start = '0x44e00000'
tb.tc_lx_create_reg_file_stop = '0x44e00154'
tb.tc_lx_readreg_mask = 0xffffffff
tb.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_WKUP
tb.tc_lx_create_reg_file_name = 'am335x_cm_wkup.reg'
tb.tc_lx_create_reg_file_start = '0x44e00400'
tb.tc_lx_create_reg_file_stop = '0x44e004dc'
tb.tc_lx_readreg_mask = 0xffffffff
tb.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_DPLL
tb.tc_lx_create_reg_file_name = 'am335x_cm_dpll.reg'
tb.tc_lx_create_reg_file_start = '0x44e00500'
tb.tc_lx_create_reg_file_stop = '0x44e00540'
tb.tc_lx_readreg_mask = 0xffffffff
tb.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_MPU
tb.tc_lx_create_reg_file_name = 'am335x_cm_mpu.reg'
tb.tc_lx_create_reg_file_start = '0x44e00600'
tb.tc_lx_create_reg_file_stop = '0x44e00608'
tb.tc_lx_readreg_mask = 0xffffffff
tb.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_DEVICE
tb.tc_lx_create_reg_file_name = 'am335x_cm_dev.reg'
tb.tc_lx_create_reg_file_start = '0x44e00700'
tb.tc_lx_create_reg_file_stop = '0x44e00704'
tb.tc_lx_readreg_mask = 0xffffffff
tb.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_RTC
tb.tc_lx_create_reg_file_name = 'am335x_cm_rtc.reg'
tb.tc_lx_create_reg_file_start = '0x44e00800'
tb.tc_lx_create_reg_file_stop = '0x44e00808'
tb.tc_lx_readreg_mask = 0xffffffff
tb.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_GFX
tb.tc_lx_create_reg_file_name = 'am335x_cm_gfx.reg'
tb.tc_lx_create_reg_file_start = '0x44e00900'
tb.tc_lx_create_reg_file_stop = '0x44e00918'
tb.tc_lx_readreg_mask = 0xffffffff
tb.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

tb.end_tc(True)
