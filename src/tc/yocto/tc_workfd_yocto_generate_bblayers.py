# SPDX-License-Identifier: GPL-2.0
#
# Description:
# create bblayer.conf file
# 
# used variables
#
# - tb.config.tc_workfd_yocto_generate_bblayers_openembedded_layers
#| used meta layers from meta-openembedded
#| default: "['meta-networking']"
#
# - tb.config.tc_workfd_yocto_generate_bblayers_xenomai_layers
#| used meta layers from meta-xenomai
#| default: '[]'
#
# End:

tb.define_variable('tc_workfd_yocto_generate_bblayers_openembedded_layers', "['meta-networking']")
tb.define_variable('tc_workfd_yocto_generate_bblayers_xenomai_layers', "[]")

from tbotlib import tbot

tb.eof_call_tc("tc_workfd_goto_yocto_code.py")
tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ', 'repo_create_bblayers.conf')
p = '$TBOT_BASEDIR_YOCTO/build'
tb.config.tc_workfd_check_if_dir_exists_name = p
tb.eof_call_tc("tc_workfd_check_if_dir_exist.py")

fn = p + '/conf/bblayers.conf'
tb.config.tc_workfd_check_if_file_exists_name = fn
ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
if ret == True:
    # if it exists, dump only
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ', 'repo_dump_bblayers.conf')
    tb.write_lx_cmd_check(tb.workfd, "cat " + fn)
    tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ_END', 'repo_dump_bblayers.conf')
    tb.end_tc(True)

tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ', 'repo_create_bblayers.conf')
# create header
cmd = 'echo "# POKY_BBLAYERS_CONF_VERSION is increased each time build/conf/bblayers.conf" > ' + fn
tb.write_lx_cmd_check(tb.workfd, cmd)
cmd = 'echo "# changes incompatibly" >> ' + fn
tb.write_lx_cmd_check(tb.workfd, cmd)
cmd = 'echo POKY_BBLAYERS_CONF_VERSION = \\"2\\" >> ' + fn
tb.write_lx_cmd_check(tb.workfd, cmd)
cmd = 'echo BBPATH = \\"\\${TOPDIR}\\" >> ' + fn
tb.write_lx_cmd_check(tb.workfd, cmd)
cmd = 'echo BBFILES ?= \\"\\" >> ' + fn
tb.write_lx_cmd_check(tb.workfd, cmd)
cmd = 'echo BBLAYERS ?= \\" \\\ >> ' + fn
tb.write_lx_cmd_check(tb.workfd, cmd)

def tbot_write_layerpath(tb, filen, layer):
    cmd = 'echo $TBOT_BASEDIR_YOCTO/' + layer + ' \\\ >> ' + filen
    tb.write_lx_cmd_check(tb.workfd, cmd)

std_layers = [
	'meta',
	'meta-poky',
	'meta-yocto-bsp'
]
for l in std_layers:
    tbot_write_layerpath(tb, fn, l)

for m in tb.config.tc_workfd_get_yocto_source_layers:
    l = m[7]
    if l == 'meta-openembedded':
        for s in tb.config.tc_workfd_yocto_generate_bblayers_openembedded_layers:
            tbot_write_layerpath(tb, fn, l + '/' + s)
    elif l == 'meta-xenomai':
        for s in tb.config.tc_workfd_yocto_generate_bblayers_xenomai_layers:
            tbot_write_layerpath(tb, fn, l + '/' + s)
    else:
        tbot_write_layerpath(tb, fn, l)
cmd = 'echo \\" >> ' + fn
tb.write_lx_cmd_check(tb.workfd, cmd)

tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ_END', 'repo_create_bblayers.conf')

tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ', 'repo_dump_bblayers.conf')
tb.write_lx_cmd_check(tb.workfd, "cat " + fn)
tb.event.create_event('main', 'tc_workfd_get_with_repo.py', 'SET_DOC_FILENAME_NOIRQ_END', 'repo_dump_bblayers.conf')

tb.end_tc(True)
