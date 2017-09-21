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
#
# simple call bitbake with tb.config.tc_workfd_bitbake_args
#
# if tb.config.tc_workfd_bitbake_machine is set, also cat
# the content of the newest file in tmp/log/cooker/" + tb.config.tc_workfd_bitbake_machine + "/*
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_bitbake_machine
except:
    tb.config.tc_workfd_bitbake_machine = ''

logging.info("args: %s %s", tb.workfd, tb.config.tc_workfd_bitbake_args)

tlist = [
	'pid',
	'tasks',
	'Loading',
	'Initialising'
]
tb.write_lx_cmd_check(tb.workfd, 'bitbake ' + tb.config.tc_workfd_bitbake_args, triggerlist=tlist)

if tb.config.tc_workfd_bitbake_machine != '':
    # list newest file in tmp/log/cooker/<machine>/*
    ma = tb.config.tc_workfd_bitbake_machine

    cmd = "ls -t tmp/log/cooker/" + ma + "/* | head -n1"
    tb.eof_write_cmd_get_line(tb.workfd, cmd)

    cmd = 'cat ' + tb.ret_write_cmd_get_line.rstrip()
    tb.write_lx_cmd_check(tb.workfd, cmd)

tb.end_tc(True)
