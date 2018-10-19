# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# get yocto code with repo tool and configure sources
#
# - check if repo command exists
#   if not try to set path to it, if tb.config.tc_workfd_repo_path
#   is set, else failure
#
# - goto repo code with testcase tc_workfd_goto_repo_code.py
#   if dir $TBOT_BASEDIR_REPO does not exist create it
#   - call "repo init" with variables
#     tb.config.tc_workfd_get_with_repo_u
#     tb.config.tc_workfd_get_with_repo_m
#     tb.config.tc_workfd_get_with_repo_b
#
# - get newest sources with "repo sync"
#
# - setup environment with samples from meta-
#   tb.config.tc_workfd_get_with_repo_metaname
#
# - check if build directory "build_" + tb.config.tc_workfd_bitbake_machine
#   exists, if not create it and set DL_DIR and SSTATE_DIR in local.conf
#   with the values from tb.config.tc_workfd_get_yocto_source_conf_dl_dir
#   and tb.config.tc_workfd_get_yocto_source_conf_sstate_dir
#
#   and setup site.conf with specific settings
#
# used variables:
#
# - tb.config.tc_workfd_get_with_repo_metaname
#| name for meta layer, from which samples get used for
#| setting up bitbake with 'TEMPLATECONF=meta-' + tb.config.tc_workfd_get_with_repo_metaname
#| default: 'beld'
#
# - tb.config.tc_workfd_get_with_repo_sync
#| call 'repo sync' if yes
#| default: 'yes'
#
# - tb.config.tc_workfd_get_with_repo_u
#| '-u' paramter for repo command
#| default: ''
#
# - tb.config.tc_workfd_get_with_repo_m
#| '-m' paramter for repo command
#| default: ''
#
# - tb.config.tc_workfd_get_with_repo_b
#| '-b' paramter for repo command
#| default: ''
#
# - tb.config.tc_workfd_get_with_repo_target
#| target directory, where source is found after "repo sync"
#| '$TBOT_BASEDIR_REPO/' + tb.config.tc_workfd_get_with_repo_target
#| default: ''
#
# End:

from tbotlib import tbot

logging.info("args: machine: %s", tb.config.tc_workfd_bitbake_machine)

tb.define_variable('tc_workfd_get_with_repo_metaname', 'beld')
tb.define_variable('tc_workfd_get_with_repo_sync', 'yes')
tb.define_variable('tc_workfd_get_with_repo_u', '')
tb.define_variable('tc_workfd_get_with_repo_m', '')
tb.define_variable('tc_workfd_get_with_repo_b', '')
tb.define_variable('tc_workfd_get_with_repo_target', '')

# check if we have the repo cmd installed
# if not try to set PATH (if tb.config.tc_workfd_repo_path is set)
ret = tb.eof_call_tc("tc_workfd_check_repo_cmd.py")

ret = tb.call_tc("tc_workfd_goto_repo_code.py")
if ret == False:
    # get sources
    # step 1: create dir
    cmd = 'mkdir -p $TBOT_BASEDIR_REPO'
    tb.write_lx_cmd_check(tb.workfd, cmd, create_doc_event=True)
    tb.eof_call_tc("tc_workfd_goto_repo_code.py")

    # step 2: repo init
    cmd = 'repo init -u ' + tb.config.tc_workfd_get_with_repo_u + ' -m ' + tb.config.tc_workfd_get_with_repo_m + ' -b ' + tb.config.tc_workfd_get_with_repo_b
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME', 'repo_init')
    tb.write_lx_cmd_check(tb.workfd, cmd, triggerlist=['objects', 'deltas'])

# step 3: repo sync
if tb.config.tc_workfd_get_with_repo_sync == 'yes':
    tb.write_lx_cmd_check(tb.workfd, 'repo sync', triggerlist=['objects', 'deltas', 'done', 'project'], create_doc_event=True)

# step 4:configure project
# goto yocto code
tb.workfd.tc_workfd_goto_yocto_code_path = '$TBOT_BASEDIR_REPO/' + tb.config.tc_workfd_get_with_repo_target
tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME', 'repo_goto_yocto_code')
tb.eof_call_tc("tc_workfd_goto_yocto_code.py")

# check if builddir exists, if not configure
tb.config.tc_workfd_check_if_dir_exists_name = tb.config.yocto_builddir
ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
if ret == False:
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME', 'repo_templateconf')
    cmd = 'TEMPLATECONF=meta-' + tb.config.tc_workfd_get_with_repo_metaname + '/conf/samples/ source oe-init-build-env ' + 'build_' + tb.config.tc_workfd_bitbake_machine
    tb.write_lx_cmd_check(tb.workfd, cmd)
    tb.eof_call_tc("tc_workfd_check_if_dir_exist.py")

    # step 5: adapt conf file
    if tb.config.tc_workfd_get_yocto_source_conf_dl_dir != 'none':
        tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME', 'repo_set_dl_dir')
        cmd = "sed -i '/DL_DIR ?=/cDL_DIR=\"" + tb.config.tc_workfd_get_yocto_source_conf_dl_dir + "\"' conf/local.conf"
        tb.write_lx_cmd_check(tb.workfd, cmd)

    if tb.config.tc_workfd_get_yocto_source_conf_sstate_dir != 'none':
        tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME', 'repo_set_sstate')
        cmd = "sed -i '/SSTATE_DIR ?=/cSSTATE_DIR=\"" + tb.config.tc_workfd_get_yocto_source_conf_sstate_dir  + "\"' conf/local.conf"
        tb.write_lx_cmd_check(tb.workfd, cmd)

    # step 6: patch/create site.conf
    tb.eof_call_tc("tc_workfd_yocto_patch_site.py")
else:
    # print current used site.conf
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ', 'repo_dump_site.conf')
    tb.write_lx_cmd_check(tb.workfd, "cat " + tb.config.yocto_builddir + "conf/site.conf")
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ_END', 'repo_dump_site.conf')

tb.end_tc(True)
