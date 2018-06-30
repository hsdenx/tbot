# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_if_file_exist.py
# check if a file in tbot workdir exist
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd.name, tb.config.tc_workfd_check_if_file_exists_name)

tmp = 'test -r ' + tb.config.tc_workfd_check_if_file_exists_name
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.end_tc(True)
