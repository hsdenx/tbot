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
