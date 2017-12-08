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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_goto_repo_code.py
#
# switch into yocto source tb.config.tc_lab_source_dir + "/repo-" + tb.config.boardlabname
#
# set tb.config.repo_name to "repo-" + tb.config.boardlabname
# and tb.config.repo_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.repo_name
# and set $TBOT_BASEDIR_REPO to tb.config.repo_fulldir_name
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_goto_repo_code_dirext
except:
    tb.config.tc_workfd_goto_repo_code_dirext = ''

try:
    tb.config.tc_workfd_goto_repo_code_checked
except:
    tb.config.tc_workfd_goto_repo_code_checked = False

logging.info("args: %s %s %s", tb.workfd, tb.config.tc_workfd_goto_repo_code_checked, tb.config.tc_workfd_goto_repo_code_dirext)

if tb.config.tc_workfd_goto_repo_code_checked == False:
    # set some global config variables
    try:
        tb.config.repo_name
    except:
        tb.config.repo_name = "repo-" + tb.config.boardlabname + tb.config.tc_workfd_goto_repo_code_dirext

    # first check, that we are in our base dir
    tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")
    tb.config.repo_fulldir_name = "$TBOT_BASEDIR/" + tb.config.repo_name

    tb.event.create_event('main', 'tc_workfd_goto_repo_code.py', 'SET_DOC_FILENAME', 'set_repo_env_var')
    tmp = 'export TBOT_BASEDIR_REPO=' + tb.config.repo_fulldir_name
    tb.write_lx_cmd_check(tb.workfd, tmp)

    tb.event.create_event('main', 'tc_workfd_goto_repo_code.py', 'SET_DOC_FILENAME', 'check_repo_dir_exist')
    tb.config.tc_workfd_check_if_dir_exists_name = '$TBOT_BASEDIR_REPO'
    ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
    if ret == False:
        tb.config.tc_workfd_goto_repo_code_checked = True
        tb.end_tc(False)
 
# cd into repo code
tmp = "cd $TBOT_BASEDIR_REPO"
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
