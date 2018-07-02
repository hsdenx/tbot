# SPDX-License-Identifier: GPL-2.0
#
# Description:
# On the sigmatek-nand board we have problems with a crash in U-boot
# We do:
# - wait until linux state is reached
# - wait random seconds (3 -10)
# - power off the board
# - wait 3 seconds for powering really of the board
# - loop this 50 times
# End:

import time
from random import randint
from tbotlib import tbot

c = tb.c_con
i = 0
# do this until error
while i < 50:
    logging.info("********************** itteration: %d ***************", i)
    tb.statusprint("********************** itteration: %d ***************" % i)
    # which bootmode
    mode = randint(1,3)
    tb.statusprint("mode %s" % mode)
    if mode == 2:
        tb.set_board_state("u-boot")
        tmp = 'boot'
        tb.eof_write(c, tmp)
    if mode == 3:
        tb.set_board_state("u-boot")
        tmp = 'run bootcmd'
        tb.eof_write(c, tmp)

    tb.set_board_state("linux")

    # sleep random time (3-10 seconds)
    timerand=randint(3,10)
    tb.statusprint("random time %s" % timerand)
    time.sleep(timerand)
    # poweroff
    tb.eof_call_tc("tc_lab_poweroff.py")
    # read rest of bytes from con
    tb.flush(c)
    time.sleep(3)
    i += 1

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
