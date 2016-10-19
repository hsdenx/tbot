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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_gpio.py
# set in linux gpio tb.config.tc_lx_gpio_nr to direction tb.config.tc_lx_gpio_dir
# and value tb.config.tc_lx_gpio_val
# End:

from tbotlib import tbot

# here starts the real test
logging.info("args: %s %s %s", tb.config.tc_lx_gpio_nr, tb.config.tc_lx_gpio_dir, tb.config.tc_lx_gpio_val)

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
