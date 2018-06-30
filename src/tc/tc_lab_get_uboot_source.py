# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# get U-Boot source
# and go into the source tree
#
# used variables
#
# - tb.config.tc_lab_get_uboot_source_git_repo
#|  repo to clone
#|  default: '/home/git/u-boot.git'
#
# - tb.config.tc_lab_get_uboot_source_git_branch
#|  branch which get checked out
#|  default: master
#
# - tb.config.tc_get_ub_source_reference
#|  reference which get used when cloning
#|  if 'none' no "--reference=..." option is
#|  used for "git clone"
#|  default: 'none'
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_get_ub_source_reference
except:
    tb.config.tc_get_ub_source_reference = 'none'

try:
    tb.config.tc_lab_get_uboot_source_git_repo
except:
    tb.config.tc_lab_get_uboot_source_git_repo = '/home/git/u-boot.git'

try:
    tb.config.tc_lab_get_uboot_source_git_branch
except:
    tb.config.tc_lab_get_uboot_source_git_branch = 'master'

logging.info("arg: %s %s %s", tb.config.tc_lab_get_uboot_source_git_repo, tb.config.tc_lab_get_uboot_source_git_branch, tb.config.tc_get_ub_source_reference)

ret = tb.call_tc("tc_workfd_goto_uboot_code.py")
if ret == False:
    u_boot_name = "u-boot-" + tb.config.boardlabname
    tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")
    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'u-boot_clone')
    # clone u-boot.git
    if tb.config.tc_get_ub_source_reference != 'none':
        opt = '--reference=' + tb.config.tc_get_ub_source_reference + ' '
    else:
        opt = ''
    tmp = "git clone " + opt + ' ' + tb.config.tc_lab_get_uboot_source_git_repo + " " + u_boot_name
    tb.write_lx_cmd_check(tb.workfd, tmp)

    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'cd2u-boot')
    tmp = "cd " + u_boot_name
    tb.write_lx_cmd_check(tb.workfd, tmp)
    # check out a specific branch
    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'u-boot_checkout')
    tmp = "git checkout " + tb.config.tc_lab_get_uboot_source_git_branch
    tb.write_lx_cmd_check(tb.workfd, tmp)
    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'u-boot_describe')
    # print some info
    tmp = "git describe --tags"
    tb.write_lx_cmd_check(tb.workfd, tmp)

    # check if there are local patches to apply with git am
    tb.eof_call_tc("tc_workfd_apply_local_patches.py")

    # check if there are patches to apply
    tb.eof_call_tc("tc_workfd_apply_patches.py")

tb.end_tc(True)
