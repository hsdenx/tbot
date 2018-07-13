# SPDX-License-Identifier: GPL-2.0
#
# Description:
# check if regulators in tb.config.tc_lx_regulator_nrs exist, and have
# the correct microvolts settings.
#
# used variables
#
# - tb.config.tc_lx_regulator_nrs
#| list of regulator strings. one string has 3 values
#| seperated by a space:
#| regulator_number name microvoltsvalue
#| default:
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lx_regulator_nrs', "['0 regulator-dummy -', '1 hsusb1_vbus 5000000',
                '2 vmmc 3300000', '3 pbias_mmc_omap2430 3000000',
                '4 DCDC1 1200000', '5 DCDC2 3300000', '6 DCDC3 1800000',
                '7 LDO1 1800000', '8 LDO2 3300000']")

tb.set_board_state("linux")

c = tb.c_con
def check_regulator(tb, c, nr, name, volts):
    tmp = 'cat /sys/class/regulator/regulator.' + nr + '/name'
    tb.eof_write(c, tmp)
    ret = tb.tbot_expect_string(c, name)
    if ret == 'prompt':
        tb.end_tc(False)
    if volts != '-':
        tb.tbot_expect_prompt(c)
        tmp = 'cat /sys/class/regulator/regulator.' + nr + '/microvolts'
        tb.eof_write_con(tmp)
        ret = tb.tbot_expect_string(c, volts)
        if ret == 'prompt':
            tb.end_tc(False)
    tb.tbot_expect_prompt(c)

for nr in tb.config.tc_lx_regulator_nrs:
    nr_list = nr.split()
    check_regulator(tb, c, nr_list[0], nr_list[1], nr_list[2])

tb.end_tc(True)
