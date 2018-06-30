# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_dfu_random_default.py
# test a U-Boot dfu alt setting tb.config.tc_ub_dfu_dfu_util_alt_setting
# with reading / writing different sizes
# End:

from tbotlib import tbot

# here starts the real test
logging.info("args: %s %s %s %s", tb.config.tc_ub_dfu_dfu_util_path,
	tb.config.tc_ub_dfu_dfu_util_ssh, tb.config.tc_ub_dfu_dfu_util_alt_setting,
	tb.config.tc_ub_dfu_rand_ubcmd)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

for size in tb.config.dfu_test_sizes_default:
    tb.config.tc_ub_dfu_rand_size = str(size)
    ret = tb.call_tc("tc_ub_dfu_random.py")
    if ret != True:
        tb.end_tc(False)

tb.end_tc(True)
