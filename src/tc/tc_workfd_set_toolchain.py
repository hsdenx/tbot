# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# set the toolchain, dependend on the architecture setting in
# tb.config.tc_workfd_set_toolchain_arch
# or source script set with tb.config.tc_workfd_set_toolchain_source
# if tb.config.tc_workfd_set_toolchain_source != 'no'
#
# supported toolchains defined in
# tb.config.tc_workfd_set_toolchain_t_p and tb.config.tc_workfd_set_toolchain_cr_co
#
# set also the ARCH environment variable with the value from
# tb.config.tc_workfd_set_toolchain_arch
#
# Add a list of also executed cmds in tb.config.tc_workfd_set_toolchain_addlist
#
# used variables
#
# - tb.config.tc_workfd_set_toolchain_source
#| if != 'none' call "source tb.config.tc_workfd_set_toolchain_source"
#| default: 'none'
#
# - tb.config.tc_workfd_set_toolchain_arch
#| architecture set with "export ARCH=tb.config.tc_workfd_set_toolchain_arch"
#| default: 'not set'
#
# - tb.config.tc_workfd_set_toolchain_addlist
#| list of commands which get called additionally
#| default: 'none'
#
# - tb.config.tc_workfd_set_toolchain_t_p
#| dictionary: keys   = architecture names
#|             values = path to toolchains
#| default: ''
#| example: https://github.com/hsdenx/tbot/blob/master/config/uboot_kconfig_check.py#L57
#
# - tb.config.tc_workfd_set_toolchain_cr_co
#| dictionary: keys   = architecture names
#|             values = cross compiler prefixes
#| default: ''
#| example: https://github.com/hsdenx/tbot/blob/master/config/uboot_kconfig_check.py#L77
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_set_toolchain_source', 'none')
tb.define_variable('tc_workfd_set_toolchain_arch', 'not set')
tb.define_variable('tc_workfd_set_toolchain_addlist', 'none')
tb.define_variable('tc_workfd_set_toolchain_t_p', '')
tb.define_variable('tc_workfd_set_toolchain_cr_co', '')

logging.info("args: %s", tb.workfd.name)

c = tb.workfd

if tb.config.tc_workfd_set_toolchain_source != 'none':
    cmd = 'source ' + tb.config.tc_workfd_set_toolchain_source
    tb.write_lx_cmd_check(c, cmd)
    tb.end_tc(True)

# set ARCH
cmd = 'export ARCH=' + tb.config.tc_workfd_set_toolchain_arch
tb.write_lx_cmd_check(c, cmd)

if tb.config.tc_workfd_set_toolchain_arch in tb.config.tc_workfd_set_toolchain_t_p:
    path = tb.config.tc_workfd_set_toolchain_t_p[tb.config.tc_workfd_set_toolchain_arch]
else:
    logging.error("args: %s unknown architecture %s", tb.workfd.name, tb.config.tc_workfd_set_toolchain_arch)
    tb.end_tc(False)

if tb.config.tc_workfd_set_toolchain_arch in tb.config.tc_workfd_set_toolchain_cr_co:
    cross = tb.config.tc_workfd_set_toolchain_cr_co[tb.config.tc_workfd_set_toolchain_arch]
else:
    logging.error("args: %s unknown architecture %s", tb.workfd.name, tb.config.tc_workfd_set_toolchain_arch)
    tb.end_tc(False)

if tb.config.tc_workfd_set_toolchain_arch == 'sandbox':
    tmp = 'export PATH=/bin:$PATH'
    tb.event.create_event('main', tb.config.boardname, "Toolchain", tmp)
    tb.eof_write_cmd(c, tmp)
    tb.end_tc(True)

tmp = "printenv PATH | grep --color=never " + path
ret = tb.write_lx_cmd_check(c, tmp, endTC=False)
if ret == False:
    tmp = 'export PATH=' + path + ':$PATH'
    tb.event.create_event('main', tb.config.boardname, "Toolchain", path)
    tb.eof_write_cmd(c, tmp)

tmp = 'export CROSS_COMPILE=' + cross
tb.eof_write_cmd(c, tmp)

if tb.config.tc_workfd_set_toolchain_addlist != 'none':
    for cmd in tb.config.tc_workfd_set_toolchain_addlist:
        tb.eof_write_cmd(c, cmd)

tb.end_tc(True)
