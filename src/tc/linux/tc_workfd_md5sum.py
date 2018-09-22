# SPDX-License-Identifier: GPL-2.0
#
# Description:
# calculate md5sum of file tb.config.tc_workfd_md5sum_name , and store it in
# tb.tc_workfd_md5sum_sum
#
# used variables
#
# - tb.config.tc_workfd_md5sum_name
#| path with filename, for which md5sum gets calculated
#| default:
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_md5sum_name', '')
logging.info("args: %s", tb.config.tc_workfd_md5sum_name)

c = tb.workfd
cmd = 'md5sum ' + tb.config.tc_workfd_md5sum_name
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
