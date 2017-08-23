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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_get_uboot_source.py
# get U-Boot source
# and go into the source tree
# End:

from tbotlib import tbot

save = tb.workfd
tb.workfd = tb.c_ctrl
ret = tb.call_tc("tc_workfd_goto_uboot_code.py")
if ret == False:
    u_boot_name = "u-boot-" + tb.config.boardlabname
    tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")
    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'u-boot_clone')
    # clone u-boot.git
    tmp = "git clone " + tb.config.tc_lab_get_uboot_source_git_repo + " " + u_boot_name
    tb.write_lx_cmd_check(tb.workfd, tmp)

    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'cd2u-boot')
    tmp = "cd " + u_boot_name
    tb.write_lx_cmd_check(tb.workfd, tmp)
    # check out a specific branch
    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'u-boot_checkout')
    tmp = "git checkout " + tb.config.tc_lab_get_uboot_source_git_branch
    tb.write_lx_cmd_check(tb.workfd, tmp)
    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'u-boot_describe')
    # print some info
    tmp = "git describe --tags"
    tb.write_lx_cmd_check(tb.workfd, tmp)


# check if there are patches to apply
tb.eof_call_tc("tc_lab_apply_patches.py")

tb.workfd = save
tb.end_tc(True)
