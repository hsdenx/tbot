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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_goto_linux_code.py
# switch into linux source tb.config.tc_lab_source_dir + "/linux-" + tb.config.boardlabname
# set tb.config.linux_name to "linux-" + tb.config.boardlabname
# and tb.config.linux_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.linux_name
# and set $TBOT_BASEDIR_LINUX to tb.config.linux_fulldir_name
# End:

from tbotlib import tbot

logging.info("args: %s", tb.workfd)

try:
    tb.workfd.tc_workfd_goto_linux_code_checked
except:
    tb.workfd.tc_workfd_goto_linux_code_checked = False

if tb.workfd.tc_workfd_goto_linux_code_checked == False:
    # set some global config variables
    tb.config.linux_name = "linux-" + tb.config.boardlabname
    tb.config.linux_fulldir_name = "$TBOT_BASEDIR/" + tb.config.linux_name

    tmp = 'export TBOT_BASEDIR_LINUX=' + tb.config.linux_fulldir_name
    tb.write_lx_cmd_check(tb.workfd, tmp)

    tb.config.tc_workfd_check_if_dir_exists_name = '$TBOT_BASEDIR_LINUX'
    ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
    if ret == False:
        tb.workfd.tc_workfd_goto_linux_code_checked = True
        tb.end_tc(False)

tmp = "cd $TBOT_BASEDIR_LINUX"
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
