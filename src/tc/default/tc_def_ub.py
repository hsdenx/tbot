# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c cfgfile -t tc_def_ub.py
# simple set default values for U-Boot testcases
# End:

from tbotlib import tbot

tb.call_tc('tc_def_tbot.py')

try:
    tb.config.tc_ub_dfu_dfu_util_downloadfile
except AttributeError:
    tmp = ('%sdfu_file' % tb.config.lab_tmp_dir)
    tb.config.__dict__.update({'tc_ub_dfu_dfu_util_downloadfile' : tmp})

try:
    tb.config.tc_ub_tftp_path
except AttributeError:
    tmp = tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir
    tb.config.__dict__.update({'tc_ub_tftp_path' : tmp})

try:
    tb.config.tc_ub_tftp_file_name
except AttributeError:
    tmp = tb.config.tc_ub_tftp_path + '/env.txt'
    tb.config.__dict__.update({'tc_ub_tftp_file_name' : tmp})

tb.gotprompt = True
tb.end_tc(True)
