# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple set default values for U-Boot testcases
#
# used variables
#
# - tb.config.tc_ub_tftp_file_addr
#| ram address to which the file gets loaded
#| default: tb.config.ub_load_board_env_addr
#
# - tb.config.tc_ub_tftp_file_name
#| file name for the tftp command
#| default: ''
#
# - tb.config.tc_ub_tftp_path
#| tftp boot directory path for tftp U-Boot command
#| default: tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir
#
# End:

from tbotlib import tbot

# set only once default variables
try:
    tb.config.tc_def_ub_set
except:
    logging.info("Setting U-Boot defaults now")
    tb.define_variable('tc_ub_tftp_path', tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir)
    tb.define_variable('tc_ub_tftp_file_addr', tb.config.ub_load_board_env_addr)
    tb.define_variable('tc_ub_tftp_file_name', tb.config.tc_ub_tftp_path + '/env.txt')

tb.config.tc_def_ub_set = 'yes'
tb.gotprompt = True
tb.end_tc(True)
