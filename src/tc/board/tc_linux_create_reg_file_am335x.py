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
# tbot.py -s lab_denx -c cuby -t tc_linux_create_reg_file_am335x.py
# create a regfile for am335x SoC registers
# End:

from tbotlib import tbot
import time

tb.workfd = tb.c_ctrl

# CTRL Module
tb.config.tc_lx_create_reg_file_name = 'am335x_ctrl_module.reg'
tb.config.tc_lx_create_reg_file_start = '44e10000'
tb.config.tc_lx_create_reg_file_stop = '44e11448'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CTRL Module (Pinmux only)
tb.config.tc_lx_create_reg_file_name = 'am335x_pinmux.reg'
tb.config.tc_lx_create_reg_file_start = '44e10800'
tb.config.tc_lx_create_reg_file_stop = '44e10a38'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_DPLL
tb.config.tc_lx_create_reg_file_name = 'am335x_cm_dpll.reg'
tb.config.tc_lx_create_reg_file_start = '44e00500'
tb.config.tc_lx_create_reg_file_stop = '44e00540'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_MPU
tb.config.tc_lx_create_reg_file_name = 'am335x_cm_mpu.reg'
tb.config.tc_lx_create_reg_file_start = '44e00600'
tb.config.tc_lx_create_reg_file_stop = '44e00608'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_PER
tb.config.tc_lx_create_reg_file_name = 'am335x_cm_per.reg'
tb.config.tc_lx_create_reg_file_start = '44e00000'
tb.config.tc_lx_create_reg_file_stop = '44e00154'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_WKUP
tb.config.tc_lx_create_reg_file_name = 'am335x_cm_wkup.reg'
tb.config.tc_lx_create_reg_file_start = '44e00400'
tb.config.tc_lx_create_reg_file_stop = '44e004dc'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CM_PER
tb.config.tc_lx_create_reg_file_name = 'am335x_cm_per.reg'
tb.config.tc_lx_create_reg_file_start = '44e00000'
tb.config.tc_lx_create_reg_file_stop = '44e00154'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# Display
tb.config.tc_lx_create_reg_file_name = 'am335x_display.reg'
tb.config.tc_lx_create_reg_file_start = '0x4830e000'
tb.config.tc_lx_create_reg_file_stop = '0x4830e074'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")


# EMIF
tb.config.tc_lx_create_reg_file_name = 'am335x_emif.reg'
tb.config.tc_lx_create_reg_file_start = '4c000000'
tb.config.tc_lx_create_reg_file_stop = '4c000124'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# USBSS
tb.config.tc_lx_create_reg_file_name = 'am335x_usbss.reg'
tb.config.tc_lx_create_reg_file_start = '47400000'
tb.config.tc_lx_create_reg_file_stop = '47400248'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# USB0
tb.config.tc_lx_create_reg_file_name = 'am335x_usb0.reg'
tb.config.tc_lx_create_reg_file_start = '47401000'
tb.config.tc_lx_create_reg_file_stop = '474010ec'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# USB0PHY
tb.config.tc_lx_create_reg_file_name = 'am335x_usb0phy.reg'
tb.config.tc_lx_create_reg_file_start = '47401300'
tb.config.tc_lx_create_reg_file_stop = '47401358'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# USB1
tb.config.tc_lx_create_reg_file_name = 'am335x_usb1.reg'
tb.config.tc_lx_create_reg_file_start = '47401800'
tb.config.tc_lx_create_reg_file_stop = '474018e8'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# USB1PHY
tb.config.tc_lx_create_reg_file_name = 'am335x_usb1phy.reg'
tb.config.tc_lx_create_reg_file_start = '47401b00'
tb.config.tc_lx_create_reg_file_stop = '47401b58'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# GPMC
tb.config.tc_lx_create_reg_file_name = 'am335x_gpmc.reg'
tb.config.tc_lx_create_reg_file_start = '50000000'
tb.config.tc_lx_create_reg_file_stop = '50000084'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CPSW_SS
tb.config.tc_lx_create_reg_file_name = 'am335x_cpsw_ss.reg'
tb.config.tc_lx_create_reg_file_start = '4a100000'
tb.config.tc_lx_create_reg_file_stop = '4a100034'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CPSW_PORT
tb.config.tc_lx_create_reg_file_name = 'am335x_cpsw_port.reg'
tb.config.tc_lx_create_reg_file_start = '4a100100'
tb.config.tc_lx_create_reg_file_stop  = '4a100250'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CPSW_ALE
tb.config.tc_lx_create_reg_file_name = 'am335x_cpsw_ale.reg'
tb.config.tc_lx_create_reg_file_start = '4a100d00'
tb.config.tc_lx_create_reg_file_stop  = '4a100d58'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")


# CPSW_SL1
tb.config.tc_lx_create_reg_file_name = 'am335x_cpsw_sl1.reg'
tb.config.tc_lx_create_reg_file_start = '4a100d80'
tb.config.tc_lx_create_reg_file_stop  = '4a100dac'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CPSW_SL2
tb.config.tc_lx_create_reg_file_name = 'am335x_cpsw_sl2.reg'
tb.config.tc_lx_create_reg_file_start = '4a100dc0'
tb.config.tc_lx_create_reg_file_stop  = '4a100dec'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# MDIO
tb.config.tc_lx_create_reg_file_name = 'am335x_cpsw_mdio.reg'
tb.config.tc_lx_create_reg_file_start = '4a101000'
tb.config.tc_lx_create_reg_file_stop  = '4a101090'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")


tb.end_tc(True)
