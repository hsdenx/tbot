# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_list_of_files_in_dir.py
# get a list of files from directory tb.tc_workfd_get_list_of_files_dir
# tb.config.tc_workfd_get_list_of_files_mask
# End:

from tbotlib import tbot

logging.info("args: workfd: %s %s %s", tb.workfd, tb.tc_workfd_get_list_of_files_dir,
             tb.config.tc_workfd_get_list_of_files_mask)

c = tb.c_con
tb.buf = c.get_log()

tb.list_of_files = []

tb.eof_write(tb.workfd, 'find ' + tb.tc_workfd_get_list_of_files_dir +
             ' -name  "' + tb.config.tc_workfd_get_list_of_files_mask + '"' +
             ' | sort')

tb.tbot_expect_prompt(tb.workfd)

tmp = tb.buf.lstrip('\r\n')
tmp = tmp.split('\r\n')
for line in tmp:
    tb.list_of_files.append(line)

tb.list_of_files.pop()
tb.end_tc(True)
