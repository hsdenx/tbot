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
# Copy the linux binaries from the compile PC
# to the tftp directory on the lab PC
#
# End:

from tbotlib import tbot

logging.info("arg: %s", tb.workfd.name)

tb.config.tc_workfd_scp_opt = ''
# zImage
tb.config.tc_workfd_scp_from = "$TBOT_BASEDIR_LINUX/arch/arm/boot/zImage"
tb.config.tc_workfd_scp_to = tb.config.user + '@' + tb.config.ip + ':' + tb.config.tftpdir + '/' + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir + '/zImage'
tb.call_tc('tc_workfd_scp.py')

# DTS
for f in tb.config.tc_workfd_compile_linux_dt_name:
    tb.config.tc_workfd_scp_from = '$TBOT_BASEDIR_LINUX/arch/arm/boot/dts/' + f
    tb.config.tc_workfd_scp_to = tb.config.user + '@' + tb.config.ip + ':' + tb.config.tftpdir + '/' + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir + '/' + f
    tb.call_tc('tc_workfd_scp.py')

# System.map
tb.config.tc_workfd_scp_from = "$TBOT_BASEDIR_LINUX/System.map"
tb.config.tc_workfd_scp_to = tb.config.user + '@' + tb.config.ip + ':' + tb.config.tftpdir + '/' + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir + '/System.map-linux'
tb.call_tc('tc_workfd_scp.py')

tb.end_tc(True)
