# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# nowadays after booting into linux there comes the message
# "random: crng init done"
#
# This pos in, and may disturb a current running test ...
#
# so call this testcase after logging into linux
# and wait until this string is read ...
#
# End:

from tbotlib import tbot

try:
    tb.config.bbb_check_crng_init
except:
    tb.config.bbb_check_crng_init = 'yes'

logging.info("args: %s", tb.config.bbb_check_crng_init)

if tb.config.bbb_check_crng_init == 'yes':
    tb.c_con.expect_string('crng init')

tb.end_tc(True)
