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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_apply_patches.py
# apply patches to source
from tbotlib import tbot

logging.info("args: %s", tb.tc_lab_apply_patches_dir)

if tb.tc_lab_apply_patches_dir == 'none':
    tb.end_tc(True)

c = tb.c_ctrl
# apply all patches in tc_lab_apply_patches_dir
tb.set_term_length(c)

tmp = 'patch -p1 < ' + tb.tc_lab_apply_patches_dir + '/' + '*.patch'
tb.eof_write(c, tmp)

searchlist = ["No such"]
tmp = True
apply_ok = True
while tmp == True:
    tmp = tb.tbot_read_line_and_check_strings(c, searchlist)
    if tmp == '0':
        apply_ok = False
        tmp = True
    elif tmp == 'prompt':
        tmp = False

if apply_ok == False:
    tb.end_tc(False)

tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_check_cmd_success.py")

tb.end_tc(True)
