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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_get_yocto_source.py
# get yocto source tb.config.tc_workfd_get_yocto_patches_git_repo with "git clone"
# check out branch:
# tb.config.tc_workfd_get_yocto_patches_git_branch
# check out commit ID:
# tb.config.tc_workfd_get_yocto_git_commit_id
# apply patches with "git am" from directory:
# tb.config.tc_workfd_get_yocto_clone_apply_patches_git_am_dir
# additionally define a reference for cloning:
# tb.config.tc_workfd_get_yocto_source_git_reference
# if a user/password for cloning is needed, define the user:
# tb.config.tc_workfd_get_yocto_source_git_repo_user
# and set the password in password.py
#
# get other layers defined in the list:
# tb.config.tc_workfd_get_yocto_source_layers
#
# at the end overwrite yocto configuration found in
# tb.config.tc_workfd_get_yocto_source_conf_dir
#
# clones into directory tb.config.yocto_name
# created with tc_workfd_goto_yocto_code.py
#
# End:

from tbotlib import tbot

logging.info("args: workdfd: %s %s %s %s", tb.workfd.name, tb.config.tc_workfd_get_yocto_patches_git_repo,
             tb.config.tc_workfd_get_yocto_patches_git_branch, tb.config.tc_lab_git_clone_apply_patches_dir)
logging.info("args: %s %s ", tb.config.tc_lab_git_clone_source_git_reference,
             tb.config.tc_lab_git_clone_source_git_repo_user)
logging.info("args: %s", tb.config.tc_workfd_get_yocto_source_conf_dir)
logging.info("args: %s", tb.config.tc_workfd_get_yocto_patches_git_repo_name)
logging.info("args: %s", tb.config.tc_workfd_get_yocto_source_layers)

clone_layers = True
ret = tb.call_tc("tc_workfd_goto_yocto_code.py")
if ret == False:
    # get the patches for the yocto layers
    if tb.config.tc_workfd_get_yocto_patches_git_repo != 'none':
        tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")
        tb.config.tc_lab_git_clone_source_git_repo = tb.config.tc_workfd_get_yocto_patches_git_repo
        tb.config.tc_lab_git_clone_source_git_branch = tb.config.tc_workfd_get_yocto_patches_git_branch
        tb.config.tc_lab_git_clone_source_git_commit_id = 'none'
        tb.config.tc_lab_git_clone_apply_patches_dir = 'none'
        tb.config.tc_lab_git_clone_apply_patches_git_am_dir = 'none'
        tb.config.tc_lab_git_clone_source_git_reference = 'none'
        tb.config.tc_lab_git_clone_source_git_repo_user = ''
        tb.config.tc_lab_git_clone_source_git_repo_name = tb.config.tc_workfd_get_yocto_patches_git_repo_name
        tb.eof_call_tc("tc_workfd_git_clone_source.py")

    tb.config.tc_lab_git_clone_source_git_repo = tb.config.tc_workfd_get_yocto_source_git_repo
    tb.config.tc_lab_git_clone_source_git_branch = tb.config.tc_workfd_get_yocto_source_git_branch
    tb.config.tc_lab_git_clone_source_git_commit_id = tb.config.tc_workfd_get_yocto_git_commit_id
    tb.config.tc_lab_git_clone_apply_patches_dir = tb.config.tc_workfd_get_yocto_apply_patches_dir
    tb.config.tc_lab_git_clone_apply_patches_git_am_dir = tb.config.tc_workfd_get_yocto_clone_apply_patches_git_am_dir
    tb.config.tc_lab_git_clone_source_git_reference = tb.config.tc_workfd_get_yocto_source_git_reference
    tb.config.tc_lab_git_clone_source_git_repo_user = tb.config.tc_workfd_get_yocto_source_git_repo_user

    tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")
    tb.config.tc_lab_git_clone_source_git_repo_name = tb.config.yocto_name
    tb.eof_call_tc("tc_workfd_git_clone_source.py")
else:
    clone_layers = False

if clone_layers:
    # now get more meta layers ...
    for l in tb.config.tc_workfd_get_yocto_source_layers:
        tb.config.tc_lab_git_clone_source_git_repo = l[0]
        tb.config.tc_lab_git_clone_source_git_branch = l[1]
        tb.config.tc_lab_git_clone_source_git_commit_id = l[2]
        tb.config.tc_lab_git_clone_apply_patches_dir = l[3]
        tb.config.tc_lab_git_clone_apply_patches_git_am_dir = l[4]
        tb.config.tc_lab_git_clone_source_git_reference = l[5]
        tb.config.tc_lab_git_clone_source_git_repo_user = l[6]
        tb.config.tc_lab_git_clone_source_git_repo_name = l[7]
        tb.eof_call_tc("tc_workfd_git_clone_source.py")
        tb.write_lx_cmd_check(tb.workfd, 'cd ..')


# source oe-init-build-env build
tb.write_lx_cmd_check(tb.workfd, 'source oe-init-build-env build')

# now copy config
src_dir = tb.config.tc_workfd_get_yocto_source_conf_dir
trg_dir = tb.config.yocto_fulldir_name + '/build/conf/'
files = ['bblayers.conf', 'local.conf']
for f in files:
    tmp = 'cp ' + src_dir + f + ' ' + trg_dir + f
    tb.write_lx_cmd_check(tb.workfd, tmp)

tb.eof_call_tc("tc_workfd_goto_yocto_code.py")

# replace TBOT_YOCTO_PATH in bblayers.conf with tb.config.yocto_fulldir_name
tmp = "sed -i -- 's+TBOT_YOCTO_PATH+" + tb.config.yocto_fulldir_name + "+g' build/conf/bblayers.conf"
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
