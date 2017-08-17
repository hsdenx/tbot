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

tb.end_tc(True)
