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
# tbot.py -s lab_denx -c smartweb -t tc_demo_part2.py
# start tc:
# - call tc_demo_get_ub_code.py
# - call tc_demo_compile_install_test.py
# End:

from tbotlib import tbot

# set wordkfd to the connection we want to work on
tb.workfd = tb.c_ctrl

# go into u-boot code
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

# set specific settings for this demo
tb.config.workfd_get_patchwork_number_user = 'hs'
tb.config.tc_workfd_apply_patchwork_patches_blacklist = []
tb.config.tc_workfd_get_patchwork_number_list_order = '-delegate'

# get current list of patches in ToDo list
tb.statusprint("get patchwork patches")
tb.eof_call_tc("tc_workfd_get_patchwork_number_list.py")

# add patchwork patches to U-Boot code
tb.statusprint("apply patchwork patches")
tb.config.tc_workfd_apply_patchwork_patches_checkpatch_cmd = 'scripts/checkpatch.pl'
tb.eof_call_tc("tc_workfd_apply_patchwork_patches.py")

# now compile, install and test the new source on the board
tb.eof_call_tc("tc_demo_compile_install_test.py")
tb.end_tc(True)
