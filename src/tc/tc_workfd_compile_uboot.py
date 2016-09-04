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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_compile_uboot.py
# compile u-boot
# End:

from tbotlib import tbot

if tb.tc_lab_compile_uboot_export_path != 'none':
    tmp = "export PATH=" + tb.tc_lab_compile_uboot_export_path + ":$PATH"
    tb.eof_write_lx_cmd_check(tb.workfd, tmp)

tmp = "make mrproper"
tb.eof_write_lx_cmd_check(tb.workfd, tmp)

defname = tb.tc_lab_compile_uboot_boardname + "_defconfig"
tmp = "make " + defname
tb.event.create_event('main', tb.boardname, "UBOOT_DEFCONFIG", defname)
tb.eof_write_lx_cmd_check(tb.workfd, tmp)
tb.event.create_event('main', tb.boardname, "UBOOT_SRC_PATH", tb.tc_lab_source_dir + "/u-boot-" + tb.boardlabname)

tmp = "make " + self.tc_lab_compile_uboot_makeoptions + " all"
tb.eof_write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
