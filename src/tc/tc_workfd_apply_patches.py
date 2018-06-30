# SPDX-License-Identifier: GPL-2.0
#
# Description:
# apply patches in tb.config.tc_lab_apply_patches_dir
#
# - tb.config.tc_lab_apply_patches_dir
#   path to directory which contains the patches
#   default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lab_apply_patches_dir', 'none')

if tb.config.tc_lab_apply_patches_dir == 'none':
    tb.end_tc(True)

c = tb.workfd
# apply all patches in tc_lab_apply_patches_dir
tb.set_term_length(c)

tmp = 'for i in ' + tb.config.tc_lab_apply_patches_dir + '/*.patch; do patch -p1 < $i; done'
tb.eof_write(c, tmp)

searchlist = ["No such", "FAILED", "Assume -R?"]
tmp = True
apply_ok = True
while tmp == True:
    tmp = tb.tbot_rup_and_check_strings(c, searchlist)
    if tmp == '0':
        apply_ok = False
        tmp = True
    if tmp == '1':
        apply_ok = False
        tmp = True
    if tmp == '2':
        tb.eof_write(c, 'y')
        tmp = True
    elif tmp == 'prompt':
        tmp = False

if apply_ok == False:
    tb.end_tc(False)

tb.eof_call_tc("tc_workfd_check_cmd_success.py")

tb.end_tc(True)
