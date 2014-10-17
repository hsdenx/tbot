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
tb.eof_write_ctrl(tmp)
ret = tb.search_str_in_readline_ctrl(cd_cmd_error_txt)
if ret == True:
    # clone u-boot.git
    tmp = "git clone " + tb.tc_lab_get_uboot_source_git_repo + " " + u_boot_name
    tb.eof_write_ctrl(tmp)
    tb.eof_search_str_in_readline_ctrl(tb.tc_lab_end_git_clone_text)

    tmp = "cd " + u_boot_name
    tb.eof_write_ctrl(tmp)
    ret = tb.search_str_in_readline_ctrl(cd_cmd_error_txt)
    if ret == True:
        tb.end_tc(False)
    #check out a specific branch
    tmp = "git checkout " + tb.tc_lab_get_uboot_source_git_branch
    tb.eof_write_ctrl(tmp)
    tb.eof_search_str_in_readline_end_ctrl(tb.tc_lab_end_git_checkout_text)

tb.eof_read_end_state_ctrl(1)
tb.end_tc(True)
