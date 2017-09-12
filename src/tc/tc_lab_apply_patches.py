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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_apply_patches.py
#
# set workfd to c_ctrl
# call  tc_workfd_apply_patches.py
# restore old workfd
#
# End:

from tbotlib import tbot

logging.info("args: %s", tb.config.tc_lab_apply_patches_dir)

if tb.config.tc_lab_apply_patches_dir == 'none':
    tb.end_tc(True)

save = tb.workfd
tb.workfd = tb.c_ctrl

tb.eof_call_tc("tc_workfd_apply_patches.py")

tb.workfd = save

tb.end_tc(True)
