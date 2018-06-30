# SPDX-License-Identifier: GPL-2.0
#
# Description:
# test a U-Boot dfu alt setting tb.config.tc_ub_dfu_dfu_util_alt_setting
# with reading / writing different sizes
# and calling testcase tc_ub_dfu_random.py
#
# used variables
#
# - tb.config.dfu_test_sizes_default
#| default: [
#|        64 - 1,
#|        64,
#|        64 + 1,
#|        128 - 1,
#|        128,
#|        128 + 1,
#|        960 - 1,
#|        960,
#|        960 + 1,
#|        4096 - 1,
#|        4096,
#|        4096 + 1,
#|        1024 * 1024 - 1,
#|        1024 * 1024,
#|        8 * 1024 * 1024,
#|    ]
#
# End:

from tbotlib import tbot

tb.define_variable('dfu_test_sizes_default', '[
        64 - 1,
        64,
        64 + 1,
        128 - 1,
        128,
        128 + 1,
        960 - 1,
        960,
        960 + 1,
        4096 - 1,
        4096,
        4096 + 1,
        1024 * 1024 - 1,
        1024 * 1024,
        8 * 1024 * 1024,
    ]')

# set board state for which the tc is valid
tb.set_board_state("u-boot")

for size in tb.config.dfu_test_sizes_default:
    tb.config.tc_ub_dfu_rand_size = str(size)
    ret = tb.call_tc("tc_ub_dfu_random.py")
    if ret != True:
        tb.end_tc(False)

tb.end_tc(True)
