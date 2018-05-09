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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_with_repo.py
#
# get yocto code with repo tool and configure sources
#
# - check if repo command exists
#   if not try to set path to it, if tb.config.tc_workfd_repo_path
#   is set, else failure
#
# - goto repo code
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
#   default: 'beld'
#
# - check if build directory "build_" + tb.config.tc_workfd_bitbake_machine
#   exists, if not create it and set DL_DIR and SSTATE_DIR in local.conf
#   with the values from tb.config.tc_workfd_get_yocto_source_conf_dl_dir
#   and tb.config.tc_workfd_get_yocto_source_conf_sstate_dir
#
#   and setup site.conf with specific settings
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_get_with_repo_metaname
except:
    tb.config.tc_workfd_get_with_repo_metaname = 'beld'

try:
    tb.config.tc_workfd_bitbake_machine
except:
    tb.config.tc_workfd_bitbake_machine = tb.config.boardname

try:
    tb.config.builddir
except:
    tb.config.builddir = "$TBOT_BASEDIR_YOCTO/build_" + tb.config.tc_workfd_bitbake_machine + "/"

try:
    tb.config.tc_workfd_get_with_repo_sync
except:
    tb.config.tc_workfd_get_with_repo_sync = 'yes'

logging.info("args: workdfd: %s", tb.workfd.name)
logging.info("args: repo u: %s", tb.config.tc_workfd_get_with_repo_u)
logging.info("args: repo m: %s", tb.config.tc_workfd_get_with_repo_m)
logging.info("args: repo b: %s", tb.config.tc_workfd_get_with_repo_b)
logging.info("args: repo target: %s", tb.config.tc_workfd_get_with_repo_target)
logging.info("args: meta name: %s", tb.config.tc_workfd_get_with_repo_metaname)
logging.info("args: builddir: %s", tb.config.builddir)
logging.info("args: machine: %s", tb.config.tc_workfd_bitbake_machine)
logging.info("args: : %s", tb.config.tc_workfd_get_with_repo_sync)

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
tb.config.tc_workfd_check_if_dir_exists_name = tb.config.builddir
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
    tb.write_lx_cmd_check(tb.workfd, "cat " + tb.config.builddir + "conf/site.conf")
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ_END', 'repo_dump_site.conf')

tb.end_tc(True)
