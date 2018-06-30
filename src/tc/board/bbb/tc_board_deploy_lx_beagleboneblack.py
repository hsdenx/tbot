# SPDX-License-Identifier: GPL-2.0
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
