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
# start with
# python2.7 src/common/tbot.py -c tbot_sirius_dds.cfg -t tc_board_sirius_dds.py
# On the sirius board we have problems with ubifs
# on nand flash and power cuts. So this is a special
# testcase for this board. We do:
# - go into statte u-boot
# - start linux with ubifs as rootfs
# - wait until Userspace APP SiriusApplicat is started
# - wait random seconds (3 -10)
# - power off the board
# - wait 3 seconds for powering really of the board
# - loop this 50 times
# if we have an ubifs error, testcase ends with error
#
import time
from random import randint
from tbotlib import tbot

i = 0
# do this until error
while i < 50:
    logging.info("********************** itteration: %d ***************", i)
    #set board state for which the tc is valid
    tb.set_board_state("u-boot")

    #run hsubi
    tb.eof_write_con("run hsubi")
    #check if 'Starting up SiriusApplicat' comes
    tb.eof_search_str_in_readline_con("Starting up SiriusApplicat")
    #sleep random time (3-10 seconds)
    timerand=randint(3,10)
    tb.statusprint("random time %s" % timerand)
    time.sleep(timerand)
    #poweroff
    tb.eof_call_tc("tc_lab_poweroff.py")
    #read rest of bytes from con
    tb.read_end_state_con()
    time.sleep(3)
    i += 1

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
