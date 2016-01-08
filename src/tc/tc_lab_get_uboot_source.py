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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_get_uboot_source.py
# get U-Boot source
# and go into the source tree
from tbotlib import tbot

cd_cmd_error_txt = "No such"
tmp = "cd " + tb.tc_lab_source_dir
tb.eof_write_ctrl(tmp)
tb.eof_search_str_in_readline_end_ctrl(cd_cmd_error_txt)

u_boot_name = "u-boot-" + tb.boardlabname
tmp = "cd " + u_boot_name
tb.eof_write_cmd(tb.channel_ctrl, tmp)
tb.workfd = tb.channel_ctrl
ret = tb.call_tc("tc_workfd_check_cmd_success.py")
if ret == False:
    # clone u-boot.git
    tmp = "git clone " + tb.tc_lab_get_uboot_source_git_repo + " " + u_boot_name
    tb.eof_write_lx_cmd_check(tb.channel_ctrl, tmp)

    tmp = "cd " + u_boot_name
    tb.eof_write_lx_cmd_check(tb.channel_ctrl, tmp)
    #check out a specific branch
    tmp = "git checkout " + tb.tc_lab_get_uboot_source_git_branch
    tb.eof_write_lx_cmd_check(tb.channel_ctrl, tmp)

# check if there are patches to apply
tb.eof_call_tc("tc_lab_apply_patches.py")

tb.end_tc(True)
