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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_get_linux_source.py
# get U-Boot source
# and go into the source tree
from tbotlib import tbot

logging.info("args: workdfd: %s %s %s %s", tb.workfd, tb.tc_lab_get_linux_source_git_repo, tb.tc_lab_get_linux_source_git_branch, tb.tc_lab_apply_patches_dir)

tmp = "cd " + tb.tc_lab_source_dir
tb.eof_write(tb.workfd, tmp)
tb.eof_read_end_state(tb.workfd, 1)
tb.eof_call_tc("tc_workfd_check_cmd_success.py")

linux_name = "linux-" + tb.boardlabname
tmp = "cd " + linux_name
tb.eof_write(tb.workfd, tmp)
tb.eof_read_end_state(tb.workfd, 1)
ret = tb.call_tc("tc_workfd_check_cmd_success.py")
#ret = tb.eof_search_str_in_readline(tb.workfd, cd_cmd_error_txt, 0)
if ret == False:
    # clone linux git
    tmp = "git clone " + tb.tc_lab_get_linux_source_git_repo + " " + linux_name
    tb.eof_write(tb.workfd, tmp)
    tb.eof_read_end_state(tb.workfd, 100)
    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

    tmp = "cd " + linux_name
    tb.eof_write(tb.workfd, tmp)
    tb.eof_read_end_state(tb.workfd, 1)
    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

    #check out a specific branch
    tmp = "git checkout " + tb.tc_lab_get_linux_source_git_branch
    tb.eof_write(tb.workfd, tmp)
    tb.eof_read_end_state(tb.workfd, 1)
    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

tb.eof_read_end_state(tb.workfd, 1)

# check if there are patches to apply
tb.eof_call_tc("tc_lab_apply_patches.py")

# check if there are local "git am" patches to apply
tb.eof_call_tc("tc_workfd_apply_local_patches.py")

tb.end_tc(True)
