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
# End:

from tbotlib import tbot

logging.info("args: workdfd: %s", tb.workfd.name)

tb.eof_call_tc("tc_workfd_goto_yocto_code.py")
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

val = '$TBOT_BASEDIR_YOCTO/meta-cuby/recipes-extended/images/files/cuby/swu-keys/priv.pem'
tbot_write_val2file(tb, fn, 'SWUPDATE_PRIVATE_KEY', val)
val = '$TBOT_BASEDIR_YOCTO/meta-cuby/recipes-extended/images/files/cuby/swu-keys/passout'
tbot_write_val2file(tb, fn, 'SWUPDATE_PASSWORD_FILE', val)

tb.end_tc(True)
