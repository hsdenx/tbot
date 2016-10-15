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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_can.py
#
# minimal can test:
# starts a new connection named tb_canm. This connection runs
# on board/PC which has a can conncetion to the board tbot
# tests, named CAN PC.
# If necessary (tb.tc_workfd_can_ssh != 'no'), tc connects first
# to ssh (if the CAN PC is not the lab PC). Also if necessary
# (tb.tc_workfd_can_su != 'no', switch to superuser on the CAN PC.
#
# Set on the CAN PC, with the "ip" command the bitrate
# tb.tc_workfd_can_bitrate for the can device tb.tc_workfd_can_dev
# and activate the interface.
#
# Now on the board, go into tb.tc_workfd_can_iproute_dir
# (which contains the "ip" command ...
# Set the bitrate with it and activate the can interface.
# Goto into tb.tc_workfd_can_util_dir which contains canutils
# Send '123#DEADBEEF' with cansend
#
# check if the CAN PC gets this string.
# End True if this is the case, False else
#
# ToDo:
# - get rid of tb.tc_workfd_can_iproute_dir and tb.tc_workfd_can_util_dir
#   (add the commands to rootfs ...)
# - support different can devices on the CAN PC and board
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s %s %s", tb.workfd.name, tb.tc_workfd_can_ssh, tb.tc_workfd_can_ssh_prompt, tb.tc_workfd_can_su)
logging.info("args: workfd %s %s", tb.tc_workfd_can_iproute_dir, tb.tc_workfd_can_util_dir)
logging.info("args: workfd %s %s", tb.tc_workfd_can_dev, tb.tc_workfd_can_bitrate)

tb.set_board_state("linux")

# create a new connection for the can "master"
can_master = Connection(tb, "tb_canm")
tb.check_open_fd(can_master)
savefd = tb.workfd
tb.workfd = can_master

if tb.tc_workfd_can_ssh != 'no':
    tb.workfd_ssh_cmd = tb.tc_workfd_can_ssh
    tb.workfd_ssh_cmd_prompt = tb.tc_workfd_can_ssh_prompt
    ret = tb.call_tc("tc_workfd_ssh.py")
    if ret == False:
        # close connection
        del can_master
        tb.workfd = savefd
        tb.end_tc(False)

if tb.tc_workfd_can_su != 'no':
    tb.switch_su_board = tb.tc_workfd_can_su
    ret = tb.call_tc("tc_workfd_switch_su.py")
    if ret == False:
        # close connection
        del can_master
        tb.workfd = savefd
        tb.end_tc(False)

tmp = 'ip link set ' + tb.tc_workfd_can_dev + ' type can bitrate ' + tb.tc_workfd_can_bitrate
tb.eof_write_cmd(can_master, tmp)
tmp = 'ip link set ' + tb.tc_workfd_can_dev + ' up'
tb.eof_write_cmd(can_master, tmp)
tmp = 'cd ' + tb.tc_workfd_can_util_dir
tb.eof_write_cmd(can_master, tmp)
tmp = './candump ' + tb.tc_workfd_can_dev
tb.eof_write(can_master, tmp)

# now we are waiting for data on can_master ...

# send some data from the board
tmp = 'cd ' + tb.tc_workfd_can_iproute_dir
tb.eof_write_cmd(tb.c_con, tmp)
tmp = './ip/ip link set ' + tb.tc_workfd_can_dev + ' type can bitrate ' + tb.tc_workfd_can_bitrate
tb.eof_write_cmd(tb.c_con, tmp)
tmp = './ip/ip link set ' + tb.tc_workfd_can_dev + ' up'
tb.eof_write_cmd(tb.c_con, tmp)
tmp = 'cd ' + tb.tc_workfd_can_util_dir
tb.eof_write_cmd(tb.c_con, tmp)
tmp = './cansend ' + tb.tc_workfd_can_dev + ' 123#DEADBEEF'
tb.eof_write_cmd(tb.c_con, tmp)

# now we must get "can0  123   [4]  DE AD BE EF"
tmp = tb.tc_workfd_can_dev + '  123   [4]  DE AD BE EF'
tb.tbot_expect_string(can_master, tmp)

# end candump
tb.send_ctrl_c(can_master)

# close connection
del can_master
tb.workfd = savefd
tb.end_tc(True)
