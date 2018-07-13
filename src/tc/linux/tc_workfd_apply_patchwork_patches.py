# SPDX-License-Identifier: GPL-2.0
#
# Description:
# apply patchworkpatches from list:
# tb.config.tc_workfd_apply_patchwork_patches_list:
# to source in current directory.
# creates event:
# - PW_NR: which patchwork number used
# - PW_CLEAN: is it checkpatch clean
# - PW_AA: already applied
# - PW_APPLY: apply it clean to source
#
# used variables
#
# - tb.config.tc_workfd_apply_patchwork_patches_list
#| list of patchwork numbers, which should be used with
#| testcasetc_workfd_apply_patchwork_patches.py
#| default: '[]'
#
# - tb.config.tc_workfd_apply_patchwork_patches_checkpatch_cmd
#| command with which the patches get checked
#| default: 'none'
#
# - tb.config.tc_workfd_apply_patchwork_patches_eof
#| if 'yes' end testcase with failure, if applying fails.
#| default: 'yes'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_apply_patchwork_patches_list', '[]')
tb.define_variable('tc_workfd_apply_patchwork_patches_checkpatch_cmd', 'none')
tb.define_variable('tc_workfd_apply_patchwork_patches_eof', 'yes')
logging.info("args: workfd: %s", tb.workfd)

def apply_one_patch(tb, nr):
    tb.config.tc_workfd_rm_file_name = 'mbox'
    ret = tb.call_tc("tc_workfd_rm_file.py")
    tmp = 'wget http://patchwork.ozlabs.org/patch/' + nr + '/mbox'
    tb.write_lx_cmd_check(tb.workfd, tmp)
    tb.event.create_event('main', 'func', 'PW_NR', nr)
    if tb.config.tc_workfd_apply_patchwork_patches_checkpatch_cmd != 'none':
        tmp = tb.config.tc_workfd_apply_patchwork_patches_checkpatch_cmd + ' mbox'
        tb.eof_write_cmd(tb.workfd, tmp)
        ret = tb.call_tc("tc_workfd_check_cmd_success.py")
        if ret != True:
            logging.warn("checkpatch error")
            tmp = 'cat mbox | grep Subject'
            tb.write_lx_cmd_check(tb.workfd, tmp)
            tb.event.create_event('main', 'func', 'PW_CLEAN', 'False')
        else:
            tb.event.create_event('main', 'func', 'PW_CLEAN', 'True')

    tmp = 'git am -3 mbox'
    loop = True
    se = ['Patch already applied']
    tb.eof_write(tb.workfd, tmp)
    while loop == True:
        tmp = tb.tbot_rup_and_check_strings(tb.workfd, se)
        if tmp == '0':
            tb.event.create_event('main', 'func', 'PW_AA', 'True')
        if tmp == 'prompt':
            ret = tb.call_tc("tc_workfd_check_cmd_success.py")
            tb.event.create_event('main', 'func', 'PW_APPLY', ret)
            if tb.config.tc_workfd_apply_patchwork_patches_eof == 'yes':
                if ret == False:
                    tb.end_tc(False)
            loop = False
            if ret == False:
                # restore source
                tmp = 'git am --abort'
                tb.write_lx_cmd_check(tb.workfd, tmp)

# print some infos
tb.eof_write_cmd(tb.workfd, 'pwd')
tb.write_lx_cmd_check(tb.workfd, 'git describe')
for nr in tb.config.tc_workfd_apply_patchwork_patches_list:
    apply_one_patch(tb, nr)

tb.end_tc(True)
