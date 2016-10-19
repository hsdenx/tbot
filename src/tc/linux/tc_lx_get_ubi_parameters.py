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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_get_ubi_parameters.py
# get ubi parameters of ubi device tb.config.tc_ubi_mtd_dev
# save them into:
# - tb.config.tc_ubi_max_leb_cnt
# - tb.config.tc_ubi_min_io_size
# - tb.config.tc_ubi_leb_size
# End:

from tbotlib import tbot

# here starts the real test
logging.info("args: %s %s %s", tb.config.tc_ubi_cmd_path, tb.config.tc_ubi_mtd_dev, tb.config.tc_ubi_ubi_dev)

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.c_con
def create_ubi_cmd(tb, cmd):
    tmp = tb.config.tc_ubi_cmd_path + '/' + cmd
    return tmp

def get_value(tb, c):
    ret = tb.tbot_expect_string(c, '\n')
    if ret == 'prompt':
        tb.end_tc(False)
    tmp2 = tb.buf.split(":")[1]
    tmp2 = tmp2.strip()
    return tmp2.split(" ")[0]

tmp = create_ubi_cmd(tb, 'ubi-utils/mtdinfo -u ' + tb.config.tc_ubi_mtd_dev)
tb.eof_write(c, tmp)

searchlist = ["Amount of eraseblocks", "Minimum input/output unit size", "error"]
tmp = True
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(c, searchlist)
    if ret == '0':
        tb.config.tc_ubi_max_leb_cnt = get_value(tb, c)
        tmp = True
    elif ret == '1':
        tb.config.tc_ubi_min_io_size = get_value(tb, c)
        tmp = True
    elif ret == '2':
        tb.tbot_expect_prompt(c)
        tb.end_tc(False)
    elif ret == 'prompt':
        tmp = False

logging.info("max leb %s", tb.config.tc_ubi_max_leb_cnt)
logging.info("min io size %s", tb.config.tc_ubi_min_io_size)

tmp = create_ubi_cmd(tb, 'ubi-utils/ubinfo ' + tb.config.tc_ubi_ubi_dev)
tb.eof_write(c, tmp)
ret = tb.tbot_expect_string(c, 'Logical eraseblock size')
if ret == 'prompt':
    tb.end_tc(False)

tb.config.tc_ubi_leb_size = get_value(tb, c)

logging.info("leb size %s", tb.config.tc_ubi_leb_size)

tb.tbot_expect_prompt(c)
tb.end_tc(True)
