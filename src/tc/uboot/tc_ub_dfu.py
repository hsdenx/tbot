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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_dfu.py
# test dfu
# - use dfu-util in tb.config.tc_ub_dfu_dfu_util_path
# - upload file tb.config.tc_ub_dfu_dfu_util_alt_setting to
#   tb.config.tc_ub_dfu_dfu_util_downloadfile
# - download it back to the board
# - upload it again
# - and compare the two files
# End:

from tbotlib import tbot

# here starts the real test
logging.info("args: %s %s %s", tb.config.tc_ub_dfu_dfu_util_path,
             tb.config.tc_ub_dfu_dfu_util_alt_setting,
             tb.config.tc_ub_dfu_dfu_util_downloadfile)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# load U-Boot environment variables for tbot
tb.eof_call_tc("tc_ub_load_board_env.py")

c = tb.c_con
# start dfu on the board
tmp = 'dfu 0 nand 0'
tb.eof_write(c, tmp)

# read until 'using id'
ret = tb.tbot_expect_string(c, 'using id')
if ret == 'prompt':
    tb.end_tc(False)

# switch to root
tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_workfd_switch_su.py")

# cd /home/hs/zug/dfu-util/
tb.config.tc_ub_dfu_dfu_util_path = "/home/hs/zug/dfu-util"
tb.config.tc_workfd_cd_name = tb.config.tc_ub_dfu_dfu_util_path
tb.eof_call_tc("tc_workfd_cd_to_dir.py")

# ./src/dfu-util -l
tb.eof_write(tb.workfd, "./src/dfu-util -l")
ret = tb.tbot_expect_string(tb.workfd, 'UNDEFINED')
if ret != 'prompt':
    tb.tbot_expect_prompt(tb.workfd)
    tb.eof_write(tb.workfd, "exit")
    tb.tbot_expect_prompt(tb.workfd)
    tb.end_tc(False)

# upload to lab
# delete tmp file
logging.info("upload file")
tmp = "rm -rf " + tb.config.tc_ub_dfu_dfu_util_downloadfile
tb.write_lx_cmd_check(tb.workfd, tmp)

tmp = "./src/dfu-util -a " + tb.config.tc_ub_dfu_dfu_util_alt_setting + " -U " + tb.config.tc_ub_dfu_dfu_util_downloadfile

tb.eof_write(tb.workfd, tmp)
searchlist = ["Claiming", "Copying data from DFU device to PC", "finished"]
tmp = True
attached = False
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
        attached = True
        tmp = True
    elif ret == 'prompt':
        tmp = False

# on board we see
####
# UPLOAD ... done
tb.tbot_expect_string(c, 'done')

###########################################
# download it back to the board
logging.info("download file")
tmp = "./src/dfu-util -a " + tb.config.tc_ub_dfu_dfu_util_alt_setting + " -D " + tb.config.tc_ub_dfu_dfu_util_downloadfile
tb.eof_write(tb.workfd, tmp)
ret = tb.tbot_expect_string(tb.workfd, 'finished')
if ret == 'prompt':
    tb.eof_write(tb.workfd, "exit")
    tb.tbot_expect_prompt(tb.workfd)
    tb.end_tc(False)
ret = tb.tbot_expect_string(tb.workfd, 'Done')
if ret == 'prompt':
    tb.eof_write(tb.workfd, "exit")
    tb.tbot_expect_prompt(tb.workfd)
    tb.end_tc(False)
tb.tbot_expect_prompt(tb.workfd)

# on board we see
####
# DOWNLOAD ... OK
tb.tbot_expect_string(c, 'OK')

###########################################
# upload to lab again
logging.info("upload file again")
# delete tmp file
tmp = "rm -rf " + tb.config.tc_ub_dfu_dfu_util_downloadfile + ".new"
tb.write_lx_cmd_check(tb.workfd, tmp)

tmp = "./src/dfu-util -a " + tb.config.tc_ub_dfu_dfu_util_alt_setting + " -U " + tb.config.tc_ub_dfu_dfu_util_downloadfile + ".new"
tb.eof_write(tb.workfd, tmp)
ret = tb.tbot_expect_string(tb.workfd, 'Claiming')
if ret == 'prompt':
    tb.eof_write(tb.workfd, "exit")
    tb.tbot_expect_prompt(tb.workfd)
    tb.end_tc(False)
ret = tb.tbot_expect_string(tb.workfd, 'Copying data from DFU device to PC')
if ret == 'prompt':
    tb.eof_write(tb.workfd, "exit")
    tb.tbot_expect_prompt(tb.workfd)
    tb.end_tc(False)
ret = tb.tbot_expect_string(tb.workfd, 'finished')
if ret == 'prompt':
    tb.eof_write(tb.workfd, "exit")
    tb.tbot_expect_prompt(tb.workfd)
    tb.end_tc(False)
tb.tbot_expect_prompt(tb.workfd)

# on board we see
####
# UPLOAD ... done
tb.tbot_expect_string(c, 'done')

#############################
# now diff the files
logging.info("diff files")
tmp = "diff " + tb.config.tc_ub_dfu_dfu_util_downloadfile + " " + tb.config.tc_ub_dfu_dfu_util_downloadfile + ".new"
tb.eof_write(tb.workfd, tmp)
ret = tb.tbot_expect_string(tb.workfd, 'diff')
if ret != 'prompt':
    ret = False
else:
    ret = True

# Ctrl+C on Board to exit ...
tb.send_ctrl_c_con()
tb.tbot_expect_prompt(c)

#############################
# exit from root
tb.eof_write(tb.workfd, "exit")
tb.tbot_expect_prompt(tb.workfd)
tb.end_tc(ret)
