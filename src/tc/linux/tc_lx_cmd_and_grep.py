# SPDX-License-Identifier: GPL-2.0
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

tb.config.tc_workfd_grep_file = 'gnlmpf'
cmds = tb.config.tc_lx_cmd_and_grep["cmds"]
for cmd in cmds:
    lxcmd = cmd + ' > ' + tb.config.tc_workfd_grep_file
    tb.write_lx_cmd_check(c, lxcmd)
    for string in tb.config.tc_lx_cmd_and_grep[cmd]:
        tb.config.tc_workfd_grep_string = '"' + string + '"'
        tb.eof_call_tc("tc_workfd_grep.py")

    tb.write_lx_cmd_check(c, 'rm ' + tb.config.tc_workfd_grep_file)

tb.end_tc(True)
