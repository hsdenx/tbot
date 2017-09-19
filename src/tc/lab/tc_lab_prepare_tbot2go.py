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
#
# do setup needed for the pi in tbot2go mode, when used as
# lapPC
#
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd, tb.config.tc_workfd_check_if_dir_exists_name)

con = True
try:
    tb.c_cpc
    if tb.workfd.name == tb.c_cpc.name:
        con = False
except:
    pass

if con == False:
    # do not set anything on compile PC
    tb.end_tc(True)

# setup ip addr for eth0 interface
cmd = 'sudo ifconfig eth0 down 192.168.3.1 up'
tb.write_lx_sudo_cmd_check(tb.workfd, cmd, tb.config.user, tb.config.ip)

tb.end_tc(True)
