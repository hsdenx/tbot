# SPDX-License-Identifier: GPL-2.0
#
# Description:
# create with i2cget tool a register dump of
# pfuze3000 on bus
# tb.config.tc_lx_create_i2c_reg_dump_pfuze_3000_bus
#
# used variables:
#
# - tb.config.tc_lx_create_i2c_reg_dump_pfuze_3000_bus
#|  i2c bus number on which the pfuze3000 is connected to.
#|  default: '0x0'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lx_create_i2c_reg_dump_pfuze_3000_bus', '0x0')

tb.config.tc_lx_create_i2c_reg_file_bus = tb.config.tc_lx_create_i2c_reg_dump_pfuze_3000_bus
tb.config.tc_lx_create_i2c_reg_file_addr = '0x08'
tb.config.tc_lx_create_i2c_reg_file_start = '0x00'
tb.config.tc_lx_create_i2c_reg_file_stop = '0x70'
tb.config.tc_lx_create_i2c_reg_file_name = 'i2c_dump_pfuze3000@' + tb.config.tc_lx_create_i2c_reg_dump_pfuze_3000_bus + '.txt'
tb.eof_call_tc("tc_lx_create_i2c_reg_file.py")

tb.end_tc(True)
