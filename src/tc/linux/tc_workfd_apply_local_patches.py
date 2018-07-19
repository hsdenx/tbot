# SPDX-License-Identifier: GPL-2.0
#
# Description:
# apply patches from directory tb.config.tc_workfd_apply_local_patches_dir
# with 'git am -3' to the source in current directory.
#
# if tb.config.tc_workfd_apply_local_patches_dir == 'none'
# do nothing.
#
# if tb.config.tc_workfd_apply_local_patches_checkpatch_cmd != 'none'
# check the patches with the checkpatch cmd tb.config.tc_workfd_apply_local_patches_checkpatch_cmd
# before applying.
#
# used variables
#
# - tb.config.tc_workfd_apply_local_patches_dir
#| path to patches which testcase should apply with "git am -3"
#| default: 'none'
#
# - tb.config.tc_workfd_apply_local_patches_checkpatch_cmd
#| if != 'none' contains command for checking patch
#| for styling errors (normaly with checkpatch)
#| default: 'none'
#
# - tb.config.tc_workfd_apply_local_patches_checkpatch_cmd_strict
#| if 'yes' return testcase with failure if checkpatch finds
#| errors.
#| default: 'no'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_apply_local_patches_dir', 'none')
tb.define_variable('tc_workfd_apply_local_patches_checkpatch_cmd', 'none')
tb.define_variable('tc_workfd_apply_local_patches_checkpatch_cmd_strict', 'no')
logging.info("args: workfd: %s", tb.workfd)

if tb.config.tc_workfd_apply_local_patches_dir == 'none':
   tb.end_tc(True)

tb.set_term_length(tb.workfd)

def apply_one_patch(tb, filename):
    if tb.config.tc_workfd_apply_local_patches_checkpatch_cmd != 'none':
        tmp = tb.config.tc_workfd_apply_local_patches_checkpatch_cmd + ' ' + filename
        tb.eof_write_cmd(tb.workfd, tmp)
        ret = tb.call_tc("tc_workfd_check_cmd_success.py")
        if ret != True:
            logging.warn("checkpatch error")
            tmp = 'ls ' + filename
            tb.write_lx_cmd_check(tb.workfd, tmp)
            if tb.config.tc_workfd_apply_local_patches_checkpatch_cmd_strict == "yes":
                tb.end_tc(False)

    tmp = 'git am -3 ' + filename
    tb.write_lx_cmd_check(tb.workfd, tmp)

# print some infos
tb.eof_write_cmd(tb.workfd, 'pwd')
tb.write_lx_cmd_check(tb.workfd, 'git describe --all')

tb.config.tc_workfd_get_list_of_files_dir = tb.config.tc_workfd_apply_local_patches_dir
tb.config.tc_workfd_get_list_of_files_mask = '*.patch'
tb.eof_call_tc("tc_workfd_get_list_of_files_in_dir.py")

for filename in tb.list_of_files:
    apply_one_patch(tb, filename)

tb.end_tc(True)
