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
# if tb.config.tc_workfd_yocto_patch_site_path_default_file != 'none'
# use this file as default
#
# add SWUPDATE_PRIVATE_KEY if tb.config.tc_workfd_yocto_patch_site_swu_priv_key
#  != 'none'
# add SWUPDATE_PASSWORD_FILE if tb.config.tc_workfd_yocto_patch_site_swu_priv_passout
#  != 'none'
# add DL_DIR if tb.config.tc_workfd_yocto_patch_site_dl_dir != 'none'
# add SSTATE_DIR if tb.config.tc_workfd_yocto_patch_site_sstate_dir != 'none'
# add SRC_LINUX_STABLE if tb.config.tc_workfd_yocto_patch_site_src_linux_stable != 'none'
# add PREMIRRORS_prepend if tb.config.tc_workfd_yocto_patch_site_premirrors != 'none'
# End:

from tbotlib import tbot

try:
    tb.config.tc_workfd_yocto_patch_site_path_default_file
except:
    tb.config.tc_workfd_yocto_patch_site_path_default_file = 'none'

try:
    tb.config.tc_workfd_yocto_patch_site_swu_priv_key
except:
    tb.config.tc_workfd_yocto_patch_site_swu_priv_key = 'none'

try:
    tb.config.tc_workfd_yocto_patch_site_swu_priv_passout
except:
    tb.config.tc_workfd_yocto_patch_site_swu_priv_passout = 'none'

try:
    tb.config.tc_workfd_yocto_patch_site_dl_dir
except:
    tb.config.tc_workfd_yocto_patch_site_dl_dir = 'none'

try:
    tb.config.tc_workfd_yocto_patch_site_sstate_dir
except:
    tb.config.tc_workfd_yocto_patch_site_sstate_dir = 'none'

try:
    tb.config.tc_workfd_yocto_patch_site_src_linux_stable
except:
    tb.config.tc_workfd_yocto_patch_site_src_linux_stable = 'none'

try:
    tb.config.tc_workfd_yocto_patch_site_premirrors
except:
    tb.config.tc_workfd_yocto_patch_site_premirrors = 'none'

logging.info("args: workdfd: %s", tb.workfd.name)
logging.info("args: default filepath: %s", tb.config.tc_workfd_yocto_patch_site_path_default_file)

tb.eof_call_tc("tc_workfd_goto_yocto_code.py")
tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ', 'repo_create_site.conf')
p = '$TBOT_BASEDIR_YOCTO/build'
tb.config.tc_workfd_check_if_dir_exists_name = p
tb.eof_call_tc("tc_workfd_check_if_dir_exist.py")

fn = p + '/conf/site.conf'
tb.config.tc_workfd_check_if_file_exists_name = fn
ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
if ret == False:
    if tb.config.tc_workfd_yocto_patch_site_path_default_file == 'none':
        cmd = 'echo SCONF_VERSION = \\"1\\" > ' + fn
        tb.write_lx_cmd_check(tb.workfd, cmd)
        cmd = 'echo  >> ' + fn
        tb.write_lx_cmd_check(tb.workfd, cmd)
    else:
        s = tb.config.tc_workfd_yocto_patch_site_path_default_file
        cmd = 'cp ' + s + ' ' + fn
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
if tb.config.tc_workfd_yocto_patch_site_dl_dir != 'none':
    val = tb.config.tc_workfd_yocto_patch_site_dl_dir
    tbot_write_val2file(tb, fn, 'DL_DIR', val)
if tb.config.tc_workfd_yocto_patch_site_sstate_dir != 'none':
    val = tb.config.tc_workfd_yocto_patch_site_sstate_dir
    tbot_write_val2file(tb, fn, 'SSTATE_DIR', val)
if tb.config.tc_workfd_yocto_patch_site_src_linux_stable != 'none':
    val = tb.config.tc_workfd_yocto_patch_site_src_linux_stable
    tbot_write_val2file(tb, fn, 'SRC_LINUX_STABLE', val)

if tb.config.tc_workfd_yocto_patch_site_premirrors != 'none':
    cmd = 'echo PREMIRRORS_prepend = \\"\\\  >> ' + fn
    tb.write_lx_cmd_check(tb.workfd, cmd)
    # write values
    tb.workfd.lab_write("cat >> " + fn + " << EOF")
    for l in tb.config.tc_workfd_yocto_patch_site_premirrors:
        tb.workfd.lab_write(l)

    tb.workfd.lab_write("EOF")
    tb.tbot_expect_prompt(tb.workfd)

    cmd = 'echo \\"  >> ' + fn
    tb.write_lx_cmd_check(tb.workfd, cmd)

tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ_END', 'repo_create_site.conf')

tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ', 'repo_dump_site.conf')
tb.write_lx_cmd_check(tb.workfd, "cat " + fn)
tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ_END', 'repo_dump_site.conf')

tb.end_tc(True)
