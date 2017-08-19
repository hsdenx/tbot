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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_prepare_laptop_hs.py
#
# do setup needed for the laptop from hs, when used as
# lapPC
#
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd, tb.config.tc_workfd_check_if_dir_exists_name)

# setup ip addr for p2p1 interface
cmd = 'sudo ifconfig p2p1 192.168.2.1 up'
tb.write_lx_sudo_cmd_check(tb.workfd, cmd, tb.config.user, tb.config.ip)

# check if ftdi module is loaded, rmmod it if yes
cmd = 'sudo lsmod | grep ftdi'
ret = tb.write_lx_sudo_cmd_check(tb.workfd, cmd, tb.config.user, tb.config.ip, endTC = False)
if ret == True:
    cmd = 'sudo rmmod ftdi_sio'
    tb.write_lx_sudo_cmd_check(tb.workfd, cmd, tb.config.user, tb.config.ip)

tb.end_tc(True)
