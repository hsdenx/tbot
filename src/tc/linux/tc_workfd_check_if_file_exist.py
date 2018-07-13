# SPDX-License-Identifier: GPL-2.0
#
# Description:
# check if a file in tbot workdir exist
#
# used variables
#
# - tb.config.tc_workfd_check_if_file_exists_name
#| filename
#| default: 'bonnie++-1.03e.tgz'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_check_if_file_exists_name', 'bonnie++-1.03e.tgz')
logging.info("args: workfd %s", tb.workfd.name)

tmp = 'test -r ' + tb.config.tc_workfd_check_if_file_exists_name
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.end_tc(True)
