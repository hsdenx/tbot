# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get yocto source tb.config.tc_workfd_get_yocto_patches_git_repo with "git clone"
#
# check out branch:
# tb.config.tc_workfd_get_yocto_patches_git_branch
#
# check out commit ID:
# tb.config.tc_workfd_get_yocto_git_commit_id
#
# if tb.config.tc_workfd_get_yocto_patches_git_repo != 'none'
#   apply patches with "git am" from directory:
#   tb.config.tc_workfd_get_yocto_clone_apply_patches_git_am_dir
#
# additionally define a reference for cloning:
# tb.config.tc_workfd_get_yocto_source_git_reference
# if a user/password for cloning is needed, define the user:
# tb.config.tc_workfd_get_yocto_source_git_repo_user
# and set the password in password.py
#
# get other layers defined in the list:
# tb.config.tc_workfd_get_yocto_source_layers
#
# if tb.config.tc_workfd_get_yocto_source_autoconf == 'none'
#     overwrite yocto configuration found in
#     tb.config.tc_workfd_get_yocto_source_conf_dir
# else
#     try to autogenerate bblayers.conf and site.conf
#
# clones into directory tb.config.yocto_name
# created with tc_workfd_goto_yocto_code.py
#
# used variables
#
# - tb.config.tc_workfd_get_yocto_source_autoconf
#| if  'none' copy config files from tb.config.tc_workfd_get_yocto_source_conf_dir
#| default: 'none'
#
# - tb.config.tc_workfd_get_yocto_source_conf_dir
#| path, in which yocto configurations file are found
#| default: 'not defined'
#
# - tb.config.tc_workfd_get_yocto_patches_git_repo
#| path to git repo with yocto patches
#| default: ''
#
# - tb.config.tc_workfd_get_yocto_patches_git_branch
#| branch which get checked out in tb.config.tc_workfd_get_yocto_patches_git_repo
#| default: ''
#
# - tb.config.tc_workfd_get_yocto_patches_git_repo_name
#| name the repo with the patches gets
#| default: ''
#
# - tb.config.tc_workfd_get_yocto_source_git_repo
#| git url, to yocto code
#| default: 'git://git.yoctoproject.org/poky.git'
#
# - tb.config.tc_workfd_get_yocto_source_git_branch
#| branch which gets checked out
#| default: 'pyro'
#
# - tb.config.tc_workfd_get_yocto_git_commit_id
#| if != 'none' commit ID to which tree gets resettet
#| default: 'none'
#
# - tb.config.tc_workfd_get_yocto_source_layers
#| list of meta layers, which get checked out
#| one element contains the following list element:
#| ['git repo',
#|  'git branch',
#|  'git commit id',
#|  'apply_patches_dir'
#|  'apply_patches_git_am_dir',
#|  'source_git_reference',
#|  'source_git_repo_user',
#|  'source_git_repo_name'
#| ]
#|
#| default: "
#| [
#| ['git://git.openembedded.org/meta-openembedded', 'morty', '659d9d3f52bad33d7aa1c63e25681d193416d76e', 'none', 'none', 'none', '', 'meta-openembedded'],
#| ['https://github.com/sbabic/meta-swupdate.git', 'master', 'b3abfa78d04b88b88bcef6f5be9f2adff1293544', 'none', 'none', 'none', '', 'meta-swupdate'],
#| ]
#| "
#
# - tb.config.tc_workfd_get_yocto_source_conf_dl_dir
#| path to yocto download directory.
#| If != 'none' testcase checks if exists, if not
#| create it. Also patch local.conf
#| default: 'none'
#
# - tb.config.tc_workfd_get_yocto_source_conf_sstate_dir
#| path to sstate directory.
#| If != 'none' testcase checks if exists, if not
#| create it. Also patch local.conf
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_get_yocto_patches_git_repo', '')
tb.define_variable('tc_workfd_get_yocto_patches_git_branch', '')
tb.define_variable('tc_workfd_get_yocto_patches_git_repo_name', '')
tb.define_variable('tc_workfd_get_yocto_source_git_repo', 'git://git.yoctoproject.org/poky.git')
tb.define_variable('tc_workfd_get_yocto_source_git_branch', 'pyro')
tb.define_variable('tc_workfd_get_yocto_git_commit_id', 'none')
tb.define_variable('tc_workfd_get_yocto_source_git_reference', '')
tb.define_variable('tc_workfd_get_yocto_source_git_repo_user', '')
tb.define_variable('tc_workfd_get_yocto_source_layers', " \
[ \
['git://git.openembedded.org/meta-openembedded', 'morty', '659d9d3f52bad33d7aa1c63e25681d193416d76e', 'none', 'none', 'none', '', 'meta-openembedded'], \
['https://github.com/sbabic/meta-swupdate.git', 'master', 'b3abfa78d04b88b88bcef6f5be9f2adff1293544', 'none', 'none', 'none', '', 'meta-swupdate'], \
] \
")
tb.define_variable('tc_workfd_get_yocto_source_autoconf', 'none')
tb.define_variable('tc_workfd_get_yocto_source_conf_dir', 'not defined')
tb.define_variable('tc_workfd_get_yocto_source_conf_dl_dir', 'none')
tb.define_variable('tc_workfd_get_yocto_source_conf_sstate_dir', 'none')

ret = tb.call_tc("tc_workfd_goto_yocto_code.py")
if ret == True:
    # sync all trees
    # first poky
    tb.event.create_event('main', 'tc_workfd_get_yocto_source.py', 'SET_DOC_FILENAME_NOIRQ', 'sync_poky')
    tb.eof_call_tc("tc_workfd_goto_yocto_code.py")
    tb.write_lx_cmd_check(tb.workfd, 'git fetch')
    tb.write_lx_cmd_check(tb.workfd, 'git pull')
    tb.event.create_event('main', 'tc_workfd_get_yocto_source.py', 'SET_DOC_FILENAME_NOIRQ_END', 'sync_poky')

    # now all meta layers
    for l in tb.config.tc_workfd_get_yocto_source_layers:
        name = l[7]
        tb.event.create_event('main', 'tc_workfd_get_yocto_source.py', 'SET_DOC_FILENAME_NOIRQ', 'sync_' + name)
        tb.write_lx_cmd_check(tb.workfd, 'cd $TBOT_BASEDIR_YOCTO/' + name)
        tb.write_lx_cmd_check(tb.workfd, 'git fetch')
        tb.write_lx_cmd_check(tb.workfd, 'git pull')
        tb.event.create_event('main', 'tc_workfd_get_yocto_source.py', 'SET_DOC_FILENAME_NOIRQ_END', 'sync_' + name)

    # print site.conf
    p = '$TBOT_BASEDIR_YOCTO/build/conf/'
    fn = p + 'site.conf'
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ', 'repo_dump_site.conf')
    tb.write_lx_cmd_check(tb.workfd, "cat " + fn)
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ_END', 'repo_dump_site.conf')
    # print local.conf
    fn = p + 'local.conf'
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ', 'repo_dump_local.conf')
    tb.write_lx_cmd_check(tb.workfd, "cat " + fn)
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ_END', 'repo_dump_local.conf')
    # print bblayers.conf
    fn = p + 'bblayers.conf'
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ', 'repo_dump_bblayers.conf')
    tb.write_lx_cmd_check(tb.workfd, "cat " + fn)
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ_END', 'repo_dump_bblayers.conf')

    tb.end_tc(True)

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
    tb.config.tc_lab_git_clone_apply_patches_dir = tb.config.tc_workfd_get_yocto_apply_patches_dir
    tb.config.tc_lab_git_clone_apply_patches_git_am_dir = tb.config.tc_workfd_get_yocto_clone_apply_patches_git_am_dir
else:
    tb.config.tc_lab_git_clone_apply_patches_dir = 'none'
    tb.config.tc_lab_git_clone_apply_patches_git_am_dir = 'none'

tb.config.tc_lab_git_clone_source_git_repo = tb.config.tc_workfd_get_yocto_source_git_repo
tb.config.tc_lab_git_clone_source_git_branch = tb.config.tc_workfd_get_yocto_source_git_branch
tb.config.tc_lab_git_clone_source_git_commit_id = tb.config.tc_workfd_get_yocto_git_commit_id
tb.config.tc_lab_git_clone_source_git_reference = tb.config.tc_workfd_get_yocto_source_git_reference
tb.config.tc_lab_git_clone_source_git_repo_user = tb.config.tc_workfd_get_yocto_source_git_repo_user

tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")
tb.config.tc_lab_git_clone_source_git_repo_name = tb.config.yocto_name
tb.event.create_event('main', 'tc_workfd_get_yocto_source.py', 'SET_DOC_FILENAME_NOIRQ', 'clone_poky')
tb.eof_call_tc("tc_workfd_git_clone_source.py")
tb.event.create_event('main', 'tc_workfd_get_yocto_source.py', 'SET_DOC_FILENAME_NOIRQ_END', 'clone_poky')

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
    tb.write_lx_cmd_check(tb.workfd, 'cd $TBOT_BASEDIR_YOCTO')

tb.write_lx_cmd_check(tb.workfd, 'source oe-init-build-env build')

if tb.config.tc_workfd_get_yocto_source_autoconf == 'none':
    # now copy config
    src_dir = tb.config.tc_workfd_get_yocto_source_conf_dir
    trg_dir = tb.config.yocto_fulldir_name + '/build/conf/'
    files = ['bblayers.conf', 'local.conf']
    for f in files:
        tmp = 'cp ' + src_dir + f + ' ' + trg_dir + f
        tb.write_lx_cmd_check(tb.workfd, tmp)

    # replace TBOT_YOCTO_PATH in bblayers.conf with tb.config.yocto_fulldir_name
    tmp = "sed -i -- 's+TBOT_YOCTO_PATH+'\"$TBOT_BASEDIR_YOCTO\"'+g' build/conf/bblayers.conf"
    tb.write_lx_cmd_check(tb.workfd, tmp)

    # setup yocto DL_DIR
    if tb.config.tc_workfd_get_yocto_source_conf_dl_dir != 'none':
        tb.config.tc_workfd_linux_mkdir_dir = tb.config.tc_workfd_get_yocto_source_conf_dl_dir
        tb.eof_call_tc("tc_workfd_linux_mkdir.py")

        tmp = "sed -i -- 's+TBOT_YOCTO_DLDIR+'" + tb.config.tc_workfd_get_yocto_source_conf_dl_dir + "'+g' build/conf/local.conf"
        tb.write_lx_cmd_check(tb.workfd, tmp)

    # setup yocto SSTATE_DIR
    if tb.config.tc_workfd_get_yocto_source_conf_sstate_dir != 'none':
        tb.config.tc_workfd_linux_mkdir_dir = tb.config.tc_workfd_get_yocto_source_conf_sstate_dir
        tb.eof_call_tc("tc_workfd_linux_mkdir.py")

        tmp = "sed -i -- 's+TBOT_YOCTO_SSTATEDIR+'" + tb.config.tc_workfd_get_yocto_source_conf_sstate_dir + "'+g' build/conf/local.conf"
        tb.write_lx_cmd_check(tb.workfd, tmp)
else:
    tb.eof_call_tc("tc_workfd_goto_yocto_code.py")
    tb.write_lx_cmd_check(tb.workfd, 'rm build/conf/bblayers.conf')
    # autogenerate bblayers.conf
    tb.eof_call_tc("tc_workfd_yocto_generate_bblayers.py")
    # and site.conf
    tb.eof_call_tc("tc_workfd_yocto_patch_site.py")

tb.end_tc(True)
