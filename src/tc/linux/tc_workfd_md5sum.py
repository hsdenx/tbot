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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_md5sum.py
# calculate md5sum of file tb.tc_workfd_md5sum_name , and store it in
# tb.tc_workfd_md5sum_sum
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd.name, tb.tc_workfd_md5sum_name)

c = tb.workfd
cmd = 'md5sum ' + tb.tc_workfd_md5sum_name
tb.eof_write(c, cmd)
searchlist = ["\n"]
tmp = True
tb.tc_workfd_md5sum_sum = 'undef'
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0':
        tmp2 = tb.buf.split(" ")
        tb.tc_workfd_md5sum_sum = tmp2[0]
        tmp = True
    elif ret == 'prompt':
        tmp = False

tb.end_tc(True)
