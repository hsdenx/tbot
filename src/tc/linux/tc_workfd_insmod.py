# SPDX-License-Identifier: GPL-2.0
#
# Description:
# insmod module tb.config.tc_workfd_insmod_module with
# module path tb.config.tc_workfd_insmod_mpath and
# tb.config.tc_workfd_insmod_module_path
# check if the strings in list tb.config.tc_workfd_insmod_module_checks
# come back when inserting the module.
#
# used variables
#
# - tb.config.tc_workfd_insmod_module
#| module name without '.ko'
#| default: ''
#
# - tb.config.tc_workfd_insmod_mpath
#| path to modules
#| default: ''
#
# - tb.config.tc_workfd_insmod_module_path
#| path to module
#| default: ''
#
# - tb.config.tc_workfd_insmod_module_checks
#| list of strings which must be found when loading module
#| default: ''
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_insmod_module', '')
tb.define_variable('tc_workfd_insmod_mpath', '')
tb.define_variable('tc_workfd_insmod_module_path', '')
tb.define_variable('tc_workfd_insmod_module_checks', '')
# here starts the real test
logging.info("args: %s", tb.workfd.name)

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.workfd
tmp = 'rmmod ' + tb.config.tc_workfd_insmod_module
tb.eof_write_cmd(c, tmp)

tmp = 'uname -r'
tb.eof_write(c, tmp)

ret = tb.tbot_expect_string(c, '\n')
if ret == 'prompt':
    tb.end_tc(False)
ret = tb.tbot_expect_string(c, '\n')
if ret == 'prompt':
    tb.end_tc(False)

vers = tb.buf.rstrip()
tb.tbot_expect_prompt(c)

tmp = 'insmod ' + tb.config.tc_workfd_insmod_mpath + '/' + vers + '/' + tb.config.tc_workfd_insmod_module_path + '/' + tb.config.tc_workfd_insmod_module + '.ko'
tb.eof_write(c, tmp)
tb.tbot_rup_check_all_strings(c, tb.config.tc_workfd_insmod_module_checks, endtc=True)
