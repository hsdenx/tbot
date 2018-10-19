# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# patch / create site.conf
#
# used variables:
#
# - tb.config.tc_workfd_yocto_patch_site_path_default_file
#| if != 'none' use this file as default
#| default: 'none'
#
# - tb.config.tc_workfd_yocto_patch_site_swu_priv_key
#| if != 'none' add SWUPDATE_PRIVATE_KEY if tb.config.tc_workfd_yocto_patch_site_swu_priv_key
#| default: 'none'
#
# - tb.config.tc_workfd_yocto_patch_site_swu_priv_passout
#| if != 'none'
#| add SWUPDATE_PASSWORD_FILE if tb.config.tc_workfd_yocto_patch_site_swu_priv_passout
# -
#| if != 'none'
#| add SWUPDATE_PUBLIC_KEY if tb.config.tc_workfd_yocto_patch_site_swu_pub_key
#| default: 'none'
#
# - tb.config.tc_workfd_yocto_patch_site_ub_key
#| if != 'none'
#| add UB_KEY_PATH if tb.config.tc_workfd_yocto_patch_site_ub_key
#| default: 'none'
#
# - tb.config.tc_workfd_yocto_patch_site_dl_dir
#| if != 'none'
#| add DL_DIR if tb.config.tc_workfd_yocto_patch_site_dl_dir
#| default: 'none'
#
# - tb.config.tc_workfd_yocto_patch_site_sstate_dir
#| if != 'none'
#| add SSTATE_DIR if tb.config.tc_workfd_yocto_patch_site_sstate_dir
#| default: 'none'
#
# - tb.config.tc_workfd_yocto_patch_site_src_linux_stable
#| if != 'none'
#| add SRC_LINUX_STABLE if tb.config.tc_workfd_yocto_patch_site_src_linux_stable
#| default: 'none'
#
# - tb.config.tc_workfd_yocto_patch_site_premirrors
#| if != 'none'
#| add PREMIRRORS_prepend if tb.config.tc_workfd_yocto_patch_site_premirrors
#| default: 'none'
#
# - tb.config.tc_workfd_yocto_patch_site_key_dir
#| if != 'none'
#| add KEY_DIR if tb.config.tc_workfd_yocto_patch_site_key_dir
#| default: 'none'
#
# - tb.config.tc_workfd_yocto_patch_site_key_desc
#| if != 'none'
#| add KEY_DESC if tb.config.tc_workfd_yocto_patch_site_key_desc
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_yocto_patch_site_path_default_file', 'none')
tb.define_variable('tc_workfd_yocto_patch_site_swu_priv_key', 'none')
tb.define_variable('tc_workfd_yocto_patch_site_swu_priv_passout', 'none')
tb.define_variable('tc_workfd_yocto_patch_site_swu_pub_key', 'none')
tb.define_variable('tc_workfd_yocto_patch_site_dl_dir', 'none')
tb.define_variable('tc_workfd_yocto_patch_site_sstate_dir', 'none')
tb.define_variable('tc_workfd_yocto_patch_site_src_linux_stable', 'none')
tb.define_variable('tc_workfd_yocto_patch_site_premirrors', 'none')
tb.define_variable('tc_workfd_yocto_patch_site_ub_key', 'none')
tb.define_variable('tc_workfd_yocto_patch_site_key_dir', 'none')
tb.define_variable('tc_workfd_yocto_patch_site_key_desc', 'none')
tb.define_variable('builddir', '$TBOT_BASEDIR_YOCTO/build/')

tb.eof_call_tc("tc_workfd_goto_yocto_code.py")
tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ', 'repo_create_site.conf')
p = tb.config.builddir
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
    tb.config.tc_workfd_grep_file = filen
    tb.config.tc_workfd_grep_string = key
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
if tb.config.tc_workfd_yocto_patch_site_swu_pub_key != 'none':
    val = tb.config.tc_workfd_yocto_patch_site_swu_pub_key
    tbot_write_val2file(tb, fn, 'SWUPDATE_PUBLIC_KEY', val)
if tb.config.tc_workfd_yocto_patch_site_dl_dir != 'none':
    val = tb.config.tc_workfd_yocto_patch_site_dl_dir
    tbot_write_val2file(tb, fn, 'DL_DIR', val)
if tb.config.tc_workfd_yocto_patch_site_sstate_dir != 'none':
    val = tb.config.tc_workfd_yocto_patch_site_sstate_dir
    tbot_write_val2file(tb, fn, 'SSTATE_DIR', val)
if tb.config.tc_workfd_yocto_patch_site_src_linux_stable != 'none':
    val = tb.config.tc_workfd_yocto_patch_site_src_linux_stable
    tbot_write_val2file(tb, fn, 'SRC_LINUX_STABLE', val)
if tb.config.tc_workfd_yocto_patch_site_ub_key != 'none':
    val = tb.config.tc_workfd_yocto_patch_site_ub_key
    tbot_write_val2file(tb, fn, 'UB_KEY_PATH', val)
if tb.config.tc_workfd_yocto_patch_site_key_dir != 'none':
    val = tb.config.tc_workfd_yocto_patch_site_key_dir
    tbot_write_val2file(tb, fn, 'KEY_DIR', val)
if tb.config.tc_workfd_yocto_patch_site_key_desc != 'none':
    val = tb.config.tc_workfd_yocto_patch_site_key_desc
    tbot_write_val2file(tb, fn, 'KEY_DESC', val)

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
