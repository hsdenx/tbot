# SPDX-License-Identifier: GPL-2.0
#
# Description:
# more dxr2 specific ubi tests, maybe make them common
# End:

from tbotlib import tbot

#here starts the real test
logging.info("args: %s %s %s", tb.config.tc_ubi_cmd_path, tb.config.tc_ubi_mtd_dev, tb.config.tc_ubi_ubi_dev)

#set board state for which the tc is valid
tb.set_board_state("linux")

def create_ubi_cmd(tb, cmd):
    tmp = tb.config.tc_ubi_cmd_path + '/' + cmd
    return tmp

tb.write_lx_cmd_check(tb.workfd, "ls -al /home/hs/zug/mnt/")
tb.write_lx_cmd_check(tb.workfd, "mount -t ubifs /dev/ubi0_0 /home/hs/zug/mnt")
tb.write_lx_cmd_check(tb.workfd, "ls -al /home/hs/zug/mnt/")
tb.write_lx_cmd_check(tb.workfd, "cat /home/hs/zug/mnt/creation_time ")
tb.write_lx_cmd_check(tb.workfd, "cmp /home/hs/ubi_random /home/hs/zug/mnt/boot/ubi_random")
tb.write_lx_cmd_check(tb.workfd, "umount /home/hs/zug/mnt")

tb.end_tc(True)
