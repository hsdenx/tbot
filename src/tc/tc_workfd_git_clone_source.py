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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_git_clone_source.py
# get source from git repo tb.config.tc_lab_git_clone_source_git_repo with "git clone"
# and go into the source tree. 
# check out branch tb.config.tc_lab_git_clone_source_git_branch
# and Apply patches if needed with:
# tc_lab_apply_patches.py and patches from directory
# tb.config.tc_lab_git_clone_apply_patches_dir
# use as reference tb.config.tc_lab_git_clone_source_git_reference
# if != 'none'
# You can give the repo a name with setting
# tb.config.tc_lab_git_clone_source_git_repo_name
# != 'none'
# If you need a user/password for clining, you can define
# the username through:
# tb.config.tc_lab_git_clone_source_git_repo_user
# define the password for this in password.py
# boardname in password.py is used as tb.config.tc_lab_git_clone_source_git_repo
# End:

from tbotlib import tbot

logging.info("args: workdfd: %s %s %s %s", tb.workfd.name, tb.config.tc_lab_git_clone_source_git_repo,
             tb.config.tc_lab_git_clone_source_git_branch, tb.config.tc_lab_git_clone_apply_patches_dir)
logging.info("args: %s %s ", tb.config.tc_lab_git_clone_source_git_reference,
             tb.config.tc_lab_git_clone_source_git_repo_user)
logging.info("args: %s ", tb.config.tc_lab_git_clone_source_git_repo_name)

if tb.config.tc_lab_git_clone_source_git_repo_name != 'none':
    repo_name = tb.config.tc_lab_git_clone_source_git_repo_name
else:
    # ToDo
    repo_name = ''

# clone ...
if tb.config.tc_lab_git_clone_source_git_reference != 'none':
    opt = '--reference=' + tb.config.tc_lab_git_clone_source_git_reference + ' '
else:
    opt = ''

tb.event.create_event('main', 'tc_workfd_git_clone_source.py', 'SET_DOC_FILENAME_NOIRQ', 'clone_' + repo_name)
tmp = "git clone " + opt + tb.config.tc_lab_git_clone_source_git_repo + " " + repo_name
tb.eof_write(tb.workfd, tmp)
searchlist = ["Username", "assword", "Authentication failed", "Receiving", "yes"]
loop = True
clone_ok = True
while loop == True:
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
        tb.write_stream(tb.workfd, tb.config.tc_lab_git_clone_source_git_repo_user)
    if ret == '1':
        if '@' in tb.config.tc_lab_git_clone_source_git_repo:
            # try to get the ip
            tmp = tb.config.tc_lab_git_clone_source_git_repo.split('@')
            u = tmp[0]
            u = u.split('/')
            u = u[-1]
            tmp = tmp[1]
            tmp = tmp.split(':')
            b = tmp[0]
        else:
            u = tb.config.tc_lab_git_clone_source_git_repo_user
            b = tb.config.tc_lab_git_clone_source_git_repo

        tb.write_stream_passwd(tb.workfd, u, b)
    if ret == '2':
        clone_ok = False
    if ret == '3':
        tb.tbot_trigger_wdt()
    if ret == '4':
        tb.eof_write(tb.workfd, 'yes', start=False)
    elif ret == 'prompt':
        loop = False

if clone_ok != True:
    tb.end_tc(False)

tb.eof_call_tc("tc_workfd_check_cmd_success.py")

tmp = "cd " + repo_name
tb.write_lx_cmd_check(tb.workfd, tmp)

# check out a specific branch
tmp = "git checkout " + tb.config.tc_lab_git_clone_source_git_branch
tb.write_lx_cmd_check(tb.workfd, tmp)

if tb.config.tc_lab_git_clone_source_git_commit_id != 'none':
    tmp = "git reset --hard " + tb.config.tc_lab_git_clone_source_git_commit_id
    tb.write_lx_cmd_check(tb.workfd, tmp)

# check if there are patches to apply
tb.config.tc_lab_apply_patches_dir = tb.config.tc_lab_git_clone_apply_patches_dir
tb.eof_call_tc("tc_lab_apply_patches.py")

tb.config.tc_workfd_apply_local_patches_dir = tb.config.tc_lab_git_clone_apply_patches_git_am_dir
# check if there are local "git am" patches to apply
tb.eof_call_tc("tc_workfd_apply_local_patches.py")

tb.event.create_event('main', 'tc_workfd_git_clone_source.py', 'SET_DOC_FILENAME_NOIRQ_END', 'clone_' + repo_name)
tb.end_tc(True)
