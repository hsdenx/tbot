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
# tbot.py -s lab_denx -c boardname -t tc_workfd_linux_get_uboot_env.py
# read U-Boot Environment variable from tb.config.linux_get_uboot_env_name
# from linux with fw_printenv, and save the value in tb.config.linux_get_uboot_env_value
# End:

from tbotlib import tbot

tb.set_board_state("linux")

logging.info("args: workfd %s %s", tb.workfd.name, tb.config.linux_get_uboot_env_name)

tb.config.linux_get_uboot_env_value = 'undef'
cmd = 'fw_printenv ' + tb.config.linux_get_uboot_env_name
tb.eof_write(tb.workfd, cmd)
ret = True
suc = False
while ret:
    tmp = tb.tbot_rup_and_check_strings(tb.workfd, '\n')
    if tmp == '0':
        tmp = tb.buf.lstrip('\r\n')
        tmp = tmp.split('\r\n')
        tmp = tmp[0].split('=')
        if len(tmp) == 2:
            tb.config.linux_get_uboot_env_value = tmp[1]
            suc = True
    if tmp == 'prompt':
        ret = False

tb.end_tc(suc)
