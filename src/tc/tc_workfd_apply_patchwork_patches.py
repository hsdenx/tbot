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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_apply_patchwork_patches.py
# apply patchworkpatches to current dir
from tbotlib import tbot

logging.info("args: workfd: %s %s %s", tb.workfd, tb.tc_workfd_apply_patchwork_patches_list, tb.tc_workfd_apply_patchwork_patches_checkpatch_cmd)

def apply_one_patch(tb, nr):
    tb.tc_workfd_rm_file_name = 'mbox'
    ret = tb.call_tc("tc_workfd_rm_file.py")
    #tb.eof_write(tb.workfd, tmp)
    tmp = 'wget http://patchwork.ozlabs.org/patch/' + nr + '/mbox'
    tb.eof_write(tb.workfd, tmp)
    tb.eof_read_end_state(tb.workfd, 1)
    tb.eof_call_tc("tc_workfd_check_cmd_success.py")
    if tb.tc_workfd_apply_patchwork_patches_checkpatch_cmd != 'none':
        tmp = tb.tc_workfd_apply_patchwork_patches_checkpatch_cmd + ' mbox'
        tb.eof_write(tb.workfd, tmp)
        tb.eof_read_end_state(tb.workfd, 1)
        ret = tb.call_tc("tc_workfd_check_cmd_success.py")
        if ret != True:
            logging.warn("checkpatch error")
            tmp = 'cat mbox | grep Subject'
            tb.eof_write(tb.workfd, tmp)
            tb.eof_read_end_state(tb.workfd, 1)
            tb.call_tc("tc_workfd_check_cmd_success.py")

    tb.eof_write(tb.workfd, 'git am -3 mbox')
    tb.eof_read_end_state(tb.workfd, 1)
    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

#print some infos
tb.eof_write(tb.workfd, 'pwd')
tb.eof_read_end_state(tb.workfd, 1)
tb.eof_write(tb.workfd, 'git describe')
tb.eof_read_end_state(tb.workfd, 1)
tb.eof_call_tc("tc_workfd_check_cmd_success.py")

for nr in tb.tc_workfd_apply_patchwork_patches_list:
    apply_one_patch(tb, nr)

tb.end_tc(True)
