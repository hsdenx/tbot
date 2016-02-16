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
## @package tc_workfd_get_linux_source
# get Linux source
# and go into the source tree
# @param: workfd filehandle on which TC sends commands
# @param: tc_lab_get_linux_source_git_repo: linux repo
#
# @return: nothing
#
from tbotlib import tbot

logging.info("args: workdfd: %s %s %s %s", tb.workfd, tb.tc_lab_get_linux_source_git_repo, tb.tc_lab_get_linux_source_git_branch, tb.tc_lab_apply_patches_dir)
logging.info("args: %s %s ", tb.tc_lab_get_linux_source_git_reference, tb.tc_lab_get_linux_source_git_repo_user)

ret = tb.call_tc("tc_workfd_goto_linux_code.py")
if ret == False:
    linux_name = "linux-" + tb.boardlabname
    tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")
    # clone linux git
    if tb.tc_lab_get_linux_source_git_reference != 'none':
        opt = '--reference=' + tb.tc_lab_get_linux_source_git_reference + ' '
    else:
        opt = ''
    tmp = "git clone " + opt + tb.tc_lab_get_linux_source_git_repo + " " + linux_name
    tb.eof_write(tb.workfd, tmp)
    searchlist = ["Username", "Password", "Authentication failed"] # add here error cases
    tmp = True
    clone_ok = True
    while tmp == True:
        tmp = tb.readline_and_search_strings(tb.workfd, searchlist)
        if tmp == 0:
            tb.write_stream(tb.workfd, tb.tc_lab_get_linux_source_git_repo_user)
            tmp = True
        if tmp == 1:
            tb.write_stream_passwd(tb.workfd, tb.tc_lab_get_linux_source_git_repo_user, tb.tc_lab_get_linux_source_git_repo)
            tmp = True
        if tmp == 2:
            clone_ok = False
            tmp = True
        elif tmp == None:
            #endless loop
            tmp = True
        elif tmp == 'prompt':
            tmp = False

    if clone_ok != True:
        tb.end_tc(False)

    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

    tmp = "cd " + linux_name
    tb.eof_write_lx_cmd_check(tb.workfd, tmp)

    #check out a specific branch
    tmp = "git checkout " + tb.tc_lab_get_linux_source_git_branch
    tb.eof_write_lx_cmd_check(tb.workfd, tmp)

# check if there are patches to applys
tb.eof_call_tc("tc_lab_apply_patches.py")

# check if there are local "git am" patches to apply
tb.eof_call_tc("tc_workfd_apply_local_patches.py")

tb.end_tc(True)
