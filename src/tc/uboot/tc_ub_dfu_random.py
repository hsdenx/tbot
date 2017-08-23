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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_dfu_random.py
# test a U-Boot dfu alt setting tb.config.tc_ub_dfu_dfu_util_alt_setting
# Therefore write a random file with size tb.config.tc_ub_dfu_rand_size
# to it, reread it and compare it. TC fails if files differ
# (If readen file is longer, this is no error!)
#
# If dfu-util is not installed on the lab PC, set
# tb.config.tc_ub_dfu_dfu_util_ssh for connecting with ssh to a PC
# which have it installed, and a USB cable connected to the board.
# Set tb.config.tc_ub_dfu_dfu_util_path to the path of dfu-util, if
# you have a self compiled version of it.
# Set tb.config.tc_ub_dfu_rand_ubcmd for the executed command on
# U-Boot shell for getting into DFU mode
# End:

from tbotlib import tbot

# here starts the real test
logging.info("args: %s %s %s %s %s", tb.config.tc_ub_dfu_dfu_util_path,
	tb.config.tc_ub_dfu_dfu_util_ssh, tb.config.tc_ub_dfu_dfu_util_alt_setting,
	tb.config.tc_ub_dfu_rand_size, tb.config.tc_ub_dfu_rand_ubcmd)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

def dfu_check_one(tb, ctrl, string):
    ret = tb.tbot_expect_string(ctrl, string)
    if ret == 'prompt':
        tb.send_ctrl_c_con()
        tb.tb_expect_prompt(tb.c_con)
        tb.eof_write(ctrl, 'exit')
        tb.tb_expect_prompt(ctrl)
        tb.end_tc(False)

# load U-Boot environment variables for tbot
tb.eof_call_tc("tc_ub_load_board_env.py")

c = tb.c_con
# print some U-Boot variables
tb.eof_write_cmd(c, "mtdparts")
tb.eof_write_cmd(c, "printenv dfu_alt_info")

# start dfu on the board
tb.eof_write(c, tb.config.tc_ub_dfu_rand_ubcmd)

# read until 'using id'
#ret = tb.tbot_expect_string(c, 'using id')
#if ret == 'prompt':
#    tb.end_tc(False)
    
tb.workfd = tb.c_ctrl
ctrl = tb.workfd
if tb.config.tc_ub_dfu_dfu_util_ssh != "none":
    tb.workfd_ssh_cmd = tb.config.tc_ub_dfu_dfu_util_ssh
    tb.config.workfd_ssh_cmd_prompt = '#'
    tb.eof_call_tc("tc_workfd_ssh.py")

if tb.config.tc_ub_dfu_dfu_util_path != 'none':
    # cd into dfu-util source
    tmp = "cd " + tb.config.tc_ub_dfu_dfu_util_path
    dfu_cmd = './src/dfu-util'
else:
    dfu_cmd = 'dfu-util'

tb.eof_write_cmd(ctrl, "pwd")

# List currently attached DFU capable devices
tb.eof_write(ctrl, dfu_cmd + " -l")
ret = tb.tbot_expect_string(ctrl, 'UNDEFINED')
if ret != 'prompt':
    tb.end_tc(False)

# create random file
tb.tc_workfd_generate_random_file_name = tb.config.lab_tmp_dir + 'random'
tb.tc_workfd_generate_random_file_length = tb.config.tc_ub_dfu_rand_size
tb.eof_call_tc("tc_workfd_generate_random_file.py");

###########################################
# download it to the board
logging.info("download file")
tmp = dfu_cmd + " -a " + tb.config.tc_ub_dfu_dfu_util_alt_setting + " -D " + tb.tc_workfd_generate_random_file_name
tb.eof_write(ctrl, tmp)

dfu_check_one(tb, ctrl, 'Claiming')
dfu_check_one(tb, ctrl, 'Copying data from PC to DFU device')
dfu_check_one(tb, ctrl, 'state(7) = dfuMANIFEST, status(0) = No error condition is present')
dfu_check_one(tb, ctrl, 'state(2) = dfuIDLE, status(0) = No error condition is present')
dfu_check_one(tb, ctrl, 'Done')
tb.tbot_expect_prompt(ctrl)

# on board we should see
####
# DOWNLOAD ... OK
ret = tb.tbot_expect_string(c, 'OK')
if ret == 'prompt':
    tb.eof_write(ctrl, 'exit')
    tb.tbot_expect_prompt(ctrl)
    tb.end_tc(False)

ret = tb.eof_write_cmd(ctrl, 'rm -f ' + tb.config.lab_tmp_dir + 'gnlmpf')
# upload it back
tmp = dfu_cmd + " -a " + tb.config.tc_ub_dfu_dfu_util_alt_setting + " -U " + tb.config.lab_tmp_dir + 'gnlmpf'
tb.eof_write(ctrl, tmp)

dfu_check_one(tb, ctrl, 'Claiming')
dfu_check_one(tb, ctrl, 'Copying data from DFU device to PC')
dfu_check_one(tb, ctrl, 'Upload done')
tb.tbot_expect_prompt(ctrl)

# on board we see
####
# UPLOAD ... done
ret = tb.tbot_expect_string(c, 'done')
if ret == 'prompt':
    tb.eof_write(ctrl, 'exit')
    tb.tbot_expect_prompt(ctrl)
    tb.end_tc(False)

# Ctrl+C on Board to exit ...
tb.send_ctrl_c_con()
tb.tbot_expect_prompt(c)

#############################
# now diff the files
logging.info("diff files")
tmp = "cmp " + tb.tc_workfd_generate_random_file_name + " " + tb.config.lab_tmp_dir + "gnlmpf"
tb.eof_write(ctrl, tmp)
searchlist = ["EOF", "differ"]
tmp = True
differ = False
differ_at_end = False
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(ctrl, searchlist)
    if ret == '0':
        differ_at_end = True
    if ret == '1':
        differ = True
    elif ret == 'prompt':
        tmp = False

if differ and not differ_at_end:
    tb.end_tc(False)

tb.eof_write_cmd(tb.workfd, "rm -f " + tb.config.lab_tmp_dir + "gnlmpf")
tb.eof_write_cmd(tb.workfd, "rm -f " + tb.config.lab_tmp_dir + "random")

#############################
# exit from root
tb.eof_write(ctrl, "exit")
tb.tbot_expect_prompt(ctrl)
tb.end_tc(True)
