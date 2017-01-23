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
# - set SOURCE_DATE_EPOCH=0 to get reproducible builds
# - get rid of local version ToDo: find a way to disable CONFIG_LOCALVERSION_AUTO
# - if tb.tc_uboot_check_kconfig_read_sumfile is != 'none'
#     read a list of boards and md5sums from the file in
#     tb.tc_uboot_check_kconfig_read_sumfile
#   else
#   - create a list of boards (all defconfigs)
#   - do for all boards:
#     - get architecture and set toolchain
#     - compile U-Boot and calculate md5sum
#       with tc_workfd_compile_uboot.py and tc_workfd_md5sum.py
#     - if tb.tc_uboot_check_kconfig_create_sumfile != 'none'
#       save the board md5sum lists in the file
#       tb.tc_uboot_check_kconfig_create_sumfile
#       you can use this now as a reference, so no need
#       to calculate always for all boards the md5sums
#       -> saves a lot of time!
#
# - apply patch(es) with tc_workfd_apply_patches.py
# - do for all boards:
#   - compile U-Boot again (patched version)
#   - calculate md5sum again
#   - calculate md5sums
#   - check if they are the same
# End:

import os
from tbotlib import tbot

tb.tc_uboot_check_kconfig_create_sumfile = 'md5sum.txt'
tb.tc_uboot_check_kconfig_read_sumfile = 'none'

logging.info("args: %s", tb.tc_uboot_check_kconfig_preparepatch)

#set board state for which the tc is valid
tb.set_board_state("lab")

# delete old u-boot source tree
tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_rm_uboot_code.py")

result = True

tmp = tb.config.tc_lab_apply_patches_dir
tb.config.tc_lab_apply_patches_dir = 'none'

# call get u-boot source
tb.statusprint("get u-boot source")
tb.eof_call_tc("tc_lab_get_uboot_source.py")

tb.config.tc_lab_apply_patches_dir = tmp

good = []
bad = []
good_spl = []
bad_spl = []
not_checked = []
compile_bad = []
arch = []
oldmd5sum = []
oldsplmd5sum = []
tb.tc_lab_compile_uboot_list_boardlist = []

ctrl = Connection(self, "tb_ctrl2")
tb.check_open_fd(ctrl)
tb.workfd = ctrl

tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# prepare U-Boot code
# set SOURCE_DATE_EPOCH to get reproducable builds
tb.eof_write(ctrl, "export SOURCE_DATE_EPOCH=0")
tb.tbot_expect_prompt(ctrl)

# get rid of differences in U-Boot version string
# Best would be to disable CONFIG_LOCALVERSION_AUTO
# we just patch setlocalverion yet ...
save = tb.config.tc_lab_apply_patches_dir
tb.config.tc_lab_apply_patches_dir = tb.tc_uboot_check_kconfig_preparepatch
ret = tb.call_tc("tc_workfd_apply_patches.py")
if ret == False:
    tb.statusprint("testing board %s apply preparepatch failed" % (board))
    tb.end_tc(False)
tb.config.tc_lab_apply_patches_dir = save

if tb.tc_uboot_check_kconfig_read_sumfile != 'none':
    fname = tb.workdir + "/" + tb.tc_uboot_check_kconfig_read_sumfile
    tb.statusprint("reading boardlist and md5sums from file %s" % (fname))
    try:
        fd = open(fname, 'r')
    except IOError:
        logging.warning("Could not open: %s", fname)
        tb.end_tc(False)

    for line in fd.readlines():
        cols = line.split()
        tb.tc_lab_compile_uboot_list_boardlist.append(cols[0])
        arch.append(cols[1])
        oldmd5sum.append(cols[2])
        oldsplmd5sum.append(cols[3])

    fd.close()

else:
    tb.tc_workfd_get_list_of_files_dir = 'configs'
    tb.config.tc_workfd_get_list_of_files_mask = '*_defconfig'
    tb.eof_call_tc("tc_workfd_get_list_of_files_in_dir.py")

    # create a list of boards
    for name in tb.list_of_files:
        tmp = name.split('_defconfig')
        tmp = tmp[0]
        tmp = tmp.split(tb.tc_workfd_get_list_of_files_dir + '/')
        tmp = tmp[1]
        tb.tc_lab_compile_uboot_list_boardlist.append(tmp)

    # overwrite board list, if you want to do a
    # short test for all supported archs
    # arm64 nds32 m68k sh mips blackfin arc avr32 microblaze nios2 openrisc sandbox sparc x86
    # tb.tc_lab_compile_uboot_list_boardlist = ['ls2080a_emu', 'adp-ag101p', 'amcore', 'ap_sh4a_4a', 'vct_premium', 'bf527-ezkit', 'axs103', 'atngw100', 'microblaze-generic', '10m50', 'openrisc-generic', 'sandbox', 'gr_ep2s60', 'chromebook_link']

    # tb.tc_lab_compile_uboot_list_boardlist = ['am335x_baltos', 'am335x_evm_spiboot', 'am335x_igep0033', 'cm_t335', 'cm_t43', 'cm_t54', 'duovero']
    # tb.tc_lab_compile_uboot_list_boardlist = ['am335x_baltos', 'am335x_evm_spiboot', 'am335x_igep0033', 'cm_t335', 'cm_t43', 'cm_t54', 'duovero', 'k2e_evm', 'k2g_evm', 'k2hk_evm', 'k2l_evm', 'omap3_pandora', 'omap3_zoom1', 'pepper']

    count = 0
    for board in tb.tc_lab_compile_uboot_list_boardlist:
        count += 1
        tb.statusprint("testing board %s %d / %d" % (board, count, len(tb.tc_lab_compile_uboot_list_boardlist)))

        tb.config.tc_lab_compile_uboot_boardname = board

        # get architecture
        tmp = "make mrproper"
        tb.write_lx_cmd_check(tb.workfd, tmp)
        tmp = "make " + board + "_defconfig"
        tb.write_lx_cmd_check(tb.workfd, tmp)
        tb.tc_workfd_grep_file = '.config'
        ret = tb.call_tc("tc_uboot_get_arch.py")
        if ret == False:
            not_checked.append(board)
            arch.append('none')
            oldmd5sum.append('none')
            oldsplmd5sum.append('none')
            tb.statusprint("testing board %s no architecture found" % (board))
            tmp = "make mrproper"
            tb.write_lx_cmd_check(tb.workfd, tmp)
            continue

        arch.append(tb.cur_uboot_arch)

        tmp = "make mrproper"
        tb.write_lx_cmd_check(tb.workfd, tmp)
        # call set toolchain
        tb.config.tc_workfd_set_toolchain_arch = tb.cur_uboot_arch
        ret = tb.call_tc("tc_workfd_set_toolchain.py")
        if ret == False:
            not_checked.append(board)
            oldmd5sum.append('notread')
            oldsplmd5sum.append('notread')
            tb.statusprint("testing board %s setting toolchain failed" % (board))
            continue

        # call compile u-boot
        ret = tb.call_tc("tc_workfd_compile_uboot.py")
        if ret == False:
            compile_bad.append(board)
            tb.statusprint("testing board %s first compile failed" % (board))
            oldmd5sum.append('notread')
            oldsplmd5sum.append('notread')
            continue

        uboot_md5sum = 'notread'
        uboot_spl_md5sum = 'notread'
        # check if u-boot-bin
        tb.config.tc_workfd_check_if_file_exists_name = 'u-boot.bin'
        ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
        if ret == True:
            # calc md5sum
            tb.tc_workfd_md5sum_name = tb.config.tc_workfd_check_if_file_exists_name
            tb.call_tc("tc_workfd_md5sum.py")
            uboot_md5sum = tb.tc_workfd_md5sum_sum
        # check if spl/u-boot-spl.bin
        tb.config.tc_workfd_check_if_file_exists_name = 'spl/u-boot-spl.bin'
        ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
        if ret == True:
            # calc md5sum
            tb.tc_workfd_md5sum_name = tb.config.tc_workfd_check_if_file_exists_name
            tb.call_tc("tc_workfd_md5sum.py")
            uboot_spl_md5sum = tb.tc_workfd_md5sum_sum

        oldmd5sum.append(uboot_md5sum)
        oldsplmd5sum.append(uboot_spl_md5sum)

    if tb.tc_uboot_check_kconfig_create_sumfile != 'none':
        fname = tb.workdir + "/" + tb.tc_uboot_check_kconfig_create_sumfile
        print("FILE : ", fname)
        try:
            fd = open(fname, 'w')
        except IOError:
            logging.warning("Could not open: %s", fname)
            tb.end_tc(False)
        count = 0
        for board in tb.tc_lab_compile_uboot_list_boardlist:
            fd.write('%-15s %15s %15s %15s\n' % (board, arch[count], oldmd5sum[count], oldsplmd5sum[count]))
            count += 1

        fd.close()

# now apply patches
if tb.config.tc_lab_apply_patches_dir != 'none':
    tb.eof_call_tc("tc_workfd_apply_patches.py")

count = 0
for board in tb.tc_lab_compile_uboot_list_boardlist:
    count += 1
    tb.statusprint("testing 2 board %s %d / %d" % (board, count, len(tb.tc_lab_compile_uboot_list_boardlist)))

    tb.config.tc_lab_compile_uboot_boardname = board

    tmp = "make mrproper"
    tb.write_lx_cmd_check(tb.workfd, tmp)

    if arch[count - 1] == 'none':
        continue

    if oldmd5sum[count - 1] == 'notread':
        continue

    # call set toolchain
    tb.config.tc_workfd_set_toolchain_arch = arch[count - 1]
    ret = tb.call_tc("tc_workfd_set_toolchain.py")
    if ret == False:
        tb.statusprint("testing board %s setting toolchain failed" % (board))
        continue

    # call compile u-boot
    ret = tb.call_tc("tc_workfd_compile_uboot.py")
    if ret == False:
        compile_bad.append(board)
        tb.statusprint("testing board %s second compile failed" % (board))
        tmp = "make mrproper"
        tb.write_lx_cmd_check(tb.workfd, tmp)
        continue

    uboot_patched_md5sum = 'notread'
    uboot_spl_patched_md5sum = 'notread'
    # check if u-boot-bin
    tb.config.tc_workfd_check_if_file_exists_name = 'u-boot.bin'
    ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
    if ret == True:
        # calc md5sum
        tb.tc_workfd_md5sum_name = tb.config.tc_workfd_check_if_file_exists_name
        tb.call_tc("tc_workfd_md5sum.py")
        uboot_patched_md5sum = tb.tc_workfd_md5sum_sum
    # check if spl/u-boot-spl.bin
    tb.config.tc_workfd_check_if_file_exists_name = 'spl/u-boot-spl.bin'
    ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
    if ret == True:
        # calc md5sum
        tb.tc_workfd_md5sum_name = tb.config.tc_workfd_check_if_file_exists_name
        tb.call_tc("tc_workfd_md5sum.py")
        uboot_spl_patched_md5sum = tb.tc_workfd_md5sum_sum

    # check md5sums
    if oldmd5sum[count - 1] != uboot_patched_md5sum:
        logging.error("%s u-boot bin diff %s != %s", board, oldmd5sum[count - 1], uboot_patched_md5sum)
        tb.statusprint("%s u-boot bin diff %s != %s" % (board, oldmd5sum[count - 1], uboot_patched_md5sum))
        result = False
        bad.append(board)
    else:
        logging.info("%s u-boot bin  same %s == %s", board, oldmd5sum[count - 1], uboot_patched_md5sum)
        good.append(board)

    if oldsplmd5sum[count - 1] != uboot_spl_patched_md5sum:
        logging.error("%s u-boot spl bin diff %s != %s", board, oldsplmd5sum[count - 1], uboot_spl_patched_md5sum)
        tb.statusprint("%s u-boot spl bin diff %s != %s" % (board, oldsplmd5sum[count - 1], uboot_spl_patched_md5sum))
        result = False
        bad_spl.append(board)
    else:
        logging.info("%s u-boot spl bin same %s == %s", board, oldsplmd5sum[count - 1], uboot_spl_patched_md5sum)
        good_spl.append(board)

# print some statistics
print("Boards      : %d" % (count))
print("compile err : %d" % len(compile_bad))
print("not checked : %d" % len(not_checked))
print("U-Boot good : %d bad %d" % (len(good), len(bad)))
print("SPL good    : %d bad %d" % (len(good_spl), len(bad_spl)))
if len(compile_bad):
    print("Boards not checked, as they had compile errors:")
    print(compile_bad)
if len(not_checked):
    print("Boards not checked, as no toolchain exists:")
    print(not_checked)
if len(bad):
    print("Boards which have differences in the resulting U-Boot bin:")
    print(bad)
if len(bad_spl):
    print("Boards which have differences in the resulting SPL bin:")
    print(bad_spl)

tb.end_tc(result)
