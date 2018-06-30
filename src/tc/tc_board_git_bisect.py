# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get a source code with tc tb.config.board_git_bisect_get_source_tc
# and start a "git bisect" session
#
# current commit is bad
#
# good commit id is defined through tb.config.board_git_bisect_good_commit
#
# tc for testing good or bad is tb.config.board_git_bisect_call_tc
#
# if you have some local patches, which needs to be applied
# each git bisect step, set tb.config.board_git_bisect_patches
#
# if you need to restore your board after a failure, set the
# variable tb.config.board_git_bisect_restore to the tc name
# which restores the board after each step
#
# used variables
#
# - tb.config.board_git_bisect_get_source_tc
#|  testcase which gets called for changing into the git source
#|  code.
#|  default: 'tc_lab_get_uboot_source.py'
#
# - tb.config.board_git_bisect_call_tc
#|  testcase, which gets called for finding out, if current
#|  checked out state of the source is good or bad
#|  default: 'tc_board_tqm5200s_ub_comp_install.py'
#
# - tb.config.board_git_bisect_good_commit
#|  last know good commit id
#|  default: 'f9860cf'
#
# - tb.config.board_git_bisect_patches
#|  patches, which get applied in each step fo git bisect
#|  default: 'none'
#
# - tb.config.board_git_bisect_restore
#|  name of testcase, which gets called after each step, for
#|  restoring your board. Used for example, if you bisect
#|  u-boot and you break with bad source code your board.
#|  default: 'none'
#
# End:
from tbotlib import tbot

tb.define_variable('board_git_bisect_get_source_tc', 'tc_lab_get_uboot_source.py')
tb.define_variable('board_git_bisect_good_commit', 'f9860cf')
tb.define_variable('board_git_bisect_patches', 'none')
tb.define_variable('board_git_bisect_restore', 'none')

#call get u-boot source
tb.statusprint("get source tree")
tb.eof_call_tc(tb.config.board_git_bisect_get_source_tc)

c = tb.c_ctrl
#git bisect start
tb.eof_write_cmd(c, 'git bisect start')

#current version is bad
tb.eof_write_cmd(c, 'git bisect bad')

#git bisect good commit
tmp = 'git bisect good ' + tb.config.board_git_bisect_good_commit
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'Bisecting')
if ret == 'prompt':
    tb.end_tc(False)
tb.tbot_expect_prompt(c)

#do the steps
i = 0
inwhile = True
error = False
while inwhile:
    i += 1
    tb.statusprint("cycle %s" % (i))
    logging.info("cycle %s", i)

    if tb.config.board_git_bisect_patches != 'none':
        tmp = tb.config.tc_lab_apply_patches_dir
        tb.config.tc_lab_apply_patches_dir = tb.config.board_git_bisect_patches
        tb.eof_call_tc("tc_lab_apply_patches.py")
        tb.config.tc_lab_apply_patches_dir = tmp

    ret = tb.call_tc(tb.config.board_git_bisect_call_tc)
    if ret == True:
        tmp = 'git bisect good'
    else:
        tmp = 'git bisect bad'
    tb.eof_write(c, tmp)
    tmp2 = True
    se = ['the first bad commit', 'Aborting']
    while tmp2 == True:
        ret = tb.tbot_rup_and_check_strings(c, se)
        if ret == '0':
            inwhile = False
        if ret == '1':
            inwhile = False
            error = True
        if ret == 'prompt':
            tmp2 = False

    if tb.config.board_git_bisect_patches != 'none':
        tb.eof_write_cmd(c, 'git reset --hard HEAD')
        tb.eof_write_cmd(c, 'git clean -f')

    if tb.config.board_git_bisect_restore != 'none':
        tb.eof_call_tc(tb.config.board_git_bisect_restore)

if error:
    tb.end_tc(False)

# print some statistic
tb.eof_write_cmd(c, 'git bisect visualize')
tb.eof_write_cmd(c, 'git bisect log')

# reset source tree
tb.eof_write_cmd(c, 'git bisect reset')

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
