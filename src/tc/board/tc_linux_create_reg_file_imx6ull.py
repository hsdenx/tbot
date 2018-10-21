# SPDX-License-Identifier: GPL-2.0
#
# Description:
# create a regfile for imx6ull SoC registers
# End:

from tbotlib import tbot
import time

tb.workfd = tb.c_ctrl

# IOMUX GPR
tb.config.tc_lx_create_reg_file_name = 'imx6ull_iomux_gpr.reg'
tb.config.tc_lx_create_reg_file_start = '0x20e4000'
tb.config.tc_lx_create_reg_file_stop = '0x20e403c'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# IOMUX SNVS
tb.config.tc_lx_create_reg_file_name = 'imx6ull_iomux_snvs.reg'
tb.config.tc_lx_create_reg_file_start = '0x2290000'
tb.config.tc_lx_create_reg_file_stop = '0x2290070'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# IOMUX
tb.config.tc_lx_create_reg_file_name = 'imx6ull_iomux.reg'
tb.config.tc_lx_create_reg_file_start = '0x20e0044'
tb.config.tc_lx_create_reg_file_stop = '0x20e06a0'
tb.eof_call_tc("tc_lx_create_reg_file.py")

tb.end_tc(True)
