# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_if_dir_exist.py
# check if a dir in tbot workdir exist
# this tc returns always true, but sets
# tb.config.tc_return True or False, because we may not
# want to end testcase failed, if dir not exists.
#
# if tb.config.tc_workfd_check_if_dir_exists_create != 'no'
# create the directory.
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_check_if_dir_exists_create
except:
    tb.config.tc_workfd_check_if_dir_exists_create = 'no'

logging.info("args: workfd %s %s", tb.workfd, tb.config.tc_workfd_check_if_dir_exists_name)

tmp = 'test -d ' + tb.config.tc_workfd_check_if_dir_exists_name
ret = tb.write_lx_cmd_check(tb.workfd, tmp, endTC=False)
if ret == True:
    tb.end_tc(True)

if tb.config.tc_workfd_check_if_dir_exists_create == 'no':
    tb.end_tc(False)

cmd = 'mkdir -p ' + tb.config.tc_workfd_check_if_dir_exists_name
tb.write_lx_cmd_check(tb.workfd, cmd)
tb.end_tc(True)
