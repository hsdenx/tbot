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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_board_dxr2_lx_ubi_tests.py
# more dxr2 specific ubi tests, maybe make them common
# End:

from tbotlib import tbot

#here starts the real test
logging.info("args: %s %s %s", tb.tc_ubi_cmd_path, tb.tc_ubi_mtd_dev, tb.tc_ubi_ubi_dev)

#set board state for which the tc is valid
tb.set_board_state("linux")

def create_ubi_cmd(tb, cmd):
    tmp = tb.tc_ubi_cmd_path + '/' + cmd
    return tmp

tb.write_lx_cmd_check(tb.workfd, "ls -al /home/hs/zug/mnt/")
tb.write_lx_cmd_check(tb.workfd, "mount -t ubifs /dev/ubi0_0 /home/hs/zug/mnt")
tb.write_lx_cmd_check(tb.workfd, "ls -al /home/hs/zug/mnt/")
tb.write_lx_cmd_check(tb.workfd, "cat /home/hs/zug/mnt/creation_time ")
tb.write_lx_cmd_check(tb.workfd, "cmp /home/hs/ubi_random /home/hs/zug/mnt/boot/ubi_random")
tb.write_lx_cmd_check(tb.workfd, "umount /home/hs/zug/mnt")

tb.end_tc(True)
