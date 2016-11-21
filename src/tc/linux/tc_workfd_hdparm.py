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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_hdparm.py
# make a minimal hdparm check
# call hdparm -t tb.config.tc_workfd_hdparm_dev
# and check if read speed is greater than tb.config.tc_workfd_hdparm_min
# It is possible to add a PATH tb.config.tc_workfd_hdparm_path
# where hdparm is installed
# Testcase fails if readen speed is <= tb.config.tc_workfd_hdparm_min
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s %s", tb.config.tc_workfd_hdparm_path, tb.config.tc_workfd_hdparm_dev, tb.config.tc_workfd_hdparm_min)

tb.set_board_state("linux")

c = tb.c_con
tmp = ''
if tb.config.tc_workfd_hdparm_path != 'none':
    tmp = tb.config.tc_workfd_hdparm_path

cmd = tmp + 'hdparm -t ' + tb.config.tc_workfd_hdparm_dev

tb.eof_write(c, cmd)
searchlist = ["MB/sec"]
tmp = True
result = False
while tmp == True:
    ret = tb.tbot_read_line_and_check_strings(c, searchlist)
    if ret == '0':
        # extract value from line
        str1 = tb.buf.split('=')
        str1 = str1[1].strip(' ')
        str1 = str1.split(' ')
        val = float(str1[0])
        # check if value is greater then expected minimum
        if val > float(tb.config.tc_workfd_hdparm_min):
            logging.info("value %s > %s -> OK", str1[0], tb.config.tc_workfd_hdparm_min)
            result = True
        else:
            logging.error("value %s <= %s", str1[0], tb.config.tc_workfd_hdparm_min)
    elif ret == 'prompt':
        tmp = False

if result != True:
    tb.end_tc(False)
tb.end_tc(True)
