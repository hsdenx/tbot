# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start all testcases for the mcx board linux stable and linux-ml
# End:

from tbotlib import tbot

tb.statusprint("tc_mcx testing linux stable")
tb.config.tc_lx_regulator_nrs = ['0 regulator-dummy -', '1 hsusb1_vbus 5000000',
		'2 vmmc 3300000', '3 vdd_core 1200000',
		'4 vddshv 3300000', '5 vdds 1800000',
		'6 LDO1 1800000', '7 LDO2 3300000']
#tb.eof_call_tc("tc_board_mcx_tests.py")

tb.statusprint("tc_mcx testing linux mainline")
tb.config.tc_lx_regulator_nrs = ['0 regulator-dummy -', '1 hsusb1_vbus 5000000',
		'2 vmmc 3300000', '3 pbias_mmc_omap2430 3000000',
		'4 DCDC1 1200000', '5 DCDC2 3300000', '6 DCDC3 1800000',
		'7 LDO1 1800000', '8 LDO2 3300000']
tb.config.ub_boot_linux_cmd = 'run tbot_boot_linux_ml'
tb.eof_call_tc("tc_board_mcx_tests.py")
tb.end_tc(True)
