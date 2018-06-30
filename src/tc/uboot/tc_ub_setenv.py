# SPDX-License-Identifier: GPL-2.0
#
# Description:
# set U-Boot Environmentvariable tb.config.setenv_name with value
# tb.config.setenv_value
#
# used variables:
#
# - tb.config.setenv_name
#| name of the U-Boot Environment variable
#| default: 'tralala'
#
# - tb.config.setenv_value
#| value of the U-Boot Environment variable
#| defalt: 'hulalahups'
#
# End:

from tbotlib import tbot

tb.define_variable('setenv_name', 'tralala')
tb.define_variable('setenv_value', 'hulalahups')

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# set env var
c = tb.c_con

tmp = 'setenv ' + tb.config.setenv_name + ' ' + tb.config.setenv_value
tb.eof_write(c, tmp)
tb.tbot_expect_prompt(c)

# check if it is set with the correct value
tmp = 'printenv ' + tb.config.setenv_name
tb.eof_write(c, tmp)
str3 = tb.config.setenv_name + '=' + tb.config.setenv_value
ret = tb.tbot_expect_string(c, str3)
if ret == 'prompt':
    tb.end_tc(False)

tb.tbot_expect_prompt(c)
tb.end_tc(True)
