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
# tbot.py -s lab_denx -c aristainetos2 -t tc_linux_create_reg_file_imx6qdl.py
# create a regfile for am335x SoC registers
# End:

from tbotlib import tbot
import time

tb.workfd = tb.c_ctrl

# IOMUX
tb.config.tc_lx_create_reg_file_name = 'imx6qdl_iomux_module.reg'
tb.config.tc_lx_create_reg_file_start = '0x20e0000'
tb.config.tc_lx_create_reg_file_stop = '0x20e0950'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")

# CCM
tb.config.tc_lx_create_reg_file_name = 'imx6qdl_ccm_module.reg'
tb.config.tc_lx_create_reg_file_start = '0x020c4000'
tb.config.tc_lx_create_reg_file_stop = '0x020c408c'
tb.config.tc_lx_readreg_mask = 0xffffffff
tb.config.tc_lx_readreg_type = 'w'
tb.eof_call_tc("tc_lx_create_reg_file.py")


tb.end_tc(True)
