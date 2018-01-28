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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_yocto_patch_site.py
#
# patch / create site.conf
#
# add SWUPDATE_PRIVATE_KEY if tb.config.tc_workfd_yocto_patch_site_swu_priv_key
#  != 'none'
# add SWUPDATE_PASSWORD_FILE if tb.config.tc_workfd_yocto_patch_site_swu_priv_passout
#  != 'none'
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_yocto_patch_site_swu_priv_key
except:
    tb.config.tc_workfd_yocto_patch_site_swu_priv_key = 'none'

try:
    tb.config.tc_workfd_yocto_patch_site_swu_priv_passout
except:
    tb.config.tc_workfd_yocto_patch_site_swu_priv_passout = 'none'

logging.info("args: workdfd: %s", tb.workfd.name)

tb.eof_call_tc("tc_workfd_goto_yocto_code.py")
tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ', 'repo_create_site.conf')
p = '$TBOT_BASEDIR_YOCTO/build'
tb.config.tc_workfd_check_if_dir_exists_name = p
tb.eof_call_tc("tc_workfd_check_if_dir_exist.py")

fn = p + '/conf/site.conf'
tb.config.tc_workfd_check_if_file_exists_name = fn
ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
if ret == False:
    cmd = 'echo SCONF_VERSION = \\"1\\" > ' + fn
    tb.write_lx_cmd_check(tb.workfd, cmd)
    cmd = 'echo  >> ' + fn
    tb.write_lx_cmd_check(tb.workfd, cmd)

def tbot_write_val2file(tb, filen, key, value):
    tb.tc_workfd_grep_file = filen
    tb.tc_workfd_grep_string = key
    ret = tb.call_tc("tc_workfd_grep.py")
    if ret == True:
        return
    cmd = 'echo  ' + key + ' = \\"' + value + '\\" >> ' + filen
    tb.write_lx_cmd_check(tb.workfd, cmd)

if tb.config.tc_workfd_yocto_patch_site_swu_priv_key != 'none':
    val = tb.config.tc_workfd_yocto_patch_site_swu_priv_key
    tbot_write_val2file(tb, fn, 'SWUPDATE_PRIVATE_KEY', val)
if tb.config.tc_workfd_yocto_patch_site_swu_priv_passout != 'none':
    val = tb.config.tc_workfd_yocto_patch_site_swu_priv_passout
    tbot_write_val2file(tb, fn, 'SWUPDATE_PASSWORD_FILE', val)

tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ_END', 'repo_create_site.conf')

tb.end_tc(True)
