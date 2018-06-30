# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_md5sum.py
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
