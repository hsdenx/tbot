# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_setenv.py
# set U-Boot Environmentvariable tb.config.setenv_name with value
# tb.config.setenv_value
# End:

from tbotlib import tbot

# here starts the real test
logging.info("testcase arg: %s %s", tb.config.setenv_name, tb.config.setenv_value)
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
