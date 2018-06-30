# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_get_version.py
# get the U-Boot and/or SPL version from a binary
# and save it in tb.uboot_vers or tb.spl_vers
# End:

from tbotlib import tbot

logging.info("arg: %s %s %s", tb.workfd.name, tb.tc_ub_get_version_file, tb.tc_ub_get_version_string)

# set board state for which the tc is valid
tb.set_board_state("lab")

# set env var
c = tb.workfd

sf = tb.tc_ub_get_version_file
se = tb.tc_ub_get_version_string

cmd = 'strings -a ' + sf + ' | grep "' + se + '" --color=never'
tb.eof_write_cmd_get_line(c, cmd)
tb.config.tc_return = tb.ret_write_cmd_get_line.strip()
if tb.config.tc_return[0] == 'V':
    tb.config.tc_return = tb.config.tc_return[1:]

tb.event.create_event('main', tb.config.boardname, "UBOOT_VERSION", tb.config.tc_return)

tb.end_tc(True)
