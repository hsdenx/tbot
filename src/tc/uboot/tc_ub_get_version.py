# SPDX-License-Identifier: GPL-2.0
#
# Description:
# search in tb.config.tc_ub_get_version_file the string
# tb.config.tc_ub_get_version_string
# and save the value in tb.config.tc_return and create
# event ID UBOOT_VERSION.
#
# used variables
#
# - tb.config.tc_ub_get_version_file
#| file in which string gets searched
#| default: ''
#
# - tb.config.tc_ub_get_version_string
#| string which get searched in file
#| default: ''
#
# End:

from tbotlib import tbot

logging.info("arg: %s", tb.workfd.name)

# set board state for which the tc is valid
tb.set_board_state("lab")

# set env var
c = tb.workfd

sf = tb.config.tc_ub_get_version_file
se = tb.config.tc_ub_get_version_string

cmd = 'strings -a ' + sf + ' | grep "' + se + '" --color=never'
tb.eof_write_cmd_get_line(c, cmd)
tb.config.tc_return = tb.ret_write_cmd_get_line.strip()
if tb.config.tc_return[0] == 'V':
    tb.config.tc_return = tb.config.tc_return[1:]

tb.event.create_event('main', tb.config.boardname, "UBOOT_VERSION", tb.config.tc_return)

tb.end_tc(True)
