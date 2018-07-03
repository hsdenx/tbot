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
#
# used variables
#
# - tb.config.bbb_check_crng_init
#| wait for string "crng init"
#| default: 'yes'
#
# End:

from tbotlib import tbot

tb.define_variable('bbb_check_crng_init', 'yes')

if tb.config.bbb_check_crng_init == 'yes':
    tb.c_con.expect_string('crng init')

tb.end_tc(True)
