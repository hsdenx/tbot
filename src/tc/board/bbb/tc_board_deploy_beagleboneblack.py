# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# Copy the binaries from the compile PC
# to the tftp directory on the lab PC
#
# End:

from tbotlib import tbot

logging.info("arg: %s", tb.workfd.name)

for f in tb.config.tc_demo_compile_install_test_files:
    tb.config.tc_workfd_scp_opt = 'none'
    tb.config.tc_workfd_scp_from = f
    tb.config.tc_workfd_scp_to = tb.config.user + '@' + tb.config.ip + ':' + tb.config.tftpdir + '/' + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir + '/' + f
    tb.eof_call_tc('tc_workfd_scp.py')

tb.end_tc(True)
