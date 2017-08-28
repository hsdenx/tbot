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
#
# Switch on/off boardpower through a GPIO pin
# from the lab PC
#
# define the gpio for powering on/off in your board config
# file with for example:
# gpio_power_on = gpo(21) # gpio number of gpio used to controll power of board
#
# End:

from tbotlib import tbot

logging.info("arg: ")

tb.set_board_state("lab")
savefd = tb.workfd
tb.workfd = tb.c_ctrl

if (tb.power_state == 'on'):
    tb.eof_call_tc("tc_workfd_set_gpio.py", highlow='high', gpio=tb.config.gpio_power_on)

elif (tb.power_state == 'off'):
    tb.eof_call_tc("tc_workfd_set_gpio.py", highlow='low', gpio=tb.config.gpio_power_on)
else:
    logging.error("%s not supported.", tb.power_state)
    tb.end_tc(False)

tb.workfd = savefd
tb.end_tc(True)
