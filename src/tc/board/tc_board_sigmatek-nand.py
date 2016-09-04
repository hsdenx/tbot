# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Description:
# start with
# python2.7 src/common/tbot.py -c tbot_sigmatek-nand.cfg -t tc_board_sigmatek-nand.py
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
