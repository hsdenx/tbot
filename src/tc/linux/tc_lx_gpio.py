# SPDX-License-Identifier: GPL-2.0
#
# Description:
# set in linux gpio tb.config.tc_lx_gpio_nr to direction tb.config.tc_lx_gpio_dir
# and value tb.config.tc_lx_gpio_val
#
# used variables
#
# - tb.config.tc_lx_gpio_nr
#| gpio number
#| default: '69'
#
# - tb.config.tc_lx_gpio_dir
#| direction to witch gpio get set 'in' or 'out'
#| default: 'out'
#
# - tb.config.tc_lx_gpio_val
#| state of gpio '0' or '1'
#| default: '1'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lx_gpio_nr', '69')
tb.define_variable('tc_lx_gpio_dir', 'out')
tb.define_variable('tc_lx_gpio_val', '1')

# set board state for which the tc is valid
tb.set_board_state("linux")

gpio_dir = '/sys/class/gpio'

c = tb.c_con
tmp = 'if [ ! -d "' + gpio_dir + '" ]; then echo FAIL; fi'
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'FAIL')
if ret == '0':
    tb.tbot_expect_prompt(c)
    tb.end_tc(False)

# check if gpio is exported
# if not export it
tmp = 'if [ ! -d "' + gpio_dir + '/gpio' + tb.config.tc_lx_gpio_nr + '" ]; then echo FAIL; fi'
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'FAIL')
if ret == '0':
    tb.tbot_expect_prompt(c)
    tmp = 'echo ' + tb.config.tc_lx_gpio_nr + ' > ' + gpio_dir + '/export'
    tb.eof_write_con_lx_cmd(tmp)

tmp_dir = gpio_dir + '/gpio' + tb.config.tc_lx_gpio_nr

# set direction
tmp = 'echo "' + tb.config.tc_lx_gpio_dir + '" > ' + tmp_dir + '/direction'
tb.eof_write_con_lx_cmd(tmp)

# set value
tmp = 'echo "' + tb.config.tc_lx_gpio_val + '" > ' + tmp_dir + '/value'
tb.eof_write_con_lx_cmd(tmp)

tb.end_tc(True)
