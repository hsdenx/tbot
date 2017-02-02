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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_sispmctl_get_variables.py
# get serial and index for tb.config.boardlabpowername for
# controlling the Gembird Silver Shield PM power controller
# and save it in tb.config.gembird_serial and tb.config.gembird_index
#
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.config.boardname, tb.config.boardlabpowername)

if tb.config.boardlabpowername == 'beagleboneblack':
    tb.config.gembird_index = '1'
    tb.config.gembird_serial = '01:01:56:a2:f1'
else:
    logging.error("boardlabname %s not found." % (tb.config.boardlabpowername))
    tb.end_tc(False)

tb.end_tc(True)
