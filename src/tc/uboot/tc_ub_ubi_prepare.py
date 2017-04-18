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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_prepare.py
# - ubi prepare
#   execute "ubi part" ith tb.config.tc_ub_ubi_prep_partname
#   if tb.config.tc_ub_ubi_prep_offset != 'none'
#   with offset tb.config.tc_ub_ubi_prep_offset
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.config.tc_ub_ubi_prep_partname, tb.config.tc_ub_ubi_prep_offset)

# set board state for which the tc is valid
tb.set_board_state("u-boot")

# load ub tbot environment
tb.eof_call_tc("tc_ub_load_board_env.py")

c = tb.c_con
# "ubi part" if yes -> call ubi detach
tmp = "if ubi part; then; echo OK; else; echo FAIL; fi"
tb.eof_write(c, tmp)
searchlist = ["OK"]
tmp = True
attached = False
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == 0:
        attached = True
    elif ret == 'prompt':
        tmp = False

if attached == True:
    tb.eof_write(c, "ubi detach")
    tb.tbot_expect_prompt(c)

tmp = "ubi part " + tb.config.tc_ub_ubi_prep_partname
if tb.config.tc_ub_ubi_prep_offset != 'none':
    tmp += " " + tb.config.tc_ub_ubi_prep_offset

def ubiprep(tb, tmp):
    tb.eof_write(tb.c_con, tmp)

    searchlist = ["init error", "available PEBs", "empty MTD device detected"]
    tmp = True
    cmd_ok = False
    while tmp:
        ret = tb.tbot_rup_and_check_strings(tb.c_con, searchlist)
        if ret == '1':
            cmd_ok = True
        elif ret == 'prompt':
            tmp = False

    if cmd_ok == False:
        tb.end_tc(False)
    return cmd_ok

# we have two execute ubi part more than once,
# -> ubi fastmap gets written ...
# This is currently a bug in U-Boot ...
cmd_ok = ubiprep(tb, tmp)
# detach it
tb.eof_write(c, "ubi detach")
tb.tbot_expect_prompt(c)
cmd_ok = ubiprep(tb, tmp)
# detach it
tb.eof_write(c, "ubi detach")
tb.tbot_expect_prompt(c)
cmd_ok = ubiprep(tb, tmp)

# clear ubi part from uboot cmd buffer
tb.eof_write(c, "ubi info")
tb.tbot_expect_prompt(c)

if cmd_ok == False:
    tb.end_tc(False)

tb.end_tc(True)
