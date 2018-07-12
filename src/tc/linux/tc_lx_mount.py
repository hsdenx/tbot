# SPDX-License-Identifier: GPL-2.0
#
# Description:
# mount device tb.config.tc_lx_mount_dev with fs type tb.config.tc_lx_mount_fs_type
# to tb.config.tc_lx_mount_dir
#
# used variables
#
# - tb.config.tc_lx_mount_dev
#| device which get mounted
#| default: '/dev/sda1'
#
# - tb.config.tc_lx_mount_fs_type
#| fs type for mount command
#| default: 'ext4'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lx_mount_dev', '/dev/sda1')
tb.define_variable('tc_lx_mount_fs_type', )
logging.info("d%s", tb.config.tc_lx_mount_dir)

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.c_con
tb.eof_write(c, "mount")
searchlist = [tb.config.tc_lx_mount_dev]
tmp = True
found = False
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        found = True
    elif ret == 'prompt':
        tmp = False

if found == True:
    tb.end_tc(True)

# mount device
tmp = "mount -t " + tb.config.tc_lx_mount_fs_type + " " + tb.config.tc_lx_mount_dev + " " + tb.config.tc_lx_mount_dir
tb.eof_write(c, tmp)
searchlist = ["mounted filesystem"]
tmp = True
cmd_ok = False
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        cmd_ok = True
    elif ret == 'prompt':
        tmp = False

if cmd_ok == True:
    tb.end_tc(True)

tb.workfd = tb.c_con
tb.eof_call_tc("tc_workfd_check_cmd_success.py")
tb.end_tc(True)
