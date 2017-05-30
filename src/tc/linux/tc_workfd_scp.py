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
# python2.7 src/common/tbot.py -s lab_denx -c exceet -t tc_workfd_scp.py
#
# start an scp transfer
# tb.config.tc_workfd_scp_opt: scp options
# tb.config.tc_workfd_scp_from: from where
# tb.config.tc_workfd_scp_to
#
# End:

from tbotlib import tbot

logging.info("args: workfd %s", tb.workfd.name)
logging.info("args: %s %s %s", tb.config.tc_workfd_scp_opt, tb.config.tc_workfd_scp_from, tb.config.tc_workfd_scp_to)

c = tb.workfd

cmd = 'scp ' + tb.config.tc_workfd_scp_opt + ' ' + tb.config.tc_workfd_scp_from + ' ' + tb.config.tc_workfd_scp_to
tb.eof_write(c, cmd)
ret = True
s = ['Are you sure']
while ret:
    tmp = tb.tbot_rup_and_check_strings(c, s)
    if tmp == '0':
        tb.eof_write(c, 'yes')
    elif tmp == 'prompt':
        ret = False

tb.end_tc(True)
