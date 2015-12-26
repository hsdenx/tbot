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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_apply_local_patches.py
# apply patchworkpatches to current dir
from tbotlib import tbot

logging.info("args: workfd: %s %s %s %s", tb.workfd, tb.tc_workfd_apply_local_patches_dir, tb.tc_workfd_apply_local_patches_checkpatch_cmd, tb.tc_workfd_apply_local_patches_checkpatch_cmd_strict)

if tb.tc_workfd_apply_local_patches_dir == 'none':
   tb.end_tc(True)

tb.set_term_length(tb.workfd)

def apply_one_patch(tb, filename):
    if tb.tc_workfd_apply_local_patches_checkpatch_cmd != 'none':
        tmp = tb.tc_workfd_apply_local_patches_checkpatch_cmd + ' ' + filename
        tb.eof_write(tb.workfd, tmp)
        tb.eof_read_end_state(tb.workfd, 10)
        ret = tb.call_tc("tc_workfd_check_cmd_success.py")
        if ret != True:
            logging.warn("checkpatch error")
            tmp = 'ls ' + filename
            tb.eof_write(tb.workfd, tmp)
            tb.eof_read_end_state(tb.workfd, 10)
            tb.call_tc("tc_workfd_check_cmd_success.py")
            if tb.tc_workfd_apply_local_patches_checkpatch_cmd_strict == "yes":
                tb.end_tc(False)

    tb.eof_write(tb.workfd, 'git am -3 ' + filename)
    tb.eof_read_end_state(tb.workfd, 10)
    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

#print some infos
tb.eof_write(tb.workfd, 'pwd')
tb.eof_read_end_state(tb.workfd, 1)
tb.eof_write(tb.workfd, 'git describe')
tb.eof_read_end_state(tb.workfd, 5)
tb.eof_call_tc("tc_workfd_check_cmd_success.py")

tb.tc_workfd_get_list_of_files_dir = tb.tc_workfd_apply_local_patches_dir
tb.tc_workfd_get_list_of_files_mask = '*.patch'
tb.eof_call_tc("tc_workfd_get_list_of_files_in_dir.py")

for filename in tb.list_of_files:
    apply_one_patch(tb, filename)

tb.end_tc(True)
