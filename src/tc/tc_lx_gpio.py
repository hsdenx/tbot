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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_gpio.py
from tbotlib import tbot

#here starts the real test
logging.info("args: %s %s %s", tb.tc_lx_gpio_nr, tb.tc_lx_gpio_dir, tb.tc_lx_gpio_val)

#set board state for which the tc is valid
tb.set_board_state("linux")

gpio_dir='/sys/class/gpio'

tmp='if [ ! -d "' + gpio_dir + '" ]; then echo FAIL; fi'
tb.eof_write_con(tmp)
tb.eof_search_str_in_readline_end_con("FAIL")

# check if gpio is exported
# if not export it
tmp='if [ ! -d "' + gpio_dir + '/gpio' + tb.tc_lx_gpio_nr + '" ]; then echo FAIL; fi'
tb.eof_write_con(tmp)
ret = tb.search_str_in_readline_con("FAIL")
if ret:
    tmp='echo ' + tb.tc_lx_gpio_nr + ' > ' + gpio_dir + '/export'
    tb.eof_write_con_lx_cmd(tmp)

tmp_dir=gpio_dir + '/gpio' + tb.tc_lx_gpio_nr

#set direction
tmp='echo "' + tb.tc_lx_gpio_dir + '" > ' + tmp_dir + '/direction'
tb.eof_write_con_lx_cmd(tmp)

#set value
tmp='echo "' + tb.tc_lx_gpio_val + '" > ' + tmp_dir + '/value'
tb.eof_write_con_lx_cmd(tmp)

tb.end_tc(True)
