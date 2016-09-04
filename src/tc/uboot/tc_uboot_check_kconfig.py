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
# python2.7 src/common/tbot.py -c config/tbot_uboot_kconfig_check.cfg -t tc_uboot_check_kconfig.py
# check for all boards, if a patch changes the u-boot binary
# If U-boot binary changed by the patch this testcase fails.
# use this testcase, if you for example move a config option
# into Kconfig. As we need reproducable builds, we need to
# patch U-Boot with tb.tc_uboot_check_kconfig_preparepatch
# - rm U-Boot code with tc_workfd_rm_uboot_code.py
# - get U-Boot code with tc_lab_get_uboot_source.py
# - create a list of boards (all defconfigs)
# - do for all boards:
#   - get architecture and set toolchain
#   - set SOURCE_DATE_EPOCH=0 to get reproducibl builds
#   - compile U-Boot and calculate md5sum
#     with tc_workfd_compile_uboot.py and tc_workfd_md5sum.py
#   - apply patch with tc_workfd_apply_patches.py
#   - compile U-Boot again (patched version)
#   - calculate md5sum
#   - check if they are the same
# End:

import os
from tbotlib import tbot

logging.info("args: %s", tb.tc_uboot_check_kconfig_preparepatch)

#set board state for which the tc is valid
tb.set_board_state("lab")

# delete old u-boot source tree
tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_rm_uboot_code.py")

result = True

tmp = tb.tc_lab_apply_patches_dir
tb.tc_lab_apply_patches_dir = 'none'

# call get u-boot source
tb.statusprint("get u-boot source")
tb.eof_call_tc("tc_lab_get_uboot_source.py")

tb.tc_lab_apply_patches_dir = tmp

tb.eof_call_tc("tc_workfd_goto_uboot_code.py")
tb.tc_workfd_get_list_of_files_dir = 'configs'
tb.tc_workfd_get_list_of_files_mask = '*_defconfig'
tb.eof_call_tc("tc_workfd_get_list_of_files_in_dir.py")

# create a list of boards
tb.tc_lab_compile_uboot_list_boardlist = []
for name in tb.list_of_files:
    tmp = name.split('_defconfig')
    tmp = tmp[0]
    tmp = tmp.split(tb.tc_workfd_get_list_of_files_dir + '/')
    tmp = tmp[1]
    tb.tc_lab_compile_uboot_list_boardlist.append(tmp)

# overwrite board list, if you want to do a
# short test for all supported archs
# nds32 m68k sh mips blackfin arc avr32 microblaze nios2 openrisc sandbox sparc x86
# tb.tc_lab_compile_uboot_list_boardlist = ['adp-ag101p', 'amcore', 'ap_sh4a_4a', 'vct_premium', 'bf527-ezkit', 'axs103', 'atngw100', 'microblaze-generic', '10m50', 'openrisc-generic', 'sandbox', 'gr_ep2s60', 'chromebook_link']

count = 0
good = []
bad = []
good_spl = []
bad_spl = []
not_checked = []
compile_bad = []
for board in tb.tc_lab_compile_uboot_list_boardlist:
    count += 1
    tb.statusprint("testing board %s %d / %d" % (board, count, len(tb.tc_lab_compile_uboot_list_boardlist)))
    ctrl = Connection(self, "tb_ctrl2")
    tb.check_open_fd(ctrl)

    tb.workfd = ctrl
    tb.tc_lab_compile_uboot_boardname = board
    tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

    # get architecture
    tb.tc_workfd_grep_file = tb.tc_workfd_get_list_of_files_dir + '/' + board + '_defconfig'
    ret = tb.call_tc("tc_uboot_get_arch.py")
    if ret == False:
        not_checked.append(board)
        tb.statusprint("testing board %s no architecture found" % (board))
        del ctrl
        continue

    # call set toolchain
    tb.tc_workfd_set_toolchain_arch = tb.cur_uboot_arch
    ret = tb.call_tc("tc_workfd_set_toolchain.py")
    if ret == False:
        not_checked.append(board)
        tb.statusprint("testing board %s setting toolchain failed" % (board))
        del ctrl
        continue

    # set SOURCE_DATE_EPOCH to get reproducable builds
    tb.eof_write(ctrl, "export SOURCE_DATE_EPOCH=0")
    tb.tbot_expect_prompt(ctrl)

    # get rid of differences in U-Boot version string
    # Best would be to disable CONFIG_LOCALVERSION_AUTO
    # we just patch setlocalverion yet ...
    save = tb.tc_lab_apply_patches_dir
    tb.tc_lab_apply_patches_dir = tb.tc_uboot_check_kconfig_preparepatch
    ret = tb.call_tc("tc_workfd_apply_patches.py")
    if ret == False:
        tb.statusprint("testing board %s apply preparepatch failed" % (board))
        tb.end_tc(False)
    tb.tc_lab_apply_patches_dir = save

    # call compile u-boot
    ret = tb.call_tc("tc_workfd_compile_uboot.py")
    if ret == False:
        compile_bad.append(board)
        tb.statusprint("testing board %s first compile failed" % (board))
        tmp = "make mrproper"
        tb.eof_write_lx_cmd_check(tb.workfd, tmp)
        tb.eof_write_cmd(tb.workfd, 'git reset --hard HEAD')
        tb.eof_write_cmd(tb.workfd, 'git clean -f')
        del ctrl
        continue

    uboot_md5sum = 'notread'
    uboot_spl_md5sum = 'notread'
    # check if u-boot-bin
    tb.tc_workfd_check_if_file_exists_name = 'u-boot.bin'
    ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
    if ret == True:
        # calc md5sum
        tb.tc_workfd_md5sum_name = tb.tc_workfd_check_if_file_exists_name
        tb.call_tc("tc_workfd_md5sum.py")
        uboot_md5sum = tb.tc_workfd_md5sum_sum
    # check if spl/u-boot-spl.bin
    tb.tc_workfd_check_if_file_exists_name = 'spl/u-boot-spl.bin'
    ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
    if ret == True:
        # calc md5sum
        tb.tc_workfd_md5sum_name = tb.tc_workfd_check_if_file_exists_name
        tb.call_tc("tc_workfd_md5sum.py")
        uboot_spl_md5sum = tb.tc_workfd_md5sum_sum

    # apply patch
    if tb.tc_lab_apply_patches_dir != 'none':
        tb.eof_call_tc("tc_workfd_apply_patches.py")

    # call compile u-boot
    ret = tb.call_tc("tc_workfd_compile_uboot.py")
    if ret == False:
        compile_bad.append(board)
        tb.statusprint("testing board %s second compile failed" % (board))
        tmp = "make mrproper"
        tb.eof_write_lx_cmd_check(tb.workfd, tmp)
        tb.eof_write_cmd(tb.workfd, 'git reset --hard HEAD')
        tb.eof_write_cmd(tb.workfd, 'git clean -f')
        del ctrl
        continue

    uboot_patched_md5sum = 'notread'
    uboot_spl_patched_md5sum = 'notread'
    # check if u-boot-bin
    tb.tc_workfd_check_if_file_exists_name = 'u-boot.bin'
    ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
    if ret == True:
        # calc md5sum
        tb.tc_workfd_md5sum_name = tb.tc_workfd_check_if_file_exists_name
        tb.call_tc("tc_workfd_md5sum.py")
        uboot_patched_md5sum = tb.tc_workfd_md5sum_sum
    # check if spl/u-boot-spl.bin
    tb.tc_workfd_check_if_file_exists_name = 'spl/u-boot-spl.bin'
    ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
    if ret == True:
        # calc md5sum
        tb.tc_workfd_md5sum_name = tb.tc_workfd_check_if_file_exists_name
        tb.call_tc("tc_workfd_md5sum.py")
        uboot_spl_patched_md5sum = tb.tc_workfd_md5sum_sum

    # check md5sums
    if uboot_md5sum != uboot_patched_md5sum:
        logging.error("%s u-boot bin diff %s != %s", board, uboot_md5sum, uboot_patched_md5sum)
        tb.statusprint("%s u-boot bin diff %s != %s" % (board, uboot_md5sum, uboot_patched_md5sum))
        result = False
        bad.append(board)
    else:
        logging.info("%s u-boot bin  same %s == %s", board, uboot_md5sum, uboot_patched_md5sum)
        if uboot_md5sum != 'notread':
            good.append(board)

    if uboot_spl_md5sum != uboot_spl_patched_md5sum:
        logging.error("%s u-boot spl bin diff %s != %s", board, uboot_spl_md5sum, uboot_spl_patched_md5sum)
        tb.statusprint("%s u-boot spl bin diff %s != %s" % (board, uboot_spl_md5sum, uboot_spl_patched_md5sum))
        result = False
        bad_spl.append(board)
    else:
        logging.info("%s u-boot spl bin same %s == %s", board, uboot_spl_md5sum, uboot_spl_patched_md5sum)
        if uboot_spl_md5sum != 'notread':
            good_spl.append(board)

    # reset base tree
    tmp = "make mrproper"
    tb.eof_write_lx_cmd_check(tb.workfd, tmp)

    if tb.tc_lab_apply_patches_dir != 'none':
        tb.eof_write_cmd(tb.workfd, 'git reset --hard HEAD')
        tb.eof_write_cmd(tb.workfd, 'git clean -f')

    # close connection
    del ctrl

# print some statistics
print("Boards      : %d" % (count))
print("compile err : %d" % len(compile_bad))
print("not checked : %d" % len(not_checked))
print("U-Boot good : %d bad %d" % (len(good), len(bad)))
print("SPL good    : %d bad %d" % (len(good_spl), len(bad_spl)))
if len(compile_bad):
    print("compile err :", compile_bad)
if len(not_checked):
    print("not checked :", not_checked)
if len(bad):
    print("bad         :", bad)
if len(bad_spl):
    print("bad spl     :", bad_spl)

tb.end_tc(result)
