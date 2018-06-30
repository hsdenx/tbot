# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c fipad -t tc_board_fipad_upd_ub_spi.py
# update SPL and u-boot.img on the SPI NOR
# End:

from tbotlib import tbot

logging.info("typ: %s", tb.tc_board_fipad_upd_ub_typ)

# not implemented yet
tb.end_tc(False)
