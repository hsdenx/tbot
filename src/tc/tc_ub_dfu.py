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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_dfu.py
# test dfu
# 
from tbotlib import tbot

#here starts the real test
logging.info("args: %s %s %s", tb.tc_ub_dfu_dfu_util_path, tb.tc_ub_dfu_dfu_util_alt_setting, tb.tc_ub_dfu_dfu_util_downloadfile)

#set board state for which the tc is valid
tb.set_board_state("u-boot")

# load U-Boot environment variables for tbot
tb.eof_call_tc("tc_ub_load_board_env.py")

#start dfu on the board
tmp = 'dfu 0 nand 0'
tb.eof_write_con(tmp)

#read until 'using id'
ret = True
while ret == True:
    ret = tb.search_str_in_readline_con("using id")
    if ret == False:
        tb.end_tc(False)

#auf pollux
#switch to root
tb.eof_write_ctrl("su")
tb.eof_search_str_in_readline_ctrl("Password")
tb.eof_write_ctrl_passwd("root", "lab")
#tb.eof_write_ctrl("PS1=ttbott #")

#cd /home/hs/zug/dfu-util/
tb.tc_ub_dfu_dfu_util_path = "/home/hs/zug/dfu-util"
tmp = "cd " + tb.tc_ub_dfu_dfu_util_path
tb.eof_write_ctrl(tmp)
tb.eof_read_end_state_ctrl(1)
tb.eof_write_ctrl("pwd")
tb.eof_search_str_in_readline_ctrl(tb.tc_ub_dfu_dfu_util_path)
tb.eof_read_end_state_ctrl(1)
#./src/dfu-util -l
tb.eof_write_ctrl("./src/dfu-util -l")
ret = tb.search_str_in_readline_ctrl("UNDEFINED")
if ret == True:
    tb.end_tc(False)

#upload to lab
#delete tmp file
logging.info("upload file")
tmp = "rm -rf " + tb.tc_ub_dfu_dfu_util_downloadfile
tb.eof_write_ctrl(tmp)
tb.eof_read_end_state_ctrl(1)

tmp = "./src/dfu-util -a " + tb.tc_ub_dfu_dfu_util_alt_setting + " -U " + tb.tc_ub_dfu_dfu_util_downloadfile
tb.eof_write_ctrl(tmp)
searchlist = ["Claiming", "Copying data from DFU device to PC", "finished"]
tmp = True
attached = False
while tmp == True:
    tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
    if tmp == 0:
        attached = True
        tmp = True
    elif tmp == 'prompt':
        tmp = False


tb.eof_search_str_in_readline_ctrl("Claiming")
tb.eof_search_str_in_readline_ctrl("Copying data from DFU device to PC")
tb.eof_search_str_in_readline_ctrl("finished")
tb.eof_read_end_state_ctrl(1)

#on board we see
####
#UPLOAD ... done
tb.eof_search_str_in_readline_con("done")

###########################################
#download it back to the board
logging.info("download file")
tmp = "./src/dfu-util -a " + tb.tc_ub_dfu_dfu_util_alt_setting + " -D " + tb.tc_ub_dfu_dfu_util_downloadfile
tb.eof_write_ctrl(tmp)
tb.eof_search_str_in_readline_ctrl("finished")
tb.eof_search_str_in_readline_ctrl("Done!")
tb.eof_read_end_state_ctrl(1)

#on board we see
####
#DOWNLOAD ... OK
tb.eof_search_str_in_readline_con("OK")

###########################################
#upload to lab again
logging.info("upload file again")
#delete tmp file
tmp = "rm -rf " + tb.tc_ub_dfu_dfu_util_downloadfile + ".new"
tb.eof_write_ctrl(tmp)
tb.eof_read_end_state_ctrl(1)

tmp = "./src/dfu-util -a " + tb.tc_ub_dfu_dfu_util_alt_setting + " -U " + tb.tc_ub_dfu_dfu_util_downloadfile + ".new"
tb.eof_write_ctrl(tmp)
tb.eof_search_str_in_readline_ctrl("Claiming")
tb.eof_search_str_in_readline_ctrl("Copying data from DFU device to PC")
tb.eof_search_str_in_readline_ctrl("finished")
tb.eof_read_end_state_ctrl(1)

#on board we see
####
#UPLOAD ... done
tb.eof_search_str_in_readline_con("done")

#############################
#now diff the files
logging.info("diff files")
tmp = "diff " + tb.tc_ub_dfu_dfu_util_downloadfile + " " + tb.tc_ub_dfu_dfu_util_downloadfile + ".new"
tb.eof_write_ctrl(tmp)
ret = tb.search_str_in_readline_ctrl("diff")
tb.eof_read_end_state_ctrl(1)
if ret == True:
    tb.end_tc(False)

#Ctrl+C on Board to exit ...
tb.send_ctrl_c_con()
tb.eof_read_end_state_con(2)

#############################
# exit from root
tb.eof_write_ctrl("exit")
tb.eof_read_end_state_ctrl(1)
tb.end_tc(True)
