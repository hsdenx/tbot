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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_dfu_random.py
# test a U-Boot dfu alt setting tb.tc_ub_dfu_dfu_util_alt_setting
# Therefore write a random file with size tb.tc_ub_dfu_rand_size
# to it, reread it and compare it. TC fails if files differ
# (If readen file is longer, this is no error!)
#
# If dfu-util is not installed on the lab PC, set
# tb.tc_ub_dfu_dfu_util_ssh for connecting with ssh to a PC
# which have it installed, and a USB cable connected to the board.
# Set tb.tc_ub_dfu_dfu_util_path to the path of dfu-util, if
# you have a self compiled version of it.
# Set tb.tc_ub_dfu_rand_ubcmd for the executed command on
# U-Boot shell for getting into DFU mode
# 
from tbotlib import tbot

#here starts the real test
logging.info("args: %s %s %s %s %s", tb.tc_ub_dfu_dfu_util_path,
	tb.tc_ub_dfu_dfu_util_ssh, tb.tc_ub_dfu_dfu_util_alt_setting,
	tb.tc_ub_dfu_rand_size, tb.tc_ub_dfu_rand_ubcmd)

#set board state for which the tc is valid
tb.set_board_state("u-boot")

# load U-Boot environment variables for tbot
tb.eof_call_tc("tc_ub_load_board_env.py")

# print some U-Boot variables
tb.eof_write_cmd(tb.channel_con, "mtdparts")
tb.eof_write_cmd(tb.channel_con, "printenv dfu_alt_info")

#start dfu on the board
tb.eof_write_con(tb.tc_ub_dfu_rand_ubcmd)

#read until 'using id'
ret = True
while ret == True:
    ret = tb.search_str_in_readline_con("using id")
    if ret == False:
        tb.end_tc(False)

tb.workfd = tb.channel_ctrl
if tb.tc_ub_dfu_dfu_util_ssh != "none":
    tb.workfd_ssh_cmd = tb.tc_ub_dfu_dfu_util_ssh
    tb.eof_call_tc("tc_workfd_ssh.py")

if tb.tc_ub_dfu_dfu_util_path != 'none':
    # cd into dfu-util source
    tmp = "cd " + tb.tc_ub_dfu_dfu_util_path
    dfu_cmd = './src/dfu-util'
else:
    dfu_cmd = 'dfu-util'

tb.eof_write_cmd(tb.workfd, "pwd")

# List currently attached DFU capable devices
tb.eof_write_ctrl(dfu_cmd + " -l")
ret = tb.search_str_in_readline_ctrl("UNDEFINED")
if ret == True:
    tb.end_tc(False)

# create random file
tb.tc_workfd_generate_random_file_name = '/tmp/random'
tb.tc_workfd_generate_random_file_length = tb.tc_ub_dfu_rand_size
tb.eof_call_tc("tc_workfd_generate_random_file.py");

###########################################
# download it to the board
logging.info("download file")
tmp = dfu_cmd + " -a " + tb.tc_ub_dfu_dfu_util_alt_setting + " -D " + tb.tc_workfd_generate_random_file_name
tb.eof_write_ctrl(tmp)
searchlist = ["Claiming", "Copying data from PC to DFU device",
raw("state(7) = dfuMANIFEST, status(0) = No error condition is present"),
raw("state(2) = dfuIDLE, status(0) = No error condition is present"),
"Done!"]
ok_list = [False, False, False, False, False]
count = 5
tmp = True
down_ok = True
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_ctrl, searchlist)
    if tmp in range(0, count):
        ok_list[tmp] = True
        if tmp > 0:
            if ok_list[tmp - 1] != True:
                logging.info("%d : %s not found", tmp - 1, searchlist[tmp - 1])
                print("%d : %s not found", tmp - 1, searchlist[tmp - 1])
                down_ok = False
        tmp = True
    elif tmp == None:
        # ! endless loop ...
        tmp = True
    elif tmp == 'prompt':
        tmp = False

if not down_ok:
    tb.end_tc(False)

# on board we should see
####
# DOWNLOAD ... OK
tb.eof_search_str_in_readline_con("OK")

tb.eof_write_cmd(tb.workfd, "rm -f /tmp/gnlmpf")
# upload it back
tmp = dfu_cmd + " -a " + tb.tc_ub_dfu_dfu_util_alt_setting + " -U /tmp/gnlmpf"
tb.eof_write_ctrl(tmp)

searchlist = ["Claiming", "Copying data from DFU device to PC",
raw("state(7) = dfuMANIFEST, status(0) = No error condition is present"),
raw("state(2) = dfuIDLE, status(0) = No error condition is present"),
"Done!"]
ok_list = [False, False, False, False, False]
count = 5
tmp = True
up_ok = True
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_ctrl, searchlist)
    if tmp in range(0, count):
        ok_list[tmp] = True
        if tmp > 0:
            if ok_list[tmp - 1] != True:
                logging.info("%d : %s not found", tmp - 1, searchlist[tmp - 1])
                down_ok = False
        tmp = True
    elif tmp == None:
        # ! endless loop ...
        tmp = True
    elif tmp == 'prompt':
        tmp = False

if not up_ok:
    tb.end_tc(False)

#on board we see
####
#UPLOAD ... done
tb.eof_search_str_in_readline_con("done")

#Ctrl+C on Board to exit ...
tb.send_ctrl_c_con()
tb.eof_read_end_state_con(2)

#############################
#now diff the files
logging.info("diff files")
tmp = "cmp " + tb.tc_workfd_generate_random_file_name + " /tmp/gnlmpf"
tb.eof_write_ctrl(tmp)
searchlist = ["EOF", "differ"]
tmp = True
differ = False
differ_at_end = False
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_ctrl, searchlist)
    if tmp == 0:
        differ_at_end = True
        tmp = True
    if tmp == 1:
        differ = True
        tmp = True
    elif tmp == None:
        # ! endless loop ...
        tmp = True
    elif tmp == 'prompt':
        tmp = False

if differ and not differ_at_end:
    tb.end_tc(False)

tb.eof_write_cmd(tb.workfd, "rm -f /tmp/gnlmpf")
tb.eof_write_cmd(tb.workfd, "rm -f /tmp/random")

#############################
# exit from root
tb.eof_write_ctrl("exit")
tb.eof_read_end_state_ctrl(1)
tb.end_tc(True)
