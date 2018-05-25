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
#
# loop over the list of strings in the tb.config.tc_lx_cmd_and_grep
# "cmds" key.
# for each command save the output in a temporary file, and
# search that all strings in key="cmd" are in the temporary file.
#
# example tb.config.tc_lx_cmd_and_grep
# tc_lx_cmd_and_grep = {"cmds" : ["cat /proc/partitions",
# 				"cat /proc/mounts"],
# 		"cat /proc/partitions" :
#			[
#				"mmcblk0p1",
#				"mmcblk0p2",
#			]
# 		,
# 		"cat /proc/mounts" : [
# 			"/ squashfs ro,noatime 0 0",
# 			"tmp /tmp tmpfs rw,relatime 0 0",
# 		]}
#
# This will do:
# - "cat /proc/partitions > gnlmpf"
# - search if gnlmpf contains the strings "mmcblk0p1" and "mmcblk0p2"
# - "cat /proc/mounts > gnlmpf"
# - search if gnlmpf contains the strings
#   "/ squashfs ro,noatime 0 0"
#   "tmp /tmp tmpfs rw,relatime 0 0"
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_lx_cmd_and_grep
except:
    logging.warn("not configured, please set tb.config.tc_lx_cmd_and_grep")
    tb.end_tc(False)

logging.info("args: workfd: %s %s", tb.workfd.name, tb.config.tc_lx_cmd_and_grep)

c = tb.workfd

# set board state for which the tc is valid
tb.set_board_state("linux")

tb.tc_workfd_grep_file = 'gnlmpf'
cmds = tb.config.tc_lx_cmd_and_grep["cmds"]
for cmd in cmds:
    lxcmd = cmd + ' > ' + tb.tc_workfd_grep_file
    tb.write_lx_cmd_check(c, lxcmd)
    for string in tb.config.tc_lx_cmd_and_grep[cmd]:
        tb.tc_workfd_grep_string = '"' + string + '"'
        tb.eof_call_tc("tc_workfd_grep.py")

    tb.write_lx_cmd_check(c, 'rm ' + tb.tc_workfd_grep_file)

tb.end_tc(True)
