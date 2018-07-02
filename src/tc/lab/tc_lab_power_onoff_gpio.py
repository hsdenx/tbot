# SPDX-License-Identifier: GPL-2.0
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
# used variables
#
# - tb.config.gpio_power_on
#| gpio pin used for powering on / off the board
#| default: ''
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
