# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get a list of files from directory tb.config.tc_workfd_get_list_of_files_dir
# tb.config.tc_workfd_get_list_of_files_mask
#
# used variables
#
# - tb.config.tc_workfd_get_list_of_files_dir
#| directory in which files get searched
#| default: ''
#
# - tb.config.tc_workfd_get_list_of_files_mask
#| find expression
#| default: '*'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_get_list_of_files_dir', '')
tb.define_variable('tc_workfd_get_list_of_files_mask', '*')
logging.info("args: workfd: %s", tb.workfd)

c = tb.c_con
tb.buf = c.get_log()

tb.list_of_files = []

tb.eof_write(tb.workfd, 'find ' + tb.config.tc_workfd_get_list_of_files_dir +
             ' -name  "' + tb.config.tc_workfd_get_list_of_files_mask + '"' +
             ' | sort')

tb.tbot_expect_prompt(tb.workfd)

tmp = tb.buf.lstrip('\r\n')
tmp = tmp.split('\r\n')
for line in tmp:
    tb.list_of_files.append(line)

tb.list_of_files.pop()
tb.end_tc(True)
