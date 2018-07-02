# SPDX-License-Identifier: GPL-2.0
#
# Description:
# dxr2 check all patches with patchworknumber > default_nr
# in patchwork, if it is checkpatch clean and applies to
# current mainline without errors
# End:

from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

#delete old u-boot source tree
tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_rm_uboot_code.py")

#cloning needs a bigger timeout, (git clone has no output)
#call get u-boot source
tb.statusprint("get u-boot source")
tb.eof_call_tc("tc_lab_get_uboot_source.py")

#call set toolchain
tb.statusprint("set toolchain")
tb.eof_call_tc("tc_lab_set_toolchain.py")

#get current list of patches in ToDo list
tb.statusprint("get patchwork patches")
tb.eof_call_tc("tc_workfd_get_patchwork_number_list.py")

# delete numbers from patchworklist, which are smaller
# than default_nr
default_nr = 589442
i = 0
nr_list = []
name_list = []
for j in tb.config.tc_workfd_apply_patchwork_patches_list:
    #logging.info("nr: %s %s\n" % (tb.config.tc_workfd_apply_patchwork_patches_list[i], tb.config.tc_workfd_apply_patchwork_patches_list_title[i]))
    nr = int(tb.config.tc_workfd_apply_patchwork_patches_list[i])
    if nr > default_nr:
        nr_list.append(tb.config.tc_workfd_apply_patchwork_patches_list[i])
        name_list.append(tb.config.tc_workfd_apply_patchwork_patches_list_title[i])
    i += 1

#i = 0
#for j in nr_list:
#    print("LIST", nr_list[i])
#    i += 1

tb.config.tc_workfd_apply_patchwork_patches_list = nr_list
tb.config.tc_workfd_apply_patchwork_patches_list_title = name_list

tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

#add patchwork patches
tb.statusprint("apply patchwork patches")
tb.config.tc_workfd_apply_patchwork_patches_checkpatch_cmd = 'scripts/checkpatch.pl'
tb.eof_call_tc("tc_workfd_apply_patchwork_patches.py")

#call compile u-boot
#tb.statusprint("compile u-boot")
#tb.eof_call_tc("tc_lab_compile_uboot.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
