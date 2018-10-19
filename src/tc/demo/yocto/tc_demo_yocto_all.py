# SPDX-License-Identifier: GPL-2.0
#
# Description:
# demo for a complete yocto workflow automatization
#
# helpful aliases:
#
# X=boardname
#
# alias tb_X="tbot.py -s lab_tbot2go -c X -p password-X.py -v"
# alias tb_boardname_y_all="tb_X -t tc_demo_yocto_all.py -l log/tbot-X-yocto-all.log"
# alias tb_boardname_y_all_nobuild_nocopy="tb_X_y_all -a '{\"tc_demo_yocto_all_copy_images\":\"none\", \"tc_demo_yocto_all_do_build\":\"no\"}'"
#
# used variables:
#
# - tb.config.tc_demo_yocto_all_get_source
#| contains a testcase name. This testcase does all the
#| setup work for baking yocto. Also it must set all
#| variables needed for testcase tc_workfd_goto_yocto_code.py
#| example: tc_workfd_get_with_repo.py
#| default: 'tc_workfd_get_with_repo.py'
#
# - tb.config.tc_demo_yocto_all_copy_images
#| testcase, which copies after successfull build
#| images to the result dir tb.config.tc_demo_yocto_all_result_dir
#| default: 'tc_yocto_get_result_files.py'
#
# - tb.config.tc_demo_yocto_all_install_images
#| testcase, which installs after successfull build
#| images on the board.
#| default: ''
#
# - tb.config.tc_demo_yocto_all_check_after_build
#| testcase, which do checks after successfull build.
#| default: 'none'
#
# - tb.config.tc_demo_yocto_all_boot
#| testcase, which boots the new images
#| default: 'none'
#
# - tb.config.tc_demo_yocto_all_do_build
#| if 'yes' do bitbake
#| default: 'yes'
#
# - tb.config.tc_demo_yocto_all_do_basic_check
#| if 'yes' do basic checks
#| default: 'yes'
#
# - tb.config.tc_demo_yocto_all_do_rootfsversion
#| if 'yes' get rootfsversion from yocto build (/etv/version)
#| and check after linux boot, if rootfs has the same
#| version number
#| default: 'yes'
#

# End:

from tbotlib import tbot

tb.define_variable('tc_demo_yocto_all_get_source', 'tc_workfd_get_with_repo.py')
tb.define_variable('tc_demo_yocto_all_copy_images', 'tc_yocto_get_result_files.py')
tb.define_variable('tc_demo_yocto_all_install_images', 'none')
tb.define_variable('tc_demo_yocto_all_check_after_build', 'none')
tb.define_variable('tc_demo_yocto_all_boot', 'none')
tb.define_variable('tc_demo_yocto_all_do_build', 'yes')
tb.define_variable('tc_demo_yocto_all_do_basic_check', 'yes')
tb.define_variable('tc_demo_yocto_all_do_rootfsversion', 'yes')

tb.eof_call_tc("tc_connect_to_compilepc.py")

# get source code
tb.eof_call_tc(tb.config.tc_demo_yocto_all_get_source)

# source oe-init-build-env build
tb.eof_call_tc("tc_workfd_goto_yocto_code.py")
if tb.config.tc_workfd_bitbake_machine:
    bs = 'build_' + tb.config.tc_workfd_bitbake_machine
else:
    bs = 'build'

if tb.config.tc_demo_yocto_all_do_build == 'yes':
    tb.write_lx_cmd_check(tb.workfd, 'source oe-init-build-env ' + bs)

    # bitbake
    tb.eof_call_tc("tc_workfd_bitbake.py")

# do checks after build
# check files if exist
for l in tb.config.yocto_check_result_files:
    tb.config.tc_workfd_check_if_file_exists_name = tb.config. yocto_deploy_dir + l
    tb.eof_call_tc("tc_workfd_check_if_file_exist.py")

# do check after build
if tb.config.tc_demo_yocto_all_check_after_build != 'none':
    tb.eof_call_tc(tb.config.tc_demo_yocto_all_check_after_build)

# get rootfs version
if tb.config.tc_demo_yocto_all_do_rootfsversion == 'yes':
    for f in tb.config.yocto_check_result_files:
        if ('tar.gz' in f) or ('tar.bz2' in f):
            tb.config.tc_yocto_get_rootfs_from_tarball = tb.config.yocto_deploy_dir + f
    tb.eof_call_tc("tc_yocto_get_rootfs_from_tarball.py")

# copy images from tb.config.yocto_check_result_files to result dir
# tb.config.tc_demo_yocto_all_result_dir on lab PC
if tb.config.tc_demo_yocto_all_copy_images != 'none':
    tb.eof_call_tc(tb.config.tc_demo_yocto_all_copy_images)

# install images
if tb.config.tc_demo_yocto_all_install_images != 'none':
    tb.eof_call_tc(tb.config.tc_demo_yocto_all_install_images)

# boot new image
if tb.config.tc_demo_yocto_all_boot != 'none':
    tb.eof_call_tc(tb.config.tc_demo_yocto_all_boot)

# make yocto checks
# first check, if we have the correct rootfs version
if tb.config.tc_demo_yocto_all_do_rootfsversion == 'yes':
    tb.eof_call_tc("tc_workfd_yocto_check_rootfs_version.py")

if tb.config.tc_demo_yocto_all_do_basic_check == 'yes':
    tb.eof_call_tc("tc_workfd_yocto_basic_check.py")

tb.end_tc(True)
